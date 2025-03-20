<style scoped>
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 50px;
  padding-bottom: 15px;
}

.markdown-editor {
  display: flex;
  justify-content: center;
  gap: 20px;
  padding: 20px;
  align-items: center;
}

.editor {
  width: 350px;
  height: 150px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: none;
}

.preview {
  height: 170px;
  width: 350px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow-y: auto;
  box-sizing: border-box;
}

.preview :deep(h1) {
  font-size: 24px;
  margin: 0px;
  border-bottom: 1px solid #edb05a;
}

.preview :deep(pre, code) {
  background: #282C34;
  color: aliceblue;
  padding: 5px;
  border-radius: 4px;
}

.notification {
  opacity: 0.75;
  display: flex;
  flex-direction: column;
  justify-items: center;
  isolation: isolate;
  position: relative;
  width: 1000px;
  height: auto;
  margin: 10px auto;
  border-radius: 1rem;
  overflow: hidden;
  font-family: 'Trebuchet MS', sans-serif;
  font-size: 16px;
}

.notification.morning {
  background-image: linear-gradient(to right, #ffecd2 0%, #fdb8a1 100%);
}

.notification.afternoon {
  background-image: linear-gradient(to right, #7dfce5 0%, #aebdfd 100%);
}

.notification.night {
  background-image: linear-gradient(to top, #7a99d3 0%, #c6d5ef 100%);
}

.notification svg {
  vertical-align: -11px;
}

.notification:before {
  position: absolute;
  content: "";
  inset: 0.0625rem;
  border-radius: 0.9375rem;
  z-index: 2
}

.notification:after {
  position: absolute;
  content: "";
  width: 0.25rem;
  inset: 0.65rem auto 0.65rem 0.5rem;
  border-radius: 0.125rem;
  background: var(--gradient);
  transition: transform 300ms ease;
  z-index: 4;
}

.notification:hover:after {
  transform: translateX(0.15rem)
}

.spliter1 {
  display: inline-block;
  vertical-align: middle;
  height: 23px;
  width: 5px;
  margin-top: 2px;
  --gradient: linear-gradient(to bottom, #2eadff, #3d83ff, #7e61ff);
  background: var(--gradient);
  border-radius: 10px;
}

.notititle {
  color: #32a6ff;
  margin: 2px 0px 0px 15px;
  font-weight: 500;
  font-size: 0.9rem;
  transition: transform 300ms ease;
  z-index: 5;
}

.notification:hover .notititle {
  transform: translateX(0.15rem)
}

.notibody {
  word-break: break-word;
  text-align: justify;
  color: #302e37;
  font-size: 1rem;
  transition: transform 300ms ease;
  z-index: 5;
  /* 上 右 下 左 */
  margin: 0 10px 0px 10px;
}

.notification:hover .notibody {
  transform: translateX(0.25rem)
}

.notiglow,
.notiborderglow {
  position: absolute;
  width: 100rem;
  height: 20rem;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle closest-side at center, rgb(255, 0, 0), transparent);
  opacity: 0;
  transition: opacity 300ms ease;
}

.notiglow {
  z-index: 3;
}

.notiborderglow {
  z-index: 1;
}

.notification:hover .notiglow {
  opacity: 0.1
}

.notification:hover .notiborderglow {
  opacity: 0.1
}
</style>

<template>
  <div class="main">
    <div class="markdown-editor">
      <textarea v-model="markdownText" placeholder="写下此刻的感受 ..." class="editor"></textarea>
      <div class="preview" v-html="compiledMarkdown"></div>

      <el-button type="primary" plain @click="submitMoment(markdownText)">提交</el-button>
    </div>
    <div v-for="post in moment.items" :key="post.id" :class="['notification', getTimeClass(post.create_time)]">
      <div class="notiglow"></div>
      <div class="notiborderglow"></div>
      <div class="notititle">
        <span class="spliter1"></span>
        <svg t="1741754994074" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
          p-id="31968" id="mx_n_1741754994075" width="30" height="30">
          <path
            d="M597.877173 341.135574l-297.529548-83.504056-45.830823 45.979142 239.83314 148.319815-125.923523 146.391657-64.370799-2.818076-45.830823 45.830822 48.797219 33.371959a136.30591 136.30591 0 0 0-22.544612 57.844727 97.594438 97.594438 0 0 0 67.188876-14.831981l25.214369 42.122827 45.682503-27.142526-8.45423-84.838934 156.625725-130.669756 150.247972 257.928157 44.495944-43.754345-77.126303-309.691773 102.637311-103.82387c44.495944-49.687138 64.3708-93.738123 44.495945-128.59328-38.563152-10.975666-78.757822-3.707995-122.067208 40.04635z"
            fill="#83C8EC" p-id="31969"></path>
          <path
            d="M724.245655 788.468134a12.607184 12.607184 0 0 1-14.831982-5.487833l-144.01854-242.799536-139.123986 121.622248 6.081113 64.964079a12.162225 12.162225 0 0 1-5.042874 11.272305l-43.606026 32.03708a12.458864 12.458864 0 0 1-18.095017-3.856315l-19.133256-32.630359-3.411356 1.779838a130.521437 130.521437 0 0 1-40.787949 13.200463H289.075319l-1.631518 0.741599a11.717265 11.717265 0 0 1-7.119351-1.483198l-1.038239-1.038238-1.928158-2.373118-1.631518-1.631517-1.483198-1.186559a12.607184 12.607184 0 0 1 0-6.971031v-12.903824a2.521437 2.521437 0 0 0 0-1.038239 118.655852 118.655852 0 0 1 7.119351-26.697566l8.45423-17.205099-33.223639-19.429896a12.458864 12.458864 0 0 1-3.559675-18.095017l31.88876-43.606026a12.903824 12.903824 0 0 1 11.272306-5.042873l64.222479 6.377752 121.918888-138.975667-241.909618-144.908458a12.458864 12.458864 0 0 1-2.076477-19.874856l49.093859-46.275782a12.310545 12.310545 0 0 1 11.717265-3.114716l295.008111 79.79606 93.441483-88.991888c52.208575-49.242178 97.594438-71.490151 136.15759-61.701043h1.483198l10.382387 3.856315 2.521437 0.889919h0.889919l2.373117 1.186558 0.741599 1.186559 1.334879 0.889919a12.162225 12.162225 0 0 1 2.373117 5.487833l3.856315 10.382387a5.339513 5.339513 0 0 0 0 1.334878c9.640788 38.711472-12.607184 83.949015-61.997683 136.15759l-88.991888 92.996524 79.94438 297.084589a13.348783 13.348783 0 0 1-2.966397 11.865585l-46.572421 48.945538a12.903824 12.903824 0 0 1-4.894554 3.263036zM722.465817 756.431054l29.663963-32.037079-78.312862-295.601391a12.607184 12.607184 0 0 1 2.966396-11.717265l93.589803-98.039398c42.716107-45.385863 58.141367-78.757822 57.103129-103.82387l-1.334879-9.492468-2.373117-6.377752-6.526072-2.521437-9.492468-1.334878c-24.32445-1.186559-57.844728 14.831981-103.82387 56.954808l-98.336037 93.293164a12.607184 12.607184 0 0 1-11.865585 2.966396l-294.266512-79.054461L266.975666 300.050985l241.168019 143.7219a12.458864 12.458864 0 0 1 2.966396 18.984937l-135.56431 154.994206a12.310545 12.310545 0 0 1-10.530707 4.152955l-63.480881-6.229433L281.807648 642.521437l31.295481 18.243337a12.310545 12.310545 0 0 1 4.301274 17.056779 163.151796 163.151796 0 0 0-12.162225 24.621089l-5.636153 20.616454 20.764775-5.487833a149.506373 149.506373 0 0 0 24.472769-12.162225 12.607184 12.607184 0 0 1 17.205098 4.449595L380.143685 741.599073l26.845886-19.578216-6.526072-64.074159a12.607184 12.607184 0 0 1 4.152955-10.679027l155.735806-135.564311a12.458864 12.458864 0 0 1 18.836616 2.966397z m6.526072-29.663962a12.458864 12.458864 0 0 1-14.831982-6.081113l-119.99073-225.001159a12.458864 12.458864 0 0 1 5.042874-16.760139 12.607184 12.607184 0 0 1 16.908459 5.042874l120.287369 225.001159a12.310545 12.310545 0 0 1-5.042873 16.760139z m-207.647741-305.835458a12.162225 12.162225 0 0 1-9.344148-1.038239L296.639629 305.390498a12.458864 12.458864 0 1 1 11.568946-21.951332l215.360371 114.502897a12.458864 12.458864 0 0 1-2.224798 22.989571z"
            fill="#333333" p-id="31970"></path>
        </svg>
        <span>{{ post.create_time }}</span>
      </div>
      <div class="notibody" v-html="renderMarkdown(post.content)"></div>
    </div>
    <div class="pagination"> <span> => 共{{ total_items }}条数据 <= </span>
          <el-pagination background layout="prev, pager, next" :current-page="currentPage" :page-count="total_pages"
            @current-change="handlePageChange" />
    </div>
  </div>
</template>
<script setup>
import { ElMessage } from 'element-plus';
import { ref, computed } from 'vue'
import { getMomentList, addMomentList } from '../../js/cur/moment.js';
import { marked } from 'marked';
import hljs from 'highlight.js';
import 'highlight.js/styles/default.css';
const moment = ref({
  items: []
})
const emits = defineEmits(['scrollToTop']);
const total_pages = ref(0)
const total_items = ref(0)
const currentPage = ref(1) 
const handlePageChange = (newPage) => {
  currentPage.value = newPage;
  fetchMomentInfo(newPage).then(() => { 
    emits('scrollToTop');
  });
};
const fetchMomentInfo = async (page = 1) => {
  const requestParams = { user_id: 123, page };
  const res = await getMomentList(requestParams);
  moment.value.items = res.data.items;
  total_pages.value = res.data.total_pages;
  total_items.value = res.data.total_items;
}
fetchMomentInfo();
const getTimeClass = (createTime) => {
  const time = new Date(createTime)
  const hours = time.getHours()

  if (hours >= 6 && hours < 12) {
    return 'morning'
  } else if (hours >= 12 && hours < 18) {
    return 'afternoon'
  } else {
    return 'night'
  }
}

const markdownText = ref('');

marked.setOptions({
  highlight: (code, lang) => {
    return hljs.highlight(code, { language: lang }).value;
  },
  breaks: true,
  gfm: true,
});
const compiledMarkdown = computed(() => {
  return marked(markdownText.value);
});
const renderMarkdown = (text) => {
  return marked(text);
};
const submitMoment = async (content) => {
  let params = {
    "content": content,
    "user_id": "123"
  }
  const res = await addMomentList(params);
  ElMessage({
    message: res.msg,
    type: 'success',
  })
  await fetchMomentInfo();
  markdownText.value = '';
};
</script>