# 项目后端服务

## 📍 概述
本分支为项目后端部分，使用 Python3.12，采用多蓝图方式实现各模块。

## 🛠 核心架构
**主要技术栈**:
- **Web框架**: Flask + SocketIO
- **数据库**: MySQL (主存储) + Redis (缓存)
- **云服务**: 阿里云OSS (对象存储)
- 
## 📝 设计文档

功能需求分析图、实体联系图、实体属性图：
![图1](../gra-design/src/assert/img1.png)

接口一览图、系统架构图、功能模块图：
![图2](../gra-design/src/assert/img2.png)

## 📁 文件结构
```bash
.
├── readme.md
├── requirements.txt
└── src
    ├── assert
    │   └── 404.jpeg
    ├── basic
    │   └── extensions.py
    ├── cur_platform
    │   ├── article
    │   │   ├── controller
    │   │   │   └── article_app.py 
    │   │   ├── entity.py
    │   │   └── service
    │   │       └── article_service.py
    │   ├── moment
    │   │   ├── controller
    │   │   │   └── moment_app.py
    │   │   ├── entity.py
    │   │   └── service
    │   │       └── moment_service.py
    │   └── todo
    │       ├── controller
    │       │   └── todo_app.py
    │       ├── entity.py
    │       └── service
    │           └── todo_service.py
    ├── final.py
    ├── scripts
    │   ├── backup_mysql.py
    │   ├── backup_redis.py
    │   ├── handle_secret.py 
    ├── third_platform
    │   ├── douban
    │   │   ├── controller
    │   │   │   └── douban_app.py
    │   │   ├── entity.py
    │   │   ├── service
    │   │   │   └── douban_service.py
    │   │   └── utils
    │   │       └── util.py
    │   └── weread
    │       ├── controller
    │       │   └── weread_app.py
    │       └── service
    │           ├── authentication.py
    │           └── weread_service.py
    └── user
        ├── controller
        │   └── user_app.py
        ├── entity.py
        ├── service
        │   ├── code_verify.py
        │   └── user_service.py
        └── utils
            └── add_score.py     
```
- **assert 文件夹**用于存储媒体数据
- **basic 文件夹**完成了项目的初始化内容，如初始化数据库，初始化 executor 队列，创建 socketIO 实例等
- **cur_platform、third_platform 和user** 是主要功能的实现。三个文件夹分别表示不同的服务模块，各模块都是 controller、service 文件夹+entity.py的主架构，分别是接口层及其对应实现。部分模块含有的 utils 文件夹里，是封装了一些工具函数。
- **scripts 文件夹**存储了脚本文件，分别是解密.env、备份 mysql 和 redis
- **final.py** 是主启动文件，包含了一些处理逻辑：websocket 的交互，各模块蓝图的注册
- **.env** 文件存储了一些字典：mysql、redis 的连接路径；阿里云 OSS、百度 AI、Kimi 的 token

## ⚠️ 不足部分

- 在微信读书的扫码登录和个人信息获取功能中（``src/third_platform/weread/``），原打算使用 pyppeteer 完成，但是由于 pyppeteer 和 flask 存在同步异步的问题，需要将 flask 重构或集成 Celery / Quart 实现，由于时间不足，未予以尝试，而是采用了原生 socket 的方式完成，详见 final.py，计划后续解耦成单独文件
- 在项目代码中，写有 todo 部分未完成
- 在 requirements.txt 中，部分包未被涵盖，导致运行可能出现 ImportError 错误，需手动安装
- 微信读书模块里，书架信息在电脑端和手机端都可以获取，阅读总结数据仅手机端含有。获取二者信息都不稳定，原因暂未知，，

## 🔍 上手使用
1. **初始化环境:**
- 安装依赖：``pip install -r requirements.txt``
- 配置数据库：创建数据库 stream，并运行脚本 stream.sql 
- 配置.env：打开``src/scripts/handle_secret.py`` 输入密钥，粘贴加密后的内容，还原.env