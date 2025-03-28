<!-- TODO 背景加上动感元素 -->
<template>
  <div class="settings-container">
    <h1 class="settings-title" align="center">账户设置</h1>

    <!-- 安全设置 -->
    <div class="settings-section">
      <h2 class="section-title" align='center'>安全设置</h2>

      <!-- 修改密码 -->
      <div class="settings-item">
        <div class="settings-header">
          <h3>修改密码</h3>
          <p>更新您的账户密码</p>
        </div>
        <div class="settings-content">
          <div class="form-group" v-if="!showPasswordForm">
            <button class="btn-primary" @click="showPasswordForm = true">修改密码</button>
          </div>
          <div v-else class="form-fields">
            <div class="form-group">
              <label for="current-password">当前密码</label>
              <input type="password" id="current-password" v-model="passwordForm.currentPassword"
                placeholder="请输入当前密码" />
            </div>
            <div class="form-group">
              <label for="new-password">新密码</label>
              <input type="password" id="new-password" v-model="passwordForm.newPassword" placeholder="请输入新密码" />
            </div>
            <div class="form-group">
              <label for="confirm-password">确认新密码</label>
              <input type="password" id="confirm-password" v-model="passwordForm.confirmPassword"
                placeholder="请再次输入新密码" />
            </div>
            <div class="form-group verification-code">
              <label for="password-verification">邮箱验证码</label>
              <div class="verification-input">
                <input type="text" id="password-verification" v-model="passwordForm.verificationCode"
                  placeholder="请输入验证码" />
                <button class="btn-verification" @click="sendVerificationCode('password')"
                  :disabled="passwordCodeSending">
                  {{ passwordCodeSending ? `${passwordCountdown}秒后重试` : '获取验证码' }}
                </button>
              </div>
            </div>
            <div class="form-actions">
              <button class="btn-cancel" @click="cancelPasswordChange">取消</button>
              <button class="btn-primary" @click="updatePassword">保存</button>
            </div>
          </div>
        </div>
      </div>

      <!-- 修改邮箱 -->
      <div class="settings-item">
        <div class="settings-header">
          <h3>修改邮箱</h3>
          <p>当前邮箱: {{ userEmail }}</p>
        </div>
        <div class="settings-content">
          <div class="form-group" v-if="!showEmailForm">
            <button class="btn-primary" @click="showEmailForm = true">修改邮箱</button>
          </div>
          <div v-else class="form-fields">
            <div class="form-group">
              <label for="new-email">新邮箱地址</label>
              <input type="email" id="new-email" v-model="emailForm.newEmail" placeholder="请输入新邮箱地址" />
            </div>
            <div class="form-group verification-code">
              <label for="email-verification">邮箱验证码</label>
              <div class="verification-input">
                <input type="text" id="email-verification" v-model="emailForm.verificationCode" placeholder="请输入验证码" />
                <button class="btn-verification" @click="sendVerificationCode('email')" :disabled="emailCodeSending">
                  {{ emailCodeSending ? `${emailCountdown}秒后重试` : '获取验证码' }}
                </button>
              </div>
            </div>
            <div class="form-actions">
              <button class="btn-cancel" @click="cancelEmailChange">取消</button>
              <button class="btn-primary" @click="updateEmail">保存</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 个人资料 -->
    <div class="settings-section">
      <h2 class="section-title" align='center'>个人资料</h2>

      <!-- 修改用户名 -->
      <div class="settings-item">
        <div class="settings-header">
          <h3>用户名</h3>
          <p>当前用户名: {{ username }}</p>
        </div>
        <div class="settings-content">
          <div class="form-group" v-if="!showUsernameForm">
            <button class="btn-primary" @click="showUsernameForm = true">修改用户名</button>
          </div>
          <div v-else class="form-fields">
            <div class="form-group">
              <label for="new-username">新用户名</label>
              <input type="text" id="new-username" v-model="usernameForm.newUsername" placeholder="请输入新用户名" />
            </div>
            <div class="form-actions">
              <button class="btn-cancel" @click="cancelUsernameChange">取消</button>
              <button class="btn-primary" @click="updateUsername">保存</button>
            </div>
          </div>
        </div>
      </div>

      <!-- 修改个性签名 -->
      <div class="settings-item">
        <div class="settings-header">
          <h3>个性签名</h3>
          <p>{{ bio || '暂无个性签名' }}</p>
        </div>
        <div class="settings-content">
          <div class="form-group" v-if="!showBioForm">
            <button class="btn-primary" @click="showBioForm = true">{{ bio ? '修改' : '添加' }}个性签名</button>
          </div>
          <div v-else class="form-fields">
            <div class="form-group">
              <label for="new-bio">个性签名</label>
              <textarea id="new-bio" v-model="bioForm.newBio" placeholder="请输入个性签名" rows="3"></textarea>
            </div>
            <div class="form-actions">
              <button class="btn-cancel" @click="cancelBioChange">取消</button>
              <button class="btn-primary" @click="updateBio">保存</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 第三方平台绑定 -->
    <div class="settings-section">
      <h2 class="section-title" align="center">第三方平台绑定</h2>

      <!-- 微信绑定 -->
      <div class="settings-item">
        <div class="settings-header">
          <h3>微信绑定</h3>
          <p>{{ wechatConnected ? '已绑定' : '未绑定' }}</p>
        </div>
        <div class="settings-content">
          <div v-if="!showWechatForm">
            <div class="form-group" v-if="wechatConnected">
              <div class="connected-info">
                <span>微信ID: {{ wechatId }}<br>微信TOKEN: **********</span>
                <span></span>
                <button class="btn-primary" @click="showWechatForm = true">修改绑定</button>
              </div>
            </div>
            <div class="form-group" v-else>
              <button class="btn-primary" @click="showWechatForm = true">绑定微信</button>
            </div>
          </div>
          <div v-else class="form-fields">
            <div class="form-group">
              <label for="wechat-token">微信Token</label>
              <input type="text" id="wechat-token" v-model="wechatForm.token" placeholder="请输入微信Token" />
            </div>
            <div class="form-group">
              <label for="wechat-id">微信ID</label>
              <input type="text" id="wechat-id" v-model="wechatForm.id" placeholder="请输入微信ID" />
            </div>
            <div class="form-actions">
              <button class="btn-cancel" @click="cancelWechatChange">取消</button>
              <button class="btn-primary" @click="updateWechat">保存</button>
            </div>
          </div>
        </div>
      </div>

      <!-- 豆瓣绑定 -->
      <div class="settings-item">
        <div class="settings-header">
          <h3>豆瓣绑定</h3>
          <p>{{ doubanConnected ? '已绑定' : '未绑定' }}</p>
        </div>
        <div class="settings-content">
          <div v-if="!showDoubanForm">
            <div class="form-group" v-if="doubanConnected">
              <div class="connected-info">
                <span>豆瓣ID: {{ doubanId }}</span>
                <button class="btn-primary" @click="showDoubanForm = true">修改绑定</button>
              </div>
            </div>
            <div class="form-group" v-else>
              <button class="btn-primary" @click="showDoubanForm = true">绑定豆瓣</button>
            </div>
          </div>
          <div v-else class="form-fields">
            <div class="form-group">
              <label for="douban-id">豆瓣ID</label>
              <input type="text" id="douban-id" v-model="doubanForm.id" placeholder="请输入豆瓣ID" />
            </div>
            <div class="form-actions">
              <button class="btn-cancel" @click="cancelDoubanChange">取消</button>
              <button class="btn-primary" @click="updateDouban">保存</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';

// 用户数据
const username = ref('用户名示例');
const userEmail = ref('example@email.com');
const bio = ref('这是一段个性签名示例文字，展示用户的个人介绍和风格。');

// 第三方平台绑定状态
const wechatConnected = ref(true);
const wechatId = ref('wechat123456');
const wechatToken = ref('wxt_abcdef123456');
const doubanConnected = ref(false);
const doubanId = ref('');

// 表单显示状态
const showPasswordForm = ref(false);
const showEmailForm = ref(false);
const showUsernameForm = ref(false);
const showBioForm = ref(false);
const showWechatForm = ref(false);
const showDoubanForm = ref(false);

// 验证码发送状态
const passwordCodeSending = ref(false);
const emailCodeSending = ref(false);
const passwordCountdown = ref(60);
const emailCountdown = ref(60);

// 表单数据
const passwordForm = reactive({
  currentPassword: '',
  newPassword: '',
  confirmPassword: '',
  verificationCode: ''
});

const emailForm = reactive({
  newEmail: '',
  verificationCode: ''
});

const usernameForm = reactive({
  newUsername: ''
});

const bioForm = reactive({
  newBio: bio.value
});

const wechatForm = reactive({
  token: wechatToken.value,
  id: wechatId.value
});

const doubanForm = reactive({
  id: doubanId.value
});

// 发送验证码
const sendVerificationCode = (type) => {
  if (type === 'password') {
    // 验证表单完整性
    if (!passwordForm.currentPassword) {
      alert('请输入当前密码');
      return;
    }
    if (!passwordForm.newPassword) {
      alert('请输入新密码');
      return;
    }
    if (!passwordForm.confirmPassword) {
      alert('请确认新密码');
      return;
    }
    
    // 验证表单合法性
    if (passwordForm.newPassword !== passwordForm.confirmPassword) {
      alert('两次输入的密码不一致');
      return;
    }
    
    if (passwordForm.newPassword.length < 6) {
      alert('新密码长度不能少于6位');
      return;
    }
    
    passwordCodeSending.value = true;
    passwordCountdown.value = 60;
    
    const timer = setInterval(() => {
      passwordCountdown.value--;
      if (passwordCountdown.value <= 0) {
        clearInterval(timer);
        passwordCodeSending.value = false;
      }
    }, 1000);
    
    // 这里添加发送验证码的API调用
    console.log('发送密码修改验证码');
  } else if (type === 'email') {
    // 验证表单完整性
    if (!emailForm.newEmail) {
      alert('请输入新邮箱地址');
      return;
    }
    
    // 验证表单合法性 - 邮箱格式
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailForm.newEmail)) {
      alert('请输入有效的邮箱地址');
      return;
    }
    
    emailCodeSending.value = true;
    emailCountdown.value = 60;
    
    const timer = setInterval(() => {
      emailCountdown.value--;
      if (emailCountdown.value <= 0) {
        clearInterval(timer);
        emailCodeSending.value = false;
      }
    }, 1000);
    
    // 这里添加发送验证码的API调用
    console.log('发送邮箱修改验证码');
  }
};

// 修改密码
const updatePassword = () => {
  // 验证表单
  if (!passwordForm.currentPassword || !passwordForm.newPassword || !passwordForm.confirmPassword || !passwordForm.verificationCode) {
    alert('请填写完整信息');
    return;
  }

  if (passwordForm.newPassword !== passwordForm.confirmPassword) {
    alert('两次输入的密码不一致');
    return;
  }

  // 这里添加修改密码的API调用
  console.log('修改密码', passwordForm);

  // 重置表单
  passwordForm.currentPassword = '';
  passwordForm.newPassword = '';
  passwordForm.confirmPassword = '';
  passwordForm.verificationCode = '';
  showPasswordForm.value = false;
};

// 取消修改密码
const cancelPasswordChange = () => {
  passwordForm.currentPassword = '';
  passwordForm.newPassword = '';
  passwordForm.confirmPassword = '';
  passwordForm.verificationCode = '';
  showPasswordForm.value = false;
};

// 修改邮箱
const updateEmail = () => {
  // 验证表单
  if (!emailForm.newEmail || !emailForm.verificationCode) {
    alert('请填写完整信息');
    return;
  }

  // 这里添加修改邮箱的API调用
  console.log('修改邮箱', emailForm);

  // 更新邮箱
  userEmail.value = emailForm.newEmail;

  // 重置表单
  emailForm.newEmail = '';
  emailForm.verificationCode = '';
  showEmailForm.value = false;
};

// 取消修改邮箱
const cancelEmailChange = () => {
  emailForm.newEmail = '';
  emailForm.verificationCode = '';
  showEmailForm.value = false;
};

// 修改用户名
const updateUsername = () => {
  // 验证表单
  if (!usernameForm.newUsername) {
    alert('请填写新用户名');
    return;
  }

  // 这里添加修改用户名的API调用
  console.log('修改用户名', usernameForm);

  // 更新用户名
  username.value = usernameForm.newUsername;

  // 重置表单
  usernameForm.newUsername = '';
  showUsernameForm.value = false;
};

// 取消修改用户名
const cancelUsernameChange = () => {
  usernameForm.newUsername = '';
  showUsernameForm.value = false;
};

// 修改个性签名
const updateBio = () => {
  // 这里添加修改个性签名的API调用
  console.log('修改个性签名', bioForm);

  // 更新个性签名
  bio.value = bioForm.newBio;

  // 重置表单
  showBioForm.value = false;
};

// 取消修改个性签名
const cancelBioChange = () => {
  bioForm.newBio = bio.value;
  showBioForm.value = false;
};

// 修改微信绑定
const updateWechat = () => {
  // 验证表单
  if (!wechatForm.token || !wechatForm.id) {
    alert('请填写完整信息');
    return;
  }

  // 这里添加修改微信绑定的API调用
  console.log('修改微信绑定', wechatForm);

  // 更新微信绑定
  wechatConnected.value = true;
  wechatToken.value = wechatForm.token;
  wechatId.value = wechatForm.id;

  // 重置表单
  showWechatForm.value = false;
};

// 取消修改微信绑定
const cancelWechatChange = () => {
  wechatForm.token = wechatToken.value;
  wechatForm.id = wechatId.value;
  showWechatForm.value = false;
};

// 修改豆瓣绑定
const updateDouban = () => {
  // 验证表单
  if (!doubanForm.id) {
    alert('请填写豆瓣ID');
    return;
  }

  // 这里添加修改豆瓣绑定的API调用
  console.log('修改豆瓣绑定', doubanForm);

  // 更新豆瓣绑定
  doubanConnected.value = true;
  doubanId.value = doubanForm.id;

  // 重置表单
  showDoubanForm.value = false;
};

// 取消修改豆瓣绑定
const cancelDoubanChange = () => {
  doubanForm.id = doubanId.value;
  showDoubanForm.value = false;
};
</script>

<style scoped>
.settings-container {
  margin-left: 330px;
  max-width: 1000px;
  padding: 20px;
  background: white;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.settings-title {
  font-size: 26px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #1e1d1d;
}

.settings-section {
  margin-bottom: 32px;
  border: 1px solid #eaeaea;
  border-radius: 8px;
  overflow: hidden;
}

.section-title {
  font-size: 18px;
  font-weight: 500;
  padding: 16px;
  background-color: #f9f9f9;
  border-bottom: 1px solid #eaeaea;
  margin: 0;
}

.settings-item {
  padding: 16px;
  border-bottom: 1px solid #eaeaea;
}

.settings-item:last-child {
  border-bottom: none;
}

.settings-header {
  margin-bottom: 16px;
}

.settings-header h3 {
  font-size: 16px;
  font-weight: 500;
  margin: 0 0 4px 0;
  color: #333;
}

.settings-header p {
  font-size: 14px;
  color: #666;
  margin: 0;
}

.form-group {
  margin-bottom: 16px;
}

.form-fields {
  background-color: #f9f9f9;
  padding: 16px;
  border-radius: 6px;
}

label {
  display: block;
  font-size: 14px;
  font-weight: 500;
  margin-bottom: 6px;
  color: #333;
}

input,
textarea {
  width: 96%;
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  color: #333;
  background-color: #fff;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #4a90e2;
}

textarea {
  resize: vertical;
  min-height: 80px;
}

.verification-code {
  margin-bottom: 16px;
}

.verification-input {
  display: flex;
  gap: 8px;
}

.verification-input input {
  flex: 1;
}

.btn-verification {
  white-space: nowrap;
  padding: 0 12px;
  height: 40px;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  color: #333;
  cursor: pointer;
}

.btn-verification:disabled {
  background-color: #f5f5f5;
  color: #999;
  cursor: not-allowed;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

.btn-primary {
  padding: 8px 16px;
  background-color: #4a90e2;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #3a80d2;
}

.btn-cancel {
  padding: 8px 16px;
  background-color: #f5f5f5;
  color: #333;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
}

.btn-cancel:hover {
  background-color: #e5e5e5;
}

.connected-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.connected-info span {
  font-size: 14px;
  color: #666;
}
</style>