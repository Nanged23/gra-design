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
import init from '../components/init/init.vue' 
import indexPage from '@/components/indexPage.vue'; 
import defaultPage from '@/components/defaultPage.vue';
const routes = [
  { 
    path: '/', 
    redirect: '/indexPage',
  },
  { 
    path: '/indexPage', 
    component: indexPage,
    children: [
      {path:'',component:defaultPage},
      { path: 'article', component: article },
      { path: 'moment', component: moment },
      { path: 'gallery', component: gallery }, 
      { path: 'todo', component: todo },
      { path: 'write', component: write },
      { path: 'third', component: third },
      { path: 'third_keep', component: third_keep },
      { path: 'third_weread', component: third_weread },
      { path: 'third_douban', component: third_douban },
      { path: 'statistics', component: statistics }
    ]
  },
  { path: '/init', component: init }
];

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router;
