// axiosConfig.js
import axios from "axios";

// 创建 Axios 实例
const instance = axios.create({
  // 基础 URL，所有请求都会基于这个 URL 发送
  baseURL: "http://u2f37p.natappfree.cc",
  // 请求超时时间，单位为毫秒
  timeout: 5000,
  // 设置请求头
  headers: {
    "Content-Type": "application/json",
  },
});

// 请求拦截器
instance.interceptors.request.use(
  (config) => {
    // 在发送请求之前做些什么，例如添加 token
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    // 处理请求错误
    console.error("请求出错:", error);
    return Promise.reject(error);
  }
);

// 响应拦截器
instance.interceptors.response.use(
  (response) => {
    // 对响应数据做点什么
    return response.data;
  },
  (error) => {
    // 处理响应错误
    console.error("响应出错:", error);
    return Promise.reject(error);
  }
);

export default instance;
