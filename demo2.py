import requests

url = "https://api.xygeng.cn/openapi/one"
response = requests.post(url)
print(response.text)
