<style scoped>
@import url("https://fonts.googleapis.com/css?family=Raleway:400,700");

body {
  background-color: #272727;
  margin: 0;
  padding: 0;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

.tips {
  text-align: center;
  font-weight: 600;
  margin-top: 5px;
}

.tips span:last-child {
  color: rgb(110, 87, 179);
  cursor: pointer;
}

*,
*:before,
*:after {
  box-sizing: border-box;
}

.container {
  top: 0;
  left: 0;
  position: fixed;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.container:hover .top:before,
.container:hover .top:after,
.container:hover .bottom:before,
.container:hover .bottom:after,
.container:active .top:before,
.container:active .top:after,
.container:active .bottom:before,
.container:active .bottom:after {
  margin-left: 200px;
  transform-origin: -200px 50%;
  transition-delay: 0s;
  z-index: 1;
}

.container:hover .center,
.container:active .center {
  opacity: 1;
  transition-delay: 0.2s;
}

.top:before,
.top:after,
.bottom:before,
.bottom:after {
  content: '';
  display: block;
  position: absolute;
  width: 200vmax;
  height: 200vmax;
  top: 50%;
  left: 50%;
  margin-top: -100vmax;
  transform-origin: 0 50%;
  transition: all 0.5s cubic-bezier(0.445, 0.05, 0, 1);
  z-index: 10;
  opacity: 0.65;
  transition-delay: 0.2s;
}

.top:before {
  transform: rotate(45deg);
  background: #e46569;
}

.top:after {
  transform: rotate(135deg);
  background: #ecaf81;
}

.bottom:before {
  transform: rotate(-45deg);
  background: #60b8d4;
}

.bottom:after {
  transform: rotate(-135deg);
  background: #3745b5;
}

.center {
  border-radius: 20px;
  background: #f7f6f6;
  position: relative;
  /* 从 absolute 改为 relative */
  width: 400px;
  height: auto;
  /* 改为 auto */
  min-height: 300px;
  /* 设置最小高度 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 30px;
  opacity: 0;
  transition: all 0.5s cubic-bezier(0.445, 0.05, 0, 1);
  transition-delay: 0s;
  color: #333;
  z-index: 2;
}

.input-items {
  position: relative;
  width: 100%;
  margin: 5px 0;
}

.input-items .input-tips {
  display: block;
  margin-bottom: 5px;
}

.center input {
  width: 100%;
  padding: 15px;
  border-radius: 10px;
  border: 2px solid #bad0be;
  font-family: inherit;
}

.verify-group {
  position: relative;
  width: 100%;
}

.verify-group input {
  width: 100%;
  padding-right: 120px;
}

.verify-btn {
  position: absolute;
  right: 2px;
  top: 50%;
  transform: translateY(-50%);
  width: 110px;
  padding: 8px 5px;
  text-align: center;
  border: none;
  cursor: pointer;
  font-weight: 700;
  color: rgb(51, 49, 116);
  background: transparent;
  transition: 0.4s;
}

.btn {
  width: 100px;
  padding: 5px;
  text-align: center;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 700;
  color: rgb(51, 49, 116);
  margin: 10px auto;
  /* 减少上下的外边距 */
  transition: 0.4s;
  border: none;
  background: #ddcff1;
  display: block;
}

.btn:hover {
  transform: scale(1.1);
}

#info {
  min-height: 20px;
  /* 确保有空间显示提示 */
  margin: 5px 0;
  /* 减少与上下元素的距离 */
}
</style>

<template>
  <div class="container">
    <div class="top"></div>
    <div class="bottom"></div>
    <div class="center">
      <h2>注册</h2>
      <div class="input-items">
        <span class="input-tips">📮邮箱</span>
        <input type="email" v-model="email" placeholder="请输入邮箱~" />
      </div>
      <div class="input-items">
        <span class="input-tips">🔑密码</span>
        <input type="password" v-model="password" placeholder="请输入密码~" />
      </div>
      <div class="input-items">
        <span class="input-tips">🛡️验证码</span>
        <div class="verify-group">
          <input type="text" v-model="verifyCode" placeholder="请输入验证码～" />
          <div class="verify-btn" @click="getCode">
            {{ countdown > 0 ? `${countdown}s后重发` : '获取验证码' }}
          </div>
        </div>
      </div>
      <div id="info" :class="infoClass" :style="{ color: '#e14e74' }">
        {{ infoText }}
      </div>
      <button type="button" class="btn" @click="handleRegister">
        立即注册
      </button>
      <div class="tips">
        <span>已有账号?</span>
        <span id="login" @click="goToLogin">立即登录</span>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { getVerifyCode, register } from '@/js/user.js'
import { ElMessage } from 'element-plus'

const email = ref('')
const password = ref('')
const verifyCode = ref('')
const infoText = ref('')
const infoClass = ref('')
const countdown = ref(0)
const router = useRouter()

const getCode = async () => {
  if (countdown.value > 0 || !email.value) return
  let params = {
    "email": email.value
  }
  const res = await getVerifyCode(params)

  if (res.status === 200) {
    ElMessage({
      message: "验证码发送成功，请注意查收～",
      type: 'success',
    })
    countdown.value = 60
    const timer = setInterval(() => {
      countdown.value--
      if (countdown.value <= 0) {
        clearInterval(timer)
      }
    }, 1000)
  } else {
    ElMessage({
      message: "网络错误，请稍后再试～",
      type: 'error',
    })
  }
}

const handleRegister = async () => {
  if (!email.value || !password.value || !verifyCode.value) {
    infoText.value = '请填写所有字段'
    return
  }

  try {
    const res = await register({
      email: email.value,
      password: password.value,
      code: verifyCode.value
    })

    if (res.statusCode === 200) {
      ElMessage({
        message: "注册成功，即将跳转登录～",
        type: 'success',
      })
      setTimeout(() => {
        router.push('/login')
      }, 1500)
    } else {
      infoText.value = res.message || '注册失败，请重试'
    }
  } catch (error) {
    ElMessage({
      message: "注册失败，用户名已存在～",
      type: 'error',
    })
  }
}

const goToLogin = () => {
  router.push('/login')
}
</script>