import api from '../../api/axios.js'
export async function getBookShelf(params) {
    try { 
        const response = await api.post(`/weread/info/`, params );
        console.log(response);
        
        return response;
    } catch (error) {
        console.error("获取微信读书列表失败:", error);
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