<template>
    <div class="reading-stats-container">
        <div class="menu-container">
            <el-menu :default-active="activeMenu" class="stats-menu" mode="horizontal" @select="handleMenuSelect"
                text-color="#1a1a1a" active-text-color="#409EFF">
                <el-menu-item index="overview1"> </el-menu-item>
                <el-menu-item index="overview2"> </el-menu-item>
                <el-menu-item index="overview3"> </el-menu-item>
                <el-menu-item index="overview">总览</el-menu-item>
                <el-menu-item index="yearly">按年</el-menu-item>
                <el-menu-item index="monthly">按月</el-menu-item>
                <el-menu-item index="weekly">按周</el-menu-item>
            </el-menu>
        </div>

        <!-- 总览 -->
        <div v-if="activeMenu === 'overview' && readingData" class="overview-section">
            <!-- 2.7 Total Read Time and Registration Time -->
            <div class="stats-summary">
                <div class="total-time">
                    <h2>总阅读时间</h2>
                    <p>{{ formatReadTime(readingData.totalReadTime) }}</p>
                </div>
                <div class="regist-time">
                    <h2>注册时间</h2>
                    <p>{{ formatDate(readingData.registTime) }}</p>
                </div>
            </div>

            <!-- Share Info -->
            <div class="share-info">
                <div class="share-item">
                    <h4>完成阅读</h4>
                    <p>{{ readingData.shareInfo.finishReadingCount }} 本</p>
                </div>
                <div class="share-item">
                    <h4>阅读过</h4>
                    <p>{{ readingData.shareInfo.hadReadingCount }} 本</p>
                </div>
                <div class="share-item">
                    <h4>笔记数</h4>
                    <p>{{ readingData.shareInfo.notesCount }} 条</p>
                </div>
                <div class="share-item">
                    <h4>阅读天数</h4>
                    <p>{{ readingData.shareInfo.totalReadingDay }} 天</p>
                </div>
            </div>

            <div class="chart-container">
                <h2>偏好作者</h2>
                <div ref="wordCloudChartEl" class="chart"></div>
            </div>

            <div class="books-container">
                <h2>阅读排行</h2>
                <div class="books-grid">
                    <div v-for="(book, index) in readingData.preferBooks" :key="index" class="book-card">
                        <div class="book-cover">
                            <img :src="book.bookInfo.cover" :alt="book.bookInfo.title" />
                        </div>
                        <div class="book-info">
                            <h4>{{ book.bookInfo.title }}</h4>
                            <p class="book-title">{{ book.title }}</p>
                            <p class="book-reason">{{ book.reason }}</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 2.3 Radar Chart for preferCategory -->
            <div class="chart-container">
                <h2>{{ readingData.preferCategoryWord }}</h2>
                <div ref="categoryRadarEl" class="chart"></div>
            </div>

            <!-- 2.4 Bar Chart for preferTime -->
            <div class="chart-container">
                <h2>{{ readingData.preferTimeWord }}</h2>
                <div ref="timeBarEl" class="chart"></div>
            </div>

            <!-- 2.5 Podium for readLongest -->
            <div v-if="readingData.readLongest && readingData.readLongest.length >= 3" class="podium-container">
                <h2>最长阅读时间</h2>
                <div class="podium">
                    <div class="podium-item second-place">
                        <div class="podium-book">
                            <img :src="readingData.readLongest[1].book.cover"
                                :alt="readingData.readLongest[1].book.title" />
                            <div class="podium-info">
                                <h4>{{ readingData.readLongest[1].book.title }}</h4>
                                <p>{{ formatReadTime(readingData.readLongest[1].readTime) }}</p>
                            </div>
                        </div>
                        <div class="podium-block">2</div>
                    </div>
                    <div class="podium-item first-place">
                        <div class="podium-book">
                            <img :src="readingData.readLongest[0].book.cover"
                                :alt="readingData.readLongest[0].book.title" />
                            <div class="podium-info">
                                <h4>{{ readingData.readLongest[0].book.title }}</h4>
                                <p>{{ formatReadTime(readingData.readLongest[0].readTime) }}</p>
                            </div>
                        </div>
                        <div class="podium-block">1</div>
                    </div>
                    <div class="podium-item third-place">
                        <div class="podium-book">
                            <img :src="readingData.readLongest[2].book.cover"
                                :alt="readingData.readLongest[2].book.title" />
                            <div class="podium-info">
                                <h4>{{ readingData.readLongest[2].book.title }}</h4>
                                <p>{{ formatReadTime(readingData.readLongest[2].readTime) }}</p>
                            </div>
                        </div>
                        <div class="podium-block">3</div>
                    </div>
                </div>
            </div>

            <!-- 2.6 Yearly Reading Times -->
            <div class="chart-container">
                <h2>年度阅读时间</h2>
                <div ref="yearlyChartEl" class="chart"></div>
            </div>


        </div>
        <!-- 年度 -->
        <div v-if="activeMenu === 'yearly' && readingData_year" class="overview-section">
            <div class="stats-summary">
                <div class="total-time">
                    <h2>总阅读时间</h2>
                    <p>{{ formatReadTime(readingData_year.totalReadTime) }}</p>
                </div>

                <div class="regist-time">
                    <h2>比去年</h2>
                    <p>{{ formatRatio(readingData_year.compare) }}%</p>
                </div>
            </div>
            <div class="share-info">
                <div class="share-item">
                    <h4>完成阅读</h4>
                    <p>{{ readingData_year.shareInfo.finishReadingCount }} 本</p>
                </div>
                <div class="share-item">
                    <h4>阅读过</h4>
                    <p>{{ readingData_year.shareInfo.hadReadingCount }} 本</p>
                </div>
                <div class="share-item">
                    <h4>笔记数</h4>
                    <p>{{ readingData_year.shareInfo.notesCount }} 条</p>
                </div>
                <div class="share-item">
                    <h4>阅读天数</h4>
                    <p>{{ readingData_year.shareInfo.totalReadingDay }} 天</p>
                </div>
            </div>
            <!-- 偏好的种类 -->
            <div class="chart-container">
                <h2>{{ readingData_year.preferCategoryWord }}</h2>
                <div ref="categoryRadarEl" class="chart"></div>
            </div>
            <!-- 阅读量前三的 -->
            <div v-if="readingData_year.readLongest && readingData_year.readLongest.length >= 3"
                class="podium-container">
                <h2>最长阅读时间</h2>
                <div class="podium">
                    <div class="podium-item second-place">
                        <div class="podium-book">
                            <img :src="readingData_year.readLongest[1].book.cover"
                                :alt="readingData_year.readLongest[1].book.title" />
                            <div class="podium-info">
                                <h4>{{ readingData_year.readLongest[1].book.title }}</h4>
                                <p>{{ formatReadTime(readingData_year.readLongest[1].readTime) }}</p>
                            </div>
                        </div>
                        <div class="podium-block">2</div>
                    </div>
                    <div class="podium-item first-place">
                        <div class="podium-book">
                            <img :src="readingData_year.readLongest[0].book.cover"
                                :alt="readingData_year.readLongest[0].book.title" />
                            <div class="podium-info">
                                <h4>{{ readingData_year.readLongest[0].book.title }}</h4>
                                <p>{{ formatReadTime(readingData_year.readLongest[0].readTime) }}</p>
                            </div>
                        </div>
                        <div class="podium-block">1</div>
                    </div>
                    <div class="podium-item third-place">
                        <div class="podium-book">
                            <img :src="readingData_year.readLongest[2].book.cover"
                                :alt="readingData_year.readLongest[2].book.title" />
                            <div class="podium-info">
                                <h4>{{ readingData_year.readLongest[2].book.title }}</h4>
                                <p>{{ formatReadTime(readingData_year.readLongest[2].readTime) }}</p>
                            </div>
                        </div>
                        <div class="podium-block">3</div>
                    </div>
                </div>
            </div>
            <!-- 年度 365 的热力图 -->
            <div class="hot-map">
                <div ref="hotMapEl" class="chart">
                    <!-- 日均阅读时长 -->
                    <!-- <h2>{{ formatReadTime(readingData_year.dayAverageReadTime) }}</h2> -->
                </div>
            </div>
        </div>
        <!-- 月度 -->
        <div v-if="activeMenu === 'monthly' && readingData_month" class="overview-section">
            <div class="stats-summary">
                <div class="total-time">
                    <h2>总阅读时间</h2>
                    <p>{{ formatReadTime(readingData_month.totalReadTime) }}</p>
                </div>

                <div class="regist-time">
                    <h2>比上月</h2>
                    <p>{{ formatRatio(readingData_month.compare) }}%</p>
                </div>
            </div>
            <div class="share-info">
                <div class="share-item">
                    <h4>完成阅读</h4>
                    <p>{{ readingData_month.shareInfo.finishReadingCount }} 本</p>
                </div>
                <div class="share-item">
                    <h4>阅读过</h4>
                    <p>{{ readingData_month.shareInfo.hadReadingCount }} 本</p>
                </div>
                <div class="share-item">
                    <h4>笔记数</h4>
                    <p>{{ readingData_month.shareInfo.notesCount }} 条</p>
                </div>
                <div class="share-item">
                    <h4>阅读天数</h4>
                    <p>{{ readingData_month.shareInfo.totalReadingDay }} 天</p>
                </div>
            </div>
            <!-- 偏好的种类 -->
            <div class="chart-container">
                <h2>{{ readingData_month.preferCategoryWord }}</h2>
                <div ref="categoryRadarEl" class="chart"></div>
            </div>
            <!-- 阅读量前三的 -->
            <div v-if="readingData_month.readLongest && readingData_month.readLongest.length >= 3"
                class="podium-container">
                <h2>最长阅读时间</h2>
                <div class="podium">
                    <div class="podium-item second-place">
                        <div class="podium-book">
                            <img :src="readingData_month.readLongest[1].book.cover"
                                :alt="readingData_month.readLongest[1].book.title" />
                            <div class="podium-info">
                                <h4>{{ readingData_month.readLongest[1].book.title }}</h4>
                                <p>{{ formatReadTime(readingData_month.readLongest[1].readTime) }}</p>
                            </div>
                        </div>
                        <div class="podium-block">2</div>
                    </div>
                    <div class="podium-item first-place">
                        <div class="podium-book">
                            <img :src="readingData_month.readLongest[0].book.cover"
                                :alt="readingData_month.readLongest[0].book.title" />
                            <div class="podium-info">
                                <h4>{{ readingData_month.readLongest[0].book.title }}</h4>
                                <p>{{ formatReadTime(readingData_month.readLongest[0].readTime) }}</p>
                            </div>
                        </div>
                        <div class="podium-block">1</div>
                    </div>
                    <div class="podium-item third-place">
                        <div class="podium-book">
                            <img :src="readingData_month.readLongest[2].book.cover"
                                :alt="readingData_month.readLongest[2].book.title" />
                            <div class="podium-info">
                                <h4>{{ readingData_month.readLongest[2].book.title }}</h4>
                                <p>{{ formatReadTime(readingData_month.readLongest[2].readTime) }}</p>
                            </div>
                        </div>
                        <div class="podium-block">3</div>
                    </div>
                </div>
            </div>
            <!-- 月度 柱状图 -->
            <div class="chart-container">
                <h2>每日阅读时间</h2>
                <div ref="timeBarMonthlyEl" class="chart"></div>
            </div>
        </div>
        <!-- 周度 -->
        <div v-if="activeMenu === 'weekly' && readingData_week" class="overview-section">
            <div class="stats-summary">
                <div class="total-time">
                    <h2>总阅读时间</h2>
                    <p>{{ formatReadTime(readingData_week.totalReadTime) }}</p>
                </div>

                <div class="regist-time">
                    <h2>比上周</h2>
                    <p>{{ formatRatio(readingData_week.compare) }}%</p>
                </div>
            </div>
            <div class="stats-summary">
                <div class="total-time">
                    <h2>排行</h2>
                    <p>{{ readingData_week.rank.text }}</p>
                </div>

                <div class="regist-time">
                    <h2>平均每日阅读</h2>
                    <p>{{ formatReadTime(readingData_week.dayAverageReadTime) }}</p>
                </div>
            </div>
            <div class="share-info">
                <div class="share-item">
                    <h4>完成阅读</h4>
                    <p>{{ readingData_week.shareInfo.finishReadingCount }} 本</p>
                </div>
                <div class="share-item">
                    <h4>阅读过</h4>
                    <p>{{ readingData_week.shareInfo.hadReadingCount }} 本</p>
                </div>
                <div class="share-item">
                    <h4>笔记数</h4>
                    <p>{{ readingData_week.shareInfo.notesCount }} 条</p>
                </div>
                <div class="share-item">
                    <h4>阅读天数</h4>
                    <p>{{ readingData_week.shareInfo.totalReadingDay }} 天</p>
                </div>
            </div>
            <div class="chart-container">
                <h2>每天阅读时间</h2>
                <div ref="timeBarweeklyEl" class="chart"></div>
            </div>

        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, nextTick, onUnmounted } from 'vue';
import * as echarts from 'echarts';
import 'echarts-wordcloud';
import dayjs from 'dayjs';
import isoWeek from 'dayjs/plugin/isoWeek';
dayjs.extend(isoWeek);
const wordCloudChartEl = ref(null);
const categoryRadarEl = ref(null);
const timeBarEl = ref(null);
const timeBarMonthlyEl = ref(null);
const timeBarweeklyEl = ref(null);
const yearlyChartEl = ref(null);
const hotMapEl = ref(null);
const activeMenu = ref('overview');
const readingData = ref(null)
const readingData_year = ref(null)
const readingData_month = ref(null)
const readingData_week = ref(null)
const chartInstances = [];
const handleMenuSelect = (key) => {
    activeMenu.value = key;
    initTab(key);
};

const formatReadTime = (seconds) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const seconds_left = seconds - hours * 3600 - minutes * 60;
    if (hours != 0) {
        return `${hours}小时${minutes}分钟`;
    }
    else {
        return `${minutes}分钟${seconds_left}秒`;
    }

};
const formatRatio = (ratioValue) => {
    const percentage = ratioValue * 100;
    return `${percentage >= 10 ? '+' : '-'}${(Math.abs(percentage)).toFixed(2)}`;
}
const formatDate = (timestamp) => {
    return dayjs.unix(timestamp).format('YYYY-MM-DD');
};

const fetchReadingData = async (time_type) => {
    if (time_type == 'overview') {
        return {
            "preferAuthor": [
                { "name": "尹维安", "value": 100 },
                { "name": "村上春树", "value": 85 },
                { "name": "东野圭吾", "value": 70 },
                { "name": "刘慈欣", "value": 65 },
                { "name": "余华", "value": 60 },
                { "name": "卡勒德·胡赛尼", "value": 55 },
                { "name": "刘擎", "value": 50 },
                { "name": "马克·李维", "value": 45 },
                { "name": "毛姆", "value": 40 },
                { "name": "加西亚·马尔克斯", "value": 35 }
            ],
            "preferBooks": [
                {
                    "bookInfo": {
                        "bookId": "23774470",
                        "cover": "https://cdn.weread.qq.com/weread/cover/46/YueWen_23774470/s_YueWen_23774470.jpg",
                        "title": "走出剧情"
                    },
                    "reason": "阅读至23:54",
                    "title": "读到深夜"
                },
                {
                    "bookInfo": {
                        "bookId": "25947490",
                        "cover": "https://cdn.weread.qq.com/weread/cover/66/YueWen_25947490/s_YueWen_25947490.jpg",
                        "title": "天才在左 疯子在右"
                    },
                    "reason": "2021/09/10/阅读",
                    "title": "第一本阅读"
                },
                {
                    "bookInfo": {
                        "bookId": "32535536",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/%E4%B8%80%E4%BA%BA%E4%BB%BD%E7%9A%84%E7%83%AD%E9%97%B9.png",
                        "title": "一人份的热闹"
                    },
                    "reason": "阅读了4小时",
                    "title": "最爱文学"
                },
                {
                    "bookInfo": {
                        "bookId": "40422961",
                        "cover": "https://cdn.weread.qq.com/weread/cover/68/YueWen_40422961/s_YueWen_40422961.jpg",
                        "title": "喂——出来：星新一脑洞小说集（译林幻系列）"
                    },
                    "reason": "分享5次",
                    "title": "最爱分享"
                },
                {
                    "bookInfo": {
                        "bookId": "838717",
                        "cover": "https://cdn.weread.qq.com/weread/cover/60/YueWen_838717/s_YueWen_838717.jpg",
                        "title": "优秀的绵羊"
                    },
                    "reason": "3位好友也爱读",
                    "title": "共读最多"
                },
                {
                    "bookInfo": {
                        "bookId": "32535536",
                        "cover":  "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/%E4%B8%80%E4%BA%BA%E4%BB%BD%E7%9A%84%E7%83%AD%E9%97%B9.png",
                        "title": "一人份的热闹"
                    },
                    "reason": "仅有7571人读过",
                    "title": "欣赏小众"
                },
                {
                    "bookInfo": {
                        "bookId": "522205",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/2000014295065.webp",
                        "title": "人性的弱点"
                    },
                    "reason": "7天只读了26%",
                    "title": "总有一天读完"
                }
            ],
            "preferCategory": [
                {
                    "categoryTitle": "文学",
                    "val": 100
                },
                {
                    "categoryTitle": "个人成长",
                    "val": 46
                },
                {
                    "categoryTitle": "科幻小说",
                    "val": 39
                },
                {
                    "categoryTitle": "心理",
                    "val": 25
                },
                {
                    "categoryTitle": "经济理财",
                    "val": 22
                },
                {
                    "categoryTitle": "哲学宗教",
                    "val": 19
                },
                {
                    "categoryTitle": "社会小说",
                    "val": 18
                },
                {
                    "categoryTitle": "艺术",
                    "val": 17
                }
            ],
            "preferCategoryWord": "偏好阅读文学",
            "preferTime": [
                661,
                2013,
                9983,
                15252,
                22495,
                13518,
                7047,
                10327,
                17054,
                18229,
                22622,
                28440,
                14346,
                20292,
                28016,
                26999,
                43864,
                34740,
                626,
                863,
                1373,
                0,
                0,
                0
            ],
            "preferTimeWord": "偏好夜晚阅读",
            "readLongest": [
                {
                    "book": {
                        "author": "Administrator",
                        "bookId": "CB_GG10bh0cy97L6mp6l56XJ9pv",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/61edWWJk7jL._SL1500_.jpg",
                        "title": "刘擎"
                    },
                    "readTime": 24192
                },
                {
                    "book": {
                        "author": "尹维安",
                        "bookId": "32535536",
                        "cover":  "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/%E4%B8%80%E4%BA%BA%E4%BB%BD%E7%9A%84%E7%83%AD%E9%97%B9.png",
                        "title": "一人份的热闹"
                    },
                    "readTime": 17359
                },
                {
                    "book": {
                        "author": "戴尔·卡耐基",
                        "bookId": "32535536",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/2000014295065.webp",
                        "title": "人性的弱点"
                    },
                    "readTime": 16359
                }
            ],
            "readTimes": {
                "1514736000": 0,
                "1546272000": 0,
                "1577808000": 0,
                "1609430400": 5973,
                "1640966400": 120104,
                "1672502400": 121903,
                "1704038400": 89291,
                "1735660800": 28301
            },
            "registTime": 1631272295,
            "shareInfo": {
                "finishReadingCount": 11,
                "hadReadingCount": 101,
                "notesCount": 114,
                "totalReadingDay": 395
            },
            "totalReadTime": 365572
        };
    } else if (time_type == 'yearly') {
        return {
            "compare": 0.09334098621361615,
            "dailyReadTimes": {
                "1735660800": 51,
                "1735747200": 0,
                "1735833600": 0,
                "1735920000": 4675,
                "1736006400": 0,
                "1736092800": 0,
                "1736179200": 4162,
                "1736265600": 0,
                "1736352000": 871,
                "1736438400": 967,
                "1736524800": 265,
                "1736611200": 87,
                "1736697600": 1663,
                "1736784000": 3,
                "1736870400": 0,
                "1736956800": 0,
                "1737043200": 0,
                "1737129600": 6764,
                "1737216000": 0,
                "1737302400": 0,
                "1737388800": 1,
                "1737475200": 0,
                "1737561600": 0,
                "1737648000": 0,
                "1737734400": 1848,
                "1737820800": 706,
                "1737907200": 151,
                "1737993600": 0,
                "1738080000": 0,
                "1738166400": 0,
                "1738252800": 1155,
                "1738339200": 5,
                "1738425600": 0,
                "1738512000": 0,
                "1738598400": 0,
                "1738684800": 0,
                "1738771200": 0,
                "1738857600": 0,
                "1738944000": 1723,
                "1739030400": 8,
                "1739116800": 0,
                "1739203200": 855,
                "1739289600": 0,
                "1739376000": 0,
                "1739462400": 0,
                "1739548800": 0,
                "1739635200": 42,
                "1739721600": 1715,
                "1739808000": 378,
                "1739894400": 0,
                "1739980800": 0,
                "1740067200": 0,
                "1740153600": 0,
                "1740240000": 0,
                "1740326400": 1,
                "1740412800": 181,
                "1740499200": 0,
                "1740585600": 24,
                "1740672000": 0,
                "1740758400": 0,
                "1740844800": 0,
                "1740931200": 0,
                "1741017600": 0,
                "1741104000": 0,
                "1741190400": 0,
                "1741276800": 0,
                "1741363200": 0,
                "1741449600": 0,
                "1741536000": 0,
                "1741622400": 0,
                "1741708800": 0,
                "1741795200": 0,
                "1741881600": 0,
                "1741968000": 0,
                "1742054400": 0,
                "1742140800": 0,
                "1742227200": 0,
                "1742313600": 0,
                "1742400000": 0,
                "1742486400": 0,
                "1742572800": 0,
                "1742659200": 0,
                "1742745600": 0,
                "1742832000": 0,
                "1742918400": 0,
                "1743004800": 0,
                "1743091200": 0,
                "1743177600": 0,
                "1743264000": 0,
                "1743350400": 0,
                "1743436800": 0,
                "1743523200": 0,
                "1743609600": 0,
                "1743696000": 0,
                "1743782400": 0,
                "1743868800": 0,
                "1743955200": 0,
                "1744041600": 0,
                "1744128000": 0,
                "1744214400": 0,
                "1744300800": 0,
                "1744387200": 0,
                "1744473600": 0,
                "1744560000": 0,
                "1744646400": 0,
                "1744732800": 0,
                "1744819200": 0,
                "1744905600": 0,
                "1744992000": 0,
                "1745078400": 0,
                "1745164800": 0,
                "1745251200": 0,
                "1745337600": 0,
                "1745424000": 0,
                "1745510400": 0,
                "1745596800": 0,
                "1745683200": 0,
                "1745769600": 0,
                "1745856000": 0,
                "1745942400": 0,
                "1746028800": 0,
                "1746115200": 0,
                "1746201600": 0,
                "1746288000": 0,
                "1746374400": 0,
                "1746460800": 0,
                "1746547200": 0,
                "1746633600": 0,
                "1746720000": 0,
                "1746806400": 0,
                "1746892800": 0,
                "1746979200": 0,
                "1747065600": 0,
                "1747152000": 0,
                "1747238400": 0,
                "1747324800": 0,
                "1747411200": 0,
                "1747497600": 0,
                "1747584000": 0,
                "1747670400": 0,
                "1747756800": 0,
                "1747843200": 0,
                "1747929600": 0,
                "1748016000": 0,
                "1748102400": 0,
                "1748188800": 0,
                "1748275200": 0,
                "1748361600": 0,
                "1748448000": 0,
                "1748534400": 0,
                "1748620800": 0,
                "1748707200": 0,
                "1748793600": 0,
                "1748880000": 0,
                "1748966400": 0,
                "1749052800": 0,
                "1749139200": 0,
                "1749225600": 0,
                "1749312000": 0,
                "1749398400": 0,
                "1749484800": 0,
                "1749571200": 0,
                "1749657600": 0,
                "1749744000": 0,
                "1749830400": 0,
                "1749916800": 0,
                "1750003200": 0,
                "1750089600": 0,
                "1750176000": 0,
                "1750262400": 0,
                "1750348800": 0,
                "1750435200": 0,
                "1750521600": 0,
                "1750608000": 0,
                "1750694400": 0,
                "1750780800": 0,
                "1750867200": 0,
                "1750953600": 0,
                "1751040000": 0,
                "1751126400": 0,
                "1751212800": 0,
                "1751299200": 0,
                "1751385600": 0,
                "1751472000": 0,
                "1751558400": 0,
                "1751644800": 0,
                "1751731200": 0,
                "1751817600": 0,
                "1751904000": 0,
                "1751990400": 0,
                "1752076800": 0,
                "1752163200": 0,
                "1752249600": 0,
                "1752336000": 0,
                "1752422400": 0,
                "1752508800": 0,
                "1752595200": 0,
                "1752681600": 0,
                "1752768000": 0,
                "1752854400": 0,
                "1752940800": 0,
                "1753027200": 0,
                "1753113600": 0,
                "1753200000": 0,
                "1753286400": 0,
                "1753372800": 0,
                "1753459200": 0,
                "1753545600": 0,
                "1753632000": 0,
                "1753718400": 0,
                "1753804800": 0,
                "1753891200": 0,
                "1753977600": 0,
                "1754064000": 0,
                "1754150400": 0,
                "1754236800": 0,
                "1754323200": 0,
                "1754409600": 0,
                "1754496000": 0,
                "1754582400": 0,
                "1754668800": 0,
                "1754755200": 0,
                "1754841600": 0,
                "1754928000": 0,
                "1755014400": 0,
                "1755100800": 0,
                "1755187200": 0,
                "1755273600": 0,
                "1755360000": 0,
                "1755446400": 0,
                "1755532800": 0,
                "1755619200": 0,
                "1755705600": 0,
                "1755792000": 0,
                "1755878400": 0,
                "1755964800": 0,
                "1756051200": 0,
                "1756137600": 0,
                "1756224000": 0,
                "1756310400": 0,
                "1756396800": 0,
                "1756483200": 0,
                "1756569600": 0,
                "1756656000": 0,
                "1756742400": 0,
                "1756828800": 0,
                "1756915200": 0,
                "1757001600": 0,
                "1757088000": 0,
                "1757174400": 0,
                "1757260800": 0,
                "1757347200": 0,
                "1757433600": 0,
                "1757520000": 0,
                "1757606400": 0,
                "1757692800": 0,
                "1757779200": 0,
                "1757865600": 0,
                "1757952000": 0,
                "1758038400": 0,
                "1758124800": 0,
                "1758211200": 0,
                "1758297600": 0,
                "1758384000": 0,
                "1758470400": 0,
                "1758556800": 0,
                "1758643200": 0,
                "1758729600": 0,
                "1758816000": 0,
                "1758902400": 0,
                "1758988800": 0,
                "1759075200": 0,
                "1759161600": 0,
                "1759248000": 0,
                "1759334400": 0,
                "1759420800": 0,
                "1759507200": 0,
                "1759593600": 0,
                "1759680000": 0,
                "1759766400": 0,
                "1759852800": 0,
                "1759939200": 0,
                "1760025600": 0,
                "1760112000": 0,
                "1760198400": 0,
                "1760284800": 0,
                "1760371200": 0,
                "1760457600": 0,
                "1760544000": 0,
                "1760630400": 0,
                "1760716800": 0,
                "1760803200": 0,
                "1760889600": 0,
                "1760976000": 0,
                "1761062400": 0,
                "1761148800": 0,
                "1761235200": 0,
                "1761321600": 0,
                "1761408000": 0,
                "1761494400": 0,
                "1761580800": 0,
                "1761667200": 0,
                "1761753600": 0,
                "1761840000": 0,
                "1761926400": 0,
                "1762012800": 0,
                "1762099200": 0,
                "1762185600": 0,
                "1762272000": 0,
                "1762358400": 0,
                "1762444800": 0,
                "1762531200": 0,
                "1762617600": 0,
                "1762704000": 0,
                "1762790400": 0,
                "1762876800": 0,
                "1762963200": 0,
                "1763049600": 0,
                "1763136000": 0,
                "1763222400": 0,
                "1763308800": 0,
                "1763395200": 0,
                "1763481600": 0,
                "1763568000": 0,
                "1763654400": 0,
                "1763740800": 0,
                "1763827200": 0,
                "1763913600": 0,
                "1764000000": 0,
                "1764086400": 0,
                "1764172800": 0,
                "1764259200": 0,
                "1764345600": 0,
                "1764432000": 0,
                "1764518400": 0,
                "1764604800": 0,
                "1764691200": 0,
                "1764777600": 0,
                "1764864000": 0,
                "1764950400": 0,
                "1765036800": 0,
                "1765123200": 0,
                "1765209600": 0,
                "1765296000": 0,
                "1765382400": 0,
                "1765468800": 0,
                "1765555200": 0,
                "1765641600": 0,
                "1765728000": 0,
                "1765814400": 0,
                "1765900800": 0,
                "1765987200": 0,
                "1766073600": 0,
                "1766160000": 0,
                "1766246400": 0,
                "1766332800": 0,
                "1766419200": 0,
                "1766505600": 0,
                "1766592000": 0,
                "1766678400": 0,
                "1766764800": 0,
                "1766851200": 0,
                "1766937600": 0,
                "1767024000": 0,
                "1767110400": 0
            },
            "dayAverageReadTime": 471,
            "preferCategory": [
                {
                    "categoryTitle": "文学",
                    "val": 100
                },
                {
                    "categoryTitle": "社会小说",
                    "val": 75
                },
                {
                    "categoryTitle": "个人成长",
                    "val": 14
                },
                {
                    "categoryTitle": "历史",
                    "val": 0
                },
                {
                    "categoryTitle": "经济理财",
                    "val": 0
                },
                {
                    "categoryTitle": "社会文化",
                    "val": 0
                },
                {
                    "categoryTitle": "哲学宗教",
                    "val": 0
                },
                {
                    "categoryTitle": "心理",
                    "val": 0
                }
            ],
            "preferCategoryWord": "偏好阅读文学",
            "readLongest": [

                {
                    "book": {
                        "author": "尹维安",
                        "bookId": "32535536",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/%E4%B8%80%E4%BA%BA%E4%BB%BD%E7%9A%84%E7%83%AD%E9%97%B9.png",
                        "title": "一人份的热闹"
                    },
                    
                    "readTime": 10273
                },
                {
                    "book": {
                        "author": "李永新",
                        "bookId": "CB_2OU7eg7atFPw6tQ6tJBchA8a",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/61edWWJk7jL._SL1500_.jpg",
                        "title": "刘擎"  },
                    "readTime": 8428
                },
                {
                    "book": {
                        "author": "戴尔·卡耐基",
                        "bookId": "CB_3rAEmKElAB6b6qL6pA5qGGz3",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/2000014295065.webp",
                        "title": "人性的弱点"
                      },
                    "readTime": 2011
                }
            ],
            "shareInfo": {
                "finishReadingCount": 2,
                "hadReadingCount": 9,
                "notesCount": 3,
                "totalReadingDay": 25
            },
            "totalReadTime": 28301

        }
    }
    else if (time_type == 'monthly') {
        return {
            "compare": 0.122310,
            "dayAverageReadTime": 22310,
            "preferCategory": [
                {
                    "categoryTitle": "文学",
                    "val": 20
                },
                {
                    "categoryTitle": "社会小说",
                    "val": 35
                },
                {
                    "categoryTitle": "个人成长",
                    "val": 44
                },
                {
                    "categoryTitle": "历史",
                    "val": 90
                },
                {
                    "categoryTitle": "经济理财",
                    "val": 44
                },
                {
                    "categoryTitle": "社会文化",
                    "val": 12
                },
                {
                    "categoryTitle": "哲学宗教",
                    "val": 22
                },
                {
                    "categoryTitle": "心理",
                    "val": 99
                }
            ],
            "preferCategoryWord": "心理",
            "readLongest": [
            {
                    "book": {
                        "author": "尹维安",
                        "bookId": "32535536",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/%E4%B8%80%E4%BA%BA%E4%BB%BD%E7%9A%84%E7%83%AD%E9%97%B9.png",
                        "title": "一人份的热闹"
                    },
                    
                    "readTime": 1027
                },
                {
                    "book": {
                        "author": "李永新",
                        "bookId": "CB_2OU7eg7atFPw6tQ6tJBchA8a",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/61edWWJk7jL._SL1500_.jpg",
                        "title": "刘擎"  },
                    "readTime": 842
                },
                {
                    "book": {
                        "author": "戴尔·卡耐基",
                        "bookId": "CB_3rAEmKElAB6b6qL6pA5qGGz3",
                        "cover": "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/2000014295065.webp",
                        "title": "人性的弱点"
                      },
                    "readTime": 201
                }
            ],
            "readTimes": {
                "1735660800": 51,
                "1735747200": 0,
                "1735833600": 0,
                "1735920000": 4675,
                "1736006400": 0,
                "1736092800": 0,
                "1736179200": 4162,
                "1736265600": 0,
                "1736352000": 871,
                "1736438400": 967,
                "1736524800": 265,
                "1736611200": 87,
                "1736697600": 1663,
                "1736784000": 3,
                "1736870400": 0,
                "1736956800": 0,
                "1737043200": 0,
                "1737129600": 6764,
                "1737216000": 0,
                "1737302400": 0,
                "1737388800": 1,
                "1737475200": 0,
                "1737561600": 0,
                "1737648000": 0,
                "1737734400": 1848,
                "1737820800": 706,
                "1737907200": 151,
                "1737993600": 0,
                "1738080000": 0,

            },
            "shareInfo": {
                "finishReadingCount": 0,
                "hadReadingCount": 7,
                "notesCount": 13,
                "totalReadingDay": 23
            },
            "totalReadTime": 2302
        }
    } else if (time_type == 'weekly') {
        return {
            "readTimes": {
                "1740326400": 162,
                "1740412800": 181,
                "1740499200": 190,
                "1740585600": 124,
                "1740672000": 134,
                "1740758400": 114,
                "1740844800": 154,
            },
            "rank": {
                "text": "朋友中排第2名"
            },
            "compare": -0.0851727982162766,
            "dayAverageReadTime": 34,
            "totalReadTime": 206,
            "shareInfo": {
                "totalReadingDay": 3,
                "hadReadingCount": 1,
                "finishReadingCount": 0,
                "notesCount": 5
            }
        }
    }

};
const initializeChart = (chartEl, optionGenerator, data) => {
    if (!chartEl.value) {
        console.warn('Chart DOM element not found for', chartEl);
        return null;
    }
    let chartInstance = echarts.getInstanceByDom(chartEl.value);
    if (!chartInstance) {
        chartInstance = echarts.init(chartEl.value);
    }

    const option = optionGenerator(data);
    chartInstance.setOption(option);

    const resizeHandler = () => {
        requestAnimationFrame(() => {
            if (chartInstance && !chartInstance.isDisposed()) {
                chartInstance.resize();
            }
        });
    };
    window.addEventListener('resize', resizeHandler);
    chartInstances.push({ instance: chartInstance, resizeHandler });
    return chartInstance;
};

const getWordCloudOption = (data) => ({
    tooltip: { show: true },
    series: [{
        type: 'wordCloud',
        shape: 'circle', left: 'center', top: 'center', width: '90%', height: '90%',
        sizeRange: [12, 60], rotationRange: [-90, 90], rotationStep: 45, gridSize: 8,
        drawOutOfBound: false,
        textStyle: {
            fontFamily: 'sans-serif', fontWeight: 'bold',
            color: function () {
                return 'rgb(' + [Math.round(Math.random() * 160) + 95, Math.round(Math.random() * 160) + 95, Math.round(Math.random() * 160) + 95].join(',') + ')';
            }
        },
        emphasis: { focus: 'self', textStyle: { shadowBlur: 10, shadowColor: '#333' } },
        data: data.preferAuthor || []
    }]
});

const getRadarChartOption = (data) => {
    const categories = (data.preferCategory || []).map(item => item.categoryTitle);
    const values = (data.preferCategory || []).map(item => item.val);
    return {
        color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
        tooltip: { trigger: 'item' },
        radar: {
            indicator: categories.map(category => ({ name: category, max: 100 })),
            shape: 'circle', splitNumber: 5, axisName: { color: '#e0e0e0' },
            splitLine: { lineStyle: { color: 'rgba(224, 224, 224, 0.3)' } },
            splitArea: { show: false },
            axisLine: { lineStyle: { color: 'rgba(224, 224, 224, 0.3)' } }
        },
        series: [{
            name: '偏好类别', type: 'radar', lineStyle: { width: 2, opacity: 0.5 },
            data: [{
                value: values, name: '类别偏好',
                areaStyle: { color: new echarts.graphic.RadialGradient(0.1, 0.6, 1, [{ color: 'rgba(0, 216, 135, 0.4)', offset: 0 }, { color: 'rgba(0, 216, 135, 0.1)', offset: 1 }]) }
            }]
        }]
    };
};

const getTimeBarOption = (data) => {
    const hours = Array.from({ length: 24 }, (_, i) => `${i}点`);
    return {
        tooltip: {
            trigger: 'axis', axisPointer: { type: 'shadow' },
            formatter: function (params) {
                const hour = params[0].axisValue;
                const value = params[0].value;
                const minutes = Math.floor(value / 60);
                return `${hour}: ${minutes}分钟`;
            }
        },
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: [{ type: 'category', data: hours, axisTick: { alignWithLabel: true }, axisLabel: { color: '#e0e0e0' } }],
        yAxis: [{ type: 'value', show: false }],
        series: [{
            name: '阅读时间', type: 'bar', barWidth: '60%', data: data.preferTime || [],
            itemStyle: { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{ offset: 0, color: '#83bff6' }, { offset: 0.5, color: '#188df0' }, { offset: 1, color: '#188df0' }]) }
        }]
    };
};
const getTimeBarOption_monthly = (monthlyData) => {
    const readTimesObject = monthlyData?.readTimes || {};
    const monthDays = [];
    const readValues = [];
    const sortedTimestamps = Object.keys(readTimesObject)
        .map(ts => parseInt(ts))
        .sort((a, b) => a - b);

    if (sortedTimestamps.length > 0) {
        const firstDate = dayjs.unix(sortedTimestamps[0]);
        const year = firstDate.year();
        const month = firstDate.month();
        const daysInMonth = firstDate.daysInMonth();
        const dailyDataMap = new Map();
        for (const ts of sortedTimestamps) {
            const dateStr = dayjs.unix(ts).format('YYYY-MM-DD');
            dailyDataMap.set(dateStr, readTimesObject[ts.toString()]);
        }
        for (let i = 1; i <= daysInMonth; i++) {
            const dayStr = i < 10 ? `0${i}` : `${i}`;
            const currentDateStr = dayjs(new Date(year, month, i)).format('YYYY-MM-DD');

            monthDays.push(`${dayStr}日`);
            readValues.push(dailyDataMap.get(currentDateStr) || 0);
        }

    } else {
        const daysInCurrentMonth = dayjs().daysInMonth();
        for (let i = 1; i <= daysInCurrentMonth; i++) {
            monthDays.push(`${i < 10 ? '0' + i : i}日`);
            readValues.push(0);
        }
    }


    return {
        tooltip: {
            trigger: 'axis',
            axisPointer: { type: 'shadow' },
            formatter: function (params) {
                const dayLabel = params[0].name;
                const seconds = params[0].value;
                const hours = Math.floor(seconds / 3600);
                const minutes = Math.floor((seconds % 3600) / 60);
                let timeStr = '';
                if (hours > 0) timeStr += `${hours}小时`;
                if (minutes > 0 || hours === 0) timeStr += `${minutes}分钟`;
                if (timeStr === '') timeStr = '0分钟';
                return `${dayLabel}: ${timeStr}`;
            }
        },
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: [{
            type: 'category',
            data: monthDays,
            axisTick: { alignWithLabel: true },
            axisLabel: { color: '#e0e0e0' }
        }],
        yAxis: [{
            type: 'value',
            axisLabel: {
                formatter: function (value) {
                    const hours = Math.floor(value / 3600);
                    return hours > 0 ? `${hours}h` : `${Math.floor(value / 60)}m`;
                },
                color: '#e0e0e0'
            }
        }],
        series: [{
            name: '阅读时间',
            type: 'bar',
            barWidth: '60%',
            data: readValues,
            itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    { offset: 0, color: '#83bff6' },
                    { offset: 0.5, color: '#188df0' },
                    { offset: 1, color: '#188df0' }
                ])
            }
        }]
    };
};

const getTimeBarOption_weekly = (weeklyData) => {
    const readTimesObject = weeklyData?.readTimes || {};
    const weekDaysLabels = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"];
    const readValues = Array(7).fill(0);
    const sortedTimestamps = Object.keys(readTimesObject)
        .map(ts => parseInt(ts))
        .filter(ts => !isNaN(ts))
        .sort((a, b) => a - b);

    let startOfWeekDate;

    if (sortedTimestamps.length > 0) {
        startOfWeekDate = dayjs.unix(sortedTimestamps[0]).startOf('isoWeek');
    } else {
        startOfWeekDate = dayjs().startOf('isoWeek');
    }
    const dailyDataMap = new Map();
    for (const ts of sortedTimestamps) {
        const currentDate = dayjs.unix(ts);
        if (currentDate.isSame(startOfWeekDate, 'isoWeek')) {
            const dateStr = currentDate.format('YYYY-MM-DD');
            dailyDataMap.set(dateStr, (dailyDataMap.get(dateStr) || 0) + readTimesObject[ts.toString()]);
        }
    }
    for (let i = 0; i < 7; i++) {
        const dayInWeek = startOfWeekDate.add(i, 'day');
        const dayInWeekStr = dayInWeek.format('YYYY-MM-DD');
        readValues[i] = dailyDataMap.get(dayInWeekStr) || 0;
    }

    return {
        tooltip: {
            trigger: 'axis',
            axisPointer: { type: 'shadow' },
            formatter: function (params) {
                const dayLabel = params[0].name;
                const seconds = params[0].value;
                const hours = Math.floor(seconds / 3600);
                const minutes = Math.floor((seconds % 3600) / 60);
                let timeStr = '';
                if (hours > 0) timeStr += `${hours}小时`;
                if (minutes > 0 || (hours === 0 && seconds > 0) || (hours === 0 && minutes === 0 && seconds === 0)) {
                    timeStr += `${minutes}分钟`;
                }
                if (timeStr === '' && seconds === 0) timeStr = '0分钟';
                else if (timeStr === '' && seconds > 0) timeStr = `${minutes}分钟`;
                return `${dayLabel}: ${timeStr}`;
            }
        },
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: [{
            type: 'category',
            data: weekDaysLabels,
            axisTick: { alignWithLabel: true },
            axisLabel: { color: '#e0e0e0' }
        }],
        yAxis: [{
            type: 'value',
            splitNumber: 4, // 尝试调整这个数字 (例如 3, 4, 5)
            minInterval: 60, // 确保刻度间至少差1分钟 (60秒)
            axisLabel: {
                formatter: function (value) {
                    if (value === 0) return '0m'; // 处理0的情况
                    const hours = Math.floor(value / 3600);
                    return hours > 0 ? `${hours}h` : `${Math.floor(value / 60)}m`;
                },
                color: '#e0e0e0'
            }
        }],
        series: [{
            name: '阅读时间',
            type: 'bar',
            barWidth: '60%',
            data: readValues,
            itemStyle: { // 可以为周度图表选择不同的颜色主题
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    { offset: 0, color: '#76eec6' }, // 例如，绿色系
                    { offset: 0.5, color: '#3fc097' },
                    { offset: 1, color: '#1a9a71' }
                ])
            }
        }]
    };
};
const getYearlyChartOption = (data) => {
    const years = Object.keys(data.readTimes || {}).map(timestamp => new Date(parseInt(timestamp) * 1000).getFullYear());
    const readHours = Object.values(data.readTimes || {}).map(seconds => Math.round(seconds / 3600));
    return {
        tooltip: { trigger: 'axis', formatter: params => `${params[0].axisValue}年: ${params[0].value}小时` },
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: { type: 'category', data: years, axisLabel: { color: '#E2D8D8' } },
        yAxis: { type: 'value', axisLabel: { formatter: '{value}小时', color: '#E2D8D8' } },
        series: [{
            data: readHours, type: 'line', smooth: true, symbol: 'circle', symbolSize: 8,
            lineStyle: { color: '#5470C6', width: 3 }, itemStyle: { color: '#5470C6' },
            areaStyle: { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{ offset: 0, color: 'rgba(84, 112, 198, 0.5)' }, { offset: 1, color: 'rgba(84, 112, 198, 0.1)' }]) }
        }]
    };
};
const getHotMapChartOption = (yearlyData) => {
    const dailyReadTimes = yearlyData?.dailyReadTimes || {};
    const chartData = [];
    let year = new Date().getFullYear().toString(); // 默认为当前年份

    if (Object.keys(dailyReadTimes).length > 0) {
        const firstTimestampKey = Object.keys(dailyReadTimes)[0];
        year = dayjs.unix(parseInt(firstTimestampKey)).format('YYYY');

        for (const timestampKey in dailyReadTimes) {
            if (Object.hasOwnProperty.call(dailyReadTimes, timestampKey)) {
                const dateStr = dayjs.unix(parseInt(timestampKey)).format('YYYY-MM-DD');
                const seconds = dailyReadTimes[timestampKey];
                chartData.push([dateStr, seconds]);
            }
        }
    }

    // 使用你已有的 formatReadTime 函数
    const customFormatReadTime = (seconds) => {
        if (seconds == null || typeof seconds !== 'number' || isNaN(seconds) || seconds < 0) {
            return '无记录';
        }
        if (seconds === 0) {
            return '0分钟';
        }
        const hours = Math.floor(seconds / 3600);
        const minutes = Math.floor((seconds % 3600) / 60);
        let result = '';
        if (hours > 0) {
            result += `${hours}小时`;
        }
        if (minutes > 0 || hours === 0) { // 如果有小时数，即使分钟为0也显示；如果小时为0，则必须显示分钟
            result += `${minutes}分钟`;
        }
        return result || '0分钟'; // 确保不会返回空字符串
    };

    return {
        title: {
            top: 10,
            left: 'center',
            text: `阅读热力图`,
            textStyle: {
                color: '#e0e0e0' // 保持与你其他图表标题颜色一致
            }
        },
        tooltip: {
            formatter: function (params) {
                // params.value 是一个数组 [dateString, valueInSeconds]
                return `${params.value[0]}<br/>阅读时长: ${customFormatReadTime(params.value[1])}`;
            }
        },
        visualMap: {
            type: 'piecewise',
            orient: 'horizontal',
            left: 'center',
            top: 45, // 给标题留出空间
            pieces: [ // 单位：秒
                { value: 0, label: '无阅读', color: '#3B4652' }, // 0 秒的颜色
                { min: 1, max: 1440, label: '< 24分钟', color: '#a1caf1' }, // 浅色
                { min: 1441, max: 2880, label: '24-48分钟', color: '#73b2f0' },
                { min: 2881, max: 4320, label: '48-72分钟', color: '#4a98e0' },
                { min: 4321, max: 5760, label: '72-96分钟', color: '#2a7bcd' },
                { min: 5761, label: '> 96分钟', color: '#135ca0' }     // 深色
            ],
            textStyle: {
                color: '#e0e0e0'
            }
        },
        calendar: {
            top: 100, // visualMap 和标题下方
            left: 40,  // 调整边距以适应标签
            right: 40,
            cellSize: ['auto', 15], // 单元格大小
            range: year, // 动态设置年份
            itemStyle: {
                borderWidth: 0.5,
                borderColor: '#33374F' // 单元格边框颜色
            },
            dayLabel: { nameMap: 'cn', firstDay: 1, color: '#e0e0e0' }, // 周一开始，中文，浅色文字
            monthLabel: { nameMap: 'cn', color: '#e0e0e0' }, // 中文月份，浅色文字
            yearLabel: { show: false, margin: 10, color: '#e0e0e0' }, // 显示年份标签
            splitLine: {
                show: true,
                lineStyle: {
                    color: '#484848', // 月份分割线颜色
                    width: 1,
                    type: 'solid'
                }
            }
        },
        series: {
            type: 'heatmap',
            coordinateSystem: 'calendar',
            data: chartData, // 使用处理后的数据
            label: {
                show: false // 通常热力图不直接在单元格显示数值标签
            },
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowColor: 'rgba(255, 255, 255, 0.5)' // 高亮时阴影
                }
            }
        }
    };
}
const initTab = async (time_type) => {
    const data = await fetchReadingData(time_type);
    if (time_type == "overview") {
        readingData.value = data;
        await nextTick();
        initializeChart(wordCloudChartEl, getWordCloudOption, data);
        initializeChart(categoryRadarEl, getRadarChartOption, data);
        initializeChart(timeBarEl, getTimeBarOption, data);
        initializeChart(yearlyChartEl, getYearlyChartOption, data);
    }
    else if (time_type == "yearly") {
        readingData_year.value = data;
        await nextTick();
        initializeChart(categoryRadarEl, getRadarChartOption, data);
        initializeChart(hotMapEl, getHotMapChartOption, data);
    } else if (time_type == "monthly") {
        readingData_month.value = data;
        await nextTick();
        initializeChart(categoryRadarEl, getRadarChartOption, data);
        initializeChart(timeBarMonthlyEl, getTimeBarOption_monthly, data);
    } else {
        readingData_week.value = data;
        await nextTick();
        initializeChart(timeBarweeklyEl, getTimeBarOption_weekly, data);
    }
}
initTab("overview")//默认初始化 overview 页面
onMounted(async () => {
    initTab("overview")
});

onUnmounted(() => {
    chartInstances.forEach(chartObj => {
        window.removeEventListener('resize', chartObj.resizeHandler);
        if (chartObj.instance && !chartObj.instance.isDisposed()) {
            chartObj.instance.dispose();
        }
    });
    chartInstances.length = 0;
});

</script>
<style>
.reading-stats-container {
    background-color: transparent;
    color: #e0e0e0;
    min-height: 100vh;
    padding: 20px;
    margin-left: 220px;
}

.menu-container {
    margin-bottom: 30px;
    margin-left:20px;
}

.stats-menu {
    width: 480px;
    border-radius: 8px;
}

.overview-section {
    display: flex;
    flex-direction: column;
    gap: 40px;
}

.chart-container {
    background: transparent;
    border-radius: 12px;
    padding: 20px;
}

.chart-container h2 {
    margin-top: 0;
    margin-bottom: 20px;
    font-size: 23px;
    color: #e2d8d8;
    text-align: center;
}

.chart {
    width: 100%;
    height: 300px;
    background-color: transparent;
}

.books-container {
    background-color: transparent;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.books-container h2 {
    margin-top: 0;
    margin-bottom: 20px;
    color: #e2d8d8;
    font-size: 23px;
    text-align: center;
}

.books-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
}


.book-card {
    background-color: transparent;
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease;
}

.book-card:hover {
    transform: translateY(-5px);
}

.book-cover {
    height: 390px;
    overflow: hidden;
}

.book-cover img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.book-info {
    text-align: center;
    padding: 15px;
}

.book-info h4 {
    margin: 0 0 8px 0;
    color: #e0e0e0;
    font-size: 16px;
}

.book-title {
    margin: 0 0 8px 0;
    color: #b0b0b0;
    font-size: 14px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.book-reason {
    margin: 0;
    color: #909090;
    font-size: 12px;
}

.podium-container {
    background-color: transparent;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.podium-container h2 {
    margin-top: 0;
    margin-bottom: 20px;
    color: #e0e0e0;
    font-size: 23px;
    text-align: center;
}

.podium {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    height: 500px;
}

.podium-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 60%;
}

.podium-book {
    width: 100%;
    height: 100%;
    background-color: transparent;
    border-radius: 8px 8px 0 0;
    overflow: hidden;
    align-content: center;
}

.podium-book img {
    width: 100%;
    height: 310px;
    object-fit: scale-down;
    border-radius: 4px;
}

.podium-info {
    padding: 10px 0;
    text-align: center;
}

.podium-info h4 {
    margin: 0 0 5px 0;
    font-size: 14px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.podium-info p {
    margin: 0;
    font-size: 12px;
    color: #b0b0b0;
}

.podium-block {
    width: 70%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    font-weight: bold;
    font-size: 24px;
}

.first-place .podium-block {
    height: 120px;
    width: 100%;
    background-color: #FFD700;
    color: #333;
}

.second-place .podium-block {
    height: 70px;
    width: 100%;
    background-color: #C0C0C0;
    color: #333;
}

.third-place .podium-block {
    height: 60px;
    width: 100%;
    background-color: #CD7F32;
    color: #333;
}

.stats-summary {
    display: flex;
    justify-content: space-between;
    gap: 20px;
}

.total-time,
.regist-time {
    flex: 1;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    text-align: center;
}

.total-time h2,
.regist-time h2 {
    margin-top: 0;
    margin-bottom: 10px;
    color: #e0e0e0;
    font-size: 23px;
}

.total-time p,
.regist-time p {
    margin: 0;
    font-size: 16px;
    color: #b0b0b0;
}

.share-info {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}


.share-item {
    text-align: center;
}

.share-item h4 {
    margin: 0 0 10px 0;
    color: #e0e0e0;
    font-size: 16px;
}

.share-item p {
    margin: 0;
    font-size: 24px;
    font-weight: bold;
    color: #409EFF;
}
</style>