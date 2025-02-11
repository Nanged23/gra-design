# # 勋章文本版，不带图案
# import requests
#
# # 请求的URL和参数
# url = "http://i.weread.qq.com/medal/list"
# params = {
#     'count': 0,
#     'auto': 1,
#     'userVid': 442726869
# }
#
# # 请求头
# headers = {
#     'accessToken': '5QIA0svF',
#     'vid': '442726869',
#     'baseapi': '31',
#     'appver': '9.0.0.10165035',
#     'User-Agent': 'WeRead/9.0.0 WRBrand/honor Dalvik/2.1.0 (Linux; U; Android 12; ALA-AN70 Build/HONORALA-AN70)',
#     'osver': '12',
#     'channelId': '0',
#     'basever': '9.0.0.10165034',
#     'Host': 'i.weread.qq.com',
#     'Connection': 'Keep-Alive',
#     'Accept-Encoding': 'gzip'
# }
#
# # 发送GET请求
# response = requests.get(url, headers=headers, params=params)
#
# # 打印响应内容
# print(response.status_code)  # 打印HTTP状态码
# print(response.text)         # 打印响应体

#
# # 阅读情况 monthly   annually weekly overall
# import requests
#
# url = "https://i.weread.qq.com/readdata/detail?mode=overall&defaultPreferBook=0&baseTime=0"
# # 请求的URL和参数
# # url = "http://i.weread.qq.com/medal/list"
# params = {
#     'count': 0,
#     'auto': 1,
#     'userVid': 442726869
# }
#
# # 请求头
# headers = {
#     'accessToken': 'hDEwbnYb',
#     'vid': '442726869',
#     'baseapi': '31',
#     'appver': '9.0.0.10165035',
#     'User-Agent': 'WeRead/9.0.0 WRBrand/honor Dalvik/2.1.0 (Linux; U; Android 12; ALA-AN70 Build/HONORALA-AN70)',
#     'osver': '12',
#     'channelId': '0',
#     'basever': '9.0.0.10165034',
#     'Host': 'i.weread.qq.com',
#     'Connection': 'Keep-Alive',
#     'Accept-Encoding': 'gzip'
# }
#
# # 发送GET请求
# response = requests.get(url, headers=headers, params=params)
#
# # 打印响应内容
# print(response.status_code)  # 打印HTTP状态码
# print(response.text)  # 打印响应体