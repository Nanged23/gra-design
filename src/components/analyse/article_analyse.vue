<style scoped>
.blog-statistics {
    margin-left: 220px;
    padding: 1rem;
    font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
    color: #333;
    overflow-x: hidden;
    overflow-y: auto;
    display: flex;
    align-items: center;
    flex-direction: column;
}

.title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(to right, #9fa1f4, #8b5cf6, #d946ef);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding: 0.5rem 0;
    text-shadow: 0 2px 10px rgba(99, 102, 241, 0.2);
    letter-spacing: 0.05em;
}

.charts-container {
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 20px;
    width: 100%;
    height: 300px;
}

.chart {
    width: 550px;
    height: 100%;
    /* 确保图表填满 wrapper */
}

.ranking-title {
    font-size: 1.5rem;
    margin: 0 0 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #f0f0f0;
    color: #1a1a1a;
    position: relative;
    display: inline-block;
}

.ranking-title::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 50%;
    height: 2px;
    background: linear-gradient(to right, #7e7fef, #8151f0);
    animation: slideRight 4s ease-in-out infinite alternate;
}

@keyframes slideRight {
    from {
        width: 0;
    }

    to {
        width: 100%;
    }
}

.ranking-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    width: 80%;
    perspective: 1000px;
    opacity: 0.8;
}

.article-card {
    display: flex;
    background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    cursor: pointer;
    transform-origin: center;
    animation: fadeInUp 0.5s ease-out forwards;
    animation-delay: var(--delay);
    opacity: 0;
    transform: translateY(20px);
    height: 120px;
}

@keyframes fadeInUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.article-card:active {
    transform: scale(0.98);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.article-card:hover {
    transform: translateY(-5px) rotateX(5deg);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
}

.article-card:hover .shine-effect {
    transform: skewX(20deg) translateX(300%);
}

.article-card:hover .article-overlay {
    opacity: 1;
}

.shine-effect {
    position: absolute;
    top: 0;
    left: -100%;
    width: 50%;
    height: 100%;
    background: linear-gradient(to right,
            rgba(255, 255, 255, 0) 0%,
            rgba(255, 255, 255, 0.3) 50%,
            rgba(255, 255, 255, 0) 100%);
    transform: skewX(20deg);
    transition: transform 1s;
    pointer-events: none;
}

.rank-1 {
    border: 2px solid rgb(233, 225, 180);
    box-shadow: 0 8px 24px rgba(255, 215, 0, 0.2);
    transform: translateY(-10px);
    z-index: 3;
}

.rank-2 {
    border: 2px solid rgb(227, 219, 219);
    box-shadow: 0 6px 18px rgba(192, 192, 192, 0.2);
    transform: translateY(-5px);
    z-index: 2;
}

.rank-3 {
    border: 2px solid #f8e9db;
    /* bronze */
    box-shadow: 0 4px 12px rgba(205, 127, 50, 0.2);
    z-index: 1;
}

.rank-1:hover {
    box-shadow: 0 15px 30px rgba(255, 215, 0, 0.3);
}

.rank-2:hover {
    box-shadow: 0 12px 24px rgba(192, 192, 192, 0.3);
}

.rank-3:hover {
    box-shadow: 0 10px 20px rgba(205, 127, 50, 0.3);
}

.article-cover {
    width: 200px;
    height: 120px;
    overflow: hidden;
    position: relative;
}

.article-cover img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.article-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.read-more {
    color: white;
    font-weight: bold;
    padding: 8px 16px;
    border-radius: 20px;
    background: rgba(99, 102, 241, 0.8);
    transform: translateY(10px);
    transition: transform 0.3s ease;
}

.article-card:hover .read-more {
    transform: translateY(0);
}

.article-card:hover .article-cover img {
    transform: scale(1.1);
}

.article-info {
    flex: 1;
    padding: 1rem 1.5rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    z-index: 1;
}

.article-title {
    font-size: 1.2rem;
    margin: 0 0 0.5rem;
    font-weight: 600;
    color: #1a1a1a;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    transition: color 0.3s ease;
}

.article-card:hover .article-title {
    color: #6366f1;
}

.article-views {
    display: flex;
    align-items: center;
    color: #666;
}

.views-icon {
    margin-top: 0.4rem;
    margin-right: 0.5rem;
}

.views-count {
    font-size: 0.9rem;
}

.medal-container {
    position: absolute;
    top: -10px;
    left: 20px;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
    transform-origin: top center;
    animation: swingMedal 1s ease-in-out;
}

@keyframes swingMedal {
    0% {
        transform: rotate(-10deg);
    }

    50% {
        transform: rotate(10deg);
    }

    100% {
        transform: rotate(0);
    }
}

.medal-ribbon {
    width: 10px;
    height: 30px;
    background: linear-gradient(to right, #e53e3e, #f56565);
    position: absolute;
    top: -15px;
    z-index: -1;
    border-radius: 5px;
}

.medal-icon {
    font-size: 2.2rem;
    filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.3));
    animation: pulse 2s infinite;
    transition: transform 0.3s ease;
}

@keyframes pulse {
    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.1);
    }

    100% {
        transform: scale(1);
    }
}

.medal-1 {
    transform: scale(1.2);
    animation: shine 2s infinite;
}

@keyframes shine {
    0% {
        filter: drop-shadow(0 0 5px rgba(255, 215, 0, 0.7));
    }

    50% {
        filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.7));
    }

    100% {
        filter: drop-shadow(0 0 5px rgba(255, 215, 0, 0.7));
    }
}

.medal-2 {
    transform: scale(1.1);
}

.medal-3 {
    transform: scale(1);
}

.medal-rank {
    position: absolute;
    top: -5px;
    right: -15px;
    background: #6366f1;
    color: white;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 0.8rem;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

@media (max-width: 768px) {
    .charts-container {
        flex-direction: column;
    }

    .article-card {
        flex-direction: column;
        height: auto;
    }

    .article-cover {
        width: 100%;
        height: 160px;
    }

    .medal-container {
        top: 10px;
        left: 10px;
    }
}
</style>
<template>
    <div class="blog-statistics">
        <h1 class="title">共创作 {{ totalWords }} 字，相当于 {{sentence}}</h1>

        <div class="charts-container">
            <div class="chart-wrapper">
                <div ref="timeChart" class="chart"></div>
            </div>
            <div class="chart-wrapper">
                <div ref="wordCloudChart" class="chart"></div>
            </div>
        </div>
        <h2 class="ranking-title">热门文章排行</h2>
        <div class="ranking-list">
            <div v-for="(article, index) in topArticles" :key="article.id" class="article-card"
                :class="`rank-${index + 1}`" @click="fetchAndGo(article)" :style="{ '--delay': `${index * 0.1}s` }">
                <div class="medal-container" v-if="index < 3">
                    <div class="medal-ribbon"></div>
                    <div class="medal-icon" :class="`medal-${index + 1}`">
                        {{ index === 0 ? '🥇' : index === 1 ? '🥈' : '🥉' }}
                    </div>
                    <div class="medal-rank">{{ index + 1 }}</div>
                </div>
                <div class="article-cover">
                    <img :src="article.cover" :alt="article.title">
                    <div class="article-overlay">
                        <span class="read-more">阅读全文</span>
                    </div>
                </div>
                <div class="article-info">
                    <h3 class="article-title">{{ article.title }}</h3>
                    <div class="article-views">
                        <span class="views-icon">
                            <Eye />
                        </span>
                        <span class="views-count">{{ article.views_count }}</span>
                    </div>
                </div>
                <div class="shine-effect"></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { Eye } from 'lucide-vue-next';
import * as echarts from 'echarts';
import 'echarts-wordcloud';
import Cookies from 'js-cookie';
import { ElMessage } from 'element-plus';
import { getTimePrefer, getTopArticles, getWordCloud, getWordCount } from '@/js/analyse/article-analyse';
import { useArticleStore } from '../../stores/article';
import { getSingleArticle } from '../../js/cur/article.js';
const emits = defineEmits(['scrollToTop']);
const articleStore = useArticleStore();
const totalWords = ref(0);
const sentence = ref(''); 
const timeChart = ref(null);
const wordCloudChart = ref(null);
const topArticles = ref([]);
const router = useRouter();
// 获取标签词云数据
const fetchTagCloudData = async () => {
    try {
        let params = { "user_id": Cookies.get("user_id") }
        const result = await getWordCloud(params);

        if (result.msg === 'success') {
            const tagData = Object.entries(result.data).map(([name, value]) => ({
                name,
                value
            }));

            return tagData;
        }
        return [];
    } catch (error) {
        ElMessage({
            type: 'error',
            message: '获取标签词云数据失败'
        })
        return [];
    }
};

// 获取字数统计数据
const fetchWordCountData = async () => {
    try {
        let params = { "user_id": Cookies.get("user_id") }
        const result = await getWordCount(params)
        if (result.msg === 'success') {
            totalWords.value = result.data.word_count;
            sentence.value = result.data.sentence;
            return result.data;
        }
        return null;
    } catch (error) {
        ElMessage({
            type: 'error',
            message: '获取字数统计数据失败'
        })
        return null;
    }
};

// 获取文章排行数据
const fetchTopArticlesData = async () => {
    try {
        let params = { "user_id": Cookies.get("user_id") }
        const result = await getTopArticles(params);

        if (result.msg === 'success') {
            topArticles.value = result.data;
            return result.data;
        }
        return [];
    } catch (error) {
        ElMessage({
            type: 'error',
            message: '获取文章排行数据失败'
        })
        return [];
    }
};

// 获取时间偏好数据
const fetchTimePreferenceData = async () => {
    try {
        let params = { "user_id": Cookies.get("user_id") }
        const result = await getTimePrefer(params);

        if (result.msg === 'success') {
            const timeData = Object.entries(result.data).map(([name, value]) => ({
                name: name,
                value: value
            }));

            return timeData;
        }
        return [];
    } catch (error) {
        ElMessage({
            type: 'error',
            message: '获取时间偏好数据失败'
        })
        return [];
    }
};

// 初始化标签词云图表
const initWordCloudChart = async () => {
    const tagData = await fetchTagCloudData();

    if (!wordCloudChart.value) return;

    const wordCloudChartInstance = echarts.init(wordCloudChart.value);
    const title = '文章标签词云';
    const fontSize = 16;
    wordCloudChartInstance.setOption({
        title: {
            text: title,
            left: 'center',
            textStyle: {
                fontSize: fontSize,
                color: '#333'
            }
        },
        tooltip: {
            show: true
        },
        series: [{
            type: 'wordCloud',
            shape: 'circle',
            left: 'center',
            top: 'center',
            width: '90%',
            height: '90%',
            right: null,
            bottom: null,
            sizeRange: [12, 30],
            rotationRange: [-90, 90],
            rotationStep: 45,
            gridSize: 8,
            drawOutOfBound: false,
            textStyle: {
                fontFamily: 'sans-serif',
                fontWeight: 'bold',
                color: function () {
                    return 'rgb(' + [
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160)
                    ].join(',') + ')';
                }
            },
            emphasis: {
                textStyle: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: tagData
        }]
    });

    // 处理窗口大小变化
    window.addEventListener('resize', () => {
        wordCloudChartInstance.resize();
    });
};

// 初始化时间偏好图表
const initTimePreferenceChart = async () => {
    const timeData = await fetchTimePreferenceData();

    if (!timeChart.value) return;

    const timeChartInstance = echarts.init(timeChart.value);
    const title = '创作偏好时间';
    const text = '创作时间';
    
    timeChartInstance.setOption({
        title: {
            text: title,
            left: 'center',
            textStyle: {
                fontSize: 16,
                color: '#333'
            }
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            top: 'middle'
        },
        series: [
            {
                name: text,
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: '#fff',
                    borderWidth: 2
                },
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: 14,
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: timeData,
                color: ['#6366f1', '#8b5cf6', '#ec4899', '#f43f5e', '#f97316']
            }
        ]
    });

    // 处理窗口大小变化
    window.addEventListener('resize', () => {
        timeChartInstance.resize();
    });
};

// 导航到文章详情页 
const fetchAndGo = async (post) => {
    const requestParams = { user_id: Cookies.get("user_id"), type: 1, extra: post.id };
    const res = await getSingleArticle(requestParams);

    articleStore.setCurrentArticle(res.data);
    router.push(`/articleDetail/${post.slug}`);
    emits('scrollToTop');
};
// 初始化所有数据
const initData = async () => {
    await fetchWordCountData();
    await fetchTopArticlesData();
    await initWordCloudChart();
    await initTimePreferenceChart();
};

onMounted(() => {
    initData();
});
</script>
