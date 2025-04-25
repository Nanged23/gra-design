from src.third_platform.douban.utils.util import generate_random_string
import requests
from lxml import etree
from flask import jsonify
from src.user.entity import UserDetail
from src.basic.extensions import db
from src.third_platform.douban.entity import Douban
import datetime
from sqlalchemy import func
from dateutil.relativedelta import relativedelta
import pytz
from sqlalchemy import text


def get_data(user_id, category, page, per_page=15):
    """
    :param page:数字，标识当前页码
    :param user_id:用户 id，非豆瓣 id
    :param category:分类，分为 -1 -2 1 2，分别表示想看和看过，图书和电影
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
    douban_id = UserDetail.query.filter_by(user_id=user_id).first().douban_id
    url = "https://api.douban.com/v2/user/" + str(douban_id) + "?apikey=054022eaeae0b00e0fc068c0c0a2102a"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Cookie": "bid=" + generate_random_string()
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return jsonify({"msg": "success", "data": response.json()}), 200


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


def get_summary(user_id):
    summary = {}

    # 1. 想看最久还没看的电影、图书
    oldest_wish_movie = Douban.query.filter_by(user_id=user_id, row_type='-2').order_by(Douban.date).first()
    oldest_wish_book = Douban.query.filter_by(user_id=user_id, row_type='-1').order_by(Douban.date).first()
    summary['oldest_wish_movie'] = oldest_wish_movie.to_dict() if oldest_wish_movie else None
    summary['oldest_wish_book'] = oldest_wish_book.to_dict() if oldest_wish_book else None

    # 2. 想看的电影中，最多的前三个标签情况 & # 6. 看过的电影中，最多的前三个标签

    def get_top_tags(row_type, limit=3):
        query = text("""
            WITH RECURSIVE tag_cte AS (
                SELECT
                    SUBSTRING_INDEX(content_type, ',', 1) AS tag,
                    -- 使用 CHAR_LENGTH() 替代 LENGTH()
                    SUBSTRING(content_type, CHAR_LENGTH(SUBSTRING_INDEX(content_type, ',', 1)) + 2) AS remaining,
                    id
                FROM douban
                WHERE user_id = :user_id AND row_type = :row_type AND content_type IS NOT NULL
                
                UNION ALL
                
                SELECT
                    SUBSTRING_INDEX(remaining, ',', 1) AS tag, 
                    SUBSTRING(remaining, CHAR_LENGTH(SUBSTRING_INDEX(remaining, ',', 1)) + 2) AS remaining,
                    id
                FROM tag_cte
                WHERE remaining != ''
            )
            SELECT tag, COUNT(*) AS count
            FROM tag_cte
            WHERE tag != ''
            GROUP BY tag
            ORDER BY count DESC
            LIMIT :limit;
        """)

        result = db.session.execute(query, {'user_id': user_id, 'row_type': row_type, 'limit': limit}).all()

        tags_count = {}
        for item in result:
            tags_count[item[0]] = item[1]

        return tags_count

    summary['top3_wish_movie_tags'] = get_top_tags('-2')
    summary['top3_watched_movie_tags'] = get_top_tags('2')

    # 3. 看过的图书中，最爱的图书出版社前三，看过的电影中，最爱的制片国家前三
    def get_top_counts(field, row_type, limit=3):

        counts = db.session.query(field, func.count('*').label('count')).filter(
            Douban.user_id == user_id, Douban.row_type == row_type
        ).group_by(field).order_by(func.count('*').desc()).limit(limit).all()

        counts_count = {}
        for item in counts:
            counts_count[item[0]] = item[1]
        return counts_count

    summary['top3_book_languages'] = get_top_counts(Douban.language, '1')
    summary['top3_movie_languages'] = get_top_counts(Douban.language, '2')

    # 4. 看过的图书中，最爱的作者前三，看过的电影中，最爱的导演前三
    summary['top3_book_authors'] = get_top_counts(Douban.author, '1')
    summary['top3_movie_directors'] = get_top_counts(Douban.author, '2')

    # 5. 按月统计近 2 年里，每个月的读书和观影情况
    def get_monthly_stats():
        two_years_ago = datetime.datetime.now(pytz.timezone('Asia/Shanghai')) - relativedelta(years=2)

        monthly_stats = {}

        # 图书
        book_counts = db.session.query(
            func.date_format(Douban.date, '%Y-%m').label('month'),
            func.count('*').label('count')
        ).filter(
            Douban.user_id == user_id,
            Douban.row_type.in_(['1', '-1']),
            Douban.date >= two_years_ago
        ).group_by('month').all()

        for month, count in book_counts:
            if month not in monthly_stats:
                monthly_stats[month] = {'book_count': 0, 'movie_count': 0}
            monthly_stats[month]['book_count'] = count

        # 电影
        movie_counts = db.session.query(
            func.date_format(Douban.date, '%Y-%m').label('month'),
            func.count('*').label('count')
        ).filter(
            Douban.user_id == user_id,
            Douban.row_type.in_(['2', '-2']),
            Douban.date >= two_years_ago
        ).group_by('month').all()

        for month, count in movie_counts:
            if month not in monthly_stats:
                monthly_stats[month] = {'book_count': 0, 'movie_count': 0}
            monthly_stats[month]['movie_count'] = count

        # 排序
        temp = sorted(monthly_stats.items(), key=lambda x: x[0])
        monthly_stats_ = {}
        for item in temp:
            monthly_stats_[item[0]] = item[1]
        return monthly_stats_

    summary['monthly_stats'] = get_monthly_stats()

    # 7. 总的图书想看数，电影想看数，图书已看数，电影已看数
    summary['total_wish_books'] = Douban.query.filter_by(user_id=user_id, row_type='-1').count()
    summary['total_wish_movies'] = Douban.query.filter_by(user_id=user_id, row_type='-2').count()
    summary['total_read_books'] = Douban.query.filter_by(user_id=user_id, row_type='1').count()
    summary['total_watched_movies'] = Douban.query.filter_by(user_id=user_id, row_type='2').count()

    return jsonify({"msg": "success", "data": summary}), 200


def temp2():
    import os
    oss_prefix = "https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E8%B1%86%E7%93%A3%E5%B0%81%E9%9D%A2/"
    data = Douban.query.filter(Douban.id > -11)
    for i in data:
        i.img = oss_prefix + os.path.basename(i.img)
    db.session.commit()
