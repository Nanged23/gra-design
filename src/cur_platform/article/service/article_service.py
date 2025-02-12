import os
import re
from pypinyin import lazy_pinyin
from src.cur_platform.article.service.ai_service import get_summary
import asyncio
from src.cur_platform.article.entity import Article
from flask import jsonify, request
from src.basic.database import db
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
import uuid
from dotenv import load_dotenv
from src.user.utils.add_score import add_score
from src.basic.database import redis_client
from collections import defaultdict

load_dotenv()

word_count_key = f"word_count"


def handle_word_diff(word_diff, user_id):
    try:
        redis_client.hincrby(word_count_key, user_id, word_diff)
        print(f"用户{user_id}文章总字数变更了{word_diff}。")
    except Exception as e:
        print(f"Redis 操作失败：{e}")


def upload_img(cover):
    auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())
    endpoint = os.getenv('OSS_ENDPOINT')
    region = os.getenv('OSS_REGION')
    bucket = oss2.Bucket(auth, endpoint, os.getenv('OSS_BUCKET_NAME'), region=region)

    filename = cover.filename
    ext = filename.rsplit('.', 1)[1].lower()  # 获取文件后缀名
    new_filename = str(uuid.uuid4()) + '.' + ext  # 生成唯一的文件名
    object_name = f'文章封面/{new_filename}'
    bucket.put_object(object_name, cover.read())
    url = "https://" + os.getenv('OSS_BUCKET_NAME') + ".oss-" + os.getenv('OSS_REGION') + ".aliyuncs.com/" + object_name
    return url


def generate_slug(title, delimiter='-'):
    """
    给文章生成 slug
    :param title:标题
    :param delimiter: 标题间词句分隔符
    :return:
    """
    # 将中文转换为拼音
    pinyin_list = lazy_pinyin(title)

    # 将拼音列表合并成一个字符串，并正常化
    normalized_text = ''.join(pinyin_list)

    # 移除非字母数字字符，保留连字符和下划线
    stripped_text = re.sub(r'[^a-zA-Z0-9\s_-]', '', normalized_text)

    # 替换空格为指定的分隔符，并将结果转换为小写
    slug = re.sub(r'\s+', delimiter, stripped_text).strip().lower()

    # 移除多余的分隔符
    final_slug = re.sub(r'[-_]+', delimiter, slug)

    return final_slug


def generate_excerpt(blog_id):
    """
    根据文章 id 查询文章内容，然后生成文章摘要
    :param blog_id: 
    :return: 
    """
    content = Article.query.filter_by(id=blog_id).first().content
    excerpt = get_summary(content)
    return excerpt


def write_article(title, content, user_id, tags, cover, word_diff, summary_min_len=500):
    if tags is None or tags == '':
        tags = ''  # TODO 使用 AI 生成标签
    if cover is None or cover == '':  # 加入默认文章封面
        cover = 'https://guli-college0.oss-cn-chengdu.aliyuncs.com/%E6%96%87%E7%AB%A0%E5%B0%81%E9%9D%A2/default_cover.png'
    else:
        cover = upload_img(cover)
    slug = generate_slug(title)
    excerpt = ''  # ai 摘要默认置空,在异步任务中会进行填充
    blog_post = Article(title=title, slug=slug, content=content, excerpt=excerpt,
                        author_id=user_id, tags=tags, cover=cover)
    db.session.add(blog_post)
    db.session.commit()
    add_score(request.full_path, user_id)
    handle_word_diff(word_diff, user_id)
    # 创建异步任务，但不等待它完成
    if len(content) >= summary_min_len:
        asyncio.create_task(generate_excerpt(blog_post.id))
    return jsonify({'msg': '🎉 恭喜你，新写了一篇文章～'}), 200


def get_article(user_id, type, extra, default_len=20):
    """
    :param user_id: 用户 id
    :param type: 表明是获取所有文章还是单篇文章
    :param extra: 当 type 为 0 时，表示当前页码；当 type 为 1 时，表示文章 id
    :param default_len:默认缩略时，截取的长度
    :return:
    """
    if type == '0':  # 获取当前页码的所有文章
        per_page = 5  # 每页显示的文章数
        articles = Article.query.filter_by(author_id=user_id).paginate(page=int(extra), per_page=per_page)
        all_articles = [article.to_dict() for article in articles.items]
        for i in all_articles:  # 缩略文本用于展示
            i['content'] = i['content'][:default_len] + '...' if len(i['content']) > default_len else i['content']
        return jsonify({"msg": "success", "data": {'total_pages': articles.pages, 'total_items': articles.total,
                                                   'items': all_articles}}), 200
    elif type == '1':  # 获取单篇文章详情
        article = Article.query.filter_by(id=extra).first()
        article.views_count += 1
        db.session.add(article)  # 将 article 对象添加到 session 中，表示要更新它
        db.session.commit()
        # 查询上一篇文章和下一篇文章
        previous_article = Article.query.filter(Article.id < extra).order_by(Article.id.desc()).first()
        next_article = Article.query.filter(Article.id > extra).order_by(Article.id.asc()).first()
        pre_article = {
            "id": previous_article.id,
            "title": previous_article.title
        } if previous_article else None

        next_article = {
            "id": next_article.id,
            "title": next_article.title
        } if next_article else None
        read_time = len(article.content) // 300
        read_time = 1 if read_time <= 1 else read_time
        return jsonify({"msg": "success",
                        "data": {'read_time': read_time, 'pre_article': pre_article, 'next_article': next_article,
                                 'items': [article.to_dict()]}}), 200
    else:
        return jsonify({'msg': '参数异常'}), 400


def delete_article(article_id, word_diff):
    article = Article.query.filter_by(id=article_id).first()
    user_id = article.author_id
    if article is None:
        return jsonify({'msg': '文章不存在~'}), 400
    db.session.delete(article)
    db.session.commit()
    handle_word_diff(word_diff, user_id)
    return jsonify({'msg': '文章删除成功~'}), 200


def update_article(article_id, data, cover_file, word_diff):
    article = Article.query.get(article_id)
    if cover_file:
        # TODO 先去删除对应的文章封面再新增
        article.cover_image = upload_img(cover_file)  # 调用 upload_img 函数
    for key, value in data.items():
        if hasattr(article, key):
            setattr(article, key, value)
    db.session.commit()
    user_id = article.author_id
    handle_word_diff(word_diff, user_id)
    return jsonify({'msg': '文章更新成功'}), 200


def get_word_count(user_id):
    dic = [
        (255, '再别康桥'),
        (800, "新闻短评"),
        (2500, "契诃夫的《变色龙》")
    ]

    value = redis_client.hget(word_count_key, user_id)
    value = int(value)
    matched_text = None
    for threshold, title in dic:
        if value <= threshold:
            matched_text = (threshold, title)
            break
        else:
            # 用户文章字数大于所有阈值，使用最后一个参考文本
            matched_text = dic[-1]
    threshold, title = matched_text
    multiple = round(value / threshold, 1)
    sentence = f"{multiple} 本{title}"
    return jsonify({'msg': 'success', "data": {'word_count': value, 'sentence': sentence}}), 200


def get_word_cloud(user_id):
    articles = Article.query.filter_by(author_id=user_id).all()
    frequency = defaultdict(int)
    for article in articles:
        tags = article.tags
        for tag in tags.split(","):
            if tag != '':
                frequency[tag] += 1
    return jsonify({"msg": "success", "data": frequency}), 200
