<template>
    <div class="bookshelf-container" style="height:auto; min-height:100vh">
        <div class="nav-container">
            <div class="user-info">
                <div class="avatar-container">
                    <img :src="userData.avatar" :alt="userData.name" class="avatar-img" />
                </div>
                <div>
                    <div class="name-location">
                        <h2 class="user-name">{{ userData.name }}</h2>
                        <span class="location-badge">{{ userData.location }}</span>
                    </div>
                    <p class="user-signature">{{ userData.signature }}</p>
                </div>
            </div>
        </div>

        <!-- 文件夹选择 -->
        <div class="folder-container scrollbar-hide">
            <button v-for="folder in bookFolders" :key="folder.id"
                :class="['folder-button', { 'folder-active': activeFolder === folder.id }]"
                @click="handleFolderChange(folder.id)">
                <div class="folder-content">
                    <FolderOpen class="folder-icon" />
                    <span>{{ folder.name }}</span>
                </div>
            </button>
        </div>

        <!-- 书籍展示区 -->
        <div class="carousel-container">
            <div class="carousel-content">
                <BookCard v-for="(book, index) in currentBooks" :key="book.id" :book="book" :index="index"
                    :position="index - activeIndex" :is-active="index === activeIndex"
                    v-show="Math.abs(index - activeIndex) <= 2" @show-detail="handleShowDetail"
                    @set-active="setActiveIndex" />
            </div>

            <!-- 导航按钮 -->
            <button class="nav-button left" @click="handlePrevious">
                <ChevronLeft class="nav-icon" />
            </button>
            <button class="nav-button right" @click="handleNext">
                <ChevronRight class="nav-icon" />
            </button>

            <!-- 分页指示器 -->
            <div class="pagination">
                <button v-for="(_, index) in currentBooks" :key="index"
                    :class="['page-dot', { 'page-active': index === activeIndex }]"
                    @click="setActiveIndex(index)"></button>
            </div>
        </div>

        <!-- 用户资料弹窗 -->
        <UserProfile v-if="showProfile" :user-data="userData" @close="toggleProfile" />
        <BookDetail v-if="selectedBook" :book="selectedBook" @close="selectedBook = null" />
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import BookCard from './BookCard.vue';
import UserProfile from './UserProfile.vue';
import BookDetail from './BookDetail.vue';
import { ChevronRight, ChevronLeft, FolderOpen, User } from "lucide-vue-next"


// 从后端获取数据（示例模拟）
const fetchData = async () => {
    const response = {
        "data": {
            "bookshelf_info": {
                "books": [
                    {
                        "bookId": "38334243",
                        "cover": "https://wfqqreader-1252317822.image.myqcloud.com/cover/243/38334243/s_38334243.jpg",
                        "title": "我的第一本人生规划手册"
                    },
                    {
                        "bookId": "37700235",
                        "cover": "https://cdn.weread.qq.com/weread/cover/97/YueWen_37700235/s_YueWen_37700235.jpg",
                        "title": "马可瓦尔多（卡尔维诺作品）"
                    },
                    {
                        "bookId": "25242032",
                        "cover": "https://wfqqreader-1252317822.image.myqcloud.com/cover/32/25242032/s_25242032.jpg",
                        "title": "投资最重要的事"
                    },
                    {
                        "bookId": "CB_CLcH0eH142kU6sU6tJELkEQ4",
                        "cover": "https://res.weread.qq.com/wrepub/CB_8SF9ih9ha0uB6lX6kjGF7D3B_parsecover",
                        "title": "时间贫困"
                    },
                    {
                        "bookId": "CB_6VQBlcBlxB6b6qL6pADfG8GW",
                        "cover": "https://res.weread.qq.com/wrepub/CB_FajGSPGSFF2C6qK6pC1wj1yz_parsecover",
                        "title": "置身事内 中国政府与经济发展【复旦经院“毕业课”解读经济生活背后的政府角色。罗永浩、刘格菘、张军、周黎安、王烁联袂推荐】"
                    },
                    {
                        "bookId": "CB_3rAEmKElAB6b6qL6pA5qGGz3",
                        "cover": "https://res.weread.qq.com/wrepub/CB_5pk2VI2TD5BP6iN6gYAVHBAs_parsecover",
                        "title": "中医基础理论(全国中医药行业高等教育\"十三五\"规划教材,全国高等中医药院校规划教材)"
                    },
                    {
                        "bookId": "CB_1yyGV6GUAGQ96th6tJEn99tJ",
                        "cover": "https://res.weread.qq.com/wrepub/CB_FJhAFtAILFnu6sc6stAlS9HQ_parsecover",
                        "title": "2008国家公务员录用考试专用教材    申论   第2版"
                    },
                    {
                        "bookId": "CB_CzW6fG6fN0l66oq6pA7pbB32",
                        "cover": "https://res.weread.qq.com/wrepub/CB_A5TGoVGo41mP6hx6gl32nG20_parsecover",
                        "title": "海葵"
                    },
                    {
                        "bookId": "3300103147",
                        "cover": "https://cdn.weread.qq.com/weread/cover/64/cpplatform_wrilau5wukgvbfsmzafchn/s_cpplatform_wrilau5wukgvbfsmzafchn1719297962.jpg",
                        "title": "草民"
                    },
                    {
                        "bookId": "CB_1BMBdcBdv5wQ6sE6tJ3cT6mN",
                        "cover": "https://res.weread.qq.com/wrepub/CB_2kGGnUGnY9J46i26g0D9wDKZ_parsecover",
                        "title": "纳瓦尔宝典（硅谷投资人纳瓦尔十年人生智慧，教你如何获得财富与幸福。新时代创业者的《穷查理宝典》）"
                    },
                    {
                        "bookId": "CB_99A11Q11qEZ76m16l5CJRBGB",
                        "cover": "https://res.weread.qq.com/wrepub/CB_9hGCxaCwT7NK6i26gj00J3Xc_parsecover",
                        "title": "沟通的方法-脱不花"
                    }
                ],
                "folders": [
                    {
                        "books": [
                            {
                                "bookId": "41139692",
                                "cover": "https://wfqqreader-1252317822.image.myqcloud.com/cover/692/41139692/s_41139692.jpg",
                                "title": "1984"
                            },
                            {
                                "bookId": "22781912",
                                "cover": "https://wfqqreader-1252317822.image.myqcloud.com/cover/912/22781912/s_22781912.jpg",
                                "title": "动物农场"
                            },
                            {
                                "bookId": "23601930",
                                "cover": "https://cdn.weread.qq.com/weread/cover/68/YueWen_23601930/s_YueWen_23601930.jpg",
                                "title": "富爸爸穷爸爸"
                            }
                        ],
                        "name": "经济政治类"
                    },
                    {
                        "books": [
                            {
                                "bookId": "CB_Eqw9By9Fj5TN6fh6gw8Pp0jV",
                                "cover": "https://res.weread.qq.com/wrepub/CB_FKwB4gB3iBdm6e66cVBtm9yM_parsecover",
                                "title": "旅行之木（日本国宝级生态摄影师星野道夫的旅行哲学 犹如树木随波逐流，暂时忘却日常 汇入无关悲喜的另一种时间洪流 理想国出品）"
                            },
                            {
                                "bookId": "CB_76l5uR5rt5XU6bY6cj",
                                "cover": "https://res.weread.qq.com/wrepub/CB_0NrAVTAU0CE86Qu6Px_parsecover",
                                "title": "遥远的向日葵地"
                            },
                            {
                                "bookId": "3300012747",
                                "cover": "https://cdn.weread.qq.com/weread/cover/47/3300012747/s_3300012747.jpg",
                                "title": "我就是你啊：走进他人内心的7项修炼"
                            }
                        ],
                        "name": "闲暇读"
                    }
                ]
            },
            "user_info": {
                "avatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/5Cd5DiaVksY2AJU7OSfgVddHzfEvEkDt73IRlf5wtXAX8P0ArBVyyM9o1I3vKHYR7xAGHRurV78V9CTMnsFnXTYApgBHIsYesd3JSlrJMZpw/132",
                "location": "河南 南阳",
                "name": "吃口大汤圆",
                "signature": "行有不得反求诸己"
            }
        },
        "mes": "success"
    };
    return response.data;
};

// 初始化数据
const initData = async () => {
    const data = await fetchData();

    // 处理用户数据
    userData.value = data.user_info;

    // 处理书籍和文件夹数据
    const uncategorizedFolder = {
        name: '未分类',
        books: data.bookshelf_info.books.map(book => ({
            id: book.bookId,
            title: book.title,
            cover: book.cover
        }))
    };

    bookFolders.value = [
        { id: 1, name: uncategorizedFolder.name },
        ...data.bookshelf_info.folders.map((folder, index) => ({
            id: index + 2,
            name: folder.name
        }))
    ];

    booksByCategory.value = {
        1: uncategorizedFolder.books,
        ...Object.fromEntries(
            data.bookshelf_info.folders.map((folder, index) => [
                index + 2,
                folder.books.map(book => ({
                    id: book.bookId,
                    title: book.title,
                    cover: book.cover
                }))
            ])
        )
    };
};
initData();
const userData = ref({});
const bookFolders = ref([]);
const booksByCategory = ref({});
const activeFolder = ref(1);
const activeIndex = ref(0);
const selectedBook = ref(null);
const showProfile = ref(false);


// 根据当前选中的文件夹获取对应的书籍
const currentBooks = computed(() => {
    return booksByCategory.value[activeFolder.value] || [];
});

const handlePrevious = () => {
    activeIndex.value = activeIndex.value === 0
        ? currentBooks.value.length - 1
        : activeIndex.value - 1;
};

const handleNext = () => {
    activeIndex.value = activeIndex.value === currentBooks.value.length - 1
        ? 0
        : activeIndex.value + 1;
};

const toggleProfile = () => {
    showProfile.value = !showProfile.value;
};

// 切换文件夹时重置活动索引
const handleFolderChange = (folderId) => {
    activeFolder.value = folderId;
    activeIndex.value = 0;
};

const setActiveIndex = (index) => {
    activeIndex.value = index;
};
const handleShowDetail = (book) => {
    selectedBook.value ={ id: book.id };
};
</script>

<style scoped>
.bookshelf-container {
    width: 100%;
    max-width: 64rem;
    position: relative;
}



.nav-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.user-info {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.avatar-container {
    position: relative;
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 9999px;
    overflow: hidden;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

.avatar-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.name-location {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.user-name {
    font-size: 1.125rem;
    font-weight: 500;
    color: white;
}

.location-badge {
    font-size: 0.75rem;
    background-color: rgba(255, 255, 255, 0.2);
    padding: 0 0.5rem;
    border-radius: 9999px;
    color: rgba(255, 255, 255, 0.8);
}

.user-signature {
    font-size: 0.875rem;
    color: rgba(255, 255, 255, 0.7);
}

.nav-actions {
    display: flex;
    align-items: center;
}

.icon-button {
    padding: 0.5rem;
    border-radius: 9999px;
    background-color: rgba(255, 255, 255, 0.1);
    transition: background-color 0.2s;
}

.icon-button:hover {
    background-color: rgba(255, 255, 255, 0.2);
}

.icon {
    width: 1.25rem;
    height: 1.25rem;
    color: rgba(255, 255, 255, 0.8);
}

.folder-container {
    padding: 1rem 1.5rem;
    overflow-x: hidden;
    display: flex;
    gap: 0.75rem;
}

.folder-button {
    padding: 0.5rem 1rem;
    border-radius: 9999px;
    transition: background-color 0.2s, color 0.2s;
    background-color: rgba(255, 255, 255, 0.05);
    color: rgba(255, 255, 255, 0.6);
}

.folder-button:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.folder-active {
    background-color: rgba(255, 255, 255, 0.2);
    color: white;
}

.folder-content {
    display: flex;
    align-items: center;
    gap: 0.375rem;
}

.folder-icon {
    width: 1rem;
    height: 1rem;
}

.carousel-container {
    position: relative;
    height: 500px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.carousel-content {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
}

.nav-button {
    position: absolute;
    padding: 0.75rem;
    border-radius: 9999px;
    background-color: #000000;
    color: white;
    z-index: 10;
}


.nav-button.left {
    left: 1rem;
}

.nav-button.right {
    right: 1rem;
}

.nav-icon {
    width: 1.5rem;
    height: 1.5rem;
}

.pagination {
    margin-top: 490px;
    position: absolute;

    display: flex;
    gap: 10px;
}

.page-dot {
    width: 0.5rem;
    height: 0.5rem;
    border-radius: 9999px;
    background-color: rgba(255, 255, 255, 0.4);
    transition: all 0.2s;
}

.page-active {
    width: 1.5rem;
    background-color: white;
}
</style>