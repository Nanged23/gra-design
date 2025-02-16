from flask import current_app
import requests


def add_score(source, user_id):
    """
    完成增加积分的操作
    :param user_id:用户 id
    :param source: 调用者身份
    :return: 
    """
    dic = {
        "/article/write": 1.5,
        "/user/login": 0.5,
        "/moment/write": 1,
        "/todo/record_memday": 1
    }
    add_score_api = current_app.config.get("ADD_SCORE_API")
    try:
        score = dic.get(source.split('?')[0])
        response = requests.get(add_score_api, params={'user_id': user_id, 'score': score})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{source}调用,错误： {e}")
