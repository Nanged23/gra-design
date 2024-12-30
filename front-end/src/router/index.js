import { createRouter, createWebHistory } from 'vue-router';
import article from '../components/write/article.vue';
import moment from '../components/write/moment.vue';
import gallery from '../components/write/gallery.vue';
import write from '../components/write/write.vue';
import todo from '../components/write/todo.vue';
import third from '../components/third-content/third.vue';
import third_keep from '../components/third-content/third_keep.vue';
import third_weread from '../components/third-content/third_weread.vue';
import third_douban from '../components/third-content/third_douban.vue';
import statistics from '../components/statistic/statistics.vue'
import login from '../components/init/login.vue'
import register from '../components/init/register.vue'
import demo from '../components/init/demo.vue' 

const routes = [
  { path: '/article', component: article, name: 'article' },
  { path: '/moment', component: moment, name: 'moment' },
  { path: '/gallery', component: gallery, name: 'gallery' },
  { path: '/todo', component: todo, name: 'todo' },
  { path: '/write', component: write, name: 'write' },
  { path: '/third', component: third, name: 'third' },
  { path: '/third_keep', component: third_keep, name: 'third_keep' },
  { path: '/third_weread', component: third_weread, name: 'third_weread' },
  { path: '/third_douban', component: third_douban, name: 'third_douban' },
  { path: '/statistics', component: statistics, name: 'statistics' },
  { path: '/login', component: login, name: 'login' },
  { path: '/register', component: register, name: 'register' },
  { path: '/demo', component: demo, name: 'demo' }, 
];

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router;
