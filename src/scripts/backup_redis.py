# 从 远程 Redis 数据库导出数据为 json 格式
import redis
import json
import os


def export_redis_data_scan(redis_url, output_file="/Users/dongliwei/Desktop/文档/CQUPT/design/backup/redis.json"):
    """
    连接到远程 Redis 服务器并使用 SCAN 将所有数据导出到本地 JSON 文件。
    """
    r = redis.from_url(redis_url)
    try:
        r.ping()
        data = {}
        cursor = "0"  # 从游标 0 开始
        while cursor != 0:
            cursor, keys = r.scan(cursor=cursor)  # SCAN 返回一个游标和一组键
            for key in keys:
                key_str = key.decode("utf-8")
                key_type = r.type(key).decode("utf-8")

                if key_type == "string":
                    value = r.get(key).decode("utf-8")
                elif key_type == "list":
                    value = [item.decode("utf-8") for item in r.lrange(key, 0, -1)]
                elif key_type == "set":
                    value = [item.decode("utf-8") for item in r.smembers(key)]
                elif key_type == "zset":
                    value = [{"member": member.decode("utf-8"), "score": score} for member, score in
                             r.zrange(key, 0, -1, withscores=True)]
                elif key_type == "hash":
                    value = {field.decode("utf-8"): val.decode("utf-8") for field, val in r.hgetall(key).items()}
                else:
                    print(f"警告：跳过键 '{key_str}'，不支持的类型：{key_type}")
                    continue

                data[key_str] = {"type": key_type, "value": value}

        # 避免覆盖错误（与之前相同的逻辑）
        base_name, ext = os.path.splitext(output_file)
        counter = 1
        while os.path.exists(output_file):
            output_file = f"{base_name}_{counter}{ext}"
            counter += 1

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"数据已使用 SCAN 导出到 {output_file} (JSON 格式)。")

    except redis.exceptions.ConnectionError as e:
        print(f"无法连接到 Redis：{e}")
    except redis.exceptions.ResponseError as e:
        print(f"Redis 响应错误：{e}")
    except Exception as e:
        print(f"发生意外错误：{e}")
    finally:
        if 'r' in locals() and r:
            r.close()


# --- 使用示例 (SCAN 版本) ---
redis_url = "rediss://red-cum665dumphs738deisg:m7GgLYQmG00rWldgGP718P7CWLaLHfjS@singapore-redis.render.com:6379"
export_redis_data_scan(redis_url)
