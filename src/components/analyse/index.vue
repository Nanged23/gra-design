<template>
    <div class="floating-bubbles-container">
        <div class="bubbles-wrapper">
            <svg class="bubbles-svg">
                <circle v-for="bubble in bubbles" :key="bubble.id" :cx="bubble.x" :cy="bubble.y" :r="bubble.size"
                    :fill="bubble.color" class="bubble" :style="{
                        '--random-x': `${bubble.randomX}px`,
                        '--random-y': `${bubble.randomY}px`,
                        '--duration': `${bubble.duration}s`
                    }" />
            </svg>
        </div>

        <div class="ring-container">
            <svg class="ring-svg" viewBox="0 0 300 300">
                <!-- Ring center -->
                <circle cx="150" cy="150" r="60" fill="rgba(255, 255, 255, 0.2)" class="ring-center" />

                <!-- Ring sections -->
                <path v-for="(section, index) in sections" :key="section.name" :d="getArcPath(index)"
                    :class="['ring-section', { active: activeSection === index }]"
                    :style="{ '--section-color': getSectionColor(index) }" @click="navigateTo(section.route)"
                    @mouseenter="activeSection = index" @mouseleave="activeSection = null" />

                <!-- Dividers -->
                <path v-for="(_, index) in sections" :key="`divider-${index}`" :d="getDividerPath(index)"
                    class="ring-divider" />

                <!-- Text labels -->
                <g v-for="(section, index) in sections" :key="`text-${section.name}`">
                    <path :id="`textPath-${index}`" :d="getTextArcPath(index)" fill="none" />
                    <text :class="['ring-text', { 'active-text': activeSection === index }]">
                        <textPath :href="`#textPath-${index}`" startOffset="50%" text-anchor="middle">
                            {{ section.name }}
                        </textPath>
                    </text>
                </g>
            </svg>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const bubbles = ref([])
const activeSection = ref(null)
const sections = [
    { name: "微信读书", route: "/analyse/weread" },
    { name: "豆瓣", route: "/analyse/douban" },
    { name: "TODO", route: "/analyse/todo" },
    { name: "瞬间", route: "/analyse/moment" },
    { name: "文章", route: "/analyse/article" },
]
const sectionColors = [
    'rgba(183, 223, 255, 0.6)',
    'rgba(204, 213, 255, 0.6)',
    'rgba(224, 231, 255, 0.6)',
    'rgba(213, 240, 255, 0.6)',
    'rgba(193, 233, 255, 0.6)',
]
const getSectionColor = (index) => {
    return sectionColors[index]
}

const getArcPath = (index) => {
    const startAngle = index * ((2 * Math.PI) / 5) - Math.PI / 2
    const endAngle = (index + 1) * ((2 * Math.PI) / 5) - Math.PI / 2

    const outerRadius = 120
    const innerRadius = 60

    const startOuterX = 150 + outerRadius * Math.cos(startAngle)
    const startOuterY = 150 + outerRadius * Math.sin(startAngle)
    const endOuterX = 150 + outerRadius * Math.cos(endAngle)
    const endOuterY = 150 + outerRadius * Math.sin(endAngle)

    const startInnerX = 150 + innerRadius * Math.cos(endAngle)
    const startInnerY = 150 + innerRadius * Math.sin(endAngle)
    const endInnerX = 150 + innerRadius * Math.cos(startAngle)
    const endInnerY = 150 + innerRadius * Math.sin(startAngle)

    const largeArcFlag = 0

    return `
      M ${startOuterX} ${startOuterY}
      A ${outerRadius} ${outerRadius} 0 ${largeArcFlag} 1 ${endOuterX} ${endOuterY}
      L ${startInnerX} ${startInnerY}
      A ${innerRadius} ${innerRadius} 0 ${largeArcFlag} 0 ${endInnerX} ${endInnerY}
      Z
    `
}

const getDividerPath = (index) => {
    const angle = index * ((2 * Math.PI) / 5) - Math.PI / 2

    const outerRadius = 120
    const innerRadius = 60

    const outerX = 150 + outerRadius * Math.cos(angle)
    const outerY = 150 + outerRadius * Math.sin(angle)
    const innerX = 150 + innerRadius * Math.cos(angle)
    const innerY = 150 + innerRadius * Math.sin(angle)

    return `M ${innerX} ${innerY} L ${outerX} ${outerY}`
}

const getTextArcPath = (index) => {
    const startAngle = index * ((2 * Math.PI) / 5) - Math.PI / 2
    const endAngle = (index + 1) * ((2 * Math.PI) / 5) - Math.PI / 2
    const midAngle = (startAngle + endAngle) / 2

    const textRadius = 90
    const isTopHalf = midAngle > -Math.PI && midAngle < 0
    const isTodoOrWechat = index === 2 || index === 0
    const shouldReverse = isTodoOrWechat ? !isTopHalf : isTopHalf

    let startX, startY, endX, endY

    if (shouldReverse) {
        startX = 150 + textRadius * Math.cos(endAngle)
        startY = 150 + textRadius * Math.sin(endAngle)
        endX = 150 + textRadius * Math.cos(startAngle)
        endY = 150 + textRadius * Math.sin(startAngle)
    } else {
        startX = 150 + textRadius * Math.cos(startAngle)
        startY = 150 + textRadius * Math.sin(startAngle)
        endX = 150 + textRadius * Math.cos(endAngle)
        endY = 150 + textRadius * Math.sin(endAngle)
    }

    const largeArcFlag = 0
    const sweepFlag = shouldReverse ? 0 : 1

    return `M ${startX} ${startY} A ${textRadius} ${textRadius} 0 ${largeArcFlag} ${sweepFlag} ${endX} ${endY}`
}
const navigateTo = (route) => {
    router.push(route)
}
onMounted(() => {
    const windowWidth = window.innerWidth
    const windowHeight = window.innerHeight

    const newBubbles = Array.from({ length: 50 }, (_, i) => ({
        id: i,
        x: Math.random() * windowWidth,
        y: Math.random() * windowHeight,
        size: Math.random() * 20 + 5,
        color: `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, 0.3)`,
        randomX: Math.random() * 200 - 50,
        randomY: Math.random() * 200 - 50,
        duration: 5 + Math.random() * 10,
    }))

    bubbles.value = newBubbles
})
</script>

<style scoped>
.floating-bubbles-container {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background: linear-gradient(to bottom right, #aedbf9, #e7d6fa);
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
}

.bubbles-wrapper {
    position: absolute;
    inset: 0;
    pointer-events: none;
}

.bubbles-svg {
    width: 100%;
    height: 100%;
}

.bubble {
    opacity: 0;
    transform-origin: center;
    animation: float var(--duration) infinite alternate ease-in-out;
}

@keyframes float {
    0% {
        opacity: 0.7;
        transform: scale(1) translate(0, 0);
    }

    50% {
        opacity: 0.3;
        transform: scale(1.1) translate(var(--random-x), var(--random-y));
    }

    100% {
        opacity: 0.7;
        transform: scale(1) translate(0, 0);
    }
}

.ring-container {
    position: absolute;
    top: 50%;
    left: 55%;
    transform: translate(-50%, -50%);
    width: 80vmin;
    height: 80vmin;
    max-width: 600px;
    max-height: 600px;
    z-index: 10;
    animation: appearWithScale 1.2s ease-out forwards,
        rotateRing 1.3s ease-in-out 0.5s forwards;
}

.ring-svg {
    width: 100%;
    height: 100%;
    filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.5));
}

.ring-section {
    fill: var(--section-color);
    stroke: rgba(255, 255, 255, 0.7);
    stroke-width: 1;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    transform-origin: 150px 150px;
    filter: drop-shadow(0 0 3px rgba(255, 255, 255, 0.5));
}

.ring-section:hover {
    fill: rgba(184, 246, 237, 0.8);
    filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.8));
    transform: scale(1.04);
}

.ring-section.active {
    fill: rgba(240, 246, 245, 0.8);
    filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.9));
    transform: scale(1.05);
}

.ring-divider {
    stroke: rgba(255, 255, 255, 0.8);
    stroke-width: 1;
    stroke-linecap: round;
    filter: drop-shadow(0 0 3px rgba(255, 255, 255, 0.5));
}

.ring-center {
    filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.8));
    transition: all 0.3s ease;
    animation: pulse 4s infinite alternate ease-in-out;
}

.ring-text {
    font-size: 14px;
    font-weight: bold;
    fill: #333;
    pointer-events: none;
    transition: all 0.3s ease;
    filter: drop-shadow(0 0 1px rgba(255, 255, 255, 0.8));
}

.active-text {
    fill: #333;
    font-size: 15px;
    font-weight: bold;
    filter: drop-shadow(0 0 2px rgba(255, 255, 255, 1));
}

@keyframes rotateRing {
    0% {
        transform: translate(-50%, -50%) rotate(0deg);
    }

    100% {
        transform: translate(-50%, -50%) rotate(360deg);
    }
}

@keyframes appearWithScale {
    0% {
        opacity: 0;
        transform: translate(-50%, -50%) scale(0.5);
    }

    60% {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1.05);
    }

    80% {
        transform: translate(-50%, -50%) scale(0.98);
    }

    100% {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
    }
}

@keyframes pulse {
    0% {
        opacity: 0.8;
        transform: scale(1);
    }

    50% {
        opacity: 0.9;
        transform: scale(1.02);
    }

    100% {
        opacity: 1;
        transform: scale(1);
    }
}
</style>