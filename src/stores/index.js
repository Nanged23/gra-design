import piniaPluginPersistedstate from "pinia-plugin-persistedstate"; //pinia持久化
import { createPinia } from "pinia";
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
export default pinia;
