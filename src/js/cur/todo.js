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
export async function writeTodo(params) {
    try {
        const response = await api.post(`/todo/record_todo`,  params );
        return response.data;
    } catch (error) {
        console.error("新增 todo 失败:", error);
        throw error;
    }
}