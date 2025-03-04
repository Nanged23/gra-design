import datetime
import pytz

now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))

# 计算一个月前的日期
one_year_ago = now - datetime.timedelta(days=365)

date_str = now.astimezone(pytz.utc).replace(tzinfo=None).strftime("%Y%m%d")
print(now, one_year_ago, date_str)
