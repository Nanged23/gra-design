// `src/main.js`
import { createApp } from 'vue';
import App from './App.vue'; 
import router from './router';
import store from './store';
import axios from './plugins/axios'; // 引入 Axios
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import "core-js/stable";
import "regenerator-runtime/runtime";
import Vuesax from 'vuesax-alpha'
// style
import 'vuesax-alpha/dist/index.css'
// vuesax darkmode
import 'vuesax-alpha/theme-chalk/dark/css-vars.css'
const app = createApp(App);

app.config.globalProperties.$axios = axios; // 将 Axios 挂载为全局属性
app.use(store) // 挂载 Vuex
  .use(router) // 挂载路由
  .use(ElementPlus) // 挂载 Element Plus
  .use(Vuesax) 
  .mount('#app');


  