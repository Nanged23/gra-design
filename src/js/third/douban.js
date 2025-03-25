import api from '../../api/axios.js'
export async function getList(params) {
    try { 
        const response = await api.get(`/douban/data/`, { params });
        return response.data;
    } catch (error) {
        console.error("获取豆瓣列表失败:", error);
        throw error;
    }
}
export async function getUser(params) {
    try { 
        const response = await api.get(`/douban/user/`, { params });
        return response.data;
    } catch (error) {
        console.error("获取豆瓣用户失败:", error);
        throw error;
    }
}