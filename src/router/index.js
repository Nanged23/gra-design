import { createRouter, createWebHistory } from 'vue-router';
import article_analyse from '@/components/analyse/article_analyse.vue';
import moment_analyse from '@/components/analyse/moment_analyse.vue';
import todo_analyse from '@/components/analyse/todo_analyse.vue';
import article from '@/components/cur/article.vue';
import moment from '@/components/cur/moment.vue';
import todo from '@/components/cur/todo.vue';
import douban from '@/components/third/douban.vue';
import weread from '@/components/third/weread.vue';
import login from '@/components/user/login.vue';
import register from '@/components/user/register.vue';
import index from '@/components/analyse/index.vue';
import defaultPage from '@/components/defaultPage.vue';
import settings from '@/components/index/settings.vue';
import articleDetail from '@/components/cur/articleDetail.vue';
import writeArticle from '@/components/cur/writeArticle.vue';
const routes = [
    {
        path: '/',
        name: 'defaultPage',
        component: defaultPage,
    }, {
        path: '/settings',
        name: 'settings',
        component: settings
    },
    {
        path: '/login',
        name: 'login',
        component: login
    },
    {
        path: '/register',
        name: 'register',
        component: register
    },
    {
        path: '/analyse/article',
        name: 'article_analyse',
        component: article_analyse,
    }, {
        path: '/analyse/moment',
        name: 'moment_analyse',
        component: moment_analyse,
    },
    {
        path: '/analyse/todo',
        name: 'todo_analyse',
        component: todo_analyse,
    },
    {
        path: '/article',
        name: 'article',
        component: article
    }, {
        path: '/moment',
        name: 'moment',
        component: moment
    }, {
        path: '/todo',
        name: 'todo',
        component: todo
    },
    {
        path: '/third/douban',
        name: 'douban',
        component: douban,
    },
    {
        path: '/third/weread',
        name: 'weread',
        component: weread,
    }, {
        path: '/analyse/index',
        name: 'index',
        component: index,
    },
    {
        path: '/articleDetail/:slug',
        name: 'articleDetail',
        component: articleDetail,
    },
    {
        path: '/writeArticle',
        name: 'writeArticle',
        component: writeArticle,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;