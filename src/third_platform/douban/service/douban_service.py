from src.third_platform.douban.utils.util import generate_random_string
import requests
from lxml import etree
import re
import json
from flask import jsonify
from src.user.entity import UserDetail
from math import ceil


def send_request(url):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Cookie": "bid=" + generate_random_string()
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text


def get_books(id, category, page, sort):
    user_id = UserDetail.query.filter_by(user_id=id).first().douban_id
    url = "https://book.douban.com/people/" + str(user_id) + "/" + category + "?sort=" + sort + "&start=" + str(
        15 * (int(page) - 1))
    text = send_request(url)
    tree = etree.HTML(text)
    parent_divs = tree.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/ul/li')
    entry = []

    for div in parent_divs:
        # 获取各条目的信息
        img_element = div.xpath('./div[1]/a/img')
        if img_element:
            img_src = img_element[0].get('src')

        link_element = div.xpath('./div[2]/h2/a')
        if link_element:
            link_href = link_element[0].get('href')
            title = link_element[0].get('title')

        time_element = div.xpath('./div[2]/div[2]/div[1]/span/text()')
        if time_element:
            cleaned_content = re.sub(r'\s+', ' ', time_element[0])
            cleaned_content = cleaned_content.strip()
            date = re.sub(r'<[^>]+>', '', cleaned_content).strip()

        entry.append({
            "img": img_src or None,
            "name": title or None,
            "link": link_href or None,
            "date": date or None,
        })
    entry = json.dumps(entry, ensure_ascii=False)

    process = tree.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div/div[2]/span/text()')
    process = re.sub(r'\s+', '', process[0])
    match = re.search(r'-(.*?)/(\d+)', process)
    totalPage = ceil(int(match.group(2).strip()) / 15)
    num = int(match.group(1).strip())
    current_page = ceil(num / 15) if num > 15 else 1
    answer = {
        "msg": "success",
        "process": process,
        "currentPage": current_page,
        "totalPage": totalPage,
        "data": entry
    }
    return jsonify(answer), 200


def get_movies(id, category, page, sort):
    """
    :param sort: 分为 time 和 rating
    :param page:数字，标识当前页码
    :param id:用户 id，非豆瓣 id
    :param category:分类，分为 wish 和 collect，分别表示看过和想看
    :return:
    """
    user_id = UserDetail.query.filter_by(user_id=id).first().douban_id
    url = "https://movie.douban.com/people/" + str(user_id) + "/" + category + "?sort=" + sort + "&start=" + str(
        15 * (int(page) - 1))
    text = send_request(url)
    tree = etree.HTML(text)
    entry = []

    parent_divs = tree.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div')

    # 获取每一页的电影列表

    for div in parent_divs:
        # 获取各条目的信息
        img_element = div.xpath('./div[1]/a/img')
        if img_element:
            img_src = img_element[0].get('src')

        link_element = div.xpath('./div[2]/ul/li[1]/a')
        if link_element:
            link_href = link_element[0].get('href')
            em_text = link_element[0].xpath('./em/text()')
            em_text = em_text[0] if em_text else ''
            title = em_text.split(' /')[0]

        time_element = div.xpath('./div[2]/ul/li[3]/span/text()')
        if time_element:
            date = time_element[0]
        entry.append({
            "img": img_src or None,
            "name": title or None,
            "link": link_href or None,
            "date": date or None,
        })
    entry = json.dumps(entry, ensure_ascii=False)
    process = tree.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[4]/span/text()')
    process = re.sub(r'\s+', '', process[0])
    match = re.search(r'-(.*?)/(\d+)', process)
    totalPage = ceil(int(match.group(2).strip()) / 15)
    num = int(match.group(1).strip())
    current_page = ceil(num / 15) if num > 15 else 1
    answer = {
        "msg": "success",
        "process": process,
        "currentPage": current_page,
        "totalPage": totalPage,
        "data": entry
    }
    return jsonify(answer), 200


def get_user(id):
    """
    :param id:
    :return:用户的个人信息
    """
    user_id = UserDetail.query.filter_by(id=id).first().douban_id
    url = "https://api.douban.com/v2/user/" + str(user_id) + "?apikey=054022eaeae0b00e0fc068c0c0a2102a"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Cookie": "bid=" + generate_random_string()
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return jsonify({"msg": "success", "data": response.json()}), 200


def movie_data():
    """
    :return:TODO 统计用户各类型的观影频次，以便生成统计图。当用户首次登录时，会初始化数据，之后每次登录，则增量更新观影情况
    """
    pass
