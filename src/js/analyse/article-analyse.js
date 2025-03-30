import api from '../../api/axios.js'
export async function getWordCloud(params) {
    try {
        const response = await api.get(`/article/word_cloud`, { params });
        return response.data;
    } catch (error) {
        console.error("获取文章词云图失败:", error);
        throw error;
    }
}
export async function getTopArticles(params) {
    try {
        const response = await api.get(`/article/most_viewed`, { params });
        return response.data;
    } catch (error) {
        console.error("获取文章排行失败:", error);
        throw error;
    }
}
export async function getWordCount(params) {
    try {
        const response = await api.get(`/article/word_count`, { params });
        return response.data;
    } catch (error) {
        console.error("获取文章字数总结失败:", error);
        throw error;
    }
}
export async function getTimePrefer(params) {
    try {
        const response = await api.get(`/article/time_preference`, { params });
        return response.data;
    } catch (error) {
        console.error("获取文章写作时间偏好失败:", error);
        throw error;
    }
}