import axios from 'axios';
import api from '../../api/axios.js'
export async function getQuote() {
    try {
        const response = await axios.post('https://api.xygeng.cn/openapi/one');
        const content = response.data.data.content;
        return content;
    } catch (error) {
        console.error('请求失败:', error);
    }
}

export async function getHotMap(params) {
    try {
        const response = await api.get(`/user/get_score`, { params });
        return response.data;
    } catch (error) {
        console.error("获取用户登录热力图失败:", error);
        throw error;
    }
}
export async function getUserDetail(params) {
    try {
        const response = await api.get(`/user/detail`, { params });
        return response.data;
    } catch (error) {
        console.error("获取用户登录热力图失败:", error);
        throw error;
    }
}
export async function getMemDay(params) {
    try {
        console.log(params);
        const response = await api.get(`/todo/get_memday`, { params });
        return response.data;
    } catch (error) {
        console.error("获取纪念日失败:", error);
        throw error;
    }
}
export async function updateUser(params) {
    try {
        console.log(params);
        const response = await api.post(`/user/update`, params);
        return response.data;
    } catch (error) {
        console.error("更新用户失败:", error);
        throw error;
    }
}
export async function sendCode(params) {
    try {
        const response = await api.post(`/user/get_code`, params);
        return response;
    } catch (error) {
        console.error("获取验证码失败:", error);
        throw error;
    }
}
