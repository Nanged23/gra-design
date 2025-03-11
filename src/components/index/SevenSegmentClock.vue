<template>
  <div class="seven-segment-clock">
    <div class="digit-group" v-for="(group, groupIndex) in displayGroups" :key="groupIndex">
      <div v-for="(digit, digitIndex) in group.digits" :key="digitIndex" class="digit">
        <div class="segment a" :class="{ active: digit.segments.a }"></div>
        <div class="segment b" :class="{ active: digit.segments.b }"></div>
        <div class="segment c" :class="{ active: digit.segments.c }"></div>
        <div class="segment d" :class="{ active: digit.segments.d }"></div>
        <div class="segment e" :class="{ active: digit.segments.e }"></div>
        <div class="segment f" :class="{ active: digit.segments.f }"></div>
        <div class="segment g" :class="{ active: digit.segments.g }"></div>
      </div>
      <div class="separator" v-if="group.separator">{{ group.separator }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SevenSegmentClock',
  data() {
    return {
      time: new Date(),
      digitPatterns: {
        0: { a: 1, b: 1, c: 1, d: 1, e: 1, f: 1, g: 0 },
        1: { a: 0, b: 1, c: 1, d: 0, e: 0, f: 0, g: 0 },
        2: { a: 1, b: 1, c: 0, d: 1, e: 1, f: 0, g: 1 },
        3: { a: 1, b: 1, c: 1, d: 1, e: 0, f: 0, g: 1 },
        4: { a: 0, b: 1, c: 1, d: 0, e: 0, f: 1, g: 1 },
        5: { a: 1, b: 0, c: 1, d: 1, e: 0, f: 1, g: 1 },
        6: { a: 1, b: 0, c: 1, d: 1, e: 1, f: 1, g: 1 },
        7: { a: 1, b: 1, c: 1, d: 0, e: 0, f: 0, g: 0 },
        8: { a: 1, b: 1, c: 1, d: 1, e: 1, f: 1, g: 1 },
        9: { a: 1, b: 1, c: 1, d: 1, e: 0, f: 1, g: 1 }
      }
    }
  },
  computed: {
    displayGroups() {
      const year = String(this.time.getFullYear())
      const month = String(this.time.getMonth() + 1).padStart(2, '0')
      const day = String(this.time.getDate()).padStart(2, '0')
      const hours = String(this.time.getHours()).padStart(2, '0')
      const minutes = String(this.time.getMinutes()).padStart(2, '0')

      return [
        { digits: year.split('').map(d => ({ segments: this.digitPatterns[d] })), separator: ' ' },
        { digits: month.split('').map(d => ({ segments: this.digitPatterns[d] })), separator: ' ' },
        { digits: day.split('').map(d => ({ segments: this.digitPatterns[d] })), separator: ' ' },
        { digits: hours.split('').map(d => ({ segments: this.digitPatterns[d] })), separator: this.time.getSeconds() % 2 === 0 ? ':' : ' ' },
        { digits: minutes.split('').map(d => ({ segments: this.digitPatterns[d] })), separator: '' }
      ]
    }
  },
  mounted() {
    setInterval(() => {
      this.time = new Date()
    }, 1000)
  }
}
</script>

<style scoped>
.seven-segment-clock {
  display: flex;
  flex-wrap: nowrap;
  /* 确保不换行 */
  align-items: center;
  transform: scale(0.45);
  /* 使用 transform 进行缩放 */
  transform-origin: center;
  /* 缩放原点设置为中心 */
  margin: 0 auto;
}

.digit-group {
  display: flex;
  flex-wrap: nowrap;
  /* 确保每组数字不换行 */
  align-items: center;
  gap: 5px;
}

.digit {
  position: relative;
  width: 30px;
  height: 50px;
  flex-shrink: 0;
  /* 防止数字被压缩 */
}

.segment {
  position: absolute;
  background: #4e4e51;
  transition: background 0.2s;
}

.segment.active {
  background: rgb(229, 226, 131);
}

.a {
  top: 0;
  left: 5px;
  width: 20px;
  height: 5px;
}

.b {
  top: 5px;
  right: 0;
  width: 5px;
  height: 20px;
}

.c {
  bottom: 5px;
  right: 0;
  width: 5px;
  height: 20px;
}

.d {
  bottom: 0;
  left: 5px;
  width: 20px;
  height: 5px;
}

.e {
  bottom: 5px;
  left: 0;
  width: 5px;
  height: 20px;
}

.f {
  top: 5px;
  left: 0;
  width: 5px;
  height: 20px;
}

.g {
  top: 22.5px;
  left: 5px;
  width: 20px;
  height: 5px;
}

.separator {
  transform: scale(1.45);
  /* 使用 transform 进行缩放 */
  transform-origin: center;
  /* 缩放原点设置为中心 */
  margin: 0 auto;
  font-size: 30px;
  color: rgb(229, 226, 131);
  width: 10px;
  text-align: center;
  flex-shrink: 0;
  /* 防止分隔符被压缩 */
}
</style>