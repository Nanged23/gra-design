import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useArticleStore = defineStore('article', () => {
    const currentArticle = ref(null);
    const setCurrentArticle = (article) => {
        currentArticle.value = article;
    };
    return { currentArticle, setCurrentArticle };
});