<template>
    <el-page-header @back="goBack">
        <template #content>
            <span class="text-large font-600 mr-3"> Title </span>
        </template>
    </el-page-header>
    写文章...
</template>
<script setup>
const goBack = () => {
    console.log("返回文章总览");

};
</script>
 