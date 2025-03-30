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
import { ref, reactive, onMounted } from 'vue';
import { getUserDetail, updateUser, sendCode } from '@/js/index/indexPage.js';
import Cookies from 'js-cookie';
import { ElMessage } from 'element-plus';
const username = ref('');
const userEmail = ref('');
const bio = ref('');
const wechatConnected = ref(false);
const wechatId = ref('');
const wechatToken = ref('');
const doubanConnected = ref(false);
const doubanId = ref('');

// 获取用户设置数据
const fetchUserSettings = async () => {

  let params = { "user_id": Cookies.get("user_id") }
  const response = await getUserDetail(params);


  const result = await response;

  if (result.data[0] && result.data[0].email) {
    userEmail.value = result.data[0].email;
  }
  if (result.data[1]) {
    const userData = result.data[1];

    // 设置用户名
    if (userData.user_name) {
      username.value = userData.user_name;
    }

    // 设置个性签名
    if (userData.signature) {
      bio.value = userData.signature;
    }

    // 设置微信绑定信息
    if (userData.wechat_id) {
      wechatConnected.value = true;
      wechatId.value = userData.wechat_id;
    }

    if (userData.wechat_token) {
      wechatToken.value = userData.wechat_token;
    }

    // 设置豆瓣绑定信息
    if (userData.douban_id) {
      doubanConnected.value = true;
      doubanId.value = userData.douban_id;
    }
  }

  // 初始化表单数据
  bioForm.newBio = bio.value;
  wechatForm.id = wechatId.value;
  wechatForm.token = wechatToken.value;
  doubanForm.id = doubanId.value;

};

// 在组件挂载时获取数据
onMounted(() => {
  fetchUserSettings();
});

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
const sendVerificationCode = async (type) => {
  if (type === 'password') {
    // 验证表单完整性
    if (!passwordForm.currentPassword) {
      ElMessage({
        message: "请输入当前密码",
        type: 'error',
      });
      return;
    }
    if (!passwordForm.newPassword) {
      ElMessage({
        message: "请输入新密码",
        type: 'error',
      });
      return;
    }
    if (!passwordForm.confirmPassword) {
      ElMessage({
        message: "请确认新密码",
        type: 'error',
      });
      return;
    }

    // 验证表单合法性
    if (passwordForm.newPassword !== passwordForm.confirmPassword) {
      ElMessage({
        message: "两次输入的密码不一致",
        type: 'error',
      });
      return;
    }

    if (passwordForm.newPassword.length < 6) {
      ElMessage({
        message: "新密码长度不能少于6位!",
        type: 'error',
      });
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

    let res = await sendCode({ "email": userEmail.value })
    if (res.statusCode == 200) {
      ElMessage({
        message: "验证码发送成功～",
        type: 'success',
      });
    }

  } else if (type === 'email') {
    // 验证表单完整性
    if (!emailForm.newEmail) {
      ElMessage({
        message: "请输入新邮箱地址",
        type: 'error',
      });

      return;
    }

    // 验证表单合法性 - 邮箱格式
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailForm.newEmail)) {
      ElMessage({
        message: "请输入有效的邮箱地址",
        type: 'error',
      });
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

    let res = await sendCode({ "email": emailForm.newEmail })
    if (res.statusCode == 200) {
      ElMessage({
        message: "验证码发送成功～",
        type: 'success',
      });
    }
  }
};

// 修改密码
const updatePassword = async () => {
  // 验证表单
  if (!passwordForm.currentPassword || !passwordForm.newPassword || !passwordForm.confirmPassword || !passwordForm.verificationCode) {
    ElMessage({
      message: "请填写完整信息",
      type: 'error',
    });
    return;
  }

  if (passwordForm.newPassword !== passwordForm.confirmPassword) {
    ElMessage({
      message: "两次输入的密码不一致",
      type: 'error',
    });
    return;
  }

  try {
    const params = {
      user_id: Cookies.get("user_id"),
      user: {
        password: passwordForm.newPassword,
        code: passwordForm.verificationCode,
        email: userEmail.value
      }
    };

    const response = await updateUser(params);
    if (response && response.msg === 'success') {
      ElMessage({
        message: "密码修改成功",
        type: 'success',
      });

    } else {
      ElMessage({
        message: "密码修改失败",
        type: 'error',
      });
    }
  } catch (error) {
    ElMessage({
      message: "密码修改失败",
      type: 'error',
    });
  }

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
const updateEmail = async () => {
  // 验证表单
  if (!emailForm.newEmail || !emailForm.verificationCode) {
    ElMessage({
      message: "请填写完整信息",
      type: 'info',
    });
    return;
  }

  try {
    const params = {
      user_id: Cookies.get("user_id"),
      user: {
        email: emailForm.newEmail,
        code: emailForm.verificationCode
      }
    };

    const response = await updateUser(params);
    if (response && response.msg === 'success') {
      // 更新邮箱
      userEmail.value = emailForm.newEmail;
      ElMessage({
        message: "邮箱修改成功",
        type: 'success',
      });
    } else {
      ElMessage({
        message: "邮箱修改失败",
        type: 'error',
      });
    }
  } catch (error) {
    ElMessage({
      message: "邮箱修改失败",
      type: 'error',
    });
  }

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
const updateUsername = async () => {
  // 验证表单
  if (!usernameForm.newUsername) {
    ElMessage({
      message: "请填写新用户名",
      type: 'error',
    });
    return;
  }
  const params = {
    user_id: Cookies.get("user_id"),
    detail: {
      user_name: usernameForm.newUsername
    }
  };

  try {
    const response = await updateUser(params);
    if (response && response.msg === 'success') {
      // 更新用户名
      username.value = usernameForm.newUsername;
      ElMessage({
        message: "用户名修改成功",
        type: 'success',
      });
    } else {
      ElMessage({
        message: "用户名修改失败",
        type: 'error',
      });
    }
  } catch (error) {
    ElMessage({
      message: "用户名修改失败",
      type: 'error',
    });
  }

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
const updateBio = async () => {
  try {
    const params = {
      user_id: Cookies.get("user_id"),
      detail: {
        signature: bioForm.newBio
      }
    };

    const response = await updateUser(params);
    if (response && response.msg === 'success') {
      // 更新个性签名
      bio.value = bioForm.newBio;
      ElMessage({
        message: "个性签名修改成功",
        type: 'success',
      });
    } else {
      ElMessage({
        message: "个性签名修改失败",
        type: 'error',
      });
    }
  } catch (error) {
    ElMessage({
      message: "个性签名修改失败",
      type: 'error',
    });
  }

  // 重置表单
  showBioForm.value = false;
};

// 取消修改个性签名
const cancelBioChange = () => {
  bioForm.newBio = bio.value;
  showBioForm.value = false;
};

// 修改微信绑定
const updateWechat = async () => {
  // 验证表单
  if (!wechatForm.token || !wechatForm.id) {
    ElMessage({
      message: "请填写完整信息",
      type: 'error',
    });
    return;
  }

  try {
    const params = {
      user_id: Cookies.get("user_id"),
      detail: {
        wechat_id: wechatForm.id,
        wechat_token: wechatForm.token
      }
    };

    const response = await updateUser(params);
    if (response && response.msg === 'success') {
      // 更新微信绑定
      wechatConnected.value = true;
      wechatToken.value = wechatForm.token;
      wechatId.value = wechatForm.id;
      ElMessage({
        message: "微信绑定修改成功",
        type: 'success',
      });
    } else {
      ElMessage({
        message: "微信绑定修改失败",
        type: 'error',
      });
    }
  } catch (error) {
    ElMessage({
      message: "微信绑定修改失败",
      type: 'error',
    });
  }

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
const updateDouban = async () => {
  // 验证表单
  if (!doubanForm.id) {
    ElMessage({
      message: "请填写豆瓣ID",
      type: 'error',
    });
    return;
  }

  try {
    const params = {
      user_id: Cookies.get("user_id"),
      detail: {
        douban_id: doubanForm.id
      }
    };

    const response = await updateUser(params);
    if (response && response.msg === 'success') {
      // 更新豆瓣绑定
      doubanConnected.value = true;
      doubanId.value = doubanForm.id;
      ElMessage({
        message: "豆瓣绑定修改成功",
        type: 'success',
      });
    } else {
      ElMessage({
        message: "豆瓣绑定修改失败",
        type: 'error',
      });
    }
  } catch (error) {
    ElMessage({
      message: "豆瓣绑定修改失败",
      type: 'error',
    });
  }

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