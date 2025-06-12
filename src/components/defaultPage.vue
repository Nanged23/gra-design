<template>
    <div class="main-container"> 
        <div class="intro-section" ref="introSection">
            <div class="background"></div>

            <!-- 用户信息区域 -->
            <div class="user-info">
                <h1 class="username">{{ userData.username }}</h1>
                <div class="signature">
                    <span ref="signatureText"></span>
                    <span class="cursor"></span>
                </div>
            </div>

            <!-- 底部海浪 -->
            <div class="wave-container">
                <svg class="waves" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                    viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
                    <defs>
                        <path id="gentle-wave"
                            d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
                    </defs>
                    <g class="parallax">
                        <use xlink:href="#gentle-wave" x="48" y="0" fill="rgba(255,255,255,0.7)" />
                        <use xlink:href="#gentle-wave" x="48" y="3" fill="rgba(255,255,255,0.5)" />
                        <use xlink:href="#gentle-wave" x="48" y="5" fill="rgba(255,255,255,0.3)" />
                        <use xlink:href="#gentle-wave" x="48" y="7" fill="#fff" />
                    </g>
                </svg>
            </div>
        </div>
 
        <div class="data-section" ref="dataSection">
            <!-- 年度剩余 -->
            <div class="time-remaining">
                <div class="year-remaining">
                    <h2>{{ currentYear }}年余额</h2>
                    <div class="days-container">
                        <div class="days-number">{{ yearRemaining.days }}</div>
                        <div class="days-text">天</div>
                        <div class="progress-circle"
                            :style="{ background: `conic-gradient(#4CAF50 0%, #4CAF50 ${yearRemaining.percentage}%, #e0e0e0 ${yearRemaining.percentage}%, #e0e0e0 100%)` }">
                            <div class="percentage">{{ yearRemaining.percentage.toFixed(2) }}%</div>
                        </div>
                    </div>
                    <div class="time-detail">{{ yearRemaining.hours }} 小时 {{ yearRemaining.minutes }} 分</div>
                </div>

                <!-- 月度剩余 -->
                <div class="month-remaining">
                    <h2>{{ currentMonth }}月余额</h2>
                    <div class="days-container">
                        <div class="days-number">{{ monthRemaining.days }}</div>
                        <div class="days-text">天</div>
                        <div class="progress-circle"
                            :style="{ background: `conic-gradient(#4CAF50 0%, #4CAF50 ${monthRemaining.percentage}%, #e0e0e0 ${monthRemaining.percentage}%, #e0e0e0 100%)` }">
                            <div class="percentage">{{ monthRemaining.percentage.toFixed(2) }}%</div>
                        </div>
                    </div>
                    <div class="time-detail">{{ monthRemaining.hours }} 小时 {{ monthRemaining.minutes }} 分</div>
                </div>
            </div>

            <!-- 纪念日信息 -->
            <div class="anniversary-section">
                <h2>纪念日</h2>
                <div class="anniversary-list">
                    <div v-for="(item, index) in anniversaryData" :key="index" class="anniversary-item">
                        <div class="anniversary-info">
                            <div class="anniversary-name">{{ item.name }}</div>
                            <div class="anniversary-date">{{ item.date }}</div>
                            <div class="anniversary-description" v-if="item.description">{{ item.description }}</div>
                        </div>
                        <div class="anniversary-days">还有 {{ item.daysLeft }} 天</div>
                        <div class="anniversary-icon">
                            <component :is="item.icon" size="24" />
                        </div>
                    </div>
                </div>
            </div>

            <!-- 热力图 -->
            <div class="heatmap-section">
                <h2>热力图</h2>
                <div class="heatmap-info">
                    -- 已注册了 {{ userData.registeredDays }} 天, 上次光临是在 {{ userData.lastVisit }} 天前
                </div>
                <div ref="heatmapChart" class="heatmap-chart"></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed, nextTick } from 'vue';
import * as echarts from 'echarts';
import { Calendar1, Cake, PencilRuler } from 'lucide-vue-next';
import { getHotMap, getUserDetail, getMemDay } from '@/js/index/indexPage.js';
import Cookie from 'js-cookie';
const heatmapData = ref([]);
const userData = ref(
    {
        username: '',
        signature: '',
        registeredDays: 0,
        lastVisit: 0
    }
);
let typingTimeoutId = null;
let restartTimeoutId = null;
const getUesrData = async () => {
    let requestParams = { "user_id": Cookie.get("user_id") }
    const hotmap_res = await getHotMap(requestParams);
    // 转换热力图数据格式
    heatmapData.value = Object.entries(hotmap_res.data.heatMap).map(([date, value]) => {
        // 将 "20250327" 转换为 "2025-03-27"
        const formattedDate = `${date.slice(0, 4)}-${date.slice(4, 6)}-${date.slice(6, 8)}`;
        // 将字符串值转换为数字
        return [formattedDate, parseFloat(value)];
    });
    const user_info_res = await getUserDetail(requestParams);
    userData.value = {
        username: user_info_res.data[1].user_name,
        signature: user_info_res.data[1].signature,
        registeredDays: getTimeDiff(hotmap_res.data.createTime),
        lastVisit: getTimeDiff(hotmap_res.data.lastLoginTime)
    }

};
const getTimeDiff = (time1) => {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const eventDate = new Date(time1);
    eventDate.setHours(0, 0, 0, 0);
    const timeDiff = eventDate - today;
    const daysDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
    return daysDiff < 0 ? -daysDiff : daysDiff
}
const now = new Date();
const currentYear = now.getFullYear();
const currentMonth = now.getMonth() + 1;

// 计算年度剩余时间
const yearRemaining = computed(() => {
    const endOfYear = new Date(currentYear, 11, 31, 23, 59, 59);
    const timeLeft = endOfYear - new Date();
    const totalDays = 365 + (isLeapYear(currentYear) ? 1 : 0);
    const daysLeft = Math.ceil(timeLeft / (1000 * 60 * 60 * 24));
    const hoursLeft = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutesLeft = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const secondsLeft = Math.floor((timeLeft % (1000 * 60)) / 1000);
    const percentage = ((totalDays - daysLeft) / totalDays) * 100;

    return {
        days: daysLeft,
        hours: hoursLeft,
        minutes: minutesLeft,
        seconds: secondsLeft,
        percentage: percentage
    };
});

// 计算月度剩余时间
const monthRemaining = computed(() => {
    const endOfMonth = new Date(currentYear, currentMonth, 0, 23, 59, 59);
    const timeLeft = endOfMonth - new Date();
    const totalDays = new Date(currentYear, currentMonth, 0).getDate();
    const daysLeft = Math.ceil(timeLeft / (1000 * 60 * 60 * 24));
    const hoursLeft = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutesLeft = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const secondsLeft = Math.floor((timeLeft % (1000 * 60)) / 1000);
    const percentage = ((totalDays - daysLeft) / totalDays) * 100;

    return {
        days: daysLeft,
        hours: hoursLeft,
        minutes: minutesLeft,
        seconds: secondsLeft,
        percentage: percentage
    };
});

// 判断是否闰年
function isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}
const formatDate = (dateString) => {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
    }).format(date)
        .replace(/\//g, '.');
}
const anniversaryData = ref(
    {
        name: "",
        description: "",
        date: 0,
        daysLeft: 0,
        icon: ''
    }
);
const getAnn = async () => {
    const categoryToIcon = {
        "生日": Cake,
        "节日": Calendar1,
        "考试": PencilRuler,
    };
    let params = { "user_id": Cookie.get('user_id') }
    let res = await getMemDay(params)
    anniversaryData.value = res.data.map(item => ({
        name: item.event_name,
        description: item.description,
        date: formatDate(item.event_date),
        daysLeft: getTimeDiff(item.event_date),
        icon: categoryToIcon[item.category] || Calendar1,
    }));
}
const signatureText = ref(null);
const heatmapChart = ref(null);
let chart = null;
const stopTypewriter = () => {
    if (typingTimeoutId) clearTimeout(typingTimeoutId);
    if (restartTimeoutId) clearTimeout(restartTimeoutId);
    typingTimeoutId = null;
    restartTimeoutId = null;
};
const typewriterEffect = () => {
  stopTypewriter(); 

  if (!signatureText.value) {
    // console.warn("signatureText is not yet bound to DOM element.");
    return;
  }

  const text = userData.value.signature || ""; // Use the fetched signature
  signatureText.value.textContent = ''; // Clear current text first

  if (!text) { // If signature is empty, do nothing further
      return;
  }

  let i = 0;
  const type = () => {
    if (!signatureText.value) { // Double check if element still exists
        stopTypewriter(); 
        return;
    }
    if (i < text.length) {
      signatureText.value.textContent = text.slice(0, i + 1);
      i++;
      typingTimeoutId = setTimeout(type, 100);
    } else {
      restartTimeoutId = setTimeout(() => {
        typewriterEffect();
      }, 3000); 
    }
  };
  type(); 
};

onMounted(async () => {
    await getUesrData();
    await getAnn();
    await nextTick();
    initHeatmap();
    typewriterEffect(); 
});
onUnmounted(() => {
    if (chart) {
        chart.dispose();
        chart = null;
    }
    stopTypewriter();
});

const initHeatmap = () => {
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
            range: String(currentYear),
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
</script>

<style scoped>
.main-container {
    position: relative;
    width: 95%;
    margin-left: 220px;
    min-height: 100vh;
    overflow-y: auto;
}

.intro-section {
    position: relative;
    width: 95%;
    height: 50vh;
    background: transparent;
}

.user-info {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #0c0d0c;
    text-align: center;
    margin-bottom: 3.2rem;
    font-weight: 400;
}

.username {
    font-size: 3rem;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(245, 246, 236, 0.5);
}

.signature {
    font-size: 1.5rem;
    text-shadow: 1px 1px 2px rgba(245, 246, 236, 0.5);
    height: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.cursor {
    display: inline-block;
    width: 3px;
    height: 1.5rem;
    background-color: #000000;
    margin-left: 5px;
    animation: blink 1s infinite;
}

@keyframes blink {

    0%,
    100% {
        opacity: 1;
    }

    50% {
        opacity: 0;
    }
}

.data-section {
    position: relative;
    width: 95%;
    padding: 2rem;
    background-color: #f5f5f5;
    opacity: 0.9;
}

.time-remaining {
    display: flex;
    align-items: center;
    gap: 3.3rem;
    margin-bottom: 2rem;
}

.year-remaining,
.month-remaining {
    width: 510px;
    padding: 1.2rem;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
}

h2 {
    text-align: center !important;
    margin: 0 !important;
    font-size: 2rem;
    font-weight: bold;
}

.days-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 1rem;
}

.days-number {
    font-size: 6rem;
    font-weight: bold;
    line-height: 1;
    margin-right: 0.5rem;
}

.days-text {
    font-size: 2rem;
    align-self: flex-end;
    margin-bottom: 1.5rem;
}

.progress-circle {
    margin-left: 70px;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.progress-circle::before {
    content: '';
    position: absolute;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background-color: white;
}

.percentage {
    position: relative;
    z-index: 1;
    font-size: 1.2rem;
    font-weight: bold;
}

.time-detail {
    font-size: 1.5rem;
    color: #666;
    margin-top: 1rem;
    text-align: center;
}

.anniversary-section {
    margin-bottom: 3rem;
    padding: 1.5rem;
    border-radius: 10px;
    width: 85%;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
}

.anniversary-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 1rem;
}

.anniversary-item {
    display: flex;
    align-items: center;
    padding: 1rem;
    border-radius: 8px;
    background-color: #f9f9f9;
    margin-bottom: 0.5rem;
}

.anniversary-info {
    flex: 1;
}

.anniversary-name {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 0.25rem;
}

.anniversary-date {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 0.25rem;
}

.anniversary-description {
    font-size: 0.9rem;
    color: #888;
    font-style: italic;
}

.anniversary-days {
    font-size: 1.5rem;
    font-weight: bold;
    margin: 0 1rem;
    color: #ff6b6b;
}

.anniversary-icon {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.heatmap-section {
    width: 85%;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
}

.heatmap-info {
    text-align: right;
    margin: 1rem 0;
    font-size: 1rem;
    color: #666;
}

.heatmap-chart {
    width: 100%;
    height: 250px;
}

.wave-container {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 150px;
    pointer-events: none;
}

.waves {
    position: absolute;
    width: 95%;
    height: 100px;
    bottom: 0;
    left: 0;
}

.parallax>use {
    animation: move-forever 25s cubic-bezier(.55, .5, .45, .5) infinite;
}

.parallax>use:nth-child(1) {
    animation-delay: -2s;
    animation-duration: 7s;
}

.parallax>use:nth-child(2) {
    animation-delay: -3s;
    animation-duration: 10s;
}

.parallax>use:nth-child(3) {
    animation-delay: -4s;
    animation-duration: 13s;
}

.parallax>use:nth-child(4) {
    animation-delay: -5s;
    animation-duration: 20s;
}

@keyframes move-forever {
    0% {
        transform: translate3d(-90px, 0, 0);
    }

    100% {
        transform: translate3d(85px, 0, 0);
    }
}
</style>
