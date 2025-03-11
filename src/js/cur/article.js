 import api from '../../api/axios.js'
export async function getArticleList(params) { 
  try {
    const response = await api.get(`/article/get`, { params }); 
    return response.data;  
  } catch (error) {
    console.error("获取用户信息失败:", error);
    throw error;  
  }
}