<style>
.article-footer {
    margin: 3rem 0;
}

.article-navigation {
    width: 100%;
    justify-content: space-between;
    display: flex;
    margin: 0 auto;
    position: relative;
    align-items: stretch;
    background-color: white;
    border-radius: 0.75rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    overflow: hidden;
    font-weight: 500;
}

.nav-item {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1.25rem 1.5rem;
    flex: 1;
    color: #333;
    text-decoration: none;
    transition: background-color 0.2s ease;
}

.nav-item:hover {
    background-color: #f8f9fa;
}

.article-navigation:has(> .nav-prev):has(> .nav-next)::before {
    content: "";
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 1px;
    background-color: #e5e7eb;
    transform: translateX(-50%);
}

.nav-prev {
    justify-content: flex-start;
}

.nav-next {
    justify-content: flex-end;
}

.nav-icon {
    flex-shrink: 0;
    width: 20px;
    height: 20px;
    cursor: pointer;
}

.nav-text {
    font-size: 1rem;
    line-height: 1.5;
    margin: 10px 4px 0 4px;
    cursor: pointer;
}

.nav-divider {
    width: 1px;
    background-color: #e5e7eb;
}

.article-navigation:has(> .nav-item:nth-child(1):nth-last-child(1)) {
    justify-content: center;
}

.article-navigation:has(> .nav-item:nth-child(1):nth-last-child(1)) .nav-item {
    flex: none;
    justify-content: center;
}

.blog-post-container {
    max-width: 64rem;
    margin-left: auto;
    margin-right: auto;
    padding: 2rem;

}

.main {
    margin-left: 220px;
}

.blog-post-container {
    max-width: none;
    margin-left: auto;
    margin-right: auto;
    padding: 2rem;
}

.cover-image {
    margin-bottom: 1.5rem;
}

.cover-img {
    width: 100%;
    height: 16rem;
    object-fit: cover;
    border-radius: 0.5rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.article-header {
    margin-bottom: 2rem;
}

.title {
    font-size: 1.875rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 1rem;
}

.article-meta {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    font-size: 0.875rem;
    color: #4b5563;
    margin-bottom: 1rem;
}

.meta-item {
    display: flex;
    align-items: center;
    margin-right: 1.5rem;
}

.icon {
    height: 1rem;
    width: 1rem;
    margin-right: 0.25rem;
}

.tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}

.tag {
    padding: 0.25rem 0.75rem;
    background-color: #f3f4f6;
    color: #1f2937;
    font-size: 0.75rem;
    font-weight: 500;
    border-radius: 9999px;
}

.excerpt {
    margin-bottom: 2rem;
    padding: 1rem;
    background: transparent;
    border-left: 4px solid #d1d5db;
    border-radius: 0.25rem;
}

.excerpt-text {
    color: #374151;
    font-style: italic;
}

.article-content {
    max-width: none;
    width: 100%;
}

.markdown-body {
    color: #24292e;
}

.markdown-body h1,
.markdown-body h2,
.markdown-body h3,
.markdown-body h4,
.markdown-body h5,
.markdown-body h6 {
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
}

.markdown-body h1 {
    font-size: 2em;
}

.markdown-body h2 {
    font-size: 1.5em;
}

.markdown-body pre {
    padding: 16px;
    overflow: auto;
    font-size: 1.2rem;
    line-height: 1.45;
    border-radius: 6px;
    margin-bottom: 16px;
    width: 100%;
    max-width: 100%;
    overflow-x: hidden;
    white-space: pre-wrap;
    word-wrap: break-word;
    box-sizing: border-box;
}

.markdown-body code {
    padding: 0.4em;
    margin: 0;
    font-size: 85%;
    background-color: #373839;
    border-radius: 4px;
    color: #e5e7eb
}

.markdown-body pre code {
    padding: 0;
    width: 100%;
    display: block;
    white-space: pre-wrap;
    word-wrap: break-word;
}

.writeLogo {
    position: fixed;
    bottom: 5%;
    right: 3%;
    z-index: 1000;
    border-radius: 50%;
    transition: all 0.3s ease;
    padding: 10px;
    cursor: pointer;
}

.writeLogo:hover {
    box-shadow: 0 0 15px rgba(0, 149, 255, 0.7);
    transform: scale(1.1);
}

.writeLogo:active {
    box-shadow: 0 0 20px rgba(0, 149, 255, 1);
    transform: scale(1.05);
}

.writeLogo svg {
    display: block;
    width: 30px;
    height: 30px;
}
</style>
<template>
    <div class="blog-post-container">
        <div class="main">
            <div v-if="post">
                <div class="writeLogo" @click="goTo('/writeArticle')">
                    <svg t="1742131249746" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="10145">
                        <path
                            d="M258.56 916.48c-30.72 0-64-5.12-92.16-15.36-64-23.04-97.28-69.12-99.84-128-2.56-89.6 66.56-120.32 120.32-143.36 51.2-23.04 79.36-35.84 79.36-74.24 0-46.08-79.36-84.48-112.64-89.6-12.8-5.12-20.48-17.92-20.48-30.72 2.56-12.8 15.36-23.04 28.16-20.48 46.08 7.68 156.16 56.32 156.16 140.8 0 74.24-61.44 99.84-110.08 120.32-56.32 25.6-92.16 43.52-89.6 97.28 0 38.4 23.04 66.56 64 81.92 66.56 25.6 166.4 7.68 192-23.04 10.24-10.24 25.6-12.8 35.84-2.56 10.24 10.24 12.8 25.6 2.56 35.84-25.6 30.72-89.6 51.2-153.6 51.2z"
                            fill="#858E9E" p-id="10146"></path>
                        <path
                            d="M435.2 757.76c-5.12 5.12 2.56 17.92 12.8 25.6s23.04 10.24 28.16 5.12l107.52-81.92-102.4-74.24-46.08 125.44zM929.28 120.32c-28.16-20.48-69.12-15.36-89.6 15.36L509.44 591.36l102.4 74.24 332.8-455.68c20.48-28.16 12.8-69.12-15.36-89.6z"
                            fill="#525C6A" p-id="10147"></path>
                    </svg>
                </div>
                <div class="cover-image">
                    <img :src="post.cover" :alt="post.title" class="cover-img" />
                </div>
                <div class="article-header">
                    <h1 class="title">{{ post.title }}</h1>
                    <div class="article-meta">
                        <div class="meta-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="icon" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <span>{{ formatDate(post.modify_time) }}</span>
                        </div>

                        <div class="meta-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="icon" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                            </svg>
                            <span>{{ post.views_count }} </span>
                        </div>
                        <div class="meta-item">
                            <svg t="1742195535756" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                xmlns="http://www.w3.org/2000/svg" p-id="12153" width="18" height="18">
                                <path
                                    d="M817.8 109.7H207.5c-12.9 0-22.7-10.6-22.7-22.7 0-12.9 10.6-22.7 22.7-22.7h610.2c12.9 0 22.7 10.6 22.7 22.7 0.8 12.1-9.8 22.7-22.6 22.7zM848 962.2H178c-13.6 0-25-11.4-25-25s11.4-25 25-25h670c13.6 0 25 11.4 25 25s-11.3 25-25 25z"
                                    p-id="12154"></path>
                                <path
                                    d="M753.4 653.3l-0.8-1.5C714 584.4 662.5 540.5 608 514c54.5-27.3 105.2-70.4 144.6-137.8l0.8-1.5C792 308 817.8 217.2 822.3 96h-44.7c-3.8 112.1-27.3 195.3-62.8 256.7l-0.8 0.8c-43.9 78-93.1 119.6-156.7 139.3l-3 0.8h-0.8c-1.5 0.8-2.3 1.5-3.8 2.3l-0.8 0.8-1.5 1.5-1.5 1.5v0.8c-0.8 0.8-1.5 2.3-2.3 3.8l-0.8 0.8-1.5 5.3v8.3l1.5 5.3 0.8 0.8c0.8 1.5 1.5 2.3 2.3 3.8v0.8l1.5 1.5v-0.8l1.5 0.8 0.8 0.8c0.8 0.8 2.3 1.5 3.8 2.3h0.8l3 1.5c64.4 20.4 112.8 61.3 157.5 138.6l0.8 1.5c18.9 31.8 33.3 70.4 44.7 115.1 2.3 12.9 10.6 40.9 12.1 77.2-35.6-31.8-134-54.5-252.1-56V461.7c1.5 0 2.3-0.8 3.8-1.5v-0.8l6.1-2.3h1.5c43.2-13.6 77.2-34.8 106-62.8 30.3-30.3 53.8-67.4 69.7-109 4.5-11.4-0.8-24.2-12.9-28.8-11.4-4.5-24.2 0.8-28.8 12.1v0.8c-13.6 34.8-33.3 67.4-59.1 93.1-23.6 22.7-51.6 40.9-87.2 51.5l-0.8 0.8-2.3 0.8-3.8 0.8-2.3-0.8-1.5-0.8-2.3-0.8c-34.8-11.4-64.4-28.8-87.1-51.5-26.5-25.7-45.4-57.5-59.1-93.1-4.5-11.4-17.4-17.4-28-12.9-11.4 4.5-16.7 16.7-12.9 28.8 15.9 41.6 38.6 78.7 69.7 109 28 28 62.8 49.2 105.2 62.8h0.8l6.1 2.3 1.5 0.8c0.8 0.8 1.5 0.8 3 1.5v349.8c-110.5 0-206.7 18.9-252.1 45.4 1.5-18.2 5.3-37.9 12.1-66.6 11.4-45.4 26.5-83.3 44.7-115.1l0.8-1.5c44.7-77.2 93.1-118.1 158.2-138.6l2.3-1.5h0.8c1.5-0.8 2.3-1.5 3.8-2.3l0.8-0.8 1.5-0.8v-0.8l1.5-1.5v-0.8c0.8-0.8 1.5-2.3 2.3-3.8v-0.8c0.8-1.5 1.5-3.8 1.5-5.3v-7.6c0-1.5-0.8-3.8-1.5-5.3v-0.8c-0.8-1.5-1.5-3-2.3-3.8v-0.8l-1.5-1.5-1.5-1.5-2.3 0.8c-1.5-0.8-2.3-1.5-3.8-2.3h-0.8l-2.3-0.8c-64.4-19.7-113.6-61.3-158.2-139.3l-0.8-0.8C274 291.7 250.5 208.4 246 96.3h-44.7c4.5 121.1 30.3 211.2 68.9 278.6l0.8 1.5c38.6 67.4 90.1 110.5 144.6 137.8C361.1 540.7 310.4 584.6 271 652l-0.8 1.5C234 717.6 208.3 802.4 203 915.2h617.8c-5.3-113.5-30.3-198.3-67.4-261.9z"
                                    p-id="12155"></path>
                            </svg>
                            <span>{{ other_data.read_time }} 分钟内</span>
                        </div>
                    </div>

                    <div class="tags">
                        <span v-for="(tag, index) in splitTags(post.tags)" :key="index" class="tag">
                            {{ tag }}
                        </span>
                    </div>

                    <div class="excerpt">
                        <p class="excerpt-text">{{ post.excerpt }}</p>
                    </div>
                </div>

                <div class="article-content">
                    <div v-html="renderedContent" class="markdown-body"></div>
                </div>

                <div class="article-footer">
                    <div class="article-navigation">
                        <div class="nav-item nav-prev" v-if="other_data.pre_post"
                            @click="goToArticle(other_data.pre_post)">
                            <span class="nav-icon">&lt;</span>
                            <span class="nav-text">{{ other_data.pre_post.title }}</span>
                        </div>
                        <div class="nav-item nav-next" v-if="other_data.next_post"
                            @click="goToArticle(other_data.next_post)">
                            <span class="nav-text">{{ other_data.next_post.title }}</span>
                            <span class="nav-icon">&gt;</span>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else>Loading...</div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { ElMessage } from 'element-plus';
import { useArticleStore } from '../../stores/article';
import { marked } from 'marked';
import hljs from 'highlight.js';
import 'highlight.js/styles/github.css';
import { getSingleArticle } from '../../js/cur/article.js';
const emits = defineEmits(['scrollToTop']);
marked.setOptions({
    highlight: function (code, lang) {
        if (lang && hljs.getLanguage(lang)) {
            return hljs.highlight(code, { language: lang }).value;
        }
        return hljs.highlightAuto(code).value;
    },
    breaks: true,
    gfm: true
});
import { useRouter, useRoute } from 'vue-router';
const router = useRouter();
const goTo = (path) => {
    router.push(path);
};
const articleStore = useArticleStore();
const route = useRoute();
const post = ref(null);
const other_data = ref({
    pre_post: null,
    next_post: null,
    read_time: null
});
const formatDate = (date) => {
    if (!date) return '';
    return new Intl.DateTimeFormat('zh-CN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    }).format(new Date(date));
};

const renderedContent = computed(() => {
    if (!post.value?.content) {
        return '';
    }
    return marked(post.value.content);
});

const splitTags = (tags) => {
    if (!tags) return [];
    return tags.split(",");
};
const loadArticle = () => {
    const res = articleStore.currentArticle;
    if (res && res.items && res.items.length > 0) {
        post.value = res.items[0];
        other_data.value = {
            pre_post: res.pre_article || null,
            next_post: res.next_article || null,
            read_time: res.read_time || null
        };
    } else {
        ElMessage({
            message: "文章加载出错了~稍后试试吧",
            type: 'error',
        });
        router.push('/article');
    }
};
onMounted(() => {
    loadArticle();
});
watch(() => route.path, () => {
    loadArticle();
    emits('scrollToTop');
});
const goToArticle = async (post) => {
    const requestParams = { user_id: 123, type: 1, extra: post.id };
    const res = await getSingleArticle(requestParams);
    articleStore.setCurrentArticle(res.data);
    router.push(`/articleDetail/${post.slug}`);
};
</script>