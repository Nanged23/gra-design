from src.user.service.user_service import record_daily_score


def add_score(source, user_id):
    """
    完成增加积分的操作
    :param user_id:用户 id
    :param source: 调用者身份
    :return:
    """
    dic = {
        "/article/write": 1.5,  # 写文章
        "/user/login": 0.5,  # 登录
        "/moment/write": 1,  # 写说说
        "/todo/record_memday": 1  # 记录纪念日
    }
    try:
        score = dic.get(source.split('?')[0])
        record_daily_score(user_id, score)
    except Exception as e:
        print(f"{source}调用,错误： {e}")
