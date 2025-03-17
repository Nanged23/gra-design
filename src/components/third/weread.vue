<template>
    <div class="floating-bubbles-container">
        <div class="bubbles-wrapper">
            <svg class="bubbles-svg">
                <circle v-for="bubble in bubbles" :key="bubble.id" :cx="bubble.x" :cy="bubble.y" :r="bubble.size"
                    :fill="bubble.color" class="bubble" :style="{
                        '--random-x': bubble.randomX + 'px',
                        '--random-y': bubble.randomY + 'px',
                        '--duration': bubble.duration + 's'
                    }" />
            </svg>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';


const bubbles = ref([]);

onMounted(() => {
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    const newBubbles = Array.from({ length: 50 }, (_, i) => ({
        id: i,
        x: Math.random() * windowWidth,
        y: Math.random() * windowHeight,
        size: Math.random() * 20 + 5,
        color: `rgba(${Math.random() * 255},${Math.random() * 255},${Math.random() * 255},0.3)`,
        randomX: Math.random() * 100 - 50,
        randomY: Math.random() * 100 - 50,
        duration: 5 + Math.random() * 10
    }));

    bubbles.value = newBubbles;
});
</script>

<style>
.floating-bubbles-container {
    position: relative; 
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background: linear-gradient(to bottom right, #aedbf9, #e7d6fa);
    content: "";
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
        transform: scale(1.2) translate(var(--random-x), var(--random-y));
    }

    100% {
        opacity: 0.7;
        transform: scale(1) translate(0, 0);
    }
}



@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}
</style>