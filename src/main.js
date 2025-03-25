import { createApp } from 'vue';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import App from './App.vue';
import router from './router/index.js';
import axios from 'axios';
import { createPinia } from 'pinia';
import Cookies from 'js-cookie'; 
const pinia = createPinia();
const app = createApp(App); 
app.config.globalProperties.$cookies = Cookies;
app.config.globalProperties.$axios = axios;

 
app.use(router);
app.use(ElementPlus);
app.use(pinia);
app.mount('#app');