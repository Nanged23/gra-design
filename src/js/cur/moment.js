import api from '../../api/axios.js'
export async function getMomentList(params) {
    try {
        const response = await api.get(`/moment/get`, { params });
        return response.data;
    } catch (error) {
        console.error("获取瞬间列表失败:", error);
        throw error;
    }
}
export async function addMomentList(params) {
    try {
        const response = await api.post(`/moment/write`, params);
        return response.data;
    } catch (error) {
        console.error("获取瞬间列表失败:", error);
        throw error;
    }
}