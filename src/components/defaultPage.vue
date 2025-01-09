<template>
    <div align="center">
        <h1>无人之岸，几多惊喜</h1>
        <img src="../assets/write.png"></img>
        <p>让思绪在笔尖绽放</p>
        <div style="height:50px;"></div>

    </div>

    <div class="contribution-graph">
        <div class="months">
            <span v-for="month in months" :key="month">{{ month }}</span>
        </div>
        <div class="calendar">
            <div class="weekdays">
                <span v-for="day in weekdays" :key="day">{{ day }}</span>
            </div>
            <div class="contributions">
                <div v-for="(contribution, index) in contributionsData" :key="index" class="contribution-cell"
                    :class="getCellClass(contribution)" :title="`${formatDate(index)}: ${contribution} contributions`">
                </div>
            </div>
        </div>
        <div class="legend">
            <span>Learn how we count contributions</span>
            <div class="legend-scale">
                <span>Less</span>
                <div v-for="level in 5" :key="level" class="legend-cell" :class="`contribution-level-${level - 1}`">
                </div>
                <span>More</span>
            </div>
        </div>
    </div>
    <div align="center">
        <h2>最近活动</h2>
        <p>最近看过的书&影视</p>
        <p>上次写到</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
const weekdays = ['Mon', 'Wed', 'Fri']

// Generate sample data for 365 days
const contributionsData = ref(Array(365).fill(0).map(() => {
    const random = Math.random()
    if (random > 0.95) return 12 // Level 4 (dark green)
    if (random > 0.90) return 8  // Level 3
    if (random > 0.85) return 4  // Level 2
    if (random > 0.80) return 2  // Level 1
    return 0                     // Level 0 (light gray)
}))

const getCellClass = (value) => {
    if (value === 0) return 'contribution-level-0'
    if (value <= 2) return 'contribution-level-1'
    if (value <= 4) return 'contribution-level-2'
    if (value <= 8) return 'contribution-level-3'
    return 'contribution-level-4'
}

const formatDate = (index) => {
    const date = new Date(2023, 0, index + 1)
    return date.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric'
    })
}
</script>

<style scoped>
.contribution-graph {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    padding: 20px;
    background: white;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.months {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    margin-left: 50px;
    margin-bottom: 10px;
    font-size: 12px;
    color: #586069;
}

.calendar {
    display: flex;
}

.weekdays {
    display: grid;
    grid-template-rows: repeat(7, 1fr);
    gap: 2px;
    margin-right: 4px;
    font-size: 12px;
    color: #586069;
}

.weekdays span {
    height: 10px;
    line-height: 10px;
    text-align: right;
    padding-right: 8px;
}

.contributions {
    display: grid;
    grid-template-columns: repeat(53, 1fr);
    gap: 2px;
}

.contribution-cell {
    width: 10px;
    height: 10px;
    border-radius: 2px;
}

.contribution-level-0 {
    background-color: #ebedf0;
}

.contribution-level-1 {
    background-color: #9be9a8;
}

.contribution-level-2 {
    background-color: #40c463;
}

.contribution-level-3 {
    background-color: #30a14e;
}

.contribution-level-4 {
    background-color: #216e39;
}

.legend {
    margin-top: 20px;
    font-size: 12px;
    color: #586069;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.legend-scale {
    display: flex;
    align-items: center;
    gap: 4px;
}

.legend-cell {
    width: 10px;
    height: 10px;
    border-radius: 2px;
}
</style>