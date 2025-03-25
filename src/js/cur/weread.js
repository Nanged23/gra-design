import api from '../../api/axios.js'
export async function login(params) {
  try {
    const response = await api.get(`/weread/login`, { params });
    return response.data;
  } catch (error) {
    console.error("获取单篇文章失败:", error);
    throw error;
  }
}
export async function getCookie() {
  try {
    const response = await api.post(`/weread/cookies`, );
    return response.data;
  } catch (error) {
    console.error("获取单篇文章失败:", error);
    throw error;
  }
}
