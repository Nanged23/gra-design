<!-- <style scoped>
.container {
  margin-left: 250px;
  display: flex;
  /* 使用flex布局 */
 
  /* 高度占满整个视窗 */
}
.logo {
  height: 30px;
  align-items: center;
}

.app_name {
  align-items: center;
}

.radio-input input {
  display: none;
}

.radio-input {
  height:150px;
  --container_width: 950px;
  position: relative;
  display: flex;
  align-items: center;
  border-radius: 10px;
  background-color: #212121;
  color: #eee;
  width: var(--container_width);
  overflow: hidden;
  border: 2px solid #fff;
}

.radio-input label {
  width: 100%;
  padding: 10px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1;
  font-weight: 600;
  letter-spacing: -1px;
  font-size: 14px;
}

.selection {
  display: none;
  position: absolute;
  height: 100%;
  width: calc(var(--container_width) / 3);
  z-index: 0;
  left: 0;
  top: 0;
  transition: 0.15s ease;
}

.radio-input label:nth-child(1):has(input:checked) {
  color: #fff;
}

.radio-input label:nth-child(2):has(input:checked) {
  color: #212121;
}

.radio-input label:nth-child(1):has(input:checked)~.selection {
  background-color: #153d5c;
  display: inline-block;
}

.radio-input label:nth-child(2):has(input:checked)~.selection {
  background-color: #8f8696;
  display: inline-block;
}

.radio-input label:nth-child(3):has(input:checked)~.selection {
  background-color: #234f2e;
  display: inline-block;
}

.radio-input label:nth-child(1):has(input:checked)~.selection {
  transform: translateX(calc(var(--container_width) * 0 / 3));
}

.radio-input label:nth-child(2):has(input:checked)~.selection {
  transform: translateX(calc(var(--container_width) * 1 / 3));
}

.radio-input label:nth-child(3):has(input:checked)~.selection {
  transform: translateX(calc(var(--container_width) * 2 / 3));
}
</style>

<template>
    <div class="container">
  <div class="radio-input">
    <label @click="navigateTo('third_weread')">
      <input type="radio" id="value-1" name="value-radio" value="1" />
      <div><img class="logo" src="../assets/微信读书.png">
        <div class="app_name">微信读书</div>
      </div>
    </label>
    <label  @click="navigateTo('third_keep')">
      <input type="radio" id="value-2" name="value-radio" value="2" />
      <div><img class="logo" src="../assets/Keep.png">
        <div class="app_name">Keep</div>
      </div>
    </label>
    <label @click="navigateTo('third_douban')">
      <input type="radio" id="value-3" name="value-radio" value="3" />
      <div><img class="logo" src="../assets/豆瓣.png">
        <div class="app_name">豆瓣</div>
      </div>
    </label>
    <span class="selection"></span>
  </div>
  <div class="content"> <router-view></router-view></div>
</div>
</template>
<script>
export default {
  data() {
    return {

    };
  },
  methods: {
    navigateTo(menu) {
      this.$router.push(`/${menu}`);
    }
  }

}
</script> -->
<template>
  
</template>