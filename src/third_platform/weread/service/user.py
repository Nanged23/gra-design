# 根据用户的vid 和 skey 获取用户相关信息
import requests


def request(vid, skey, url, type):
    headers = {
        "Host": "i.weread.qq.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
    }

    cookies = {
        "wr_skey": skey,
        "wr_vid": vid,
    }
    params = dict(userVid=vid)
    if type == 1:
        r = requests.get(url, headers=headers, cookies=cookies, verify=False)
    else:
        r = requests.get(url, params=params, headers=headers, cookies=cookies, verify=False)
    if r.ok:
        return r.json()
    else:
        return None


def get_user_bookshelf(vid, skey):
    """
    :param vid: 用户 id
    :param skey: 用户 token
    :return:用户的书架内容
    """
    url = "https://i.weread.qq.com/shelf/sync"
    response = request(vid, skey, url, 0)
    result = {
        "archive": [
            {
                "name": archive["name"],
                "bookIds": archive["bookIds"]
            } for archive in response["archive"]
        ],
        "books": [
            {
                "bookId": book["bookId"],
                "title": book["title"],
                "cover": book["cover"]
            } for book in response["books"]
        ]
    }
    return result


def get_user_info(vid, skey):
    """
    :param vid: 用户 id
    :param skey: 用户 token
    :return:用户的个人信息
    """
    url = "https://weread.qq.com/web/user?userVid={}".format(vid)
    response = request(vid, skey, url, 1)
    result = {
        "name": response["name"],
        "avatar": response["avatar"],
        "location": response["location"],
        "signature": response["signature"]
    }
    return result
