<template>
    <div class="main">
        <nav class="menu-bar" @mouseenter="isHovered = true" @mouseleave="isHovered = false">
            <div class="nav-glow" :class="{ 'nav-glow-hover': true }"></div>
            <ul class="menu-list">
                <div v-for="(item, index) in menuItems" :key="item.label" class="menu-item">
                    <div class="menu-item-container" @mouseenter="hoveredItem = index" @mouseleave="hoveredItem = null">
                        <div class="item-glow" :style="{ background: item.gradient }"
                            :class="{ 'item-glow-hover': hoveredItem === index }"></div>
                        <a :href="item.href" class="menu-link front"
                            :class="{ 'menu-link-hover': hoveredItem === index }">
                            <span class="icon" :class="[item.iconColor, { 'icon-hover': hoveredItem === index }]">
                                <component :is="item.icon" />
                            </span>
                            <span>{{ item.label }}</span>
                        </a>
                        <a :href="item.href" class="menu-link back"
                            :class="{ 'menu-link-hover': hoveredItem === index }">
                            <span class="icon" :class="[item.iconColor, { 'icon-hover': hoveredItem === index }]">
                                <component :is="item.icon" />
                            </span>
                            <span>{{ item.label }}</span>
                        </a>
                    </div>
                </div>
            </ul>
        </nav>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { Home, Settings, Bell, User } from 'lucide-vue-next';

const hoveredItem = ref(null);

const menuItems = [

    {
        icon: Settings,
        label: "列表视图",
        href: "#",
        gradient: "radial-gradient(circle, rgba(34,197,94,0.15) 0%, rgba(22,163,74,0.06) 50%, rgba(21,128,61,0) 100%)",
        iconColor: "icon-green",
    },
    {
        icon: User,
        label: "日历视图",
        href: "#",
        gradient: "radial-gradient(circle, rgba(239,68,68,0.15) 0%, rgba(220,38,38,0.06) 50%, rgba(185,28,28,0) 100%)",
        iconColor: "icon-red",
    },
];
</script>

<style scoped>
.main {
    margin-left: 220px;
    background: transparent;
    position: relative;
    z-index: 0;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}

.menu-bar {
    padding: 0.5rem;
    border-radius: 1rem;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.4));
    backdrop-filter: blur(10px);
    border: 1px solid rgba(229, 231, 235, 0.4);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    position: relative;
    overflow: hidden;
}

.nav-glow {
    position: absolute;
    inset: -0.5rem;
    background: radial-gradient(circle, transparent 0%,
            rgba(59, 130, 246, 0) 30%,
            rgba(124, 58, 237, 0) 60%,
            rgba(239, 68, 68, 0) 90%,
            transparent 100%);
    border-radius: 1.5rem;
    z-index: 0;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.5s ease;
}

.nav-glow-hover {
    opacity: 1;
    background: radial-gradient(circle, transparent 0%,
            rgba(59, 130, 246, 0.2) 30%,
            rgba(124, 58, 237, 0.2) 60%,
            rgba(239, 68, 68, 0.2) 90%,
            transparent 100%);
}

.menu-list {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    position: relative;
    z-index: 10;
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
    transition: opacity 0.5s ease, transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.item-glow-hover {
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
    border-radius: 0.75rem;
    transition: color 0.3s ease;
    backface-visibility: hidden;
}

.menu-link-hover {
    color: #111827;
}

.front {
    transform-style: preserve-3d;
    transform-origin: center bottom;
    transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.back {
    position: absolute;
    inset: 0;
    transform-style: preserve-3d;
    transform-origin: center top;
    transform: rotateX(90deg);
    opacity: 0;
    transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
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
    transition: color 0.3s ease;
    color: #111827;
}

.icon-blue.icon-hover {
    color: #3B82F6;
}

.icon-orange.icon-hover {
    color: #F97316;
}

.icon-green.icon-hover {
    color: #22C55E;
}

.icon-red.icon-hover {
    color: #EF4444;
}
</style>