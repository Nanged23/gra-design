<style scoped>
.all {
    margin-left: 250px;
}

.archive-grid {
    width: 100%;
}

.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 10px;
    height: 300px;
    /* Adjust as needed */
    width: 100%;
}

.grid-item {
    overflow: hidden;
}

.book-cover {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Optional: Add specific positioning if needed */
.grid-item-1 {
    grid-area: 1 / 1 / 2 / 2;
}

/* Top Left */
.grid-item-2 {
    grid-area: 1 / 2 / 2 / 3;
}

/* Top Right */
.grid-item-3 {
    grid-area: 2 / 1 / 3 / 2;
}

/* Bottom Left */
.grid-item-4 {
    grid-area: 2 / 2 / 3 / 3;
}

/* Bottom Right */
.archive-container {
    padding: 16px;
}

.thumbnail-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    /* 两列布局 */
    grid-template-rows: 1fr 1fr;
    /* 两行布局 */
    gap: 8px;
    /* 图片之间的间距 */
    width: 200px;
    /* 缩略图的总宽度 */
    height: 200px;
    /* 缩略图的总高度 */
    position: relative;
    overflow: hidden;
}

.grid-item {
    width: 100%;
    height: 100%;
    position: relative;
}

.grid-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.grid-item.top-left {
    grid-area: 1 / 1;
    /* 第一行第一列 */
}

.grid-item.top-right {
    grid-area: 1 / 2;
    /* 第一行第二列 */
}

.grid-item.bottom-left {
    grid-area: 2 / 1;
    /* 第二行第一列 */
}

.grid-item.bottom-right {
    grid-area: 2 / 2;
    /* 第二行第二列 */
}

.book-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    /* 卡片之间的间距 */
    justify-content: flex-start;
    /* 从左侧开始排列 */
}

.card {
    box-sizing: border-box;
    width: calc((100% - 4 * 16px) / 5);
    /* 计算每个卡片的宽度，减去间距 */
    backdrop-filter: blur(6px);
    justify-content: center;
    border-radius: 17px;
    text-align: center;
    cursor: pointer;
    transition: all 0.5s;
    margin-bottom: 16px;
    /* 垂直方向的间距 */
}

.card-content {
    justify-content: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.card-image {
    border-radius: 17px;
    object-fit: cover;
    width: 128px;
    height: 185px;
    /* 可以根据需要调整 */
}

.card-title {
    justify-content: center;
    margin-top: 8px;
    width: 100%;
    word-wrap: break-word;
    text-align: center;
    padding: 0 5px;
    height: 60px;
}

.card:hover {

    transform: scale(1.05);
}
</style>
<template>
    <div class="all">
        <button @click="get_message()">
            获取
        </button>

        <!-- 渲染文件 -->
        <div class="book-grid">
            <div v-for="book in booksNotInarchives()" :key="book.bookId" class="card">
                <div class="card-content">
                    <img :src="book.cover" class="card-image">
                    <div class="card-title">{{ truncatedTitle(book.title) }}</div>
                </div>
            </div>
        </div>

        <!-- 渲染文件夹 -->
        <div class="archive-grid" v-if="archive && getBooksInarchive(archive.bookIds).length > 0">
            <div class="grid-container">
                <div v-for="(book, index) in getBooksInarchive(archive.bookIds).slice(0, 4)" :key="book.bookId"
                    :class="`grid-item grid-item-${index + 1}`">
                    <img :src="book.cover" :alt="book.title" class="book-cover" />
                </div>
            </div>
            <h3>{{ archive.name }}</h3>
            <hr>
        </div>
    </div>
</template>

<script>
import Cookies from 'js-cookie';
import axios from 'axios';
export default {
    mounted() {
        Cookies.set('skey', 'cMsL2qYX', { expires: 7 });
        Cookies.set('vid', '442726869', { expires: 7 });
    },
    data() {
        return {
            data: {
                books: [],
                archive: [],
                archive: null
            },
            archive: null
        }
    },
    computed: {},
    methods: {
        getGridPositionClass(index) {
            // 根据索引返回对应的区域类名
            const positions = ['top-left', 'top-right', 'bottom-left', 'bottom-right'];
            return positions[index % 4]; // 循环分配
        },
        get_message() {
            const url = '/weread/info';
            this.$axios.post(url, {}, { withCredentials: true }) // 第二个参数是请求体 (data)，这里为空对象
                .then(response => {
                    const jsonData = response.data; // axios 自动解析 JSON 数据
                    this.data = jsonData;

                    console.log('Full Data:', jsonData); // Log full data
                    console.log('Archive:', jsonData.archive); // Log archive data
                    console.log('Books:', jsonData.books); // Log books
                    console.log('Archive:', jsonData.archive); // Log archive again

                    this.archive = jsonData.archive;
                    this.$nextTick(() => {
                        const archivesInBooks = this.booksNotInarchives();
                        const booksInarchive = this.getBooksInarchive(this.archive?.bookIds);
                        console.log('Books in archive:', booksInarchive);
                    });
                })
                .catch(error => {
                    console.error("获取用户信息时出现 bug " + error);
                })


        },
        // 获取某个文件夹中包含的书籍
        getBooksInarchive(bookIds) {
            if (!bookIds || !this.data?.books) return [];
            return this.data.books.filter(book =>
                bookIds.includes(book.bookId)
            );
        },
        booksNotInarchives() {
            if (!this.data?.books || !this.data?.archive) return [];
            return this.data.books.filter(book =>
                !this.data.archive.some(archive =>
                    archive.bookIds.includes(book.bookId)
                )
            );
        },
        truncatedTitle(title) {
            if (title.length > 15) title = title.substring(0, 15) + '...'
            return title;
        }
    },
};
</script>
