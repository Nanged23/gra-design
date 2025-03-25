<template>
    <div class="raining-container">
      <div class="title-container">
        <h1 ref="titleElement" class="scrambled-title">RAINING LETTERS</h1>
      </div>
      <span
        v-for="(char, index) in characters"
        :key="index"
        :class="[
          'character',
          activeIndices.has(index) ? 'character-active' : 'character-inactive'
        ]"
        :style="{
          left: `${char.x}%`,
          top: `${char.y}%`
        }"
      >
        {{ char.char }}
      </span>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive, onMounted, onBeforeUnmount, computed } from 'vue';
  
  // TextScramble class for the title animation
  class TextScramble {
    constructor(el) {
      this.el = el;
      this.chars = '!<>-_\\/[]{}—=+*^?#';
      this.queue = [];
      this.frame = 0;
      this.frameRequest = 0;
      this.resolve = () => {};
      this.update = this.update.bind(this);
    }
  
    setText(newText) {
      const oldText = this.el.innerText;
      const length = Math.max(oldText.length, newText.length);
      const promise = new Promise((resolve) => this.resolve = resolve);
      this.queue = [];
      
      for (let i = 0; i < length; i++) {
        const from = oldText[i] || '';
        const to = newText[i] || '';
        const start = Math.floor(Math.random() * 40);
        const end = start + Math.floor(Math.random() * 40);
        this.queue.push({ from, to, start, end });
      }
      
      cancelAnimationFrame(this.frameRequest);
      this.frame = 0;
      this.update();
      return promise;
    }
  
    update() {
      let output = '';
      let complete = 0;
      
      for (let i = 0, n = this.queue.length; i < n; i++) {
        let { from, to, start, end, char } = this.queue[i];
        if (this.frame >= end) {
          complete++;
          output += to;
        } else if (this.frame >= start) {
          if (!char || Math.random() < 0.28) {
            char = this.chars[Math.floor(Math.random() * this.chars.length)];
            this.queue[i].char = char;
          }
          output += `<span class="dud">${char}</span>`;
        } else {
          output += from;
        }
      }
      
      this.el.innerHTML = output;
      if (complete === this.queue.length) {
        this.resolve();
      } else {
        this.frameRequest = requestAnimationFrame(this.update);
        this.frame++;
      }
    }
  }
  
  // Character interface
  const characters = ref([]);
  const activeIndices = ref(new Set());
  const titleElement = ref(null);
  let scrambler = null;
  let animationFrameId = null;
  
  // Create initial characters
  const createCharacters = () => {
    const allChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?";
    const charCount = 300;
    const newCharacters = [];
  
    for (let i = 0; i < charCount; i++) {
      newCharacters.push({
        char: allChars[Math.floor(Math.random() * allChars.length)],
        x: Math.random() * 100,
        y: Math.random() * 100,
        speed: 0.1 + Math.random() * 0.3,
      });
    }
  
    return newCharacters;
  };
  
  // Initialize scrambler for title
  const initScrambler = () => {
    if (titleElement.value && !scrambler) {
      scrambler = new TextScramble(titleElement.value);
      
      const phrases = [
        '在这里...',
        '记录时光',
        '找寻自我',
        '铭记...',
        '有意义的瞬间',
        '很难忘的时刻'
      ];
      
      let counter = 0;
      const next = () => {
        if (scrambler) {
          scrambler.setText(phrases[counter]).then(() => {
            setTimeout(next, 2000);
          });
          counter = (counter + 1) % phrases.length;
        }
      };
  
      next();
    }
  };
  
  // Update character positions
  const updatePositions = () => {
    characters.value = characters.value.map(char => ({
      ...char,
      y: char.y + char.speed,
      ...(char.y >= 100 && {
        y: -5,
        x: Math.random() * 100,
        char: "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"[
          Math.floor(Math.random() * "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?".length)
        ],
      }),
    }));
    
    animationFrameId = requestAnimationFrame(updatePositions);
  };
  
  // Update active indices for flicker effect
  const updateActiveIndices = () => {
    const newActiveIndices = new Set();
    const numActive = Math.floor(Math.random() * 3) + 3;
    for (let i = 0; i < numActive; i++) {
      newActiveIndices.add(Math.floor(Math.random() * characters.value.length));
    }
    activeIndices.value = newActiveIndices;
  };
  
  let flickerInterval = null;
  
  onMounted(() => {
    characters.value = createCharacters();
    initScrambler();
    
    // Start animation
    animationFrameId = requestAnimationFrame(updatePositions);
    
    // Start flicker effect
    flickerInterval = setInterval(updateActiveIndices, 50);
  });
  
  onBeforeUnmount(() => {
    if (animationFrameId) {
      cancelAnimationFrame(animationFrameId);
    }
    
    if (flickerInterval) {
      clearInterval(flickerInterval);
    }
  });
  </script>
  
  <style>
  .raining-container {
    position: relative;
    width: 100%;
    height: 100vh;
    background-color: black;
    overflow: hidden;
  }
  
  .title-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 20;
  }
  
  .scrambled-title {
    color: white;
    font-size: 3.75rem;
    font-weight: bold;
    letter-spacing: 0.05em;
    justify-content: center;
    font-family: monospace;
  }
  
  .character {
    position: absolute;
    font-size: 1.8rem;
    transform: translate(-50%, -50%);
    transition: color 0.1s, transform 0.1s, text-shadow 0.1s;
    will-change: transform, top;
  }
  
  .character-inactive {
    color: #64748b;
    font-weight: 300;
    opacity: 0.4;
    transform: translate(-50%, -50%) scale(1);
    text-shadow: none;
  }
  
  .character-active {
    color: #00ff00;
    font-size: 1.25rem;
    font-weight: bold;
    transform: translate(-50%, -50%) scale(1.25);
    z-index: 10;
    opacity: 1;
    text-shadow: 0 0 8px rgba(255,255,255,0.8), 0 0 12px rgba(255,255,255,0.4);
    animation: pulse 1s infinite;
  }
  
  .dud {
    color: #0f0;
    opacity: 0.7;
  }
  
  @keyframes pulse {
    0%, 100% {
      opacity: 1;
    }
    50% {
      opacity: 0.8;
    }
  }
  </style>