from src.third_platform.douban.utils.util import generate_random_string
import requests
from lxml import etree
from flask import jsonify
from src.user.entity import UserDetail
from src.basic.extensions import db
from src.third_platform.douban.entity import Douban


def get_data(user_id, category, page, per_page=15):
    """
    :param page:数字，标识当前页码
    :param user_id:用户 id，非豆瓣 id
    :param category:分类，分为 wish 和 collect，分别表示看过和想看
    :param per_page:每页条目数量
    :return:
    """
    movies = Douban.query.filter(Douban.user_id == user_id, Douban.row_type == category).order_by(
        Douban.create_time.desc()).paginate(page=int(page), per_page=per_page)
    all_movies = [movie.to_dict() for movie in movies.items]
    return jsonify({"msg": "success", "data": {'total_pages': movies.pages, 'total_items': movies.total,
                                               'items': all_movies}}), 200


def get_user(user_id):
    """
    :param user_id:用户 id
    :return:用户的个人信息
    """
    user_id = UserDetail.query.filter_by(id=user_id).first().douban_id
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
    :return:TODO 统计用户各类型的观影频次（豆瓣自带的标签统计不好用），以便生成统计图。当用户首次登录时，会初始化数据，之后每次登录，则增量更新观影情况
    """
    pass


def temp():
    def send_request(url):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "identity",
            "accept-language": "zh,zh-CN;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "cookie": "bid=hs507jrCDYs; douban-fav-remind=1; ll=\"108309\"; push_noty_num=0; push_doumail_num=0; viewed=\"11597363_35929450_25902728_26449601_7005249_30351293_35886603_36361860_36685093_36328704\"; dbcl2=\"265266112:0u9b5Y4juWE\"; ck=ZMmI; frodotk_db=\"d124b171d88e60c6736e145589ab2252\"",
            "priority": "u=0, i",
            "referer": "https://www.douban.com/people/172612296/?_i=1234084hs507jr",
            "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-site",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        return response.text

    a = {
        "data": [],
    }
    a = a["data"]
    for _ in a:
        try:
            target = etree.HTML(send_request(_['link']))
            publisher = target.xpath("/html/body/div[3]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]//text()")
            author = target.xpath("/html/body/div[3]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/a//text()")
            author = author[0].split(']')[1].strip()
            publisher = publisher[0]
            row_type = -1
            content_type = None
            user_id = 123
            douban = Douban(user_id, _['img'], _['link'], _['name'], _['date'], row_type, content_type, author,
                            publisher)
            db.session.add(douban)
            db.session.commit()
        except Exception:
            continue
