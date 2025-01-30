import instance from ".";
/**
 * 登录
 * @param {*} params
 * @returns
 */
export function login(params) {
  return instance.post("/user/login", params);
}

/**
 * 注册
 * @param {*} params
 * @returns
 */
export function register(params) {
  return instance.post("/user/register", params);
}

/**
 * 发送验证码
 * @param {*} params
 * @returns
 */
export function sendCheckCode(params) {
  return instance.post("/user/get_code", params);
}
