# 通过更换 get_dashboard_workouts 函数中的 url 为 response.json5中的 url，来获得 Keep 不同的数据
import requests
import base64
import json
from urllib.parse import urlencode


# 模拟登录，获得专属 token
def login(mobile, password):
    url = "https://api.gotokeep.com/v1.1/users/login"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    data = {"mobile": mobile, "password": password}
    data = urlencode(data)
    response = requests.post(url, data=data, headers=headers)
    print(response.json())
    return response.json()


# 使用字典代替存储
storage = {}


# 设置数据到 storage 中
def set_storage(key, value):
    storage[key] = value


# 获取存储的数据
def get_storage(key):
    return storage.get(key, None)


# 解码 Base64
def base64_decode(base64_string):
    padding = '=' * (4 - len(base64_string) % 4)  # 补充缺少的 padding
    return base64.b64decode(base64_string + padding).decode('utf-8')


# 模拟获取 token
def get_token():
    authentication = get_storage('authentication') or {}
    return 'Bearer ' + authentication.get('token', '')


# 发起 HTTP GET 请求
def http_get(url, options=None):
    if options is None:
        options = {}
    headers = {
        'Authorization': get_token(),
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    options['headers'] = headers

    try:
        response = requests.get(url, headers=headers)
        response.encoding = "UTF-8"
        return response.json()  # 返回 json 格式的响应内容
    except Exception as e:
        print(f"HTTP GET 请求失败: {e}")
        return None


# 模拟处理认证
def handle_authentication(response):
    if response.get('ok', False):
        set_storage('authentication', response['data'])
        # 解码 token
        token_data = response['data']['token'].split('.')[1]
        decoded_data = base64_decode(token_data)
        set_storage('userData', decoded_data)


# 获取 Dashboard Workouts
def get_dashboard_workouts():
    url = 'https://api.gotokeep.com/v2/home/dashboard/pwData'
    response_data = http_get(url)
    return response_data


if __name__ == '__main__':
    # 示例：模拟 response 内容
    response = login('15909339497', 'TianCai54')
    # 处理认证
    handle_authentication(response)

    # 获取 Dashboard Workouts 数据
    workouts = get_dashboard_workouts()
    print(json.dumps(workouts, indent=2, ensure_ascii=False))
