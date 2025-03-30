import api from '../../api/axios.js'
export async function getYearlyTodos(params) {
    try {
        const response = await api.get(`/todo/annually_todos`, { params });
        return response.data;
    } catch (error) {
        console.error("获取todo-年度失败:", error);
        throw error;
    }
}
export async function getMonthlyTodos(params) {
    try {
        const response = await api.get(`/todo/monthly_todos`, { params });
        return response.data;
    } catch (error) {
        console.error("获取todo-月度失败:", error);
        throw error;
    }
}