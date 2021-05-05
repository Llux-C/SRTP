<template>
<div>
    <div class="logo">
        <img src="@/assets/logo.png">
    </div>
    <a-menu
        theme="light"
        mode="horizontal"
        :default-selected-keys="['1']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1" @click="goTo('/home')">
            <a-icon type="home" />
          首页
        </a-menu-item>
        <a-menu-item key="2" @click="goTo('/check')">
            <a-icon type="line-chart" />
          数据查看
        </a-menu-item>
        <a-menu-item key="3" @click="goTo('/calculate')">
            <a-icon type="calculator" />
          数据填充
        </a-menu-item>
      </a-menu>

    
</div>
</template>
<style scoped>
.logo{
    width: 120px;
    height: 32px;
    margin: 16px 24px 16px 24px;
    float: left;
}.logo img  {
        max-width: 100%;
        max-height: 100%;
        display: block;
        margin: auto;
    }
</style>

<script>
export default {
  data() {
    return {

    };
  },
  methods:{
      goTo(path){
          this.$router.push(path);
      },
  }
};
</script>
