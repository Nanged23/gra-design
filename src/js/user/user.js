import api from '../../api/axios.js'
export async function getVerifyCode(params) {
    try {
        const response = await api.post(`/user/get_code`, params);
        return response;
    } catch (error) {
        console.error("获取验证码失败:", error);

    }
}
export async function register(params) {
    try {
        const response = await api.post(`/user/register`, params);
        return response;
    } catch (error) {
        console.error("注册失败:", error);

    }
}
export async function login(params) {
    try {
        const response = await api.post(`/user/login`, params);
        return response;
    } catch (error) {
        console.error("获取验证码失败:", error);

    }
}