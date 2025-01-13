<template>
    <div class="content" :class="{ 'sidebar-collapsed': isCollapsed }">
        <div class="text-content" :class="{ 'text-collapsed': isCollapsed }">
            这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article 这是 article
        </div>
    </div>
</template>

<script>
export default {
     
    data() {
        return {
            isCollapsed: false
        }
    },
    mounted() {
       
    },
    methods: {
       
    },
    
}
</script>

<style scoped>
.content {
    position: relative; 
    margin-top: 60px;
    padding: 20px;
    transition: all 0.3s ease;
    width: calc(100% - 290px);
}

.content.sidebar-collapsed {
    margin-left: 70px;
    width: calc(100% - 90px);
}

.text-content {
    width: 100%;
    transition: all 0.3s ease;
}
</style>