<style scoped>
.container {
    padding: 20px;
    display: flex;
    justify-content: center;
    flex-direction: column; 
    align-items: center;
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
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    width: 100%;
    transition: all 0.3s ease;
    margin-bottom: 20px;
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
    padding: 20px;
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
        <div v-for="post in blogPost.items" :key="post.id" class="blog-post-card">
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
                        <!-- 使用 v-for 循环渲染标签 -->
                        <span v-for="(tag, index) in splitTags(post.tags)" :key="index" class="tag">
                            {{ tag }}
                        </span>
                    </span>

                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { View, Timer, PriceTag } from '@element-plus/icons-vue'
import { ref, computed } from 'vue'
import { getArticleList } from '../../js/cur/article.js';
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
const fetchUserInfo = async () => {
    const requestParams = { user_id: 123, type: 0, extra: 1 };
    const res = await getArticleList(requestParams);
    blogPost.value.items = res.data.items;
}
fetchUserInfo();
</script>