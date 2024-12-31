// `src/main.js`
import { createApp } from 'vue';
import App from './App.vue';
import './assets/styles.css';
import router from './router';
import store from './store';
import axios from './plugins/axios'; // 引入 Axios
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App);

app.config.globalProperties.$axios = axios; // 将 Axios 挂载为全局属性
app.use(store) // 挂载 Vuex
  .use(router) // 挂载路由
  .use(ElementPlus) // 挂载 Element Plus
  .mount('#app');
