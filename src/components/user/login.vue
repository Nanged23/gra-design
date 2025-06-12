<style scoped>
* {
  font-family: "Aguazyuan", Courier, monospace;
}

.gradient-container {
  top: 0;
  left: 0;
  position: fixed;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: linear-gradient(45deg, #0b0f30, #635ea7, #7a8dc4, #391657);
  background-size: 400% 400%;
  animation: gradientAnimation 10s ease infinite;
}

@keyframes gradientAnimation {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.particles-container {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

.particle {
  position: absolute;
  border-radius: 50%;
  background-color: rgba(118, 146, 239, 0.3);
  box-shadow: 0 0 15px 2px rgba(100, 255, 255, 0.4);
  filter: blur(6px);
  animation: floatAnimation linear infinite;
  transform: translate(-50%, -50%);
}

@keyframes floatAnimation {
  0% {
    transform: translate(-50%, -50%) translateY(0) translateX(0);
  }

  25% {
    transform: translate(-50%, -50%) translateY(-40px) translateX(40px);
  }

  50% {
    transform: translate(-50%, -50%) translateY(0) translateX(80px);
  }

  75% {
    transform: translate(-50%, -50%) translateY(40px) translateX(40px);
  }

  100% {
    transform: translate(-50%, -50%) translateY(0) translateX(0);
  }
}

.content {
  position: relative;
  z-index: 10;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0.75
}

.login-wrapper {
  width: 70vw;
  height: 80vh;
  background-color: #fff;
  border-radius: 40px;
  display: flex;
}

.left-img {
  border-radius: 40px;
  flex: 1;
  background: url(../../assets/pngs/bg.png) no-repeat;
  background-size: cover;
  position: relative;
}

.right-login-form {
  flex: 1;
  position: relative;
}

.form-wrapper {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.input-items {
  margin: 20px 0;
}

.input-tips {
  display: inline-block;
  font-weight: 600;
  font-size: 20px;
  margin: 10px 0;
}

.inputs {
  width: 100%;
  height: 50px;
  border-radius: 10px;
  border: 1px solid rgb(227, 227, 227);
  padding: 20px;
  box-sizing: border-box;
  outline: none;
  transition: 0.5s;
}

.inputs:focus {
  border: 1px solid rgb(128, 106, 196);
}

.forgot {
  float: right;
  font-weight: 600;
  text-align: right;
  margin: 5px 0;
  font-size: 13px;
  cursor: pointer;
}

.btn {
  width: 100%;
  height: 50px;
  background-color: rgb(128, 106, 196);
  border: 0;
  border-radius: 10px;
  color: #fff;
  font-size: 25px;
  margin: 20px 0;
  cursor: pointer;
}

.siginup-tips {
  text-align: center;
  font-weight: 600;
  margin: 10px 0;
}

.siginup-tips span:last-child {
  color: rgb(110, 87, 179);
  cursor: pointer;
}

 
</style>
<template>
  <div class="gradient-container">
    <div class="particles-container">
      <div v-for="n in particleCount" :key="n" class="particle" :style="{
        left: `${Math.random() * 100}%`,
        top: `${Math.random() * 100}%`,
        width: `${10 + Math.random() * 40}px`,
        height: `${10 + Math.random() * 40}px`,
        animationDelay: `${Math.random() * 2}s`,
        animationDuration: `${4 + Math.random() * 8}s`,
        opacity: 0.2 + Math.random() * 0.6,
        backgroundColor: n % 3 === 0 ? 'rgba(100, 255, 255, 0.3)' :
          n % 3 === 1 ? 'rgba(180, 180, 255, 0.3)' :
            'rgba(255, 255, 255, 0.3)'
      }"></div>
    </div>
    <div class="content">
      <div class="login-wrapper">
        <div class="left-img"></div>
        <div class="right-login-form">
          <div class="form-wrapper">
            <br />
            <div id="info" :class="infoClass" :style="{ color: '#e14e74' }">
              {{ infoText }}
            </div>
            <div class="input-items">
              <span class="input-tips">📮邮箱</span>
              <input type="text" v-model="email" class="inputs" placeholder="请输入用户名~" />
            </div>
            <div class="input-items">
              <span class="input-tips">🔑密码</span>
              <input type="password" v-model="password" class="inputs" placeholder="请输入密码~" />
              <span class="forgot">忘记密码?</span>
            </div>
            <button type="button" class="btn" @click="handleLogin">
              立即登录
            </button>
            <div class="siginup-tips">
              <span>没有账号?</span>
              <span id="register" @click="goTo('/register')">立即注册</span>
            </div>
            <br />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ElMessage } from 'element-plus'
import { ref } from 'vue'
import Cookies from 'js-cookie';
import { useRouter } from 'vue-router'
import { login } from '@/js/user/user.js';
const particleCount = ref(40);
const email = ref('')
const password = ref('')
const infoText = ref('')
const infoClass = ref('')
const router = useRouter()

const handleLogin = async () => {
  if (!email.value || !password.value) {
    infoText.value = '请输入用户名或密码~'
    infoClass.value = 'error'
  } else {
    let params = {
      "email": email.value,
      "password": password.value
    }
    const res = await login(params)

    if (res.status === 200) {
      ElMessage({
        message: "登录成功～",
        type: 'success',
      })
      let user_info = res.data.data
      Cookies.set('user_id', user_info['user_id'], { expires: 365 });
      Cookies.set('user_name', user_info['user_name'], { expires: 365 });
      goTo('/indexPage');
    } else {
      ElMessage({
        message: "网络异常，请稍后再试～",
        type: 'error',
      })
    }
  }
}

const goTo = (path) => {
  router.push(path)
}
</script>
