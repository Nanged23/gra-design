<template>
  <div class="container">
    <div class="login-container">
      <div class="left-section">
        <div class="background-image">
          <img src="../../assets/wave.png" alt="Student studying" />
        </div>
        <div class="text-overlay">
          <h2>无人之岸，几多惊喜</h2>
          <p>在这里，记录自我成长的故事</p>
          <br>
        </div>
      </div>

      <div class="right-section">
        <div class="login-form">
          <div class="logo">
            <img src="../../assets/logo.png" alt="Mastery Hub Logo " />
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
            没有账户？ <a @click.prevent="gotoRegister" style="cursor: pointer;">立即注册！</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      emailError: '',
      passwordError: ''
    }
  },
  methods: {
    gotoRegister() {
      this.$router.push('/register')
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


          try {
              const response = await axios.post('http://localhost:5000/user/register', {
                  email: this.email,
                  password: this.password,
                  code: this.code
              })
              
              // 展示返回的消息
              ElMessage.success(response.data.data)
              this.$router.push('/indexPage')
               
          } catch (error) {
              if (error.response && error.response.data && error.response.data.data) {
                  ElMessage.error(error.response.data.data)
              } else {
                  ElMessage.error('登录失败，请稍后重试')
              }
          }
      },
  }
}
</script>
<style>
/* :root {
  --primary-color: #2A9D8F;
  --text-color: #264653;
  --background-color: #e8f6f4;
  --border-color: #E2E8F0;
}

html,
body,
#app {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  background-color: var(--background-color);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

body {
  color: var(--text-color);
} */

.container {
  width: 100%;
  max-width: 1200px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  margin: 0 auto;
}

.login-container {
  display: flex;

  background: white;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  max-width: 1000px;
  width: 100%;
}

.left-section {
  flex: 1;
  height: 600px;
  position: relative;
  background-color: var(--primary-color);
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  overflow: hidden;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.background-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 0% 0%;
}

.text-overlay {
  position: relative;
  z-index: 1;
  padding: 10px;
  text-align: center;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0) 100%);
}

.text-overlay h2 {
  margin-bottom: 10px;
  font-size: 32px;
  color: #385761;
  font-weight: bold;
  opacity: 0.7;
  font-family: 'Arial';
}

.text-overlay p {
  margin-bottom: 10px;
  font-size: 26px;
  line-height: 1.5;

  color: #264653;
  font-family: 'Dancing Script', cursive;
}

.right-section {
  flex: 1;
  padding: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: rgb(248, 248, 245);
}

.illustration {
  max-width: 400px;
  margin-bottom: 32px;
}

.illustration img {
  width: 100%;
  height: auto;
}




.login-form {
  width: 100%;
  max-width: 400px;
}

.logo {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 62px;
}

.logo img {
  height: 100px;
  object-fit: contain;
}

form {
  width: 100%;
}

.input-wrapper {
  position: relative;
  width: 100%;
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

.forgot-password {
  display: block;
  text-align: right;
  color: var(--primary-color);
  text-decoration: none;
  font-size: 14px;
  margin-top: 8px;
}

.sign-in-btn {
  width: 100%;
  padding: 12px;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s;
}

.sign-in-btn:hover {
  background-color: #238276;
}

.signup-prompt {
  text-align: center;
  margin-top: 24px;
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

@media (max-width: 768px) {
  .login-container {
    flex-direction: column;
  }

  .left-section {
    padding: 20px;
  }

  .right-section {
    padding: 20px;
  }
}
</style>
