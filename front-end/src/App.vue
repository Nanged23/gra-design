<template>
 
  <router-view />
 
</template>
<script>
import indexPage from './components/indexPage.vue'
import Loading from './components/Loading.vue';
import login from './components/init/login.vue'
import register from './components/init/register.vue';
export default {
  components: { 
  
    indexPage
  },

}
</script>
<style> 

</style>