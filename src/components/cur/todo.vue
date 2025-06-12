<style scoped>
.menu-bar {
    padding: 0.5rem;
    border-radius: 1rem;
    background: linear-gradient(90deg,
            rgba(204, 219, 244, 0.7),
            rgba(237, 211, 193, 0.7),
            rgba(212, 243, 224, 0.7),
            rgba(243, 210, 210, 0.7));
    backdrop-filter: blur(10px);
    border: 1px solid rgba(229, 231, 235, 0.4);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    position: relative;
    overflow: hidden;
    margin-right: 20px;
    width: auto;
    display: inline-block;
}

.nav-glow {
    position: absolute;
    inset: -0.5rem;
    background: radial-gradient(circle,
            transparent 0%,
            rgba(59, 130, 246, 0) 30%,
            rgba(124, 58, 237, 0) 60%,
            rgba(239, 68, 68, 0) 90%,
            transparent 100%);
    border-radius: 1.5rem;
    z-index: 0;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.menu-list {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    position: relative;
    z-index: 10;
    list-style-type: none;
    padding: 0;
    margin: 0;
    justify-content: center;
}

.menu-item {
    position: relative;
}

.menu-item-container {
    display: block;
    border-radius: 0.75rem;
    overflow: visible;
    position: relative;
    perspective: 600px;
}

.item-glow {
    position: absolute;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    border-radius: 1rem;
    opacity: 0;
    transform: scale(0.8);
    transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1),
        transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.item-glow-active {
    opacity: 1;
    transform: scale(2);
}

.menu-link {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    position: relative;
    z-index: 10;
    background: transparent;
    color: #6B7280;
    /* text-muted-foreground */
    transition: color 0.3s ease;
    border-radius: 0.75rem;
    text-decoration: none;
    backface-visibility: hidden;
}

.menu-link-hover {
    color: #111827;
    /* text-foreground */
}

.front {
    transform-style: preserve-3d;
    transform-origin: center bottom;
    transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1),
        opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.back {
    position: absolute;
    inset: 0;
    transform-style: preserve-3d;
    transform-origin: center top;
    transform: rotateX(90deg);
    opacity: 0;
    transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1),
        opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.menu-item-container:hover .front {
    transform: rotateX(-90deg);
    opacity: 0;
}

.menu-item-container:hover .back {
    transform: rotateX(0);
    opacity: 1;
}

.icon {
    color: #111827;
    transition: color 0.3s ease;
}

.icon-svg {
    height: 1.25rem;
    width: 1.25rem;
}

.text-blue-500 {
    color: #3B82F6;
}

.text-orange-500 {
    color: #F97316;
}

.text-green-500 {
    color: #22C55E;
}

.text-red-500 {
    color: #EF4444;
}

/* New enhanced styles for the content area and todo items */
.content-area {
    padding: 2rem;
    flex: 1;
    background: transparent;
    color: #111827;
    position: relative;
    overflow: hidden;
}

.content-area::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    z-index: 1;
}

.tab-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.list-item {
    position: relative;
    padding: 1.5rem;
    border-radius: 1rem;
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    transition: all 0.3s ease;
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.75rem;
    overflow: hidden;
    transform-style: preserve-3d;
    transform: perspective(1000px) translateZ(0);
}

.list-item::before {
    content: '';
    position: absolute;
    inset: 0;
    z-index: -1;
    background: linear-gradient(135deg,
            rgba(255, 255, 255, 0.4) 0%,
            rgba(255, 255, 255, 0.1) 100%);
    border-radius: inherit;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.list-item:hover {
    transform: perspective(1000px) translateZ(10px) rotateX(2deg) rotateY(2deg);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.list-item:hover::before {
    opacity: 1;
}

.list-item::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg,
            var(--item-color-start, rgba(59, 130, 246, 0.7)),
            var(--item-color-end, rgba(124, 58, 237, 0.7)));
    transition: transform 0.3s ease;
    transform-origin: left;
}

.list-item:hover::after {
    transform: scaleX(1.05);
}

.list-item-title {
    font-weight: 600;
    font-size: 1.125rem;
    color: #111827;
    margin: 0;
    position: relative;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transform: translateZ(10px);
}

.list-item-title::before {
    content: '';
    display: block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--item-color-start, #3B82F6);
    box-shadow: 0 0 8px var(--item-color-start, rgba(59, 130, 246, 0.7));
}

.list-item-tags {
    font-size: 0.875rem;
    color: #6B7280;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    transform: translateZ(5px);
}

.tag {
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    background: rgba(239, 233, 245, 0.7);
    transition: all 0.3s ease;
}

.tag:hover {
    background: rgba(211, 193, 217, 0.9);
    transform: translateY(-2px);
}

.list-item-time {
    font-size: 0.875rem;
    color: #6B7280;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transform: translateZ(5px);
}

.time-icon {
    opacity: 0.7;
}

/* Category-specific colors */
.list-item-recent {
    --item-color-start: rgba(59, 130, 246, 0.7);
    --item-color-end: rgba(37, 99, 235, 0.7);
}

.list-item-future {
    --item-color-start: rgba(249, 115, 22, 0.7);
    --item-color-end: rgba(234, 88, 12, 0.7);
}

.list-item-unknown {
    --item-color-start: rgba(34, 197, 94, 0.7);
    --item-color-end: rgba(22, 163, 74, 0.7);
}

.list-item-completed {
    --item-color-start: rgba(239, 68, 68, 0.7);
    --item-color-end: rgba(220, 38, 38, 0.7);
}

/* Animation for new items */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.list-item {
    animation: fadeIn 0.5s ease forwards;
    animation-delay: calc(var(--index) * 0.1s);
    opacity: 0;
}

.page-container {
    display: flex;
    flex-direction: column;
    margin-left: 230px;
}
</style>
<template>
    <div class="page-container">
        <nav class="menu-bar" @mouseenter="isHovered = true" @mouseleave="isHovered = false">
            <div class="nav-glow" :class="{ 'nav-glow-active': isHovered }"></div>
            <ul class="menu-list">
                <li v-for="(item, index) in menuItems" :key="item.label" class="menu-item">
                    <div class="menu-item-container" @mouseenter="hoveredItem = index" @mouseleave="hoveredItem = null"
                        @click="selectMenu(index)">
                        <div class="item-glow" :class="{ 'item-glow-active': hoveredItem === index }"
                            :style="{ background: item.gradient }"></div>
                        <a :href="item.href" class="menu-link front"
                            :class="{ 'menu-link-hover': hoveredItem === index }">
                            <span :class="['icon', { [item.iconColorClass]: hoveredItem === index }]">
                                <component :is="item.icon" class="icon-svg" />
                            </span>
                            <span>{{ item.label }}</span>
                        </a>
                        <a :href="item.href" class="menu-link back"
                            :class="{ 'menu-link-hover': hoveredItem === index }">
                            <span :class="['icon', { [item.iconColorClass]: hoveredItem === index }]">
                                <component :is="item.icon" class="icon-svg" />
                            </span>
                            <span>{{ item.label }}</span>
                        </a>
                    </div>
                </li>
                <li>
                    <span style="margin-left:120px;">
                        <el-button type="primary" @click="openFormDialog">➕</el-button>
                    </span>
                </li>
            </ul>


        </nav>
        <el-dialog v-model="dialogFormVisible" title="我的表单" width="500px" :before-close="handleDialogClose">
            <el-form ref="form" :model="form.value" label-width="80px">
                <el-form-item label="待办名称">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>

                <el-form-item label="预计完成">
                    <el-col :span="11">
                        <el-date-picker type="date" placeholder="日期" v-model="form.date1"
                            style="width: 100%;"></el-date-picker>
                    </el-col>
                    <el-col class="line" :span="2">-</el-col>
                    <el-col :span="11">
                        <el-time-picker placeholder="时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
                    </el-col>
                </el-form-item>
                <el-form-item label="所属标签">
                    <el-checkbox-group v-model="form.type1"> <!-- 确保 v-model 访问的是 form.value.type -->
                        <el-checkbox value="生活" name="type">生活</el-checkbox>
                        <el-checkbox value="学习" name="type">学习</el-checkbox>
                        <el-checkbox value="工作" name="type">工作</el-checkbox>
                    </el-checkbox-group>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">立即创建</el-button>
                    <el-button>取消</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
        <div class="content-area">
            <ul class="tab-list">
                <li v-for="(item, index) in currentList" :key="item.id" :class="[
                    'list-item',
                    `list-item-${menuItems[selectedIndex].apiEndpoint}`
                ]" :style="{ '--index': index }">
                    <h3 class="list-item-title">{{ item.title }}</h3>
                    <div class="list-item-tags">
                        <span v-if="item.tags" v-for="tag in formatTags(item.tags)" :key="tag" class="tag">
                            {{ tag }}
                        </span>
                    </div>
                    <div v-if="item.set_time" class="list-item-time">
                        <span class="time-icon">📅</span>
                        <span>{{ formatDate(item.set_time) }}</span>
                    </div>
                    <div v-if="item.finish_time" class="list-item-time">
                        <span class="time-icon">✅</span>
                        <span>{{ formatDate(item.finish_time) }}</span>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { Home, Settings, Bell, Crosshair } from 'lucide-vue-next';
import Cookies from 'js-cookie';
import { getTodoList, writeTodo } from '@/js/cur/todo';
const dialogFormVisible = ref(false);
const isHovered = ref(false);
const hoveredItem = ref(null);
const selectedIndex = ref(0);
const lists = ref({});
const other_data = ref({});
const form = ref({
    name: '',
    date1: null,
    date2: null,
    type1: ["学习", "工作", "生活"]
});
const formRef = ref(null);
const openFormDialog = () => {
    dialogFormVisible.value = true;
    form.value.name = '';
    form.value.date1 = null;
    form.value.date2 = null;
    form.value.type1 = [];
    if (formRef.value) {
        formRef.value.clearValidate();
    }
};
const handleDialogClose = (done) => {
    done(); 
};
const onSubmit = async () => {
    if (!formRef.value) return;
    let expectedCompletionTime = null;
    if (form.value.date1 && form.value.date2) {
        const datePart = new Date(form.value.date1);
        const timePart = new Date(form.value.date2);
        expectedCompletionTime = new Date(
            datePart.getFullYear(),
            datePart.getMonth(),
            datePart.getDate(),
            timePart.getHours(),
            timePart.getMinutes(),
            timePart.getSeconds()
        );
    } else if (form.value.date1) {
        expectedCompletionTime = new Date(form.value.date1);
    } const params = {
        name: form.value.name, // 从 form.value 读取
        expectedCompletionTime: expectedCompletionTime,
        tags: form.value.type1 // 从 form.value 读取
    };

    try {
        const response = await writeTodo(params);
        if (response && response.success) {
            ElMessage.success(response.message || '创建成功！');
            dialogFormVisible.value = false; // 关闭对话框

            // 4. 刷新页面
            window.location.reload();
        } else {
            ElMessage.error(response.message || '创建失败，请稍后再试。');
        }
    } catch (error) {
        console.error("创建待办事项失败:", error);
        ElMessage.error('创建过程中发生错误。');
    }
};
const currentList = computed(() => {
    const endpoint = menuItems[selectedIndex.value].apiEndpoint;
    return lists.value[endpoint] || [];
});

const menuItems = [{
    icon: Home,
    label: "最近",
    href: "#",
    gradient: "radial-gradient(circle, rgba(59,130,246,0.15) 0%, rgba(37,99,235,0.06) 50%, rgba(29,78,216,0) 100%)",
    iconColorClass: "text-blue-500",
    apiEndpoint: "recent"
},
{
    icon: Bell,
    label: "以后",
    href: "#",
    gradient: "radial-gradient(circle, rgba(249,115,22,0.15) 0%, rgba(234,88,12,0.06) 50%, rgba(194,65,12,0) 100%)",
    iconColorClass: "text-orange-500",
    apiEndpoint: "future"
},
{
    icon: Settings,
    label: "某天",
    href: "#",
    gradient: "radial-gradient(circle, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.06) 50%, rgba(21,128,61,0) 100%)",
    iconColorClass: "text-green-500",
    apiEndpoint: "unknown"
},
{
    icon: Crosshair,
    label: "已完成",
    href: "#",
    gradient: "radial-gradient(circle, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.06) 50%, rgba(185,28,28,0) 100%)",
    iconColorClass: "text-red-500",
    apiEndpoint: "completed"
}];

const formatTags = (tags) => {
    if (!tags) return [];
    return typeof tags === 'string' ? tags.split(',').map(tag => tag.trim()) : [];
};

const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('zh-CN', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    }).format(date);
};

const fetchList = async (endpoint) => {
    console.log(endpoint);
    let params = {
        "user_id": Cookies.get('user_id'),
        "page": 1
    }
    if (endpoint == "completed") {
        params = { ...params, "is_finished": 1 }
    } else {
        params = { ...params, "is_finished": 0 }
        params = { ...params, "type": endpoint }
    }
    const res = await getTodoList(params)
    other_data.value = {
        "total_items": res.data.total_items,
        "total_pages": res.data.total_pages,
    };
    console.log(other_data.value);

    lists.value[endpoint] = res.data.items;
};

const selectMenu = (index) => {
    selectedIndex.value = index;
    const endpoint = menuItems[index].apiEndpoint;
    if (!lists.value[endpoint]) {
        fetchList(endpoint);
    }
};

onMounted(() => {
    fetchList(menuItems[0].apiEndpoint);
});
</script>
