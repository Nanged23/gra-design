import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from "@/stores/user";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/login",
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/login.vue"),
    },
    {
      path: "/main",
      name: "main",
      component: () => import("../layout/index.vue"),
    },
  ],
});
router.beforeEach((to, from, next) => {
  const user = useUserStore();

  if (to.path !== "/login" && !user.isLogin) {
    next("/login");
  }
  next();
});
export default router;
