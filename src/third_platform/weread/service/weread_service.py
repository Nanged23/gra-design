# 根据用户的vid 和 skey 获取用户相关信息
import requests
import json
from flask import jsonify

browser_instance = None

overall_template = {
    "readTimes": {},
    "readLongest": [
        {
            "book": {
                "bookId": "",
                "title": "",
                "author": "",
                "cover": ""
            },
            "readTime": 0
        }

    ],
    "preferCategory": [
        {
            "categoryTitle": "",
            "val": 0,
        }
    ],
    "preferCategoryWord": "",
    "preferTime": [],
    "preferTimeWord": "",
    "preferAuthor": [
        {
            "name": "",
            "count": 0
        }
    ],
    "registTime": 0,
    "totalReadTime": 0,
    "shareInfo": {
        "totalReadingDay": 0,
        "hadReadingCount": 0,
        "finishReadingCount": 0,
        "notesCount": 0,
    },
    "preferBooks": [
        {
            "title": "",
            "bookInfo": {
                "bookId": "",
                "title": "",
                "cover": ""
            },
            "reason": ""
        }
    ]
}


def extract_json(template, json_data):
    """
    从 another_json 中提取出 simple_json 格式的内容。

    Args:
        template:  一个字典，定义了需要提取的 JSON 结构。
        json_data: 一个字典，包含了 simple_json 的所有键值，以及其他可能无用的键值。

    Returns:
        一个字典，final_json，包含了从 another_json 中提取出的，
        与 simple_json 结构相同的键值对。
        如果 another_json 中没有 simple_json 中对应的键，则对应的值为 None。
    """

    final_json = {}

    def traverse_and_extract(simple_sub_json, another_sub_json, final_sub_json):
        """
        递归遍历 simple_json，并在 another_json 中查找对应的值。
        """
        for key, value in simple_sub_json.items():
            if isinstance(value, dict):  # 如果值是字典，则递归处理
                final_sub_json[key] = {}
                if key in another_sub_json and isinstance(another_sub_json[key], dict):
                    traverse_and_extract(value, another_sub_json[key], final_sub_json[key])
                # else:  如果another_sub_json 没有这个key，或者key对应的不是字典，则final_sub_json[key]保持{}(空字典)
            elif isinstance(value, list):  # 如果值是列表
                final_sub_json[key] = []
                if key in another_sub_json and isinstance(another_sub_json[key], list):
                    # 处理列表，列表中的元素可能是字典，也可能是基本类型
                    for i, simple_item in enumerate(value):
                        if i < len(another_sub_json[key]):  # 防止another_json中的列表比simple_json短
                            another_item = another_sub_json[key][i]
                            if isinstance(simple_item, dict):
                                # 如果simple_json列表中是字典，则another_json列表也应该是字典，才可以extract
                                if isinstance(another_item, dict):
                                    new_item = {}
                                    traverse_and_extract(simple_item, another_item, new_item)
                                    final_sub_json[key].append(new_item)
                                else:
                                    final_sub_json[key].append(None)  # 类型不匹配
                            else:
                                # 如果 simple_json 列表中元素是基本类型，直接复制
                                final_sub_json[key].append(another_item)
                        else:  # another_json中的列表比simple_json短，则后续的都设置为None
                            final_sub_json[key].append(None)
                # else: 如果 another_json 中没有这个 key，或者对应的不是列表，则 final_sub_json[key] 保持 [](空列表)
            else:  # 如果值不是字典也不是列表（例如，是基本类型如 int, string, bool）
                if key in another_sub_json:
                    final_sub_json[key] = another_sub_json[key]
                else:
                    final_sub_json[key] = None  # 如果需要，可以省略这个键

    traverse_and_extract(template, json_data, final_json)
    if "readLongest" in final_json and isinstance(final_json["readLongest"], list):
        final_json["readLongest"] = final_json["readLongest"][:3]

        # 特殊处理 preferTime
    if "preferTime" in final_json and isinstance(final_json["preferTime"], list):
        final_json["preferTime"] = final_json["preferTime"][-6:] + final_json["preferTime"][:-6]

    return final_json


def android_request(vid, skey, url):
    params = {
        'count': 0,
        'auto': 1,
        'userVid': vid
    }

    # 请求头
    headers = {
        'accessToken': skey,
        'vid': vid,
        'baseapi': '31',
        'appver': '9.3.0.10165973',
        'User-Agent': 'WeRead/9.3.0 WRBrand/honor Dalvik/2.1.0 (Linux; U; Android 12; ALA-AN70 Build/HONORALA-AN70)',
        'osver': '12',
        'channelId': '22',
        'basever': '9.3.0.10165973',
        'Host': 'i.weread.qq.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    print(response.json())
    return response.json()


def mac_request(vid, skey, url, type):
    # 封装的基础请求函数
    headers = {
        "Host": "weread.qq.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
    }

    cookies = {
  "_clck": "1sq5wgf|1|ftj|0",
  "_qimei_fingerprint": "65257215be7487d9169c58539e064a0e",
  "_qimei_h38": "ca20fefa61d54e05599ff65d0300000a718501",
  "_qimei_q36": "",
  "eas_sid": "31v7T1b6c9Z0l3o6T2A151N5g3",
  "fopenid": "64E4CAA57F58D7B2C96E7890DFA220F1",
  "fqm_pvqid": "86d90983-be5d-43c0-b331-be75aa6ce116",
  "ied_qq": "o2074759416",
  "it_c": "0",
  "o_cookie": "2074759416",
  "p_skey": "Rao7lTH-37DdtaHshbms6TSu2k9m93uEPCDCBdOBt-8_",
  "p_uin": "o2074759416",
  "pac_uid": "0_fjjsDpZmfK67t",
  "pgv_info": "ssid=s2531873086",
  "pgv_pvid": "32612000",
  "pt4_token": "awiEk4pKB5LA-Ec*DRV-uG4ui3stHF*heV-ut90917A_",
  "ptcz": "473705f82ffde7baeef31279e09cf14f049a380e56e8d7316e707b714763636b",
  "qbmac_uid": "aaaaoervw3l45fb6571isp6py1uy88cb",
  "qm_device_id": "g0++FFDMHylM8rkpyx0fw5k3U3AHMvq+CdpIZUbNgKPSODcz/Ly6FWyVFDgmJGUY",
  "qm_logintype": "qq",
  "qq_domain_video_guid_verify": "0b1e78e8f1e30859",
  "RK": "MiPwOzJ+ef",
  "sid": "2074759416&30e7b44b30934c3490e0d9f8bbf559d7,qWVdOYVVBQS1xU2w3UDBhVm9XQ1VSN0NPOE5NN1Z2cUdOWUwzOUtlLTZlNF8.",
  "skey": "@9I0SaroSd",
  "suid": "user_0_fjjsDpZmfK67t",
  "token": "6CF357A5E792EB7856AEA0D495E6319A",
  "uin": "o2074759416",
  "wr_avatar": "https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2F5Cd5DiaVksY2AJU7OSfgVddHzfEvEkDt73IRlf5wtXAX8P0ArBVyyM1fwiaMVdPx5PjnCEORshpf0nGm6ic8bicyY4iaETDiaNOvI1mJy3tvl1aMU%2F132",
  "wr_fp": "3300175283",
  "wr_gender": "1",
  "wr_gid": "290404310",
  "wr_localvid": "a44325a081a6379d5a44b11",
  "wr_name": "%E5%90%83%E5%8F%A3%E5%A4%A7%E6%B1%A4%E5%9C%86",
  "wr_pf": "undefined",
  "wr_rt": "web%40tmNT1q_K_Z6Thpz1baG_AL",
  "wr_skey": "6K00x_6b",
  "wr_vid": "442726869",
  "xm_data_ticket": "13102663099633912&CAESIGgTSSAALozNe6pQ-HsxJPzZOytFiEGVvPZmqUTz5lMT",
  "xm_device_id": "cc5a4691",
  "xm_envid": "456_kWRWAR6bFCxG2viDCpplaSU+WtZb2+Q2fn0uu8yFH6nz5RKGPiP0HFKh1yP43O9cd0xfh+uyoVLitBDdXex7xgDDGuZbp5xxD0bCjqngBAeQdnsRJT7FhYcSPu7ZndC6FK1cleOYFs+LWEyETAqnw677jj0Dvf5NND1CtgpU47Gbm5+ksQ2sAi8u2hrgy9Y=",
  "xm_muti_sid": "13102663099633912&zfhoeoxQSnUuqkJFAHsyMAAA",
  "xm_pcache": "13102663099633912&V2@ztDOe5w5RNq0EwPYQqQ4OwAA@0",
  "xm_sid": "zfhoeoxQSnUuqkJFAHsyMAAA",
  "xm_skey": "13102663099633912&488d9e486c4f10ae9d268bcc7a47f23f",
  "xm_uin": "13102663099633912",
  "xm_ws": "13102663099633912&a93bb7ffe4720475a85a0b5a34f9ac2c"
}

    params = dict(userVid=vid)
    if type == 1:
        r = requests.get(url, headers=headers, cookies=cookies, verify=False)
    else:
        r = requests.get(url, params=params, headers=headers, cookies=cookies, verify=False)
    if r.ok:
        return r.text
    else:
        print("在获取书架信息时:", r.text)
        return None


def get_user_bookshelf(vid, skey):
    """
    :param vid: 用户 id
    :param skey: 用户 token
    :return:用户的书架内容
    """
    url = "https://i.weread.qq.com/shelf/sync"
    response = mac_request(vid, skey, url, 0)
    # response = android_request(vid, skey, url)
    print(response)
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

    info2 = result

    bookshelf_info = {
        "folders": [],
        "books": []
    }

    folder_book_ids = set()  # 创建一个集合来存储已经添加到文件夹的 bookId

    # 处理 folders 字段
    for archive_item in info2["archive"]:
        folder = {
            "name": archive_item["name"],
            "books": []
        }
        for book_id in archive_item["bookIds"]:
            for book in info2["books"]:
                if book["bookId"] == book_id:
                    folder["books"].append(book)
                    folder_book_ids.add(book_id)  # 将 bookId 添加到集合中
                    break
        bookshelf_info["folders"].append(folder)

    # 处理顶层的 books 字段，只添加不在文件夹中的图书
    for book in info2["books"]:
        if book["bookId"] not in folder_book_ids:  # 检查 bookId 是否在集合中
            bookshelf_info["books"].append(book)

    # 将结果转换为 JSON 字符串并打印 (ensure_ascii=False 保证中文不被转义)
    result_json = json.dumps(bookshelf_info, indent=2, ensure_ascii=False)

    return json.loads(result_json)


def get_user_info(vid, skey):
    """
    :param vid: 用户 id
    :param skey: 用户 token
    :return:用户的个人信息
    """
    url = "https://weread.qq.com/web/user?userVid={}".format(vid)
    response = mac_request(vid, skey, url, 1)
    result = {
        "name": response["name"],
        "avatar": response["avatar"],
        "location": response["location"],
        "signature": response["signature"]
    }
    return result


def get_summary(vid, skey, type):
    # 阅读情况 weekly monthly annually  overall
    if type not in ["monthly", "annually", "weekly", "overall"]:
        return jsonify({"msg": "type 参数错误"}), 400
    elif type == "overall":
        template = overall_template
    elif type == "annually":
        annually_template = {
            key: value
            for key, value in overall_template.items()
            if key not in ['readTimes', 'preferTime', 'preferTimeWord', 'preferAuthor', 'registTime', 'preferBooks']
        }
        annually_template["dailyReadTimes"] = {}
        annually_template["compare"] = 0
        annually_template["dayAverageReadTime"] = 0
        template = annually_template
    elif type == "monthly":
        monthly_template = {
            key: value
            for key, value in overall_template.items()
            if key not in ['preferTime', 'preferTimeWord',
                           'preferAuthor', 'registTime', 'preferBooks']
        }
        monthly_template["compare"] = 0
        monthly_template["dayAverageReadTime"] = 0
        template = monthly_template
    else:  # weekly
        weekly_template = {
            key: value
            for key, value in overall_template.items()
            if key not in ['readLongest', 'preferCategory', 'preferCategoryWord', 'preferTime', 'preferTimeWord',
                           'preferAuthor', 'registTime', 'preferBooks']
        }
        weekly_template["rank"] = {'text': ""}
        weekly_template["compare"] = 0
        weekly_template["dayAverageReadTime"] = 0
        template = weekly_template
    url = "https://i.weread.qq.com/readdata/detail?mode=" + type + "&defaultPreferBook=0&baseTime=0"
    return jsonify({"msg": "success", "data": extract_json(template, android_request(vid, skey, url))}), 200


def get_book_detail(vid, skey, book_id):
    book_id = str(book_id)
    dic = [
        {
            'url': "https://i.weread.qq.com/book/readinfo?bookId=" + book_id + "&finishedDate=1&readingBookIndex=1&finishedBookIndex=1",
            'template': {
                "readingBookDate": 0,
                "readingTime": 0,
            }
        }, {
            'url': "https://i.weread.qq.com/book/readingStat?bookId=" + book_id + "&dataType=1",
            'template': {
                "readingCount": 0,
                "finishReadingCount": 0
            }
        }, {
            'url': "https://i.weread.qq.com/book/info?bookId=" + book_id,
            'template': {
                "bookId": '',
                "title": '',
                "author": '',
                "cover": '',
                "intro": '',
                "publishTime": '',
                "category": '',
                "publisher": '',
                "totalWords": 0,
                "newRating": 0,
                "newRatingCount": 0,
                "newRatingDetail": {
                    "good": 0,
                    "fair": 0,
                    "poor": 0,
                    "title": '',
                },
                "AISummary": ''
            }
        }
    ]
    book_detail = {}
    for i in dic:
        book_detail.update(extract_json(i['template'], android_request(vid, skey, i["url"])))
    return jsonify({"msg": "success", "data": book_detail}), 200
