<!-- TODO 完成数据装填 -->
<template>
    <main class="bg-gradient" style="margin-left: 230px; height: auto; overflow-y: auto;">
        <div v-if="hasCookie">
            <BookshelfDisplay />
        </div>
        <div v-else>
            <button @click="showModal = true">打开弹窗</button>

            <div v-if="showModal" class="modal">
                <div class="modal-content1">
                    <div align="center">使用微信扫一扫</div>
                    <br>

                    <div class="qrcode-placeholder">
                        <div v-if="!qrcode">
                            <img src='../../assets/pngs/loading.gif' style="width:300px;height:300px" />
                        </div>
                        <div v-else>
                            <img :src="qrcode" alt="二维码" class="qrcode" />
                        </div>
                    </div>
            

                <div class="footer_btn">
                    <button @click="showModal = false">关闭</button>
                    <button @click="handleScanned">我已扫码</button>
                </div>

            </div>
        </div>
        </div>
    </main>
</template>

<script setup>
import socket from '@/socket/socket.js';
import BookshelfDisplay from './BookshelfDisplay.vue';
import { ref, watch, onUnmounted, onMounted } from 'vue';
import Cookies from 'js-cookie';
let showModal = ref(false);
let qrcode = ref('');
let timer = null;
let hasCookie = ref(false);
let hasNotQrcode = ref(true);
let cookie = ref({
    'wr_vid': "",
    'wr_skey': ""
});
const fetchQRCode = async () => {
    socket.emit('message');
};
// 二维码倒计时 3 分钟
const startTimer = () => {
    console.log("开始计时");

    clearTimeout(timer);
    timer = setTimeout(() => {
        fetchQRCode();
        startTimer();
    }, 3 * 60 * 1000);
};
// 尝试从无头浏览器获取 cookie
const handleScanned = async () => { 
    socket.emit('cookie_data');
    showModal.value = false;
    clearTimeout(timer);
    hasCookie = true;
    Cookies.setCookie('wr_vid', cookie.value.wr_vid);
    Cookies.setCookie('wr_skey', cookie.value.wr_skey);
};

watch(showModal, (newVal) => {
    if (newVal) {
        if (qrcode.value == '') {
            fetchQRCode();
            console.log('开始轮询');
            const intervalId = setInterval(() => {
                if (qrcode.value != '') {
                    console.log('qrcode 已更新，轮询结束');
                    clearInterval(intervalId);
                    hasNotQrcode = true;
                }
            }, 100);
            setTimeout(() => {
                clearInterval(intervalId);
                console.log('3 秒轮询结束');
                hasNotQrcode = true;
            }, 3000);
        } else {
            hasNotQrcode = true;
        }
        startTimer();
    } else {
        clearTimeout(timer);
    }
});

onUnmounted(() => {
    clearTimeout(timer);
});
onMounted(() => {
    hasCookie = Cookies.get("wr_skey") == undefined ? false : true;
    socket.on('connect', () => {
        console.log('已连接到后端');
    });

    socket.on('disconnect', () => {
        console.log('与后端断开连接');
    });
    socket.on('message', (data) => {
        qrcode.value = data;
    });
    socket.on('get_cookie', (data) => {
        cookie.value = data;
    });
});
</script>

<style>
.scrollbar-hide {
    -ms-overflow-style: none;
    /* IE and Edge */
    scrollbar-width: none;
    /* Firefox */
}

.scrollbar-hide::-webkit-scrollbar {
    display: none;
    /* Chrome, Safari and Opera */
}

/* 添加字体 */
@font-face {
    font-family: 'PingFang SC';
    src: local('PingFang SC'), local('PingFang-SC');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}

body {
    font-family: 'PingFang SC', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

.footer_btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
}

.bg-gradient {
    background: transparent;
}

.qrcode-placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal-content1 {
    background: white;
    padding: 20px;
    border-radius: 5px;
}

.qrcode {
    max-width: 200px;
    margin-bottom: 10px;
}
</style>