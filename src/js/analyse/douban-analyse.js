import api from '../../api/axios.js'
export async function getDouBan(params) {
    try {
        const response = await api.get(`/douban/summary`, { params });
        return response.data;
    } catch (error) {
        console.error("获取douban总结失败:", error);
        throw error;
    }
}