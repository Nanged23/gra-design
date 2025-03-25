<template>
  <div class="literary-browser">
    <!-- User Profile Section -->
    <div class="user-profile">
      <div class="user-avatar">
        <img :src="userDetail.avatar" alt="User Avatar">
      </div>
      <div class="user-info">
        <h2 class="user-name">{{ userDetail.name }}</h2>
        <p class="user-desc">{{ userDetail.desc }}</p>
        <div class="user-meta">
          <span class="user-location">
            <MapPin size="16px" />
            {{ userDetail.loc_name }}
          </span>
          <span class="user-created">
            加入于 {{ formatDate(userDetail.created) }}
          </span>
        </div>
      </div>
    </div>

    <div class="header">
      <h1>文艺生活</h1>
      <p class="quote">读万卷书，行万里路 </p>

    </div>

    <!-- Filter Controls -->
    <div class="filter-controls">
      <div class="filter-group media-type">
        <button v-for="option in mediaTypes" :key="option.id" :class="{ active: selectedMediaType === option.id }"
          @click="selectMediaType(option.id)">
          {{ option.label }}
        </button>
      </div>

      <div class="divider"></div>

      <div class="filter-group status-type">
        <button v-for="option in statusTypes" :key="option.id" :class="{ active: selectedStatusType === option.id }"
          @click="selectStatusType(option.id)">
          {{ option.label }}
        </button>
      </div>
    </div>
    <div class="page-name">
      <h2>{{ pagename }}</h2>
      <div class="ink-line"></div>
    </div>
    <div class="content-area">
      <div v-if="loading" class="loading-state">
        <div class="book">
          <div class="book-page"></div>
        </div>
        <p>正在翻阅...</p>
      </div>
      <div v-else-if="error" class="error-state">
        <p>{{ error }}</p>
        <button @click="fetchData">重新探索</button>
      </div>
      <div v-else-if="data.length" class="media-collection">
        <div v-for="item in data" :key="item.id" class="media-item" @click="change_href(item)">
          <div class="media-cover">
            <div class="cover-shadow"></div>
            <img :src="item.img" :alt="item.name">
          </div>
          <div class="media-details">
            <h3>{{ item.name }}</h3>
            <p class="creator">{{ selectedMediaType === 'books' ? item.author : item.author }}</p>
            <p class="content_type">{{ item.content_type || '' }}</p>
            <p class="language">{{ item.language || '中文' }}</p>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="empty-state">
        <div class="empty-bookshelf">
          <div class="shelf"></div>
          <div class="shadow"></div>
        </div>
        <p>这里还是空的，不如添加一些{{ selectedMediaType === 'books' ? '书籍' : '电影' }}？</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { getList, getUser } from '@/js/third/douban';
import Cookie from 'js-cookie'
import { MapPin } from 'lucide-vue-next';
import VueTypedJs from 'vue-typed-js'
const userDetail = ref({
  avatar: "",
  created: "",
  desc: "",
  loc_name: "",
  name: "",
});
const change_href = (item) => {
  window.open(item.link, '_blank');
}
const doSmth = () => { }
const mediaTypes = [
  { id: 'books', label: '图书' },
  { id: 'movies', label: '电影' }
];

const statusTypes = [
  { id: 'currently-watching', label: '看过' },
  { id: 'want-to-watch', label: '想看' }
];

// State management
const selectedMediaType = ref('books');
const selectedStatusType = ref('currently-watching');
const data = ref([]);
const loading = ref(false);
const error = ref(null);

// Computed page name
const pagename = computed(() => {
  const mediaLabel = selectedMediaType.value === 'books' ? '书' : '影';
  const statusLabel = selectedStatusType.value === 'currently-watching' ? '看过の' : '想看の';
  return `${statusLabel}${mediaLabel}`;
});

const selectMediaType = (typeId) => {
  selectedMediaType.value = typeId;
  fetchData();
};

const selectStatusType = (typeId) => {
  selectedStatusType.value = typeId;
  fetchData();
};

const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return date.getFullYear() + '-' +
    String(date.getMonth() + 1).padStart(2, '0') + '-' +
    String(date.getDate()).padStart(2, '0');
};

const getUserDetail = async (userId) => {
  let params = {
    "user_id": Cookie.get("user_id"),
  }
  let res = await getUser(params);
  userDetail.value = res.data;
};

const fetchData = async () => {
  loading.value = true;
  error.value = null;

  const params = {
    "category": selectedMediaType.value === 'books'
      ? (selectedStatusType.value === 'currently-watching' ? 1 : -1)
      : (selectedStatusType.value === 'currently-watching' ? 2 : -2),
    "user_id": Cookie.get("user_id"),
    "page": 1,
  };

  try {
    const res = await getList(params);
    data.value = res.data.items;
  } catch (err) {
    error.value = '获取数据失败，请稍后重试';
    console.error('Error fetching data:', err);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  const userId = Cookie.get("user_id");
  getUserDetail(userId);
  fetchData();
});

watch([selectedMediaType, selectedStatusType], () => {
  fetchData();
});
</script>

<style scoped>
.literary-browser {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  margin-left: 230px;
  font-family: 'Times New Roman', Georgia, serif;
  max-width: 1200px;
  padding: 15px 20px;
  color: #2c3e50;
  background: transparent;
  min-height: 100vh;
}

/* User Profile Styles */
.user-profile {
  display: flex;
  align-items: center;
  width: 100%;
  margin-bottom: 40px;
  padding: 20px;
  background-image: linear-gradient(to right, #f3ecce, #f5d0bf);
  border-radius: 10px;
  border-left: 4px solid #6c6658;
  opacity: 0.9
}

.user-avatar {
  flex-shrink: 0;
  width: 80px;
  height: 80px;
  margin-right: 20px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  border: 3px solid #f7f9d8;
}

.user-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-info {
  flex-grow: 1;
}

.user-name {
  margin: 0 0 5px 0;
  font-size: 1.5rem;
  font-weight: 600;
  color: #3c3c3c;
}

.user-desc {
  margin: 0 0 10px 0;
  font-size: 1rem;
  color: #6d6d6d;
  font-style: italic;
  line-height: 1.4;
}

.user-meta {
  display: flex;
  gap: 20px;
  font-size: 0.85rem;
  color: #8a8a8a;
}

.user-location {
  display: flex;
  align-items: center;
}

.location-icon {
  display: inline-block;
  width: 12px;
  height: 12px;
  margin-right: 5px;
  background-color: #d3c6a6;
  border-radius: 50%;
}

.header {
  text-align: center;
  margin-bottom: 20px;
}

.header h1 {
  font-size: 2.5rem;
  font-weight: normal;
  letter-spacing: 2px;
  margin: 0;
  color: #3c3c3c;
}

.quote {
  font-style: italic;
  color: #8a8a8a;
  margin-top: 8px;
  font-size: 1rem;
}

/* Filter Controls */
.filter-controls {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 40px;
}

.filter-group {
  display: flex;
  border: 1px solid #d3c6a6;
  border-radius: 30px;
  overflow: hidden;
}

.filter-group button {
  background: none;
  border: none;
  padding: 10px 24px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  color: #6d6d6d;
  font-family: inherit;
}

.filter-group button.active {
  background-color: #d3c6a6;
  color: #fff;
  font-weight: 500;
}

.filter-group button:hover:not(.active) {
  background-color: rgba(211, 198, 166, 0.2);
}

.divider {
  width: 1px;
  height: 30px;
  background-color: #d3c6a6;
  margin: 0 20px;
}

/* Page name */
.page-name {
  text-align: center;
  margin-bottom: 40px;
  position: relative;
}

.page-name h2 {
  font-size: 1.8rem;
  font-weight: normal;
  color: #3c3c3c;
  margin: 0 0 15px 0;
}

.ink-line {
  height: 2px;
  width: 100px;
  background-color: #d3c6a6;
  margin: 0 auto;
  position: relative;
}

.ink-line::after {
  content: '';
  position: absolute;
  width: 8px;
  height: 8px;
  background-color: #d3c6a6;
  border-radius: 50%;
  bottom: -3px;
  left: 50%;
  transform: translateX(-50%);
}

/* Content Area */
.content-area {
  min-height: 400px;
}

/* Loading State */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 300px;
}

.book {
  width: 60px;
  height: 80px;
  position: relative;
  perspective: 1000px;
  margin-bottom: 20px;
}

.book-page {
  position: absolute;
  width: 100%;
  height: 100%;
  transform-origin: left center;
  background-color: #fff;
  border-left: 4px solid #d3c6a6;
  box-shadow: 5px 0 15px rgba(0, 0, 0, 0.1);
  animation: flip-page 1.5s infinite ease-in-out;
}

@keyframes flip-page {
  0% {
    transform: rotateY(0deg);
  }

  50% {
    transform: rotateY(-180deg);
  }

  100% {
    transform: rotateY(0deg);
  }
}

.loading-state p {
  color: #8a8a8a;
  font-style: italic;
}

/* Error State */
.error-state {
  text-align: center;
  padding: 40px;
  color: #a83232;
}

.error-state button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #d3c6a6;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-family: inherit;
}

.error-state button:hover {
  background-color: #c2b696;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 40px;
  color: #8a8a8a;
}

.empty-bookshelf {
  width: 200px;
  height: 30px;
  margin: 0 auto 20px;
  position: relative;
}

.shelf {
  width: 100%;
  height: 10px;
  background-color: #d3c6a6;
  position: absolute;
  bottom: 0;
}

.shadow {
  width: 80%;
  height: 5px;
  background-color: rgba(0, 0, 0, 0.1);
  position: absolute;
  bottom: -5px;
  left: 10%;
  border-radius: 50%;
}

/* Media Collection */
.media-collection {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
}

/* Media Item */
.media-item {
  display: flex;
  flex-direction: column;
  transition: transform 0.3s;
}

.media-item:hover {
  transform: translateY(-10px);
}

.media-cover {
  position: relative;
  margin-bottom: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  transition: transform 0.3s, box-shadow 0.3s;
  overflow: hidden;
  border-radius: 5px;
  aspect-ratio: 2/3;
  max-width: 160px;
  margin: 0 auto 15px;
}

.media-item:hover .media-cover {
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}

.cover-shadow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0) 70%, rgba(0, 0, 0, 0.7) 100%);
  z-index: 1;
}

.media-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s;
}

.media-item:hover .media-cover img {
  transform: scale(1.05);
}

.rating {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background-color: rgba(211, 198, 166, 0.9);
  color: white;
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 0.8rem;
  z-index: 2;
}

.media-details {
  padding: 0 5px;
  text-align: center;
}

.media-details h3 {
  margin: 0 0 5px 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #3c3c3c;
}

.creator {
  margin: 0 0 3px 0;
  font-size: 0.9rem;
  color: #6d6d6d;
  font-style: italic;
}

.content_type {
  margin: 0 0 3px 0;
  font-size: 0.8rem;
  color: #8a8a8a;
}

.language {
  margin: 0;
  font-size: 0.8rem;
  color: #8a8a8a;
} 
</style>