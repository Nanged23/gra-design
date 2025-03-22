<!-- TODO 添加分页功能，调整样式～ -->
<style scoped>
.menu-bar {
    padding: 0.5rem;
    border-radius: 1rem;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(241, 238, 227, 0.4));
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

.content-area {
    padding: 2rem;
    flex: 1;
    background: transparent;
    color: #111827;
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
            </ul>
        </nav>
        <div class="content-area">
            <ul class="tab-list">
                <li v-for="item in currentList" :key="item.id" class="list-item">
                    <span>{{ item.title }}</span>
                    <span>{{ item.tags }}</span>
                    <span v-if="item.set_time">{{ item.set_time }}</span>
                    <span v-if="item.finish_time">{{ item.finish_time }}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { Home, Settings, Bell, Crosshair } from 'lucide-vue-next';
import Cookies from 'js-cookie';
import { getTodoList } from '@/js/cur/todo';
const isHovered = ref(false);
const hoveredItem = ref(null);
const selectedIndex = ref(0);
const lists = ref({});
const other_data = ref({});
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