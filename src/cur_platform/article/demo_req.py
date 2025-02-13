import requests

url = 'https://gra-design.onrender.com/article/update'  # 替换成你的 Flask 应用 URL
files = {'cover': ('image.jpg', open('/Users/dongliwei/Downloads/demo.png', 'rb'), 'image/jpeg')}
data = {
    "title": "测试111文111章1",
    'article_id': 6,
    "word_diff": -100,
}
response = requests.post(url, data=data, files=files)
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)


