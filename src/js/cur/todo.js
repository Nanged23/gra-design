import api from '../../api/axios.js'
export async function getTodoList(params) {
    try {
        const response = await api.get(`/todo/get_todo`, { params });
        return response.data;
    } catch (error) {
        console.error("获取 todo 列表失败:", error);
        throw error;
    }
}