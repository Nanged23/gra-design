<template>
  <div class="container">
    <el-card class="cardBox">
      <div class="form" :class="!isRegister ? 'left' : 'right'">
        <img src="../assets/login/logo.png" class="loginLogo" alt="" />
        <el-form
          v-if="refresh"
          class="formPosition"
          ref="ruleFormRef"
          :model="ruleForm"
          status-icon
          :rules="rules"
        >
          <el-form-item prop="email">
            <vs-input v-model="ruleForm.email" placeholder="邮箱">
              <template #icon>
                <el-icon><Message /></el-icon>
              </template>
            </vs-input>
          </el-form-item>
          <el-form-item
            prop="verificationCode"
            class="formItem"
            v-if="isRegister"
          >
            <vs-input
              v-model="ruleForm.verificationCode"
              placeholder="验证码"
              class="verificationCode"
              style="width: 100px"
            >
              <template #icon>
                <img src="@/assets/login/验证码.png" class="icon" alt="" />
              </template>
            </vs-input>
            <el-button
              :type="isSend ? 'info' : 'success'"
              round
              @click="send"
              class="verificationCodeBtn"
              >{{
                isSend ? (cd !== 0 ? cd + "s" : "重新发送") : "发送验证码"
              }}</el-button
            >
          </el-form-item>
          <el-form-item prop="password">
            <vs-input
              type="password"
              v-model="ruleForm.password"
              placeholder="密码"
              :visiblePassword="hasVisiblePassword"
              @click-icon="hasVisiblePassword = !hasVisiblePassword"
            >
              <template #icon>
                <el-icon><Lock /></el-icon>
              </template>

              <template v-if="getProgress >= 100" #message-success>
                Secure password
              </template>
            </vs-input>
          </el-form-item>
          <el-form-item>
            <el-button class="btn" type="primary" @click="submitForm">
              {{ !isRegister ? "登录" : "注册" }}
            </el-button>
          </el-form-item>
        </el-form>
        <div class="info">
          <span> {{ !isRegister ? "没有账户？" : "已有账户？" }}</span>
          <el-link type="primary" @click="handle">{{
            !isRegister ? "立即注册!" : "立即登录!"
          }}</el-link>
        </div>
      </div>
      <div
        :class="isRegister ? 'left leftBack' : 'right rightBack'"
        class="img"
      >
        <img
          v-if="!isRegister"
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
import { ref, reactive } from "vue";
import { ElMessage } from "element-plus";
import { login } from "@/request/login";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";
import { ElLoading } from 'element-plus'
const { onLogin } = useUserStore();
const router = useRouter();
const ruleForm = ref({
  password: "",
  email: "",
  verificationCode: "",
});
const validateEmail = (rule, value, callback) => {
  const emailRegex = /^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!emailRegex.test(value)) {
    callback(new Error("请输入正确的邮箱"));
  } else {
    callback();
  }
};
const refresh = ref(true);
const rules = reactive({
  email: [{ validator: validateEmail, trigger: "blur" }],
  password: [
    {
      required: true,
      message: "请填写密码",
      trigger: "blur",
    },
  ],
});
const isRegister = ref(false);
const isSend = ref(false);
const cd = ref(60);
const timer = null;
const ruleFormRef = ref(null);
const desCd = () => {
  timer = setInterval(() => {
    cd.value = cd.value - 1;
    if (cd.value === 0) {
      clearInterval(timer);
    }
  }, 1000);
};
const reset = () => {
  isSend.valid = false;
  cd.value = 0;
  timer = null;
};
const handle = () => {
  isRegister.value = !isRegister.value;
  refresh.value = false;
  setTimeout(() => {
    refresh.value = true;
  });
};
const send = () => {
  if (isSend.value && cd.value) {
    return;
  }
  isSend.value = true;
  desCd();
};
const handleLogin = () => {
  const loading = ElLoading.service({
    lock: true,
    text: "Loading",
    background: "rgba(0, 0, 0, 0.7)",
  });
  login({
    email: ruleForm.value.email,
    password: ruleForm.value.password,
  })
    .then((data) => {
      ElMessage.success("登录成功");
      onLogin();
      router.push("/main");
    })
    .catch(() => {
      ElMessage.error("登录失败");
    })
    .finally(() => {
      loading.close();
    });
};
const submitForm = () => {
  console.log(ruleFormRef.value);
  ruleFormRef.value.validate((valid) => {
    if (valid) {
      if (isRegister.value) {
        handleRegister();
      } else {
        handleLogin();
      }
    }
  });
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
        .formItem {
          height: 100%;
          width: 100%;

          ::v-deep(.el-form-item__content) {
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
          }
          ::v--deep(.vs-input__original) {
            width: 100px;
          }

          .verificationCodeBtn {
            width: 90px;
            height: 42px;
            margin-left: 10px;
            background-color: #2e9d8f;
          }
        }
        .icon {
          width: 22px;
          height: 22px;
        }
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
