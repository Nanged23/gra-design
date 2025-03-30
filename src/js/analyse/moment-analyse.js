import api from '../../api/axios.js'
export async function getMomentByYear(params) {
    try {
        const response = await api.get(`/moment/annually_moods`, { params });
        return response.data;
    } catch (error) {
        console.error("获取瞬间-年度失败:", error);
        throw error;
    }
}
export async function getMomentByMonth(params) {
    try {
        const response = await api.get(`/moment/monthly_moods`, { params });
        return response.data;
    } catch (error) {
        console.error("获取瞬间-月度失败:", error);
        throw error;
    }
}