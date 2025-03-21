<template> 
<router-view />
</template>

<script> 
import login from './components/user/login.vue'
export default {
  name: 'App',
  components: {
  login
  }
}
</script>

<style>
#app { 
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
   
}
</style>
