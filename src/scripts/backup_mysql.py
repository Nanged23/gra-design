# 从 远程 MySQL 数据库导出数据到 sql 文件
import subprocess
import os
import urllib.parse

# MySQL 连接字符串（请替换为你的实际信息）
CONNECTION_STRING = 'mysql+pymysql://jXqskZdNwTBSfmK.root:LifkC7ywynJ5p6TM@gateway01.eu-central-1.prod.aws.tidbcloud.com:4000/stream'

# 备份文件夹
BACKUP_PATH = '/Users/dongliwei/Desktop/文档/CQUPT/design/backup/'


def backup_database():
    """
    执行 MySQL 数据库备份，从连接字符串中提取信息。
    """
    try:
        # 解析连接字符串
        parsed_url = urllib.parse.urlparse(CONNECTION_STRING)
        db_user, db_password = parsed_url.netloc.split('@')[0].split(':')
        db_host = parsed_url.netloc.split('@')[1].split(':')[0]
        db_port = parsed_url.netloc.split('@')[1].split(':')[1]
        db_name = parsed_url.path[1:]
        backup_file = os.path.join(BACKUP_PATH, f"dump.sql")

        # 构建 mysqldump 命令
        command = [
            'mysqldump',
            '-h', db_host,
            '-P', str(db_port),  # 端口必须是字符串
            '-u', db_user,
            '-p' + db_password,  # 注意: 密码直接跟在 -p 后面，不要有空格
            db_name,
            f'--result-file={backup_file}'  # 输出到文件
        ]

        # 执行命令
        subprocess.run(command, check=True)
        print(f"Database backup created successfully: {backup_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error during database backup: {e}")
    except FileNotFoundError:
        print("Error: mysqldump command not found. Make sure MySQL client is installed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # 确保备份目录存在
    os.makedirs(BACKUP_PATH, exist_ok=True)
    backup_database()
