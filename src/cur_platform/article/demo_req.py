import requests

url = 'http://localhost:5000/article/update'  # 替换成你的 Flask 应用 URL
files = {'cover': ('image.jpg', open('/Users/dongliwei/Desktop/new.png', 'rb'), 'image/jpeg')}
data = {
    "title": "demo 文章 tit11le",
    'article_id': 6,
    "word_diff": 100,
}
# 默认都是 SCR 需要更新为新的new
response = requests.post(url, data=data, files=files)
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)
