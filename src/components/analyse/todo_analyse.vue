<template>
    <div class="todo-summary">
        <h1 class="title">Todo 总结</h1>
        <div class="menu-container">
            <div class="menu-item" :class="{ active: activeView === 'month' }" @click="setActiveView('month')">
                月
            </div>
            <div class="menu-item" :class="{ active: activeView === 'year' }" @click="setActiveView('year')">
                年
            </div>
        </div>

        <!-- Main Content -->
        <div v-if="responseData.tag_summary!=[]" class="summary-content">
            <!-- Key Metrics -->
            <div class="metrics-grid">
                <div class="metric-card">
                    <div class="metric-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                            class="lucide lucide-check-circle">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                            <polyline points="22 4 12 14.01 9 11.01" />
                        </svg>
                    </div>
                    <div class="metric-details">
                        <h3>总完成</h3>
                        <div class="metric-value">{{ responseData.finished_count }} / {{ responseData.total_count }}项
                        </div>
                        <div class="metric-subtext">千里之行，始于足下</div>
                    </div>
                </div>

                <div class="metric-card">
                    <div class="metric-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                            class="lucide lucide-timer">
                            <path d="M10 2h4" />
                            <path d="M12 14v-4" />
                            <path d="M4 13a8 8 0 0 1 8-7 8 8 0 1 1-5.3 14L4 17.6" />
                            <path d="M9 17H4v5" />
                        </svg>
                    </div>
                    <div class="metric-details">
                        <h3>准时完成</h3>
                        <div class="metric-value">共 {{ responseData.ontime_finished_count }} 项</div>
                        <div class="metric-subtext">今日事，今日毕🎉</div>
                    </div>
                </div>

                <div class="metric-card">
                    <div class="metric-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                            class="lucide lucide-zap">
                            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
                        </svg>
                    </div>
                    <div class="metric-details">
                        <h3>效率 Max</h3>
                        <div class="metric-value">{{ formatDate(responseData.most_productive_day.date) }}</div>
                        <div class="metric-subtext">{{ responseData.most_productive_day.count }}项任务被搞定！</div>
                    </div>
                </div>

                <div class="metric-card">
                    <div class="metric-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                            class="lucide lucide-hourglass">
                            <path d="M5 22h14" />
                            <path d="M5 2h14" />
                            <path d="M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22" />
                            <path d="M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2" />
                        </svg>
                    </div>
                    <div class="metric-details">
                        <h3>拖延 ing
                        </h3>
                        <div class="metric-value truncate-text">{{ responseData.longest_pending_todo.title }}</div>
                        <div class="metric-subtext">立于 {{ formatDate(responseData.longest_pending_todo.create_time) }}
                        </div>
                    </div>
                </div>
            </div>
            <div class="highlights-container">
                <div class="highlight-card">
                    <h3>最快完成💪</h3>
                    <div class="highlight-content">
                        <div class="highlight-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" class="lucide lucide-rocket">
                                <path
                                    d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z" />
                                <path
                                    d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z" />
                                <path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0" />
                                <path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5" />
                            </svg>
                        </div>
                        <div class="highlight-details">
                            <div class="highlight-title truncate-text">{{ responseData.fastest_todo.title }}</div>
                            <div class="highlight-value">{{ formatTime(responseData.fastest_todo.completion_time) }}
                            </div>
                        </div>
                    </div>
                </div>

                <div class="highlight-card">
                    <h3>最慢完成😴</h3>
                    <div class="highlight-content">
                        <div class="highlight-icon slow">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" class="lucide lucide-snail">
                                <path d="M2 13a6 6 0 1 0 12 0 4 4 0 1 0-8 0 2 2 0 0 0 4 0" />
                                <circle cx="10" cy="13" r="8" />
                                <path d="M2 21h12c4.4 0 8-3.6 8-8V7a2 2 0 1 0-4 0v6" />
                                <path d="M18 3 19.1 5.1" />
                                <path d="M22 3 20.9 5.1" />
                            </svg>
                        </div>
                        <div class="highlight-details">
                            <div class="highlight-title truncate-text">{{ responseData.slowest_todo.title }}</div>
                            <div class="highlight-value">{{ formatTime(responseData.slowest_todo.completion_time) }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tag Summary Chart -->
            <div class="chart-container">
                <h3>按标签👀</h3>
                <div ref="tagChartRef" class="tag-chart"></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import * as echarts from 'echarts/core';
import { BarChart, PieChart } from 'echarts/charts';
import { getMonthlyTodos, getYearlyTodos } from '@/js/analyse/todo-analyse';
import Cookies from 'js-cookie';
import {
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    GridComponent
} from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
echarts.use([
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    GridComponent,
    BarChart,
    PieChart,
    CanvasRenderer
]);
const responseData = ref({
  finished_count: 0,
  total_count: 0,
  ontime_finished_count: 0,
  most_productive_day: { date: '', count: 0 },
  longest_pending_todo: { title: '', create_time: '' },
  fastest_todo: { title: '', completion_time: 0 },
  slowest_todo: { title: '', completion_time: 0 },
  tag_summary: []
});

const activeView = ref('month');
const tagChartRef = ref(null);
let tagChart = null;


// Set active view
const setActiveView = (view) => {
    activeView.value = view;
};

// Format date for display
const formatDate = (dateString) => {
    if (!dateString) return '';
    if (dateString.includes(' ')) {
        dateString = dateString.split(' ')[0];
    }

    const [year, month, day] = dateString.split('-');
    return `${year}-${month}-${day}`;
};
const formatTime = (seconds) => {
    if (!seconds) return '';

    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);

    if (hours > 24) {
        const days = Math.floor(hours / 24);
        return `${days} day${days > 1 ? 's' : ''}`;
    } else if (hours > 0) {
        return `${hours} hour${hours > 1 ? 's' : ''} ${minutes} min`;
    } else {
        return `${minutes} minutes`;
    }
};
const renderTagChart = () => {
    if (!tagChartRef.value) return;
    if (tagChart) {
        tagChart.dispose();
    }
    tagChart = echarts.init(tagChartRef.value);
    const tags = responseData.value.tag_summary.map(item => item.tag);
    const completionRates = responseData.value.tag_summary.map(item => parseFloat(item.completion_rate));
    const finishedCounts = responseData.value.tag_summary.map(item => parseInt(item.finished));
    const totalCounts = responseData.value.tag_summary.map(item => item.total);
    const option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            },
            formatter: function (params) {
                const tagIndex = params[0].dataIndex;
                const tagData = responseData.value.tag_summary[tagIndex];
                return `
            <div style="font-weight: bold; margin-bottom: 5px;">${tagData.tag}</div>
            <div>完成情况: ${tagData.finished}/${tagData.total}</div>
            <div>完成率: ${Number(tagData.completion_rate).toFixed(2)}%</div>
          `;
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            data: tags,
            axisLabel: {
                interval: 0,
                rotate: 30
            }
        },
        yAxis: [
            {
                type: 'value',
                name: 'Todo 已完成/总量',
                min: 0,
                max: Math.max(...totalCounts) + 1,
                interval: 1,
                axisLabel: {
                    formatter: '{value}'
                }
            },
            {
                type: 'value',
                name: '完成率',
                min: 0,
                max: 100,
                interval: 20,
                axisLabel: {
                    formatter: '{value}%'
                }
            }
        ],
        series: [
            {
                name: 'Total Tasks',
                type: 'bar',
                barWidth: '40%',
                stack: 'Tasks',
                itemStyle: {
                    color: 'rgba(128, 128, 255, 0.3)'
                },
                data: totalCounts
            },
            {
                name: '完成',
                type: 'bar',
                stack: 'Tasks',
                barWidth: '40%',
                itemStyle: {
                    color: 'rgba(64, 158, 255, 0.8)'
                },
                data: finishedCounts
            },
            {
                name: '完成率',
                type: 'line',
                yAxisIndex: 1,
                symbol: 'circle',
                symbolSize: 8,
                itemStyle: {
                    color: '#ff9f7f'
                },
                lineStyle: {
                    width: 3
                },
                data: completionRates
            }
        ],
        color: ['#8378EA', '#47A0FF', '#FF7B7B', '#FFC257', '#55D8C5']
    };

    // Set chart options and render
    tagChart.setOption(option);

    // Handle window resize
    window.addEventListener('resize', () => {
        tagChart.resize();
    });
};
const fetchData = async () => {
    let params = {
        "user_id": Cookies.get("user_id")
    } 

    if (activeView.value == 'month' ) {
        let res=await getMonthlyTodos(params)
        responseData.value = res.data;
    }
    else {
        let res=await getYearlyTodos(params)
        responseData.value = res.data;
    }
}
watch(activeView, () => {
    fetchData();
});
watch(() => responseData.value, () => {
    renderTagChart();
}, { deep: true });


fetchData();
renderTagChart();

</script>

<style>
.todo-summary {
    font-family: 'Inter', 'Helvetica', 'Arial', sans-serif;
    max-width: 1200px;
    margin-left: 230px;
    padding: 2rem;
    color: #333;
    background: transparent;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
}

.title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    color: #2c3e50;
    text-align: center;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: fadeIn 0.8s ease-out;
}

.menu-container {
    display: flex;
    gap: 1rem;
    margin-left: 130px;
    align-items: left;
    margin-bottom: 2rem;
    position: relative;
}

.menu-item {
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    color: #64748b;
    background-color: #fff;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.menu-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.menu-item.active {
    color: #fff;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
}

.summary-content {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    animation: slideUp 0.5s ease-out;
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    opacity: 0.9;
}

.metric-card {

    background-color: #f1f7f9;
    border-radius: 12px;
    padding: 1.5rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
}

.metric-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
}

.metric-details {
    flex: 1;
    align-items: center;
    justify-items: center;
}

.metric-details h3 {
    font-size: 1.3rem;
    font-weight: 600;
    color: #64748b;
    margin: 0 0 0.5rem 0;
}

.metric-value {
    font-size: 1.1rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.25rem;
}

.metric-subtext {
    font-size: 0.75rem;
    color: #94a3b8;
}

.highlights-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
}

.highlight-card {
    background-image: linear-gradient(-20deg, #e9defa 0%, #fbfcdb 100%);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.highlight-card h3 {
    font-size: 1.1rem;
    font-weight: 600;
    color: #334155;
    margin: 0 0 1rem 0;
}

.highlight-content {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.highlight-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: linear-gradient(135deg, #10b981, #34d399);
    color: white;
}

.highlight-icon.slow {
    background: linear-gradient(135deg, #f97316, #fb923c);
}

.highlight-details {
    flex: 1;
}

.highlight-title {
    font-size: 1rem;
    font-weight: 600;
    color: #334155;
    margin-bottom: 0.5rem;
}

.highlight-value {
    font-size: 0.9rem;
    color: #64748b;
}

.chart-container {
    text-align: center;
    background-image: linear-gradient(135deg, #f5f7fa 0%, #d1daea 100%);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.chart-container h3 {
    font-size: 1.5rem;
    font-weight: 600;
    color: #334155;
}

.tag-chart {
    height: 400px;
    width: 100%;
}

.truncate-text {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 100%;
}

/* Animations */
@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .todo-summary {
        padding: 1.5rem;
    }

    .title {
        font-size: 2rem;
    }

    .metrics-grid {
        grid-template-columns: 1fr;
    }

    .highlights-container {
        grid-template-columns: 1fr;
    }

    .tag-chart {
        height: 300px;
    }
}
</style>