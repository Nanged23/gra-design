<style scoped>
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

.container::after {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: url("../../assets/back.png");
    background-size: 100vw 100vh;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    z-index: -1;
    padding: 20px;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}

.pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 50px;
    padding-bottom: 15px;
}

.tag {
    background-color: #ECF5FF;
    color: #409EFF;
    border-radius: 3px;
    border: 1px solid #9FCEFF;
    margin: 0 2px;
    padding: 2px 5px;
}

.blog-post-card {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-items: center;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    width: 80%;
    height: 150px;
    transition: all 0.3s ease;
    margin-bottom: 20px;
    margin-left: auto;
    margin-right: auto;
}

.blog-post-card:nth-child(odd) .image-container {
    order: 0;
}

.blog-post-card:nth-child(even) .image-container {
    order: 2;
}

.blog-post-card:nth-child(even) .content-container {
    order: 1
}

.blog-post-card:hover {
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    transform: translateY(-3px);
    transition: all 0.3s ease;
}

.image-container {
    flex: 0 0 15%;
    height: 200px;
    max-width: 300px;
    position: relative;
    mask-image: url('../../assets/pngs/edge.png');
    background-size: cover;
    background-position: center;
    mask-repeat: no-repeat;
    mask-position: center;
    mask-size: contain;
    mask-mode: luminance;
}


.content-container {
    flex: 1;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #333;
}

.content {
    font-size: 16px;
    color: #666;
    line-height: 1.6;
    margin-bottom: 15px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
}

.meta-info {
    font-size: 14px;
    color: #999;
    display: flex;
    align-items: center;
    justify-content: flex-start;

}

.meta-info>span {
    margin: 0 5px;
}

.author {
    font-weight: bold;
}
</style>
<template>
    <div class="container">
        <div class="writeLogo" @click="goTo('/writeArticle')">
            <svg t="1742131249746" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="10145">
                <path
                    d="M258.56 916.48c-30.72 0-64-5.12-92.16-15.36-64-23.04-97.28-69.12-99.84-128-2.56-89.6 66.56-120.32 120.32-143.36 51.2-23.04 79.36-35.84 79.36-74.24 0-46.08-79.36-84.48-112.64-89.6-12.8-5.12-20.48-17.92-20.48-30.72 2.56-12.8 15.36-23.04 28.16-20.48 46.08 7.68 156.16 56.32 156.16 140.8 0 74.24-61.44 99.84-110.08 120.32-56.32 25.6-92.16 43.52-89.6 97.28 0 38.4 23.04 66.56 64 81.92 66.56 25.6 166.4 7.68 192-23.04 10.24-10.24 25.6-12.8 35.84-2.56 10.24 10.24 12.8 25.6 2.56 35.84-25.6 30.72-89.6 51.2-153.6 51.2z"
                    fill="#858E9E" p-id="10146"></path>
                <path
                    d="M435.2 757.76c-5.12 5.12 2.56 17.92 12.8 25.6s23.04 10.24 28.16 5.12l107.52-81.92-102.4-74.24-46.08 125.44zM929.28 120.32c-28.16-20.48-69.12-15.36-89.6 15.36L509.44 591.36l102.4 74.24 332.8-455.68c20.48-28.16 12.8-69.12-15.36-89.6z"
                    fill="#525C6A" p-id="10147"></path>
            </svg>
        </div>
        <div v-for="post in blogPost.items" :key="post.id" class="blog-post-card" @click="fetchAndGo(post)">
            <div class="image-container" :style="{ backgroundImage: dynamicColor(post) }" />
            <div class="content-container">
                <h2 class="title">{{ post.title }}</h2>
                <p class="content">{{ post.content }}</p>
                <div class="meta-info">
                    <span>
                        <el-icon>
                            <component :is="Timer" />
                        </el-icon>{{ formatDate(post.modify_time) }}</span>
                    <span>/</span>
                    <span>
                        <el-icon>
                            <component :is="View" />
                        </el-icon>
                        {{ post.views_count }}
                    </span>
                    <span>/</span>
                    <span>
                        <el-icon>
                            <component :is="PriceTag" />
                        </el-icon> 
                        <span v-for="(tag, index) in splitTags(post.tags)" :key="index" class="tag">
                            {{ tag }}
                        </span>
                    </span>

                </div>
            </div>
        </div>
        <div class="pagination"> <span> => 共{{ total_items }}条数据 <= </span>
                    <el-pagination background layout="prev, pager, next" :current-page="currentPage"
                        :page-count="total_pages" @current-change="handlePageChange" />
        </div>

    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { View, Timer, PriceTag } from '@element-plus/icons-vue'
import { ref } from 'vue'
import { getArticleList, getSingleArticle } from '../../js/cur/article.js';
import { useArticleStore } from '../../stores/article';
const articleStore = useArticleStore();
const router = useRouter();
const total_pages = ref(0)
const total_items = ref(0)
const currentPage = ref(1)
const blogPost = ref({
    items: []
})
const formatDate = (dateTime) => {
    if (dateTime) {
        return dateTime.split(" ")[0];
    }
    return "";
};
const dynamicColor = (post) => {
    return `url(${post.cover})`;
};
const splitTags = (tags) => {
    return tags.split(",");
};
const goTo = (path) => {
    router.push(path);
};
const fetchAndGo = async (post) => {
    const requestParams = { user_id: 123, type: 1, extra: post.id };
    const res = await getSingleArticle(requestParams);

    articleStore.setCurrentArticle(res.data);
    router.push(`/articleDetail/${post.slug}`);
};
const handlePageChange = (newPage) => {
    currentPage.value = newPage;
    fetchArticleInfo(newPage).then(() => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
};
const fetchArticleInfo = async (extra = 1) => {
    const requestParams = { user_id: 123, type: 0, extra };
    const res = await getArticleList(requestParams);
    blogPost.value.items = res.data.items;
    total_pages.value = res.data.total_pages;
    total_items.value = res.data.total_items;
};
fetchArticleInfo();
</script>