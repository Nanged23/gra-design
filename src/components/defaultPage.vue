<template>
  <div class="card-container">
    <div
      ref="containerRef"
      @mouseenter="handleMouseEnter"
      @mousemove="handleMouseMove"
      @mouseleave="handleMouseLeave"
      class="card-wrapper"
    >
      <div class="card-body">
        <div 
          ref="titleRef" 
          class="card-title"
          :style="getItemStyle(50)"
        >
          Make things float in air
        </div>
        
        <p 
          ref="descriptionRef" 
          class="card-description"
          :style="getItemStyle(60)"
        >
          Hover over this card to unleash the power of CSS perspective
        </p>
        
        <div 
          ref="imageContainerRef" 
          class="card-image-container"
          :style="getItemStyle(100)"
        >
          <img
            src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=2560&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            class="card-image"
            alt="thumbnail"
          />
        </div>
        
        <div class="card-footer">
          <a
            ref="tryNowRef"
            href="https://twitter.com/mannupaaji"
            target="_blank"
            class="try-now-link"
            :style="getItemStyle(20)"
          >
            Try now →
          </a>
          
          <button
            ref="signUpRef"
            class="sign-up-button"
            :style="getItemStyle(20)"
          >
            Sign up
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';

// Refs for elements
const containerRef = ref(null);
const titleRef = ref(null);
const descriptionRef = ref(null);
const imageContainerRef = ref(null);
const tryNowRef = ref(null);
const signUpRef = ref(null);

// State
const isMouseEntered = ref(false);

// Methods
const handleMouseMove = (e) => {
  if (!containerRef.value) return;
  const { left, top, width, height } = containerRef.value.getBoundingClientRect();
  const x = (e.clientX - left - width / 2) / 25;
  const y = (e.clientY - top - height / 2) / 25;
  containerRef.value.style.transform = `rotateY(${x}deg) rotateX(${y}deg)`;
};

const handleMouseEnter = () => {
  isMouseEntered.value = true;
};

const handleMouseLeave = () => {
  if (!containerRef.value) return;
  isMouseEntered.value = false;
  containerRef.value.style.transform = `rotateY(0deg) rotateX(0deg)`;
};

// Helper function to get transform style for card items
const getItemStyle = (translateZ = 0, translateX = 0, translateY = 0, rotateX = 0, rotateY = 0, rotateZ = 0) => {
  if (isMouseEntered.value) {
    return {
      transform: `translateX(${translateX}px) translateY(${translateY}px) translateZ(${translateZ}px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) rotateZ(${rotateZ}deg)`
    };
  } else {
    return {
      transform: 'translateX(0px) translateY(0px) translateZ(0px) rotateX(0deg) rotateY(0deg) rotateZ(0deg)'
    };
  }
};

// Watch for mouse enter/leave to update card items
watch(isMouseEntered, () => {
  // Animation will be handled by the getItemStyle function
});
</script>

<style scoped>
/* Container styles */
.card-container {
  padding-top: 5rem;
  padding-bottom: 5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 1000px;
}

/* Card wrapper */
.card-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: all 200ms linear;
  transform-style: preserve-3d;
}

/* Card body */
.card-body {
  background-color: rgb(249, 250, 251);
  position: relative;
  width: auto;
  height: auto;
  border-radius: 0.75rem;
  padding: 1.5rem;
  border: 1px solid rgba(0, 0, 0, 0.1);
  height: 24rem;
  width: 24rem;
  transform-style: preserve-3d;
}

.card-body > * {
  transform-style: preserve-3d;
}

/* Dark mode styles */
.dark .card-body {
  background-color: black;
  border-color: rgba(255, 255, 255, 0.2);
}

.dark .card-body:hover {
  box-shadow: 0 25px 50px -12px rgba(16, 185, 129, 0.1);
}

/* Card title */
.card-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: rgb(82, 82, 91);
  width: fit-content;
  transition: duration-200 ease-linear;
}

.dark .card-title {
  color: white;
}

/* Card description */
.card-description {
  color: rgb(115, 115, 115);
  font-size: 0.875rem;
  max-width: 24rem;
  margin-top: 0.5rem;
  width: fit-content;
  transition: duration-200 ease-linear;
}

.dark .card-description {
  color: rgb(163, 163, 163);
}

/* Image container */
.card-image-container {
  width: 100%;
  margin-top: 1rem;
  transition: duration-200 ease-linear;
}

/* Card image */
.card-image {
  height: 15rem;
  width: 100%;
  object-fit: cover;
  border-radius: 0.75rem;
}

.group-hover\/card .card-image {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

/* Card footer */
.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 5rem;
}

/* Try now link */
.try-now-link {
  padding-left: 1rem;
  padding-right: 1rem;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  border-radius: 0.75rem;
  font-size: 0.75rem;
  font-weight: 400;
  width: fit-content;
  transition: duration-200 ease-linear;
}

.dark .try-now-link {
  color: white;
}

/* Sign up button */
.sign-up-button {
  padding-left: 1rem;
  padding-right: 1rem;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  border-radius: 0.75rem;
  background-color: black;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  width: fit-content;
  transition: duration-200 ease-linear;
}

.dark .sign-up-button {
  background-color: white;
  color: black;
}

/* Responsive styles */
@media (min-width: 640px) {
  .card-body {
    width: 30rem;
  }
}

/* Utility classes */
.dark {
  color-scheme: dark;
}
</style>