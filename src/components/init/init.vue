  <template>

    <div class="container">
      <div class="login-container">
        <div class="leftSection" :class="{ leftActive: isSwitched, rightActive: !isSwitched }">
          <img v-if="!isSwitched" src="../../assets/think.png" style="margin-top:50px"></img>
          <img v-else src="../../assets/surf.png" style="transform: scale(0.55);"></img>
        </div>
        <div class="rightSection" :class="{ rightActive: isSwitched, leftActive: !isSwitched }">
          <div v-if="!isSwitched">
            <div class="login-form">
              <div class="logo">
                <img src="../../assets/logo.png" alt="logo" />
              </div>
              <form @submit.prevent="handleSubmit">
                <div class="form-group">
                  <div class="input-wrapper">
                    <input type="email" v-model="email" placeholder="邮箱" @blur="validateEmail"
                      :class="{ error: emailError }">
                    <svg class="input-icon" t="1734505635026" viewBox="0 0 1024 1024" version="1.1"
                      xmlns="http://www.w3.org/2000/svg" p-id="10395" width="20" height="20">
                      <path
                        d="M805.56544 134.55872H218.43456c-75.74528 0-137.25184 61.50656-137.25184 137.25184v480.37888c0 75.74528 61.51168 137.25184 137.25184 137.25184h587.13088c75.74528 0 137.25696-61.50656 137.25696-137.25184V271.81056c-0.512-75.74528-61.51168-137.25184-137.25696-137.25184zM138.68544 695.28064V328.70912l183.53664 183.04512-183.53664 183.5264z m453.4016-154.94144c-21.1968 21.19168-49.77664 33.01888-80.3328 33.01888s-58.64448-11.83232-80.32768-33.01888L142.62784 251.04896c11.33568-36.96128 44.35456-61.11232 84.76672-61.11232h569.21088c40.41728 0 73.43616 23.6544 84.76672 61.11232l-289.28512 289.29024z m-236.15488 10.25024L399.36 590.08c34.77504 32.64 71.48544 42.51648 112.88576 42.51648 41.39008 0 77.19424-13.39392 109.19424-42.51648l41.99936-39.49056 218.92096 218.91072c-10.34752 38.93248-43.86304 64.07168-85.75488 64.07168H227.39456c-41.89184 0-75.40224-25.1392-85.75488-63.58016l214.29248-219.40224z m529.37728-221.88032v366.57152l-183.5264-183.5264 183.5264-183.04512z"
                        p-id="10396" fill="#E2E8F0"></path>
                    </svg>
                  </div>
                  <span v-if="emailError" class="error-message">{{ emailError }}</span>
                </div>

                <div class="form-group">
                  <div class="input-wrapper">
                    <input type="password" v-model="password" placeholder="密码" @blur="validatePassword"
                      :class="{ error: passwordError }">
                    <svg class="input-icon" t="1734505437475" viewBox="0 0 1024 1024" version="1.1"
                      xmlns="http://www.w3.org/2000/svg" p-id="4288" width="20" height="20">
                      <path
                        d="M753.845117 371.674021l-17.46272 0 0-83.669608c0-59.275012-22.62837-115.203812-63.715137-157.482731-42.170448-43.394323-99.369172-67.291592-161.058163-67.291592-126.040624 0-224.772276 98.731652-224.772276 224.7733l0 83.669608-16.680914 0c-62.788022 0-113.688295 50.900274-113.688295 113.688295L156.467611 842.961784c0 62.788022 50.900274 113.688295 113.688295 113.688295l483.690234 0c62.788022 0 113.688295-50.900274 113.688295-113.688295L867.534436 485.362316C867.532389 422.574295 816.633139 371.674021 753.845117 371.674021zM328.176344 288.005436c0-102.858646 80.573083-183.432753 183.431729-183.432753 50.423413 0 97.093339 19.447934 131.410935 54.762231 33.547047 34.519188 52.021817 80.214926 52.021817 128.670521l0 83.669608L328.176344 371.675044 328.176344 288.005436zM826.191842 842.961784c0 39.956014-32.390711 72.346725-72.346725 72.346725L270.154883 915.308509c-39.956014 0-72.346725-32.390711-72.346725-72.346725L197.808158 485.362316c0-39.956014 32.390711-72.346725 72.346725-72.346725l483.690234 0c39.956014 0 72.346725 32.390711 72.346725 72.346725L826.191842 842.961784z"
                        fill="#E2E8F0" p-id="4289"></path>
                      <path
                        d="M509.932921 580.446905c-11.416004 0-20.670785 9.254781-20.670785 20.670785l0 109.554138c0 11.414981 9.254781 20.670785 20.670785 20.670785 11.416004 0 20.670785-9.254781 20.670785-20.670785L530.603707 601.116667C530.602683 589.701686 521.348925 580.446905 509.932921 580.446905z"
                        fill="#E2E8F0" p-id="4290"></path>
                    </svg>
                  </div>
                  <span v-if="passwordError" class="error-message">{{ passwordError }}</span>
                </div>

                <button type="submit" class="sign-in-btn">登录</button>


              </form>
              <p class="signup-prompt">
                没有账户？ <a @click="gotoRegister" style="cursor: pointer;">立即注册！</a>
              </p>
            </div>
          </div>
          <div v-else>
            <div class="login-form">
              <div class="logo">
                <img src="../../assets/logo.png" alt="logo" />
              </div>
              <form @submit.prevent="handleSubmit2">
                <div class="form-group">
                  <div class="input-wrapper">
                    <input type="email" v-model="email" placeholder="邮箱" @blur="validateEmail"
                      :class="{ error: emailError }">
                    <svg class="input-icon" t="1734505635026" viewBox="0 0 1024 1024" version="1.1"
                      xmlns="http://www.w3.org/2000/svg" p-id="10395" width="20" height="20">
                      <path
                        d="M805.56544 134.55872H218.43456c-75.74528 0-137.25184 61.50656-137.25184 137.25184v480.37888c0 75.74528 61.51168 137.25184 137.25184 137.25184h587.13088c75.74528 0 137.25696-61.50656 137.25696-137.25184V271.81056c-0.512-75.74528-61.51168-137.25184-137.25696-137.25184zM138.68544 695.28064V328.70912l183.53664 183.04512-183.53664 183.5264z m453.4016-154.94144c-21.1968 21.19168-49.77664 33.01888-80.3328 33.01888s-58.64448-11.83232-80.32768-33.01888L142.62784 251.04896c11.33568-36.96128 44.35456-61.11232 84.76672-61.11232h569.21088c40.41728 0 73.43616 23.6544 84.76672 61.11232l-289.28512 289.29024z m-236.15488 10.25024L399.36 590.08c34.77504 32.64 71.48544 42.51648 112.88576 42.51648 41.39008 0 77.19424-13.39392 109.19424-42.51648l41.99936-39.49056 218.92096 218.91072c-10.34752 38.93248-43.86304 64.07168-85.75488 64.07168H227.39456c-41.89184 0-75.40224-25.1392-85.75488-63.58016l214.29248-219.40224z m529.37728-221.88032v366.57152l-183.5264-183.5264 183.5264-183.04512z"
                        p-id="10396" fill="#E2E8F0"></path>
                    </svg>
                  </div>
                  <span v-if="emailError" class="error-message">{{ emailError }}</span>
                </div>
                <div class="form-group">
                  <div class="input-wrapper">
                    <input type="text" v-model="code" placeholder="验证码" @blur="validateCode"
                      :class="{ error: codeError }">
                    <svg t="1736316469397" class="input-icon" viewBox="0 0 1024 1024" version="1.1"
                      xmlns="http://www.w3.org/2000/svg" p-id="4262" width="20" height="20">
                      <path
                        d="M943.1 172c-2.4-0.2-245.1-25.3-413.8-147.8-5.1-3.7-11-5.6-17.3-5.6-6.2 0-12.2 1.9-17.3 5.6C326.9 146 83.3 171.8 80.9 172c-15.2 1.4-26.6 14.1-26.6 29.3 0 6.7 0.6 165.8 54.8 344.4 32.1 105.8 76.4 196.4 131.9 269.2 70.3 92.3 158.5 156 262 189.2 2.9 0.9 5.9 1.4 9 1.4s6.1-0.5 8.9-1.4c103.6-33.2 191.7-96.8 262-189.2 55.4-72.7 99.8-163.2 131.9-269.2 54.1-178.6 54.8-337.7 54.8-344.4C969.7 186.1 958.3 173.5 943.1 172zM910.1 227.2l-0.1 1.6c-2.9 58.1-13.4 174.4-51.4 299.9-66.7 220.1-183.1 360.1-346 416.1L512 945l-0.6-0.2C349 888.9 232.7 749.4 165.8 530.1c-39.8-130.5-49.4-254.2-51.8-301.4l-0.1-1.6 1.5-0.2c70.6-10.3 250.5-44.8 395.5-142.4l0.9-0.7 1 0.7C658 182.1 837.9 216.6 908.5 227L910.1 227.2z"
                        p-id="4263" fill="#E2E8F0"></path>
                      <path
                        d="M641.8 351 467 580.3l-89-76.1c-5.3-4.5-12.1-7-19.1-7-8.6 0-16.8 3.7-22.4 10.3-10.5 12.3-9.1 31 3.3 41.5l112.7 96.4c5.2 4.4 12.4 7 19.6 7 0.9 0 1.8 0 2.7-0.1 8-0.8 15.4-5 20.3-11.4l193.7-254c4.8-6.3 6.8-14 5.7-21.8-1-7.8-5.1-14.7-11.3-19.5C670.1 335.6 651.6 338.1 641.8 351z"
                        p-id="4264" fill="#E2E8F0"></path>
                    </svg>
                    <button :class="['verify-btn', { 'disabled': isCountingDown }]" :disabled="isCountingDown"
                      @click="startCountdown">
                      {{ buttonText }}
                    </button>
                  </div>
                  <span v-if="codeError" class="error-message">{{ codeError }}</span>
                </div>
                <div class="form-group">
                  <div class="input-wrapper">
                    <input type="password" v-model="password" placeholder="密码" @blur="validatePassword"
                      :class="{ error: passwordError }">
                    <svg class="input-icon" t="1734505437475" viewBox="0 0 1024 1024" version="1.1"
                      xmlns="http://www.w3.org/2000/svg" p-id="4288" width="20" height="20">
                      <path
                        d="M753.845117 371.674021l-17.46272 0 0-83.669608c0-59.275012-22.62837-115.203812-63.715137-157.482731-42.170448-43.394323-99.369172-67.291592-161.058163-67.291592-126.040624 0-224.772276 98.731652-224.772276 224.7733l0 83.669608-16.680914 0c-62.788022 0-113.688295 50.900274-113.688295 113.688295L156.467611 842.961784c0 62.788022 50.900274 113.688295 113.688295 113.688295l483.690234 0c62.788022 0 113.688295-50.900274 113.688295-113.688295L867.534436 485.362316C867.532389 422.574295 816.633139 371.674021 753.845117 371.674021zM328.176344 288.005436c0-102.858646 80.573083-183.432753 183.431729-183.432753 50.423413 0 97.093339 19.447934 131.410935 54.762231 33.547047 34.519188 52.021817 80.214926 52.021817 128.670521l0 83.669608L328.176344 371.675044 328.176344 288.005436zM826.191842 842.961784c0 39.956014-32.390711 72.346725-72.346725 72.346725L270.154883 915.308509c-39.956014 0-72.346725-32.390711-72.346725-72.346725L197.808158 485.362316c0-39.956014 32.390711-72.346725 72.346725-72.346725l483.690234 0c39.956014 0 72.346725 32.390711 72.346725 72.346725L826.191842 842.961784z"
                        fill="#E2E8F0" p-id="4289"></path>
                      <path
                        d="M509.932921 580.446905c-11.416004 0-20.670785 9.254781-20.670785 20.670785l0 109.554138c0 11.414981 9.254781 20.670785 20.670785 20.670785 11.416004 0 20.670785-9.254781 20.670785-20.670785L530.603707 601.116667C530.602683 589.701686 521.348925 580.446905 509.932921 580.446905z"
                        fill="#E2E8F0" p-id="4290"></path>
                    </svg>
                  </div>
                  <span v-if="passwordError" class="error-message">{{ passwordError }}</span>
                </div>

                <button type="submit" class="sign-in-btn">注册</button>


              </form>
              <p class="signup-prompt">
                已有账户？ <a @click="gotoLogin" style="cursor: pointer;">立即登录！</a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </template>

<script>
import { ElMessage } from 'element-plus';
import { login } from '../../services/user.js'
import { register } from '../../services/user.js'
import { getCode } from '../../services/user.js'
export default {
  data() {
    return {
      email: '',
      password: '',
      emailError: '',
      code: '',
      codeError: '',
      passwordError: '',
      isSwitched: false,
      isCountingDown: false,
      countdown: 60,
      buttonText: '获取验证码'
    }
  },
  methods: {
    setCookie(username) {
      if (localStorage.getItem('user_name')) {
        localStorage.removeItem('user_name')
      }
      localStorage.setItem('user_name', username)
    },
    async startCountdown() {
      this.isCountingDown = true;
      this.countdown = 60;
      const timer = setInterval(() => {
        this.countdown--;
        this.buttonText = `${this.countdown}s 后重试`;
        if (this.countdown <= 0) {
          clearInterval(timer);
          this.isCountingDown = false;
          this.buttonText = '获取验证码';
        }
      }, 1000);
      let answer = await getCode(this.email);
      if (answer.status != 200 && answer.status != 201) {
        ElMessage.error(answer.data.data)
        console.log(answer.data.data, answer.status);
        return
      } else {
        ElMessage.success(answer.data.data)

      }
    },
    gotoLogin() {
      this.isSwitched = !this.isSwitched;
      this.emailError = ''
      this.codeError = ''
      this.passwordError = ''
    },
    gotoRegister() {
      // 逻辑和登录相同
      this.gotoLogin()
    },
    validateCode() {
      if (this.code.length != 6) {
        this.codeError = '验证码必须为 6 位！'
      } else {
        this.codeError = ''
      }
    },
    validateEmail() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (this.email && !emailRegex.test(this.email)) {
        this.emailError = '邮箱不符合规范'
      } else {
        this.emailError = ''
      }
    },
    validatePassword() {
      const hasUpperCase = /[A-Z]/.test(this.password)
      const hasLowerCase = /[a-z]/.test(this.password)

      if (this.password && (!hasUpperCase || !hasLowerCase)) {
        this.passwordError = '密码必须包含大小写字母'
      } else {
        this.passwordError = ''
      }
    },
    async handleSubmit() {
      // 登录 
      this.validateEmail()
      this.validatePassword()

      // 检查是否所有字段都已填写
      if (!this.email || !this.password) {

        ElMessage.error('请填写所有字段')
        return
      }

      // 检查是否有验证错误
      if (this.emailError || this.passwordError) {
        ElMessage.error('请修正表单中的错误')
        return
      }
      let answer = await login(this.email, this.password);
      if (answer.status != 200 && answer.status != 201) {
        ElMessage.error(answer.data.data)
        console.log(answer.data.data, answer.status);
        return
      } else {
        ElMessage.success(answer.data.data)
        console.log("登录成功");
        console.log(answer.data.mes);

        this.setCookie(answer.data.mes);
        this.$router.push('/indexPage')
      }

    },
    async handleSubmit2() {
      // 验证所有字段
      this.validateEmail()
      this.validatePassword()

      // 检查是否所有字段都已填写
      if (!this.email || !this.password || !this.code) {

        ElMessage.error('请填写所有字段')
        return
      }

      // 检查是否有验证错误
      if (this.emailError || this.passwordError || this.codeError) {
        ElMessage.error('请修正表单中的错误')
        return
      }
      let answer = await register(this.email, this.password, this.code);
      if (answer.status != 200 && answer.status != 201) {
        ElMessage.error(answer.data.data)
        console.log(answer.data.data, answer.status);
        return
      } else {
        ElMessage.success(answer.data.data)
        console.log("注册成功，已为您自动登录～");
        console.log(answer.data);
        this.setCookie(answer.data.mes);
        this.$router.push('/indexPage')
      }
    },
  }
}
</script>
<style scoped>
:root {
  --primary-color: #2A9D8F;
  --border-color: #E2E8F0;
}

.body {
  background-image: url("../../assets/bg.png");
}

.container {
  width: 100%;

  max-width: 1000px;
  display: flex;
  align-items: center;
  justify-content: center;

  margin: 130px auto;
  transition: all 1.5s ease;
}

.login-container {
  position: relative;
  background: white;
  border-radius: 24px;
  height: 570px;
  overflow: hidden;
  min-height: 500px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  max-width: 1000px;
  width: 100%;

}

.leftSection {

  width: 50%;
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  transition: all 1.5s ease;
}

.leftActive {
  left: 0;
  right: 500px;
  background-color: #bfeef6;
}

.rightActive {
  right: 0;
  left: 500px;
  background-color: #ebe4f7;
}

.rightSection {
  height: 570px;
  width: 50%;

  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  background-color: #F7EEF9;
  transition: all 1.5s ease;
}



.login-form {
  width: 100%;
  align-items: center;
  justify-content: center;
  margin-top: 0px;

}

.register-form {
  width: 100%;
  max-width: 400px;
}

.logo {
  display: flex;
  margin-bottom: 50px;
}

.logo img {
  margin-left: 80px;
  height: 100px;

}

form {
  width: 100%;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  width: 300px;
}

.input-wrapper input {
  width: 100%;
  padding: 12px 12px 12px 40px;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.input-wrapper .input-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
}

.verify-btn {
  position: absolute;
  font-size: 15px;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  padding: 6px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background: white;
  color: #333;
  cursor: pointer;
  transition: all 0.3s ease;
}

.verify-btn.disabled {
  background: #f5f5f5;
  border-color: #ddd;
  color: #999;
  cursor: not-allowed;
}

.verify-btn:hover:not(.disabled) {
  border-color: #409EFF;
  color: #409EFF;
}

.input-wrapper input:focus {
  outline: none;
  border-color: var(--primary-color);
}

.input-wrapper input::placeholder {
  color: #999;
}

.input-wrapper input.error {
  border-color: #ff4d4f;
}

.form-group {
  margin-bottom: 20px;
}

.sign-in-btn {
  margin-top: 20px;
  width: 80%;
  padding: 12px;
  margin-left: 30px;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
  background-color: #2f9d8f;
}

.sign-in-btn:hover {
  background-color: #1c5d54;
}

.signup-prompt {
  text-align: center;
  margin-top: 34px;
  margin-left: 35px;
  font-size: 14px;
  color: #718096;
}

.signup-prompt a {
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 500;
}

.error-message {
  color: #ff4d4f;
  font-size: 14px;
  margin-top: 4px;
  display: block;
}
</style>
