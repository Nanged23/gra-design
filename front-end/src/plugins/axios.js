import axios from 'axios';
import store from '@/store'; // 引入 Vuex 的 store

// 创建一个 Axios 实例
const instance = axios.create({
  baseURL: 'http://localhost:5000', // 配置你的 API 基础地址
  timeout: 5000, // 请求超时时间
  
});

// 请求拦截器：请求发起时显示加载动画
instance.interceptors.request.use((config) => {
  store.dispatch('loading/startLoading'); // 触发 Vuex 的加载动画状态
  return config;
}, (error) => {
  store.dispatch('loading/stopLoading'); // 请求错误时停止动画
  return Promise.reject(error);
});

// 响应拦截器：请求完成后隐藏加载动画
instance.interceptors.response.use((response) => {
  store.dispatch('loading/stopLoading'); // 停止加载动画
  return response;
}, (error) => {
  store.dispatch('loading/stopLoading'); // 请求错误也停止动画
  return Promise.reject(error);
});

export default instance;
