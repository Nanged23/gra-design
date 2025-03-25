<template>
    <div class="modal-overlay">
      <div class="modal-backdrop" @click="$emit('close')"></div>
      
      <div class="modal-container">
        <button class="close-button" @click="$emit('close')">
          <X class="close-icon" />
        </button>
        
        <div class="profile-header">
          <div class="avatar-container">
            <img :src="userData.avatar" :alt="userData.name" class="avatar-img" />
          </div>
          
          <h2 class="user-name">{{ userData.name }}</h2>
          <div class="location-badge">{{ userData.location }}</div>
          <p class="user-signature">"{{ userData.signature }}"</p>
          
          <div class="stats-grid">
            <div class="stat-card">
              <p class="stat-value">{{ userData.booksRead }}</p>
              <p class="stat-label">已读书籍</p>
            </div>
            <div class="stat-card">
              <p class="stat-value">{{ userData.readingTime }}</p>
              <p class="stat-label">阅读时长</p>
            </div>
            <div class="stat-card">
              <p class="stat-value">{{ userData.notes }}</p>
              <p class="stat-label">笔记数量</p>
            </div>
          </div>
        </div>
        
        <div class="profile-footer">
          <h3 class="section-title">阅读统计</h3>
          <div class="progress-container">
            <div class="progress-item">
              <div class="progress-header">
                <span class="progress-label">本周阅读</span>
                <span class="progress-value">4小时32分钟</span>
              </div>
              <div class="progress-bar">
                <div class="progress-fill weekly"></div>
              </div>
            </div>
            <div class="progress-item">
              <div class="progress-header">
                <span class="progress-label">完成进度</span>
                <span class="progress-value">75%</span>
              </div>
              <div class="progress-bar">
                <div class="progress-fill completion"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import {X}from 'lucide-vue-next'
  defineProps({
    userData: {
      type: Object,
      required: true
    }
  });
  
  defineEmits(['close']);
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    inset: 0;
    z-index: 50;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
  }
  
  .modal-backdrop {
    position: absolute;
    inset: 0;
    background-color: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
  }
  
  .modal-container {
    position: relative;
    width: 100%;
    max-width: 28rem;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.05));
    backdrop-filter: blur(1rem);
    border-radius: 1rem;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  }
  
  .close-button {
    position: absolute;
    right: 1rem;
    top: 1rem;
    padding: 0.5rem;
    border-radius: 9999px;
    background-color: rgba(0, 0, 0, 0.2);
    color: white;
    transition: background-color 0.2s;
  }
  
  .close-button:hover {
    background-color: rgba(0, 0, 0, 0.3);
  }
  
  .close-icon {
    width: 1.25rem;
    height: 1.25rem;
  }
  
  .profile-header {
    padding: 2.5rem 1.5rem 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .avatar-container {
    position: relative;
    width: 6rem;
    height: 6rem;
    border-radius: 9999px;
    overflow: hidden;
    border: 4px solid rgba(255, 255, 255, 0.2);
    margin-bottom: 1rem;
  }
  
  .avatar-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .user-name {
    font-size: 1.5rem;
    font-weight: 600;
    color: white;
    margin-bottom: 0.25rem;
  }
  
  .location-badge {
    font-size: 0.875rem;
    background-color: rgba(255, 255, 255, 0.2);
    padding: 0 0.5rem;
    border-radius: 9999px;
    color: rgba(255, 255, 255, 0.8);
    margin-bottom: 0.5rem;
  }
  
  .user-signature {
    color: rgba(255, 255, 255, 0.7);
    margin-bottom: 1.5rem;
    text-align: center;
  }
  
  .stats-grid {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    text-align: center;
  }
  
  .stat-card {
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 0.75rem;
    padding: 1rem;
  }
  
  .stat-value {
    font-size: 1.5rem;
    font-weight: 600;
    color: white;
  }
  
  .stat-label {
    color: rgba(255, 255, 255, 0.7);
    font-size: 0.875rem;
  }
  
  .profile-footer {
    background-color: rgba(255, 255, 255, 0.05);
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding: 1.5rem;
  }
  
  .section-title {
    font-size: 1.125rem;
    font-weight: 500;
    color: white;
    margin-bottom: 1rem;
  }
  
  .progress-container {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .progress-item {
    margin-bottom: 0.5rem;
  }
  
  .progress-header {
    display: flex;
    justify-content: space-between;
    font-size: 0.875rem;
    margin-bottom: 0.25rem;
  }
  
  .progress-label {
    color: rgba(255, 255, 255, 0.7);
  }
  
  .progress-value {
    color: white;
  }
  
  .progress-bar {
    height: 0.5rem;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 9999px;
    overflow: hidden;
  }
  
  .progress-fill {
    height: 100%;
  }
  
  .progress-fill.weekly {
    width: 65%;
    background: linear-gradient(to right, #2dd4bf, #0ea5e9);
  }
  
  .progress-fill.completion {
    width: 75%;
    background: linear-gradient(to right, #a855f7, #ec4899);
  }
  </style>