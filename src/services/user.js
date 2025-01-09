// 这里是有关用户个人信息的服务
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000/user/',
  headers: {
    'Content-Type': 'application/json'
  }
});
// 注册
export const register = async (email, password, code) => {
  try {
    const response = await apiClient.post('/register', {
      email, password, code
    })
    return response;
  } catch (error) {
    console.error(error);
    return error.response;
  }
};
// 登录
export const login = async (email, password) => {
  try {
    const response = await apiClient.post('/login', {
      email, password
    })

    return response;
  } catch (error) {
    console.error(error);
    return error.response;
  }
}
// 获取验证码
export const getCode = async (email) => {
  try {
    const response = await apiClient.post('/get_code', {
      email
    })
    return response;
  } catch (error) {
    console.error(error);
    return error.response;
  }
}
