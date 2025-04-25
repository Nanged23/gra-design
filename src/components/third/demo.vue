<template>
  <div class="all">
    <h1>WebSocket 示例</h1>
    <button @click="sendMessage">发送消息</button>
    <p>收到消息: {{ message }}</p>
  </div>
</template>
<style>
.all {
  margin-left: 250px;
}
</style>
<script>
import socket from '@/socket/socket.js';

export default {
  name: 'SocketDemo',
  data() {
    return {
      message: '',
    };
  },
  mounted() {
    // 监听后端发送的事件
     
  },
  methods: {
    sendMessage() {
      // 向后端发送事件
      socket.emit('message', 'Hello from Vue!');
    },
  },
  beforeDestroy() {
    // 清理监听器，避免内存泄漏
    socket.off('connect');
    socket.off('disconnect');
    socket.off('message');
  },
};
</script>