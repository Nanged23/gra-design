<template>
    <div class="douban-summary">
        <div class="background-decoration">
            <div class="circle circle-1"></div>
            <div class="circle circle-2"></div>
            <div class="circle circle-3"></div>
        </div>

        <header>
            <h1 class="title">
                <span class="title-text">我的豆瓣足迹</span>
                <div class="title-underline"></div>
            </h1>

            <div class="summary-stats">
                <div class="stat-card" v-for="(stat, index) in stats" :key="index" ref="statCards">
                    <div class="stat-number" ref="statNumbers">{{ stat.value }}</div>
                    <div class="stat-label">{{ stat.label }}</div>
                    <div class="stat-icon" :class="stat.icon"></div>
                </div>
            </div>
        </header>

        <section class="timeline-section" ref="timelineSection">
            <h2>阅读与观影时间线</h2>
            <div class="timeline-container">
                <div class="timeline-controls">
                    <button @click="changeTimelineView('year')" :class="{ active: timelineView === 'year' }">年度</button>
                    <button @click="changeTimelineView('month')"
                        :class="{ active: timelineView === 'month' }">月度</button>
                </div>
                <div class="timeline-chart" ref="timelineChart"></div>
            </div>
        </section>

        <section class="collections-section">
            <h2>珍藏发现</h2>
            <div class="collections-container">
                <div class="collection-tabs">
                    <button @click="activeCollection = 'books'"
                        :class="{ active: activeCollection === 'books' }">书籍</button>
                    <button @click="activeCollection = 'movies'"
                        :class="{ active: activeCollection === 'movies' }">电影</button>
                </div>

                <transition-group name="collection-fade" tag="div" class="collection-items">
                    <div v-if="activeCollection === 'books'" key="books" class="collection-grid">
                        <div class="collection-card book-card" ref="bookCard">
                            <div class="card-image">
                                <img :src="data.oldest_wish_book.img" :alt="data.oldest_wish_book.name" />
                                <div class="card-overlay">
                                    <a :href="data.oldest_wish_book.link" target="_blank" class="card-link">查看详情</a>
                                </div>
                            </div>
                            <div class="card-content">
                                <div class="card-badge">最早想读</div>
                                <h3>{{ data.oldest_wish_book.name }}</h3>
                                <p class="card-author">{{ data.oldest_wish_book.author }}</p>
                                <p class="card-publisher">{{ data.oldest_wish_book.language }}</p>
                                <div class="card-date">
                                    <span class="date-icon"></span>
                                    {{ formatDate(data.oldest_wish_book.create_time) }}
                                </div>
                            </div>
                        </div>

                        <div class="authors-visualization">
                            <h3>最常读的作者</h3>
                            <div class="authors-bubbles" ref="authorsBubbles"></div>
                        </div>

                        <div class="publishers-visualization">
                            <h3>出版社分布</h3>
                            <div class="publishers-bars" ref="publishersBars">
                                <div v-for="(count, publisher) in data.top3_book_languages" :key="publisher"
                                    class="publisher-bar-container">
                                    <div class="publisher-name">{{ publisher }}</div>
                                    <div class="publisher-bar-wrapper">
                                        <div class="publisher-bar" :style="{ width: '0%' }"
                                            :data-width="`${(count / Math.max(...Object.values(data.top3_book_languages))) * 100}%`">
                                        </div>
                                        <span class="publisher-count">{{ count }}本</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div v-if="activeCollection === 'movies'" key="movies" class="collection-grid">
                        <div class="collection-card movie-card" ref="movieCard">
                            <div class="card-image">
                                <img :src="data.oldest_wish_movie.img" :alt="data.oldest_wish_movie.name" />
                                <div class="card-overlay">
                                    <a :href="data.oldest_wish_movie.link" target="_blank" class="card-link">查看详情</a>
                                </div>
                            </div>
                            <div class="card-content">
                                <div class="card-badge">最早想看</div>
                                <h3>{{ data.oldest_wish_movie.name }}</h3>
                                <p class="card-director">{{ data.oldest_wish_movie.author }}</p>
                                <p class="card-country">{{ data.oldest_wish_movie.language }}</p>
                                <p class="card-genre">{{ data.oldest_wish_movie.content_type }}</p>
                                <div class="card-date">
                                    <span class="date-icon"></span>
                                    {{ formatDate(data.oldest_wish_movie.create_time) }}
                                </div>
                            </div>
                        </div>

                        <div class="directors-visualization">
                            <h3>最常看的导演</h3>
                            <div class="directors-bubbles" ref="directorsBubbles"></div>
                        </div>

                        <div class="countries-visualization">
                            <h3>电影国家/地区分布</h3>
                            <div class="countries-bars" ref="countriesBars">
                                <div v-for="(count, country) in data.top3_movie_languages" :key="country"
                                    class="country-bar-container">
                                    <div class="country-name">{{ country }}</div>
                                    <div class="country-bar-wrapper">
                                        <div class="country-bar" :style="{ width: '0%' }"
                                            :data-width="`${(count / Math.max(...Object.values(data.top3_movie_languages))) * 100}%`">
                                        </div>
                                        <span class="country-count">{{ count }}部</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </transition-group>
            </div>
        </section>

        <section class="tags-section" ref="tagsSection">
            <h2>电影标签云</h2>
            <div class="tags-container">
                <div class="tags-tabs">
                    <button @click="activeTagsView = 'watched'"
                        :class="{ active: activeTagsView === 'watched' }">看过的电影</button>
                    <button @click="activeTagsView = 'wish'"
                        :class="{ active: activeTagsView === 'wish' }">想看的电影</button>
                </div>

                <transition name="tags-fade" mode="out-in" @after-enter="renderAfterEnter">
                    <div v-if="activeTagsView === 'watched'" key="watched" class="tags-cloud" ref="watchedTagsCloud">
                    </div>
                    <div v-else key="wish" class="tags-cloud" ref="wishTagsCloud"></div>
                </transition>
            </div>
        </section>

        <section class="reading-habits-section">
            <h2>阅读习惯分析</h2>
            <div class="reading-habits-container" ref="readingHabitsContainer">
                <div class="reading-chart" ref="readingChart"></div>
                <div class="reading-insights">
                    <div class="insight-card">
                        <div class="insight-icon book-icon"></div>
                        <div class="insight-content">
                            <h3>阅读偏好</h3>
                            <p>您最常阅读的作者是 <strong>{{ Object.keys(data.top3_book_authors)[0] }}</strong>，共读过 {{
                                Object.values(data.top3_book_authors)[0] }} 本作品。</p>
                        </div>
                    </div>
                    <div class="insight-card">
                        <div class="insight-icon calendar-icon"></div>
                        <div class="insight-content">
                            <h3>阅读高峰</h3>
                            <p>您在 <strong>{{ getPeakReadingMonth() }}</strong> 阅读量最高，共读了 {{ getPeakReadingCount() }} 本书。
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script setup>
import { ref, nextTick, reactive, onMounted, onBeforeUnmount, watch } from 'vue';
import * as echarts from 'echarts/core';
import { BarChart, LineChart } from 'echarts/charts';
import {
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    GridComponent
} from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import * as d3 from 'd3';
import cloud from 'd3-cloud';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { getDouBan } from '@/js/analyse/douban-analyse';
import Cookies from 'js-cookie';
// 注册 GSAP 插件
gsap.registerPlugin(ScrollTrigger);

// 注册 ECharts 组件
echarts.use([
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    GridComponent,
    BarChart,
    LineChart,
    CanvasRenderer
]);

// DOM 引用
const statCards = ref([]);
const statNumbers = ref([]);
const timelineSection = ref(null);
const timelineChart = ref(null);
const bookCard = ref(null);
const movieCard = ref(null);
const authorsBubbles = ref(null);
const directorsBubbles = ref(null);
const publishersBars = ref(null);
const countriesBars = ref(null);
const tagsSection = ref(null);
const watchedTagsCloud = ref(null);
const wishTagsCloud = ref(null);
const readingHabitsContainer = ref(null);
const readingChart = ref(null);

// 图表实例存储
const chartInstances = ref({});

// 状态变量
const timelineView = ref('month');
const activeCollection = ref('books');
const activeTagsView = ref('watched');
 
const data = ref({
 
        "monthly_stats": {
            "2023-03": { "book_count": 0, "movie_count": 1 },
            "2023-04": { "book_count": 0, "movie_count": 0 },
            "2023-05": { "book_count": 0, "movie_count": 9 },
            "2023-06": { "book_count": 0, "movie_count": 0 },
            "2023-07": { "book_count": 0, "movie_count": 3 },
            "2023-08": { "book_count": 0, "movie_count": 2 },
            "2023-09": { "book_count": 0, "movie_count": 3 },
            "2023-10": { "book_count": 0, "movie_count": 4 },
            "2023-11": { "book_count": 0, "movie_count": 2 },
            "2023-12": { "book_count": 0, "movie_count": 1 },
            "2024-01": { "book_count": 0, "movie_count": 4 },
            "2024-02": { "book_count": 0, "movie_count": 5 },
            "2024-03": { "book_count": 0, "movie_count": 4 },
            "2024-04": { "book_count": 0, "movie_count": 0 },
            "2024-05": { "book_count": 0, "movie_count": 4 },
            "2024-06": { "book_count": 0, "movie_count": 2 },
            "2024-07": { "book_count": 0, "movie_count": 2 },
            "2024-08": { "book_count": 0, "movie_count": 1 },
            "2024-09": { "book_count": 0, "movie_count": 2 },
            "2024-10": { "book_count": 0, "movie_count": 1 },
            "2024-11": { "book_count": 0, "movie_count": 2 },
            "2024-12": { "book_count": 0, "movie_count": 1 },
            "2025-01": { "book_count": 0, "movie_count": 0 },
            "2025-02": { "book_count": 0, "movie_count": 2 },
            "2025-03": { "book_count": 0, "movie_count": 1 }
        },
        "oldest_wish_book": {
            "author": "安德烈·纪德",
            "content_type": null,
            "create_time": "2025-03-06 14:03:09",
            "date": "2023-12-03 00:00:00",
            "img": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E8%B1%86%E7%93%A3%E5%B0%81%E9%9D%A2/s4373749.jpg",
            "language": "上海译文出版社",
            "link": "https://book.douban.com/subject/4246974/",
            "name": "伪币制造者"
        },
        "oldest_wish_movie": {
            "author": "史蒂芬·戴德利",
            "content_type": "剧情,爱情",
            "create_time": "2025-03-06 12:22:55",
            "date": "2018-02-17 00:00:00",
            "img": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E8%B1%86%E7%93%A3%E5%B0%81%E9%9D%A2/p1140984198.jpg",
            "language": "美国,德国",
            "link": "https://movie.douban.com/subject/2213597/",
            "name": "朗读者"
        },
        "top3_book_authors": {
            "弗拉基米尔·纳博科夫": 2,
            "杜鲁门·卡波特": 2,
            "科马克·麦卡锡": 1
        },
        "top3_book_languages": {
            "上海译文出版社": 4,
            "人民文学出版社": 3,
            "湖南文艺出版社": 2
        },
        "top3_movie_directors": {
            "努里·比格·锡兰": 2,
            "宫崎骏": 2,
            "杨德昌": 4
        },
        "top3_movie_languages": {
            "中国台湾": 7,
            "中国大陆": 4,
            "美国": 5
        },
        "top3_watched_movie_tags": {
            "剧情": 38,
            "喜剧": 11,
            "爱情": 12
        },
        "top3_wish_movie_tags": {
            "剧情": 36,
            "爱情": 10,
            "犯罪": 8
        },
        "total_read_books": 16,
        "total_watched_movies": 45,
        "total_wish_books": 22,
        "total_wish_movies": 44
    
});
 
const fetchData = async () => {
    let params = {
        "user_id": Cookies.get("user_id"),
    }
    let res = await getDouBan(params)
    data.value=res.data;  
}
fetchData().then(() => {
    nextTick(() => {
        renderTimelineChart();
        renderBubbleChart();
    });
});

// 统计数据
const stats = [
    { label: '读过的书', value: data.value.total_read_books, icon: 'book-icon' },
    { label: '看过的电影', value: data.value.total_watched_movies, icon: 'movie-icon' },
    { label: '想读的书', value: data.value.total_wish_books, icon: 'wish-book-icon' },
    { label: '想看的电影', value: data.value.total_wish_movies, icon: 'wish-movie-icon' }
];

// 日期格式化函数
const formatDate = (dateString) => {
    const date = new Date(dateString);
    return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
};

// 获取阅读高峰月份
const getPeakReadingMonth = () => {
    let peakMonth = '';
    let peakCount = 0;

    Object.entries(data.value.monthly_stats).forEach(([month, stats]) => {
        if (stats.book_count > peakCount) {
            peakCount = stats.book_count;
            peakMonth = month;
        }
    });

    // 格式化月份显示
    const [year, month] = peakMonth.split('-');
    const monthNames = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'];
    return `${year}年${monthNames[parseInt(month) - 1]}`;
};

// 获取阅读高峰数量
const getPeakReadingCount = () => {
    return Math.max(...Object.values(data.value.monthly_stats).map(stats => stats.book_count));
};

// 切换时间线视图
const changeTimelineView = (view) => {
    timelineView.value = view;
    renderTimelineChart();
};

// 初始化或获取图表实例
const getChartInstance = (el, id) => {
    if (!el) return null;

    // 如果已经存在实例，先销毁
    if (chartInstances.value[id]) {
        chartInstances.value[id].dispose();
    }

    // 创建新实例
    const instance = echarts.init(el);
    chartInstances.value[id] = instance;
    return instance;
};

// 渲染时间线图表
const renderTimelineChart = () => {
    if (!timelineChart.value) return;

    const chartInstance = getChartInstance(timelineChart.value, 'timeline');
    if (!chartInstance) return;

    // 处理数据
    const months = Object.keys(data.value.monthly_stats).sort();
    const bookData = months.map(month => data.value.monthly_stats[month].book_count);
    const movieData = months.map(month => data.value.monthly_stats[month].movie_count);

    // 如果是年度视图，合并月度数据
    let xAxisData, bookSeriesData, movieSeriesData;

    if (timelineView.value === 'year') {
        const yearlyData = {};

        months.forEach((month, index) => {
            const year = month.split('-')[0];
            if (!yearlyData[year]) {
                yearlyData[year] = { books: 0, movies: 0 };
            }

            yearlyData[year].books += bookData[index];
            yearlyData[year].movies += movieData[index];
        });

        xAxisData = Object.keys(yearlyData).sort();
        bookSeriesData = xAxisData.map(year => yearlyData[year].books);
        movieSeriesData = xAxisData.map(year => yearlyData[year].movies);
    } else {
        // 月度视图
        xAxisData = months;
        bookSeriesData = bookData;
        movieSeriesData = movieData;
    }

    // 设置图表选项
    chartInstance.setOption({
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            },
            formatter: function (params) {
                const bookValue = params[0].value;
                const movieValue = params[1].value;
                return `${params[0].axisValue}<br/>
                  书籍: ${bookValue} 本<br/>
                  电影: ${movieValue} 部`;
            }
        },
        legend: {
            data: ['书籍', '电影'],
            right: '5%',
            top: '2%'
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            top: '15%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            data: xAxisData,
            axisLabel: {
                interval: timelineView.value === 'month' ? 2 : 0,
                rotate: timelineView.value === 'month' ? 45 : 0
            }
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name: '书籍',
                type: 'bar',
                data: bookSeriesData,
                itemStyle: {
                    color: '#41b883'
                },
                emphasis: {
                    itemStyle: {
                        color: '#5ccb95'
                    }
                },
                animationDelay: function (idx) {
                    return idx * 50;
                }
            },
            {
                name: '电影',
                type: 'bar',
                data: movieSeriesData,
                itemStyle: {
                    color: '#e76f51'
                },
                emphasis: {
                    itemStyle: {
                        color: '#f4a261'
                    }
                },
                animationDelay: function (idx) {
                    return idx * 50 + 100;
                }
            }
        ],
        animationEasing: 'elasticOut',
        animationDuration: 1200
    });
};

// 渲染气泡图
const renderBubbleChart = (container, data, colorScale) => {
    if (!container) return;

    // 清空容器
    d3.select(container).selectAll('*').remove();

    // 设置尺寸
    const width = container.clientWidth;
    const height = container.clientHeight;

    // 创建SVG
    const svg = d3.select(container)
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    // 创建气泡数据
    const bubbleData = Object.entries(data).map(([name, value]) => ({
        name,
        value
    }));

    // 计算气泡大小
    const maxValue = Math.max(...bubbleData.map(d => d.value));
    const radiusScale = d3.scaleSqrt()
        .domain([0, maxValue])
        .range([30, 70]);

    // 创建模拟力
    const simulation = d3.forceSimulation(bubbleData)
        .force('charge', d3.forceManyBody().strength(5))
        .force('center', d3.forceCenter(width / 2, height / 2))
        .force('collision', d3.forceCollide().radius(d => radiusScale(d.value) + 2));

    // 创建气泡
    const bubbles = svg.selectAll('.bubble')
        .data(bubbleData)
        .enter()
        .append('g')
        .attr('class', 'bubble');

    // 添加圆形
    bubbles.append('circle')
        .attr('r', 0)
        .style('fill', (d, i) => colorScale(i))
        .style('stroke', '#fff')
        .style('stroke-width', 2)
        .transition()
        .duration(1000)
        .attr('r', d => radiusScale(d.value));

    // 添加文本
    bubbles.append('text')
        .attr('text-anchor', 'middle')
        .attr('dy', '.3em')
        .style('font-size', '12px')
        .style('fill', '#fff')
        .style('pointer-events', 'none')
        .style('opacity', 0)
        .text(d => d.name)
        .transition()
        .delay(700)
        .duration(300)
        .style('opacity', 1);

    // 添加数值
    bubbles.append('text')
        .attr('text-anchor', 'middle')
        .attr('dy', '1.5em')
        .style('font-size', '14px')
        .style('font-weight', 'bold')
        .style('fill', '#fff')
        .style('pointer-events', 'none')
        .style('opacity', 0)
        .text(d => d.value)
        .transition()
        .delay(1000)
        .duration(300)
        .style('opacity', 1);

    // 更新气泡位置
    simulation.on('tick', () => {
        bubbles.attr('transform', d => `translate(${d.x},${d.y})`);
    });
};

// 渲染标签云
const renderTagCloud = (container, tags, colorScale) => {
    if (!container) return;

    // 清空容器
    d3.select(container).selectAll('*').remove();

    // 设置尺寸
    const width = container.clientWidth;
    const height = container.clientHeight;

    // 创建SVG
    const svg = d3.select(container)
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    // 创建标签数据
    const tagData = Object.entries(tags).map(([text, size]) => ({
        text,
        size
    }));

    // 计算字体大小
    const maxSize = Math.max(...tagData.map(d => d.size));
    const fontSizeScale = d3.scaleSqrt()
        .domain([0, maxSize])
        .range([14, 48]);

    // 创建布局
    const layout = cloud()
        .size([width, height])
        .words(tagData)
        .padding(10)
        .rotate(() => 0)
        .fontSize(d => fontSizeScale(d.size))
        .on('end', draw);

    // 开始布局
    layout.start();

    // 绘制标签
    function draw(words) {
        const cloud = svg.append('g')
            .attr('transform', `translate(${width / 2},${height / 2})`)
            .selectAll('text')
            .data(words)
            .enter()
            .append('text')
            .style('font-size', d => `${d.size}px`)
            .style('font-family', 'PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif')
            .style('fill', (d, i) => colorScale(i))
            .attr('text-anchor', 'middle')
            .attr('transform', d => `translate(${d.x},${d.y}) rotate(${d.rotate})`)
            .text(d => d.text)
            .style('opacity', 0);

        // 添加动画
        cloud.transition()
            .delay((d, i) => i * 50)
            .duration(500)
            .style('opacity', 1);
    }
};

// 渲染阅读习惯图表
const renderReadingHabitsChart = () => {
    if (!readingChart.value) return;

    const chartInstance = getChartInstance(readingChart.value, 'readingHabits');
    if (!chartInstance) return;

    // 处理数据
    const months = Object.keys(data.value.monthly_stats).sort();
    const bookData = months.map(month => data.value.monthly_stats[month].book_count);

    // 设置图表选项
    chartInstance.setOption({
        tooltip: {
            trigger: 'axis',
            formatter: '{b}: {c} 本'
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            top: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: months,
            axisLabel: {
                interval: 3,
                rotate: 45
            }
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name: '阅读量',
                type: 'line',
                smooth: true,
                symbol: 'circle',
                symbolSize: 8,
                sampling: 'average',
                itemStyle: {
                    color: '#41b883'
                },
                areaStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        {
                            offset: 0,
                            color: 'rgba(65, 184, 131, 0.5)'
                        },
                        {
                            offset: 1,
                            color: 'rgba(65, 184, 131, 0.1)'
                        }
                    ])
                },
                data: bookData
            }
        ],
        animationDuration: 2000,
        animationEasing: 'cubicInOut'
    });
};
const renderAfterEnter = () => {
    const watchedTagColors = d3.scaleOrdinal().range(['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51']);
    const wishTagColors = d3.scaleOrdinal().range(['#e76f51', '#f4a261', '#e9c46a', '#2a9d8f', '#264653']);
    if (activeTagsView.value === 'watched' && watchedTagsCloud.value) {
        renderTagCloud(watchedTagsCloud.value, data.value.top3_watched_movie_tags, watchedTagColors);
    } else if (activeTagsView.value === 'wish' && wishTagsCloud.value) {
        renderTagCloud(wishTagsCloud.value, data.value.top3_wish_movie_tags, wishTagColors);
    } else {
        console.warn('Tag cloud ref is null after enter');
    }
};
watch(activeCollection, (newValue) => {
    setTimeout(() => {
        const authorColors = d3.scaleOrdinal()
            .range(['#41b883', '#2c3e50', '#6a8bad']);

        const directorColors = d3.scaleOrdinal()
            .range(['#e76f51', '#f4a261', '#e9c46a']);

        if (newValue === 'books') {
            if (authorsBubbles.value) {
                renderBubbleChart(authorsBubbles.value, data.value.top3_book_authors, authorColors);
            }

            if (publishersBars.value) {
                const bars = publishersBars.value.querySelectorAll('.publisher-bar');
                bars.forEach(bar => {
                    const targetWidth = bar.getAttribute('data-width');
                    gsap.to(bar, {
                        width: targetWidth,
                        duration: 1.5,
                        ease: "power2.out"
                    });
                });
            }
        } else if (newValue === 'movies') {
            if (directorsBubbles.value) {
                renderBubbleChart(directorsBubbles.value, data.value.top3_movie_directors, directorColors);
            }

            if (countriesBars.value) {
                const bars = countriesBars.value.querySelectorAll('.country-bar');
                bars.forEach(bar => {
                    const targetWidth = bar.getAttribute('data-width');
                    gsap.to(bar, {
                        width: targetWidth,
                        duration: 1.5,
                        ease: "power2.out"
                    });
                });
            }
        }
    }, 100);
});
ScrollTrigger.defaults({
    scroller: '.content-layer'
});
// // 初始化动画和可视化
onMounted(() => {

    // 初始化统计数字动画
    statNumbers.value.forEach((el, index) => {
        gsap.from(el, {
            textContent: 0,
            duration: 2,
            ease: "power1.inOut",
            snap: { textContent: 1 },
            stagger: 0.25,
            onUpdate: function () {
                el.textContent = Math.round(el.textContent);
            }
        });
    });

    // 初始化卡片动画
    gsap.from(statCards.value, {

        opacity: 0,
        duration: 0.8,
        stagger: 0.2,
        ease: "back.out(1.7)",
        onComplete: () => {
            statCards.value.forEach(card => card.style.height = '180px'); // 强制恢复高度
        }
    });

    // 初始化时间线图表
    renderTimelineChart();

    // 初始化气泡图颜色
    const authorColors = d3.scaleOrdinal()
        .range(['#41b883', '#2c3e50', '#6a8bad']);

    const directorColors = d3.scaleOrdinal()
        .range(['#e76f51', '#f4a261', '#e9c46a']);

    // 设置滚动触发动画
    ScrollTrigger.create({
        trigger: timelineSection.value,
        start: "top 80%",
        onEnter: () => {
            renderTimelineChart();
        },
    });

    // 书籍卡片动画
    if (bookCard.value) {
        gsap.from(bookCard.value, {
            scrollTrigger: {
                trigger: bookCard.value,
                start: "top 80%"
            },
            x: -50,
            opacity: 0,
            duration: 0.8,
            ease: "power2.out"
        });
    }

    // 电影卡片动画
    if (movieCard.value) {
        gsap.from(movieCard.value, {
            scrollTrigger: {
                trigger: movieCard.value,
                start: "top 80%"
            },
            x: -50,
            opacity: 0,
            duration: 0.8,
            ease: "power2.out"
        });
    }

    // 作者气泡图
    if (authorsBubbles.value && activeCollection.value === 'books') {
        ScrollTrigger.create({
            trigger: authorsBubbles.value,
            start: "top 80%",
            onEnter: () => {
                renderBubbleChart(authorsBubbles.value, data.value.top3_book_authors, authorColors);
            }
        });
    }

    // 导演气泡图
    if (directorsBubbles.value && activeCollection.value === 'movies') {
        ScrollTrigger.create({
            trigger: directorsBubbles.value,
            start: "top 80%",
            onEnter: () => {
                renderBubbleChart(directorsBubbles.value, data.value.top3_movie_directors, directorColors);
            }
        });
    }

    // 出版社条形图动画
    if (publishersBars.value && activeCollection.value === 'books') {
        ScrollTrigger.create({
            trigger: publishersBars.value,
            start: "top 80%",
            onEnter: () => {
                if (!publishersBars.value) {
                    console.warn('publishersBars is null');
                    return;
                }
                const bars = publishersBars.value.querySelectorAll('.publisher-bar');
                bars.forEach(bar => {
                    const targetWidth = bar.getAttribute('data-width');
                    gsap.to(bar, { width: targetWidth, duration: 1.5, ease: "power2.out" });
                });

            }
        });
    }

    // 国家条形图动画
    if (countriesBars.value && activeCollection.value === 'movies') {
        ScrollTrigger.create({
            trigger: countriesBars.value,
            start: "top 80%",
            onEnter: () => {
                const bars = countriesBars.value.querySelectorAll('.country-bar');
                bars.forEach(bar => {
                    const targetWidth = bar.getAttribute('data-width');
                    gsap.to(bar, {
                        width: targetWidth,
                        duration: 1.5,
                        ease: "power2.out"
                    });
                });
            }
        });
    }

    // 标签云
    const watchedTagColors = d3.scaleOrdinal()
        .range(['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51']);

    const wishTagColors = d3.scaleOrdinal()
        .range(['#e76f51', '#f4a261', '#e9c46a', '#2a9d8f', '#264653']);

    if (watchedTagsCloud.value && activeTagsView.value === 'watched') {
        ScrollTrigger.create({
            trigger: tagsSection.value,
            start: "top 80%",
            onEnter: () => {
                const watchedTagColors = d3.scaleOrdinal().range(['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51']);
                const wishTagColors = d3.scaleOrdinal().range(['#e76f51', '#f4a261', '#e9c46a', '#2a9d8f', '#264653']);
                if (activeTagsView.value === 'watched' && watchedTagsCloud.value) {
                    renderTagCloud(watchedTagsCloud.value, data.value.top3_watched_movie_tags, watchedTagColors);
                } else if (activeTagsView.value === 'wish' && wishTagsCloud.value) {
                    renderTagCloud(wishTagsCloud.value, data.value.top3_wish_movie_tags, wishTagColors);
                }
            },
        });
    }



    // 阅读习惯图表
    if (readingChart.value) {
        ScrollTrigger.create({
            trigger: readingHabitsContainer.value,
            start: "top 80%",
            onEnter: () => {
                renderReadingHabitsChart();
            }
        });
    }

    setTimeout(() => {
        ScrollTrigger.refresh();
    }, 100);


});
onBeforeUnmount(() => {
    Object.values(chartInstances.value).forEach(chart => chart.dispose());
    ScrollTrigger.getAll().forEach(trigger => {
        trigger.kill();
    });
});
</script>

<style>
.douban-summary {
    max-width: 1200px;
    margin-left: 220px;
    padding: 2rem;
    font-family: 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
    color: #333;
    background: transparent;
    position: relative;
}

/* 背景装饰 */
.background-decoration {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    overflow: hidden;
    pointer-events: none;
}

.circle {
    position: absolute;
    border-radius: 50%;
    opacity: 0.05;
}

.circle-1 {
    top: -10%;
    right: -5%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, #41b883 0%, transparent 70%);
    animation: float 15s ease-in-out infinite;
}

.circle-2 {
    bottom: -15%;
    left: -10%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, #e76f51 0%, transparent 70%);
    animation: float 20s ease-in-out infinite reverse;
}

.circle-3 {
    top: 40%;
    right: 20%;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, #f4a261 0%, transparent 70%);
    animation: float 12s ease-in-out infinite;
}

@keyframes float {
    0% {
        transform: translate(0, 0) rotate(0deg);
    }

    50% {
        transform: translate(20px, 20px) rotate(5deg);
    }

    100% {
        transform: translate(0, 0) rotate(0deg);
    }
}

/* 标题样式 */
header {
    position: relative;
    z-index: 1;
    text-align: center;
    margin-bottom: 4rem;
}

.title {
    position: relative;
    display: inline-block;
    margin-bottom: 3rem;
}

.title-text {
    font-size: 2.8rem;
    font-weight: 300;
    color: #2c3e50;
    letter-spacing: 2px;
}

.title-underline {
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 120px;
    height: 3px;
    background: linear-gradient(90deg, #41b883, #e76f51);
}

/* 统计卡片 */
.summary-stats {
    display: flex;
    justify-content: center;
    height: auto;
    gap: 2rem;

}

.stat-card {
    margin-top: 20px;
    position: relative;
    width: 180px;
    height: 180px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    background-image: linear-gradient(to top, #f5ecee 0%, #e9f0fa 99%, #e2ebfa 100%);
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
    padding: 1.5rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease;

}

.stat-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

.stat-number {
    font-size: 3rem;
    font-weight: 300;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 1rem;
    color: #666;
}

.stat-icon {
    position: absolute;
    bottom: 15px;
    right: 15px;
    width: 40px;
    height: 40px;
    opacity: 0.2;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
}

.book-icon {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2341b883' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 19.5A2.5 2.5 0 0 1 6.5 17H20'%3E%3C/path%3E%3Cpath d='M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z'%3E%3C/path%3E%3C/svg%3E");
}

.movie-icon {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23e76f51' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='2' y='2' width='20' height='20' rx='2.18' ry='2.18'%3E%3C/rect%3E%3Cline x1='7' y1='2' x2='7' y2='22'%3E%3C/line%3E%3Cline x1='17' y1='2' x2='17' y2='22'%3E%3C/line%3E%3Cline x1='2' y1='12' x2='22' y2='12'%3E%3C/line%3E%3Cline x1='2' y1='7' x2='7' y2='7'%3E%3C/line%3E%3Cline x1='2' y1='17' x2='7' y2='17'%3E%3C/line%3E%3Cline x1='17' y1='17' x2='22' y2='17'%3E%3C/line%3E%3Cline x1='17' y1='7' x2='22' y2='7'%3E%3C/line%3E%3C/svg%3E");
}

.wish-book-icon {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2341b883' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z'%3E%3C/path%3E%3C/svg%3E");
}

.wish-movie-icon {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23e76f51' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolygon points='12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2'%3E%3C/polygon%3E%3C/svg%3E");
}

/* 时间线部分 */
.timeline-section {
    position: relative;
    z-index: 1;
    margin-bottom: 4rem;
}

.timeline-container {
    background: transparent;
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
    padding: 2rem;
}

.timeline-controls {
    display: flex;
    justify-content: center;
    margin-bottom: 1.5rem;
}

.timeline-controls button {
    background: none;
    border: none;
    padding: 0.5rem 1.5rem;
    margin: 0 0.5rem;
    font-size: 1rem;
    color: #666;
    cursor: pointer;
    border-radius: 20px;
    transition: all 0.3s ease;
}

.timeline-controls button.active {
    background-color: #41b883;
    color: white;
    box-shadow: 0 4px 10px rgba(65, 184, 131, 0.3);
}

.timeline-chart {
    width: 100%;
    height: 400px;
}

/* 收藏部分 */
.collections-section {
    position: relative;
    z-index: 1;
    margin-bottom: 4rem;
}

.collections-container {
    background: transparent;
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
    padding: 2rem;
}

.collection-tabs {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
}

.collection-tabs button {
    background: none;
    border: none;
    padding: 0.5rem 1.5rem;
    margin: 0 0.5rem;
    font-size: 1rem;
    color: #666;
    cursor: pointer;
    border-radius: 20px;
    transition: all 0.3s ease;
}

.collection-tabs button.active {
    background-color: #e76f51;
    color: white;
    box-shadow: 0 4px 10px rgba(231, 111, 81, 0.3);
}

.collection-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

.collection-card {
    display: flex;
    flex-direction: column;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 100%;
}

.collection-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
}

.card-image {
    position: relative;
    height: 300px;
    overflow: hidden;
}

.card-image img {
    width: 100%;
    height: 100%;
    object-fit: scale-down;
    transition: transform 0.5s ease;
}

.collection-card:hover .card-image img {
    transform: scale(1.05);
}

.card-overlay {
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

.collection-card:hover .card-overlay {
    opacity: 1;
}

.card-link {
    display: inline-block;
    padding: 0.8rem 1.5rem;
    background-color: #fff;
    color: #2c3e50;
    text-decoration: none;
    border-radius: 30px;
    font-weight: 500;
    transform: translateY(20px);
    transition: transform 0.3s ease;
}

.collection-card:hover .card-link {
    transform: translateY(0);
}

.card-content {
    flex: 1;
    padding: 1.5rem;
    position: relative;
}

.card-badge {
    position: absolute;
    top: -15px;
    right: 20px;
    background: linear-gradient(90deg, #41b883, #2c3e50);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 500;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.movie-card .card-badge {
    background: linear-gradient(90deg, #e76f51, #f4a261);
}

.card-content h3 {
    margin-top: 0.5rem;
    margin-bottom: 1rem;
    font-size: 1.3rem;
    color: #2c3e50;
}

.card-author,
.card-director {
    font-weight: 500;
    color: #41b883;
    margin-bottom: 0.5rem;
}

.movie-card .card-director {
    color: #e76f51;
}

.card-publisher,
.card-country,
.card-genre {
    color: #666;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
}

.card-date {
    display: flex;
    align-items: center;
    margin-top: 1rem;
    color: #999;
    font-size: 0.8rem;
}

.date-icon {
    display: inline-block;
    width: 16px;
    height: 16px;
    margin-right: 5px;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23999' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E");
    background-size: contain;
    background-repeat: no-repeat;
}

/* 气泡可视化 */
.authors-visualization,
.directors-visualization {
    grid-column: span 2;
    background: transparent;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.authors-bubbles,
.directors-bubbles {
    width: 100%;
    height: 350px;
}

/* 条形图可视化 */
.publishers-visualization,
.countries-visualization {
    grid-column: span 2;
    background: transparent;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    margin-top: 2rem;
}

.publisher-bar-container,
.country-bar-container {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}

.publisher-name,
.country-name {
    width: 150px;
    font-size: 0.9rem;
    color: #666;
    text-align: right;
    padding-right: 1rem;
}

.publisher-bar-wrapper,
.country-bar-wrapper {
    flex: 1;
    height: 30px;
    background-color: #f1f1f1;
    border-radius: 15px;
    position: relative;
    overflow: hidden;
}

.publisher-bar,
.country-bar {
    height: 100%;
    border-radius: 15px;
    position: relative;
}

.publisher-bar {
    background: linear-gradient(90deg, #41b883, #2c3e50);
}

.country-bar {
    background: linear-gradient(90deg, #e76f51, #f4a261);
}

.publisher-count,
.country-count {
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    color: rgb(50, 50, 4);
    font-weight: 500;
    font-size: 0.9rem;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

/* 标签云部分 */
.tags-section {
    position: relative;
    z-index: 1;
    margin-bottom: 4rem;
}

.tags-container {
    background: transparent;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
    border-radius: 12px;
    padding: 2rem;
}

.tags-tabs {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
}

.tags-tabs button {
    background: none;
    border: none;
    padding: 0.5rem 1.5rem;
    margin: 0 0.5rem;
    font-size: 1rem;
    color: #666;
    cursor: pointer;
    border-radius: 20px;
    transition: all 0.3s ease;
}

.tags-tabs button.active {
    background-color: #2a9d8f;
    color: white;
    box-shadow: 0 4px 10px rgba(42, 157, 143, 0.3);
}

.tags-cloud {
    width: 100%;
    height: 300px;
}

/* 阅读习惯部分 */
.reading-habits-section {
    position: relative;
    z-index: 1;
    margin-bottom: 4rem;
}

.reading-habits-container {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 2rem;
}

.reading-chart {
    background: transparent;
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
    padding: 2rem;
    height: 400px;
}

.reading-insights {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.insight-card {
    background-image: linear-gradient(to top, #f5ecee 0%, #e9f0fa 99%, #e2ebfa 100%);
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
    padding: 1.5rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    transition: transform 0.3s ease;
}

.insight-card:hover {
    transform: translateY(-5px);
}

.insight-icon {
    width: 40px;
    height: 40px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    opacity: 0.8;
}

.book-icon {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2341b883' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 19.5A2.5 2.5 0 0 1 6.5 17H20'%3E%3C/path%3E%3Cpath d='M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z'%3E%3C/path%3E%3C/svg%3E");
}

.calendar-icon {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23e76f51' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E");
}

.insight-content h3 {
    margin-top: 0;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
    color: #2c3e50;
}

.insight-content p {
    margin: 0;
    color: #666;
    font-size: 0.9rem;
    line-height: 1.5;
}

.insight-content strong {
    color: #41b883;
}

/* 过渡动画 */
.collection-fade-enter-active,
.collection-fade-leave-active {
    transition: opacity 0.5s ease;
}

.collection-fade-enter-from,
.collection-fade-leave-to {
    opacity: 0;
}

.tags-fade-enter-active,
.tags-fade-leave-active {
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.tags-fade-enter-from,
.tags-fade-leave-to {
    opacity: 0;
    transform: translateY(20px);
}
</style>