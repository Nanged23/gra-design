import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from flask import jsonify
from src.basic.database import redis_client
import random

def send_email(email):
    """
    发送验证码到邮箱
    :return: Boolean 发送状态
    """
    sender = ('flow-er', '2074759416@qq.com')  # 发件人
    token = 'zkkdadcdczjkcibf'  # 发件人邮箱授权码
    receive = ("test", email)  # 收件人
    content = '<p>尊敬的用户, 您好!🥳</p><p>&nbsp;&nbsp;&nbsp;&nbsp;<span>欢迎</span>注册本网站, 您本次的验证码是 <b>' + get_random_code(
        email) + '</b>, 该验证码 5 分钟之内有效, 请尽快使用!</p> '
    try:
        msg = MIMEText(content, 'html', 'utf-8')  # 填写邮件内容
        msg['From'] = formataddr(sender)  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(receive)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "欢迎来到 flow-er "  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(sender[1], token)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.sendmail(sender[1], receive[1], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:
        print(e)  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        return jsonify({"data": "验证码发送失败，请稍后再试!"}), 500
    return jsonify({"data": "验证码发送成功，请注意查收!"}), 200


def get_random_code(email, expiration=300):
    """
    TODO 设置随机验证码，并存储在 redis 数据库
    :return:
    """
    value = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    redis_client.set(email, value, ex=expiration)
    return '123456'


if __name__ == '__main__':
    send_email()
