> 于2025.03.08 开始前端！！
# 项目前端服务

## 📍 概述
本分支为项目前端部分，使用 npm@8.19.4、node@16.20.2

## 🛠 核心架构
- **核心框架**: Vue.js
- **主要的依赖**: ElementsUI (组件库) + Echarts (图表展示) + lucide (Icon) + axios (HTTP请求)

## 📁 文件结构
```bash
.
├── babel.config.js
├── jsconfig.json
├── package-lock.json
├── package.json
├── public
│   ├── favicon.ico
│   └── index.html
├── README.md
├── src
│   ├── api
│   │   └── axios.js
│   ├── App.vue
│   ├── assets
│   │   └── pngs
│   ├── components
│   │   ├── analyse
│   │   ├── cur
│   │   ├── defaultPage.vue
│   │   ├── index
│   │   │   ├── settings.vue
│   │   │   └── SevenSegmentClock.vue
│   │   ├── indexPage.vue
│   │   ├── third
│   │   └── user
│   │       ├── login.vue
│   │       └── register.vue
│   ├── js
│   │   ├── analyse
│   │   ├── cur
│   │   ├── index
│   │   ├── third
│   │   └── user
│   ├── main.js
│   ├── router
│   │   └── index.js
│   ├── socket
│   │   └── socket.js
│   └── stores
│       └── article.js
└── vue.config.js
```
- 开发内容主要集中在 **src 文件夹**中
- **api 文件夹**封装了基础 https 请求，并暴露给 js 文件夹
- **assets 文件夹**存储了各个页面的背景图片
- **components文件夹** 各个页面的渲染代码：
  - **analyse 文件夹：** 包括总结模块涵盖的各个子菜单，为各个模块提供数据看板功能
  - **cur文件夹：** 本平台提供的功能：文章模块、瞬间模块、待办模块
  - **index 文件夹：** 个人信息设置页面和菜单栏时间小组件
  - **third 文件夹：** 展示第三方平台的信息，目前接入的有豆瓣、微信读书
  - **user文件夹:** 登录注册页面
  - **defaultPage.vue:** 主页展示
  - **indexPage.vue:** 各个页面都存在的侧边菜单栏
- **js 文件夹：** api调用部分，和 components文件夹结构对应
- **route/index.js：** vue 各页面的路由
- **socket/socket.js：** 微信读书部分目前采用 socket 完成前后端交互，本文件初始化了 socket 连接
- **stores/article.js：** 文章模块使用了 pinia 进行存储,本文件进行了声明和初始化

## 📃 页面效果
页面效果图如下所示：

![image-20250612134257583](../src/assets/pngs/网站效果图.png)

## ⚠️不足之处
- 在微信读书模块中，各实体信息的展示，目前采用的是 json 直接渲染，后续需要改为调用后端正常交互
- 在豆瓣模块中，目前是直接从数据库读取死数据，后续考虑改为动态获取豆瓣数据
- 在个人设置页面，填写的 token 没有用到，后续需要优化

## 开始使用
1. 修改后端连接路径：``src/api/js/axios.js``
2. 修改 socket 连接路径：``src/socket/socket.js``
3. 运行：
```bash
npm install
npm run serve
```
