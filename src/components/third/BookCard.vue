<template>
  <div ref="cardRef" :class="['book-card']" :style="cardStyle" @mouseenter="isHovered = true"
    @mouseleave="isHovered = false" @click="handleCardClick">
    <div class="cover-container">
      <img :src="book.cover" :alt="book.title" class="cover-image" />
      <div :class="['title-overlay', { 'overlay-visible': isHovered }]">
        <h2 class="overlay-title">{{ book.title }}</h2>
      </div>
    </div>

    <div class="card-content">
      <h2 class="book-title">{{ book.title }}</h2> 
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
const emit = defineEmits(['show-detail', 'set-active']); // 添加 set-active 事件
import VanillaTilt from 'vanilla-tilt';
const props = defineProps({
  book: {
    type: Object,
    required: true
  },
  position: {
    type: Number,
    required: true
  },
  isActive: {
    type: Boolean,
    default: false
  },
  index: { type: Number, required: true }
});

const cardRef = ref(null);
const isHovered = ref(false);
const showDetail = ref(false);
let vanillaTilt = null;

// 根据位置计算样式
const cardStyle = computed(() => {
  const translateX = props.position * 60;
  const translateZ = props.isActive ? 0 : -100;
  const opacity = props.isActive ? 1 : 0.6;
  const scale = props.isActive ? 1 : 0.85;
  const zIndex = props.isActive ? 10 : 5 - Math.abs(props.position);

  return {
    transform: `translateX(${translateX}%) translateZ(${translateZ}px) scale(${scale})`,
    opacity: opacity,
    zIndex: zIndex
  };
});

const handleCardClick = () => {
  emit('set-active', props.index); // 点击时发出 set-active 事件，传递当前卡片的索引
  if (props.isActive) {
    emit('show-detail', props.book); // 保留原有的 show-detail 逻辑
  }
};
// 初始化 vanilla-tilt
const initTilt = async () => {
  if (props.isActive && cardRef.value) {
    try {
      vanillaTilt = VanillaTilt.init(cardRef.value, {
        max: 10,
        speed: 400,
        glare: true,
        'max-glare': 0.3,
        scale: 1.05
      });
    } catch (error) {
      console.error('Failed to load vanilla-tilt:', error);
    }
  }
};

const destroyTilt = () => {
  if (vanillaTilt) {
    vanillaTilt.destroy();
    vanillaTilt = null;
  }
};

onMounted(() => {
  initTilt();
});

onUnmounted(() => {
  destroyTilt();
});

watch(() => props.isActive, (newValue) => {
  if (newValue) {
    destroyTilt();
    initTilt();
  } else {
    destroyTilt();
  }
});
</script>

<style scoped>
.book-card {
  position: absolute;
  transform: translate(-50%, -50%);
  width: 320px;
  height: 450px;
  border-radius: 1rem;
  overflow: hidden;
  transition: all 0.5s;
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.05));
  backdrop-filter: blur(0.5rem);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

.cover-container {
  height: 100%;
  position: relative;
  overflow: hidden;
}

.cover-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s;
}

.cover-container:hover .cover-image {
  transform: none;
  /* 默认移除缩放效果 */
}

/* 只有活跃卡片 hover 时才触发图片缩放 */
.cover-container:hover .cover-image {
  transform: scale(1.1);
  /* 默认移除缩放效果 */
}

.title-overlay {
  transition: opacity 0.3s;
  opacity: 0;
}

/* 只有活跃卡片 hover 时才触发标题渐显 */
.book-card:not(.no-animation) .title-overlay.overlay-visible {
  opacity: 1;
}

.overlay-visible {
  opacity: 1;
}

.overlay-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: white;
}

.card-content {
  padding: 1rem;
  color: white;
  display: flex;
  /* 新增：使用 flexbox 布局 */
  flex-direction: column;
  /* 新增：垂直排列子元素 */
  justify-content: center;
  /* 新增：垂直居中 */
  align-items: center;
  /* 新增：水平居中 */
  text-align: center;
  /* 新增：确保文本居中 */
}

.book-title {
  padding-left:4px;
  padding-right:4px;
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.book-author {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
  margin-bottom: 0.75rem;
}

.book-description {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.875rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>