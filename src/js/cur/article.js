import api from '../../api/axios.js'
export async function getArticleList(params) {
  try {
    const response = await api.get(`/article/get`, { params });
    return response.data;
  } catch (error) {
    console.error("获取文章列表失败:", error);
    throw error;
  }
}
export async function getSingleArticle(params) {
  try {
    const response = await api.get(`/article/get`, { params });
    return response.data;
  } catch (error) {
    console.error("获取单篇文章失败:", error);
    throw error;
  }
}