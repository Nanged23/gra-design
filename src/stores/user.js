import { defineStore } from "pinia";
import { ref } from "vue";
export const useUserStore = defineStore(
  "counter",
  () => {
    const isLogin = ref(false);
    const onLogin = () => {
      isLogin.value = true;
    };
    return { isLogin, onLogin };
  },
  {
    persist: true, // 开启持久化
  }
);
