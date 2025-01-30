import { createApp } from "vue";
import "@/assets/icon/icon.less";
import pinia from "./stores";
import App from "./App.vue";
import router from "./router";
import Vuesax from "vuesax-alpha";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
// style
import "vuesax-alpha/dist/index.css";
// vuesax darkmode
import "vuesax-alpha/theme-chalk/dark/css-vars.css";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";

const app = createApp(App);
app.use(pinia);
app.use(router);
app.use(ElementPlus);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

app.use(Vuesax);
app.mount("#app");
