<template>
  <div class="container">
    <el-card class="cardBox">
      <div class="form" :class="!isLogin ? 'left' : 'right'">
        <img src="../assets/login/logo.png" class="loginLogo" alt="" />
        <el-form
          class="formPosition"
          ref="ruleFormRef"
          :model="ruleForm"
          status-icon
          :rules="rules"
        >
          <el-form-item prop="email">
            <vs-input v-model="value1" placeholder="邮箱">
              <template #icon>
                <el-icon><Message /></el-icon>
              </template>
            </vs-input>
          </el-form-item>
          <el-form-item prop="pasword">
            <vs-input
              type="password"
              v-model="value"
              label-placeholder="Password"
              :progress="getProgress"
              :visiblePassword="hasVisiblePassword"
              icon-after
              @click-icon="hasVisiblePassword = !hasVisiblePassword"
            >
              <template #icon>
                <i v-if="!hasVisiblePassword" class="bx bx-show-alt"></i>
                <i v-else class="bx bx-hide"></i>
              </template>

              <template v-if="getProgress >= 100" #message-success>
                Secure password
              </template>
            </vs-input>
          </el-form-item>
          <el-form-item>
            <el-button
              class="btn"
              type="primary"
              @click="submitForm(ruleFormRef)"
            >
              {{ !isLogin ? "登录" : "注册" }}
            </el-button>
          </el-form-item>
        </el-form>
        <div class="info">
          <span> {{ isLogin ? "没有账号？" : "已有账户？" }}</span>
          <el-link type="primary" @click="handle">{{
            isLogin ? "立即注册!" : "立即登录!"
          }}</el-link>
        </div>
      </div>
      <div :class="isLogin ? 'left leftBack' : 'right rightBack'" class="img">
        <img
          v-if="!isLogin"
          src="../assets/login/think.png"
          class="think"
          alt=""
        />
        <img v-else src="../assets/login/surf.png" class="surf" alt="" />
      </div>
    </el-card>
  </div>
</template>
<script setup>
import { ref } from "vue";

const ruleForm = ref({});
const isLogin = ref(false);
const handle = () => {
  isLogin.value = !isLogin.value;
};
</script>
<style lang="less" scoped>
.container {
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, #caf4fb, #f8ebed);
  display: flex;
  justify-content: center;
  align-items: center;
  .cardBox {
    width: 1200px;
    height: 650px;
    border-radius: 20px;
    overflow: hidden;
    position: relative;
    background-color: linear-gradient(to right, #ebe4f6, #f7eef9);
    .form {
      position: absolute;
      width: 600px;
      height: 100%;
      transition: all 1s ease;
      background-color: #f7eef9;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px;
      .formPosition {
        margin-top: 40px;
        padding: 20px;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      .loginLogo {
        width: 120px;
        height: 120px;
      }
    }
    .img {
      width: 600px;
      height: 100%;
      position: absolute;
      transition: all 1s ease;

      display: flex;
      justify-content: center;
      align-items: center;
    }

    .left {
      left: 0;
      right: 600px;
    }
    .right {
      right: 0;
      left: 600px;
    }
  }

  ::v-deep(.el-card__body) {
    height: 100%;
    padding: 0;
    background: linear-gradient(to right, #f7eef9, #ebe4f6);
  }
}
.leftBack {
  background-color: #beeef6;
}
.rightBack {
  background-color: #ebe4f6;
}
.think {
  width: 70%;
}
.surf {
  width: 50%;
}
.info {
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
}
::v-deep(.el-link__inner) {
  font-size: 14px;
  color: #53aca1;
}
.btn {
  width: 200px;
  height: 40px;
  background-color: #2e9d8f;
}
</style>
