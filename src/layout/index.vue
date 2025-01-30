<template>
  <div class="layout">
    <div class="side" :class="{ fold, unfold: !fold }">
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        :collapse="fold"
        @open="handleOpen"
        @close="handleClose"
      >
      </el-menu>
      <div class="buttons">
        <i class="iconfont icon-fix"></i>
        <el-icon class="iconfont"><House /></el-icon>
        <i class="iconfont icon-shezhi"></i>
      </div>
    </div>
    <div class="content" @click="onFold"><RouterView /></div>
    <el-button class="unFoldBtn" circle v-if="fold" @click="open">
      <el-icon><DArrowRight /></el-icon>
    </el-button>
  </div>
</template>
<script setup>
import { ref } from "vue";
const fold = ref(false);
const onFold = () => {
  if (!fold.value) {
    fold.value = true;
  }
};
const open = () => {
  fold.value = false;
};
</script>
<style scoped lang="less">
.layout {
  width: 100%;
  height: 100%;
  display: flex;
  .side {
    transition: all 0.5s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    border-right: 1px solid #ccc;
    .buttons {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      padding-bottom: 10px;
      .iconfont {
        font-size: 28px;
        margin: 5px 18px 5px;
      }
    }
  }
  .content {
    flex: 1;
    transition: all 0.5s ease;
  }
  .fold {
    width: 0;
  }
  .unfold {
    width: 200px;
  }
  .unFoldBtn {
    width: 50px;
    height: 50px;
    position: fixed;
    bottom: 30px;
    left: 30px;
    font-size: 24px;
  }
}
</style>
