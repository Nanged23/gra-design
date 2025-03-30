<style>
.raining-container {
  position: relative;
  width: 100%;
  min-height: 100vh;
  background-image: linear-gradient(to top, #cdfbe2 0%, #e9fecb 100%);
  overflow: hidden;
  padding-bottom: 50px;
}

.title-container {
  position: absolute;
  top: 15%;
  left: 57%;
  transform: translate(-50%, -50%);
  z-index: 20;
}

.scrambled-title {
  color: rgb(32, 32, 32);
  font-size: 3.75rem;
  font-weight: bold;
  letter-spacing: 0.05em;
  justify-content: center;
  font-family: monospace;
}

.menu-container {
  position: absolute;
  top: 25%;
  left: 57%;
  transform: translateX(-50%);
  z-index: 20;
  width: 80%;
  max-width: 600px;
}

.menu {
  display: flex;
  justify-content: center;
  gap: 20px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 10px;
  border-radius: 8px;
  backdrop-filter: blur(5px);
}

.menu-item {
  padding: 8px 20px;
  border: none;
  background-color: transparent;
  color: #333;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.menu-item:hover {
  background-color: rgba(74, 222, 128, 0.2);
}

.menu-item.active {
  background-color: rgba(74, 222, 128, 0.5);
  font-weight: bold;
}

.charts-container {
  position: absolute;
  top: 32%;
  left: 57%;
  transform: translateX(-50%);
  width: 90%;
  max-width: 1200px;
  z-index: 40;
  background: transparent;
  border-radius: 12px;
  padding: 20px;
  backdrop-filter: blur(5px);
  overflow-x: hidden;
  overflow-y: visible;
}

.chart-row {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 20px;
  min-height: 300px;
}

.chart {
  flex: 1;
  min-width: 300px;
  height: 300px;
  background: transparent;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.heatmap-chart {
  width: 100%;
  height: 300px;
}

.character {
  position: absolute;
  font-size: 1.8rem;
  transform: translate(-50%, -50%);
  transition: color 0.1s, transform 0.1s, text-shadow 0.1s;
  will-change: transform, top;
}

.character-inactive {
  color: #64748b;
  font-weight: 300;
  opacity: 0.4;
  transform: translate(-50%, -50%) scale(1);
  text-shadow: none;
}

.character-active {
  color: #00ff00;
  font-size: 1.25rem;
  font-weight: bold;
  transform: translate(-50%, -50%) scale(1.25);
  z-index: 10;
  opacity: 1;
  text-shadow: 0 0 8px rgba(255, 255, 255, 0.8), 0 0 12px rgba(255, 255, 255, 0.4);
  animation: pulse 1s infinite;
}

.dud {
  color: #0f0;
  opacity: 0.7;
}

@keyframes pulse {

  0%,
  100% {
    opacity: 1;
  }

  50% {
    opacity: 0.8;
  }
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .title-container {
    top: 10%;
  }

  .scrambled-title {
    font-size: 2.5rem;
  }

  .menu-container {
    top: 20%;
    width: 90%;
  }

  .charts-container {
    top: 28%;
    height: 65%;
    padding: 10px;
  }

  .chart-row {
    flex-direction: column;
    height: auto;
  }

  .chart {
    height: 300px;
    min-width: 100%;
  }
}
</style>
<template>
  <div class="raining-container">
    <!-- Title moved up -->
    <div class="title-container">
      <h1 ref="titleElement" class="scrambled-title">MOMENT</h1>
    </div>

    <!-- Menu -->
    <div class="menu-container">
      <div class="menu">
        <button :class="['menu-item', activeView === 'monthly' ? 'active' : '']" @click="setActiveView('monthly')">
          月度视图
        </button>
        <button :class="['menu-item', activeView === 'yearly' ? 'active' : '']" @click="setActiveView('yearly')">
          年度视图
        </button>
      </div>
    </div>

    <div class="charts-container">
      <!-- Monthly View -->
      <div v-if="activeView === 'monthly'" class="monthly-view">
        <div class="chart-row">
          <div ref="monthlyBarChart" class="chart"></div>
          <div ref="monthlyPieChart" class="chart"></div>
        </div>
      </div>

      <!-- Yearly View -->
      <div v-else class="yearly-view">
        <div class="chart-row">
          <div ref="yearlyBarChart" class="chart"></div>
          <div ref="yearlyPieChart" class="chart"></div>
        </div>
        <div class="chart-row">
          <div ref="heatmapChart" class="chart heatmap-chart"></div>
        </div>
      </div>
    </div>

    <!-- Raining Characters -->
    <span v-for="(char, index) in characters" :key="index" :class="[
      'character',
      activeIndices.has(index) ? 'character-active' : 'character-inactive'
    ]" :style="{
      left: `${char.x}%`,
      top: `${char.y}%`
    }">
      {{ char.char }}
    </span>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch, nextTick } from 'vue';
import * as echarts from 'echarts';
import { getMomentByYear, getMomentByMonth } from '@/js/analyse/moment-analyse';
import Cookies from 'js-cookie';
import { ElMessage } from 'element-plus';
const activeView = ref('monthly');
const heatmapData = ref([]);
const setActiveView = (view) => {
  activeView.value = view;
};

// Chart references
const monthlyBarChart = ref(null);
const monthlyPieChart = ref(null);
const yearlyBarChart = ref(null);
const yearlyPieChart = ref(null);
const heatmapChart = ref(null);

// Chart instances
let monthlyBarChartInstance = null;
let monthlyPieChartInstance = null;
let yearlyBarChartInstance = null;
let yearlyPieChartInstance = null;
let heatmapChartInstance = null;

// Data refs to store API responses
const monthlyData = ref(null);
const yearlyData = ref(null);

// API calls (to be implemented by you)
const fetchMonthlyData = async () => {
  try {
    let params = {
      "user_id": Cookies.get("user_id")
    }
    const result = await getMomentByMonth(params);
    if (result.msg === 'success') {
      monthlyData.value = result.data;
    }
  } catch (error) {
    ElMessage({
      type: 'error',
      message: '获取月度数据失败',
    })
  }
};

const fetchYearlyData = async () => {
  try {
    let params = {
      "user_id": Cookies.get("user_id")
    }
    const result = await getMomentByYear(params);
    if (result.msg === 'success') {
      yearlyData.value = result.data;
      heatmapData.value = Object.entries(result.data.heatMap).map(([date, value]) => {
        // 将 "20250327" 转换为 "2025-03-27"
        const formattedDate = `${date.slice(0, 4)}-${date.slice(4, 6)}-${date.slice(6, 8)}`;
        // 将字符串值转换为数字
        return [formattedDate, parseFloat(value)];
    });
    }
  } catch (error) {
    ElMessage({
      type: 'error',
      message: '获取年度数据失败',
    })
  }
}; 
const filterMoodKeys = (data) => {
  return Object.keys(data).filter(key =>
    !['bad_moods_count', 'good_moods_count', 'total_count'].includes(key)
  );
}; 
const initMonthlyBarChart = () => {
  if (!monthlyBarChart.value || !monthlyData.value) return;

  monthlyBarChartInstance = echarts.init(monthlyBarChart.value);

  // Dynamically get categories and values, excluding mood counts
  const categories = filterMoodKeys(monthlyData.value);
  const values = categories.map(key => monthlyData.value[key]);

  const option = {
    title: {
      text: '月度活动统计',
      left: 'center'
    },
    tooltip: {
      trigger: 'axis'
    },
    xAxis: {
      type: 'category',
      data: categories
    },
    yAxis: {
      type: 'value'
    },
    series: [{
      data: values,
      type: 'bar',
      itemStyle: {
        color: '#4ade80'
      }
    }]
  };
  monthlyBarChartInstance.setOption(option);
};

const initMonthlyPieChart = () => {
  if (!monthlyPieChart.value || !monthlyData.value) return;

  monthlyPieChartInstance = echarts.init(monthlyPieChart.value);

  const pieData = [
    { value: monthlyData.value.good_moods_count, name: '好心情' },
    { value: monthlyData.value.bad_moods_count, name: '坏心情' }
  ];

  const option = {
    title: {
      text: '月度分布',
      left: 'center'
    },
    tooltip: {
      trigger: 'item',
      formatter: '{a}<br/>{b}: {c} ({d}%)'
    },
    series: [{
      name: '心情分布',
      type: 'pie',
      radius: '60%',
      center: ['50%', '50%'],
      data: pieData,
      emphasis: {
        itemStyle: {
          shadowBlur: 10
        }
      },
      itemStyle: {
        color: function (params) {
          const colorList = ['#4ade80', '#22c55e'];
          return colorList[params.dataIndex % colorList.length];
        }
      }
    }]
  };
  monthlyPieChartInstance.setOption(option);
};

const initYearlyBarChart = () => {
  if (!yearlyBarChart.value || !yearlyData.value) return;
  yearlyBarChartInstance = echarts.init(yearlyBarChart.value); 
  const categories = filterMoodKeys(yearlyData.value.moods_sum);
  const values = categories.map(key => yearlyData.value.moods_sum[key]);

  const option = {
    title: {
      text: '年度活动统计',
      left: 'center'
    },
    tooltip: {
      trigger: 'axis'
    },
    xAxis: {
      type: 'category',
      data: categories
    },
    yAxis: {
      type: 'value'
    },
    series: [{
      data: values,
      type: 'bar',
      itemStyle: {
        color: '#4ade80'
      }
    }]
  };
  yearlyBarChartInstance.setOption(option);
};

const initYearlyPieChart = () => {
  if (!yearlyPieChart.value || !yearlyData.value) return;

  yearlyPieChartInstance = echarts.init(yearlyPieChart.value);

  const pieData = [
    { value: yearlyData.value.moods_sum.good_moods_count, name: '好心情' },
    { value: yearlyData.value.moods_sum.bad_moods_count, name: '坏心情' }
  ];

  const option = {
    title: {
      text: '年度分布',
      left: 'center'
    },
    tooltip: {
      trigger: 'item',
      formatter: '{a}<br/>{b}: {c} ({d}%)'
    },
    series: [{
      name: '心情分布',
      type: 'pie',
      radius: '60%',
      center: ['50%', '50%'],
      data: pieData,
      emphasis: {
        itemStyle: {
          shadowBlur: 10
        }
      },
      itemStyle: {
        color: function (params) {
          const colorList = ['#4ade80', '#22c55e'];
          return colorList[params.dataIndex % colorList.length];
        }
      }
    }]
  };
  yearlyPieChartInstance.setOption(option);
};
let chart = null;
const initHeatmapChart = () => {
    if (chart) {
        chart.dispose();
    }
    chart = echarts.init(heatmapChart.value);

    const option = {
        tooltip: {
            position: 'top',
            formatter: function (params) {
                return params.data[0] + ': ' + params.data[1] + ' 积分';
            }
        },
        visualMap: {
            show: false,
            min: 0,
            max: 4,
            calculable: true,
            orient: 'horizontal',
            left: 'center',
            bottom: '0%',
            color: ['#136329', '#2CA44F', '#4BC16B', '#ACEEBB']
        },
        calendar: {
            top: 50,
            left: 30,
            right: 30,
            cellSize: ['auto', 15],
            range: String(2025),
            itemStyle: {
                borderWidth: 0.5
            },
            yearLabel: { show: true }
        },
        series: {
            type: 'heatmap',
            coordinateSystem: 'calendar',
            data: heatmapData.value
        }
    };
    chart.setOption(option);
}; 
const initCharts = async () => {
  await nextTick();
  setTimeout(() => {
    if (activeView.value === 'monthly') {
      initMonthlyBarChart();
      initMonthlyPieChart();
    } else {
      initYearlyBarChart();
      initYearlyPieChart();
      initHeatmapChart();
    }
  }, 100);
};

// Watch for view changes
watch(activeView, async () => {
  await nextTick();
  initCharts();
});

// Rest of the code (characters, scrambler, etc.) remains unchanged
const characters = ref([]);
const activeIndices = ref(new Set());
const titleElement = ref(null);
let scrambler = null;
let animationFrameId = null;

class TextScramble {
  constructor(el) {
    this.el = el;
    this.chars = '!<>-_\\/[]{}—=+*^?#';
    this.queue = [];
    this.frame = 0;
    this.frameRequest = 0;
    this.resolve = () => { };
    this.update = this.update.bind(this);
  }

  setText(newText) {
    const oldText = this.el.innerText;
    const length = Math.max(oldText.length, newText.length);
    const promise = new Promise((resolve) => this.resolve = resolve);
    this.queue = [];

    for (let i = 0; i < length; i++) {
      const from = oldText[i] || '';
      const to = newText[i] || '';
      const start = Math.floor(Math.random() * 50);
      const end = start + Math.floor(Math.random() * 50);
      this.queue.push({ from, to, start, end });
    }

    cancelAnimationFrame(this.frameRequest);
    this.frame = 0;
    this.update();
    return promise;
  }

  update() {
    let output = '';
    let complete = 0;

    for (let i = 0, n = this.queue.length; i < n; i++) {
      let { from, to, start, end, char } = this.queue[i];
      if (this.frame >= end) {
        complete++;
        output += to;
      } else if (this.frame >= start) {
        if (!char || Math.random() < 0.28) {
          char = this.chars[Math.floor(Math.random() * this.chars.length)];
          this.queue[i].char = char;
        }
        output += `<span class="dud">${char}</span>`;
      } else {
        output += from;
      }
    }

    this.el.innerHTML = output;
    if (complete === this.queue.length) {
      this.resolve();
    } else {
      this.frameRequest = requestAnimationFrame(this.update);
      this.frame++;
    }
  }
}

// Create initial characters
const createCharacters = () => {
  const allChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?";
  const charCount = 300;
  const newCharacters = [];

  for (let i = 0; i < charCount; i++) {
    newCharacters.push({
      char: allChars[Math.floor(Math.random() * allChars.length)],
      x: Math.random() * 100,
      y: Math.random() * 100,
      speed: 0.01 + Math.random() * 0.1,
    });
  }

  return newCharacters;
};

const initScrambler = () => {
  if (titleElement.value && !scrambler) {
    scrambler = new TextScramble(titleElement.value);

    const phrases = [
      '在这里...',
      '记录时光',
      '找寻自我',
      '铭记...',
      '有意义的瞬间',
      '很难忘的时刻'
    ];

    let counter = 0;
    const next = () => {
      if (scrambler) {
        scrambler.setText(phrases[counter]).then(() => {
          setTimeout(next, 1000);
        });
        counter = (counter + 1) % phrases.length;
      }
    };

    next();
  }
};

// Update character positions
const updatePositions = () => {
  characters.value = characters.value.map(char => ({
    ...char,
    y: char.y + char.speed,
    ...(char.y >= 100 && {
      y: -5,
      x: Math.random() * 100,
      char: "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"[
        Math.floor(Math.random() * "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?".length)
      ],
    }),
  }));

  animationFrameId = requestAnimationFrame(updatePositions);
};

// Update active indices for flicker effect
const updateActiveIndices = () => {
  const newActiveIndices = new Set();
  const numActive = Math.floor(Math.random() * 3) + 3;
  for (let i = 0; i < numActive; i++) {
    newActiveIndices.add(Math.floor(Math.random() * characters.value.length));
  }
  activeIndices.value = newActiveIndices;
};

let flickerInterval = null;

// Handle window resize
const handleResize = () => {
  if (monthlyBarChartInstance) monthlyBarChartInstance.resize();
  if (monthlyPieChartInstance) monthlyPieChartInstance.resize();
  if (yearlyBarChartInstance) yearlyBarChartInstance.resize();
  if (yearlyPieChartInstance) yearlyPieChartInstance.resize();
  if (heatmapChartInstance) heatmapChartInstance.resize();
};

onMounted(async () => {
  // Fetch data first
  await fetchMonthlyData();
  await fetchYearlyData();

  characters.value = createCharacters();
  initScrambler();
  animationFrameId = requestAnimationFrame(updatePositions);
  flickerInterval = setInterval(updateActiveIndices, 100);

  setTimeout(() => {
    initCharts();
  }, 300);

  window.addEventListener('resize', handleResize);
});

onBeforeUnmount(() => {
  if (animationFrameId) cancelAnimationFrame(animationFrameId);
  if (flickerInterval) clearInterval(flickerInterval);
  window.removeEventListener('resize', handleResize);

  if (monthlyBarChartInstance) monthlyBarChartInstance.dispose();
  if (monthlyPieChartInstance) monthlyPieChartInstance.dispose();
  if (yearlyBarChartInstance) yearlyBarChartInstance.dispose();
  if (yearlyPieChartInstance) yearlyPieChartInstance.dispose();
  if (heatmapChartInstance) heatmapChartInstance.dispose();
});
</script>