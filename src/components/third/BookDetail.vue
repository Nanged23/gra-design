<template>
  <div class="modal-overlay" style="margin-left:230px;">
    <div class="modal-backdrop" @click="$emit('close')"></div>

    <div class="modal-container">
      <button class="close-button" @click="$emit('close')">
        <X class="close-icon" />
      </button>

      <!-- 添加条件渲染 -->
      <div class="modal-content" v-if="bookDetail">
        <div class="left-column">
          <div class="book-cover-container">
            <img :src="bookDetail.cover" :alt="bookDetail.title" class="book-cover" />
          </div>

          <div class="info-section">
            <div class="info-card">
              <h3 class="info-title">
                <Users class="info-icon" />
                阅读数据
              </h3>
              <div class="stats-grid">
                <div>
                  <p class="stat-value">{{ formatNumber(bookDetail.readingCount) }}</p>
                  <p class="stat-label">读过的人数</p>
                </div>
                <div>
                  <p class="stat-value">{{ formatNumber(bookDetail.finishReadingCount) }}</p>
                  <p class="stat-label">读完的人数</p>
                </div>
              </div>
            </div>

            <div class="info-card">
              <h3 class="info-title">
                <Star class="info-icon" />
                评价情况
              </h3>
              <div class="ratings-container">
                <div class="rating-item">
                  <div class="rating-header">
                    <span class="rating-label">
                      <ThumbsUp class="rating-thumb" /> 好评
                    </span>
                    <span class="rating-percent">{{ ratings.positive }}%</span>
                  </div>
                  <div class="rating-bar">
                    <div class="rating-progress positive" :style="{ width: `${ratings.positive}%` }"></div>
                  </div>
                </div>
                <div class="rating-item">
                  <div class="rating-header">
                    <span class="rating-label">中评</span>
                    <span class="rating-percent">{{ ratings.neutral }}%</span>
                  </div>
                  <div class="rating-bar">
                    <div class="rating-progress neutral" :style="{ width: `${ratings.neutral}%` }"></div>
                  </div>
                </div>
                <div class="rating-item">
                  <div class="rating-header">
                    <span class="rating-label">
                      <ThumbsDown class="rating-thumb" /> 差评
                    </span>
                    <span class="rating-percent">{{ ratings.negative }}%</span>
                  </div>
                  <div class="rating-bar">
                    <div class="rating-progress negative" :style="{ width: `${ratings.negative}%` }"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="right-column">
          <div class="book-header">
            <h1 class="book-title">{{ bookDetail.title }}</h1>
            <p class="book-author">{{ bookDetail.author }}</p>
          </div>

          <div class="meta-grid">
            <div class="meta-item">
              <p class="meta-label">
                <BookOpen class="meta-icon" /> 分类
              </p>
              <p class="meta-value">{{ bookDetail.category }}</p>
            </div>
            <div class="meta-item">
              <p class="meta-label">
                <Building class="meta-icon" /> 出版社
              </p>
              <p class="meta-value">{{ bookDetail.publisher }}</p>
            </div>
            <div class="meta-item">
              <p class="meta-label">出版时间</p>
              <p class="meta-value">{{ bookDetail.publishTime.split(' ')[0] }}</p>
            </div>
            <div class="meta-item">
              <p class="meta-label">
                <Clock class="meta-icon" /> 阅读时长
              </p>
              <p class="meta-value">{{ formatReadingTime(bookDetail.readingTime) }}</p>
            </div>
            <div class="meta-item">
              <p class="meta-label">总字数</p>
              <p class="meta-value">{{ formatNumber(bookDetail.totalWords) }}字</p>
            </div>
          </div>

          <div class="content-card">
            <h3 class="content-title">AI 智能摘要</h3>
            <p class="content-text">{{ bookDetail.AISummary }}</p>
          </div>

          <div class="content-card">
            <h3 class="content-title">内容简介</h3>
            <p class="content-text">{{ bookDetail.intro }}</p>
          </div>

          <div class="content-card">
            <h3 class="content-title">读者评价</h3>
            <p class="content-text">{{ bookDetail.newRatingDetail.title }}</p>
          </div>
        </div>
      </div>
      <div v-else class="loading">加载中...</div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { Users, X, Star, ThumbsUp, ThumbsDown, BookOpen, Building, Clock } from 'lucide-vue-next';

const props = defineProps({
  book: {
    type: Object,
    required: true
  }
});

defineEmits(['close']);

const bookDetail = ref(null);

// 计算评分百分比
const ratings = computed(() => {
  if (!bookDetail.value || !bookDetail.value.newRatingCount) return { positive: 0, neutral: 0, negative: 0 };
  const total = bookDetail.value.newRatingCount;
  const detail = bookDetail.value.newRatingDetail;
  return {
    positive: Math.round((detail.good / total) * 100),
    neutral: Math.round((detail.fair / total) * 100),
    negative: Math.round((detail.poor / total) * 100)
  };
});

// 获取书籍详情
const fetchBookDetail = async (bookId) => {
  const response = {
    "data": {
      "AISummary": "本书通过解剖学的视角，深入探讨了人生规划、资源配置、时间管理、知识管理和职场修炼五大方面，旨在帮助读者系统地理解并应用这些关键策略。",
      "author": "柏永辉",
      "bookId": "38334243",
      "category": "个人成长-励志成长",
      "cover": "https://wfqqreader-1252317822.image.myqcloud.com/cover/243/38334243/s_38334243.jpg",
      "finishReadingCount": 13796,
      "intro": "作者用解剖学教科书的理念，分别在人生规划大方向，资源配置，时间管理，专业知识学习，以及职场实战落地的五个角度，针对同一个“人生规划”的问题，做了深入浅出的系统性交代。",
      "newRating": 762,
      "newRatingCount": 2228,
      "newRatingDetail": {
        "fair": 357,
        "good": 1643,
        "poor": 228,
        "title": "值得一读"
      },
      "publishTime": "2021-02-02 00:00:00",
      "publisher": "中国商业出版社",
      "readingBookDate": 1740407782,
      "readingCount": 73864,
      "readingTime": 523,
      "title": "我的第一本人生规划手册",
      "totalWords": 141353
    },
    "msg": "success"
  };
  return response.data;
};

// 格式化数字
const formatNumber = (num) => {
  return num.toLocaleString();
};

// 格式化阅读时长
const formatReadingTime = (minutes) => {
  const hours = Math.floor(minutes / 60);
  const remainingMinutes = minutes % 60;
  return `${hours}小时${remainingMinutes > 0 ? `${remainingMinutes}分钟` : ''}`;
};

// 初始化加载数据
onMounted(async () => {
  bookDetail.value = await fetchBookDetail(props.book.id);
});
</script>

<style scoped>
/* 添加加载样式 */
.loading {
  color: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 2rem;
}
</style>
<style scoped>
::-webkit-scrollbar {
  width: 10px;
  /* 设置滚动条宽度 */
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
  /* 滚动条轨道背景 */
}

::-webkit-scrollbar-thumb {
  background: #888;
  /* 滚动条滑块颜色 */
  border-radius: 5px;
  /* 圆角 */
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
  /* 鼠标悬停时的颜色 */
}

/* 针对 Firefox */
* {
  scrollbar-width: none;
  /* 设置滚动条宽度：auto | thin | none */
  scrollbar-color: #888 #f1f1f1;
  /* 滑块颜色 轨道颜色 */
}

.modal-overlay {
  height:auto;
  position: fixed;
  inset: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  background-image: linear-gradient(to right, #434343 0%, black 100%);
}

.modal-backdrop {
  position: absolute;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(4px);
}

.modal-container {
  position: relative;
  width: 100%;
  max-width: 64rem;
  height: 90%;
  overflow-y: auto;
  background: linear-gradient(to bottom, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.9));
  backdrop-filter: blur(1rem);
  border-radius: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.close-button {
  position: absolute;
  right: 1rem;
  top: 1rem;
  padding: 0.5rem;
  border-radius: 9999px;
  background-color: rgba(0, 0, 0, 0.3);
  color: white;
  transition: background-color 0.2s;
  z-index: 10;
}

.close-button:hover {
  background-color: rgba(0, 0, 0, 0.5);
}

.close-icon {
  width: 1.25rem;
  height: 1.25rem;
}

.modal-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 1.5rem;
  padding: 1.5rem 2rem;
}

 

.left-column {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.book-cover-container {
  position: relative;
  width: 100%;
  max-width: 250px;
  aspect-ratio: 2/3;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  margin-bottom: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.book-cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.info-section {
  width: 100%;
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.info-card {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 0.75rem;
  padding: 1rem;
  backdrop-filter: blur(4px);
}

.info-title {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.info-icon {
  width: 1rem;
  height: 1rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
}

.stat-value {
  font-size: 1.25rem;
  font-weight: 600;
  color: white;
}

.stat-label {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.75rem;
}

.ratings-container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.rating-item {
  margin-bottom: 0.5rem;
}

.rating-header {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  margin-bottom: 0.25rem;
}

.rating-label {
  color: rgba(255, 255, 255, 0.7);
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.rating-thumb {
  width: 0.75rem;
  height: 0.75rem;
}

.rating-percent {
  color: white;
}

.rating-bar {
  height: 0.375rem;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 9999px;
  overflow: hidden;
}

.rating-progress {
  height: 100%;
}

.rating-progress.positive {
  background: linear-gradient(to right, #34d399, #10b981);
}

.rating-progress.neutral {
  background: linear-gradient(to right, #fbbf24, #f59e0b);
}

.rating-progress.negative {
  background: linear-gradient(to right, #f87171, #ef4444);
}

.right-column {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.book-header {
  margin-bottom: 0.5rem;
}

.book-title {
  font-size: 1.875rem;
  font-weight: 700;
  color: white;
  margin-bottom: 0.5rem;
}

.book-author {
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.125rem;
}

.meta-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

 
.meta-item {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 0.5rem;
  padding: 0.75rem;
  backdrop-filter: blur(4px);
}

.meta-label {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.75rem;
  margin-bottom: 0.25rem;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.meta-icon {
  width: 0.75rem;
  height: 0.75rem;
}

.meta-value {
  color: white;
  font-weight: 500;
}

.content-card {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 0.75rem;
  padding: 1.25rem;
  backdrop-filter: blur(4px);
}

.content-title {
  color: white;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.content-text {
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.6;
}
</style>