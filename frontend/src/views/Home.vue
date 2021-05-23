<template>
  <div class="home" style="minHeight:calc(100vh - 139px)">
    <a-carousel autoplay autoplaySpeed=200 style="">
      <!-- photo 1 -->
      <div>
        <a @click="goTo('/check')"><img src="../assets/1.jpg" /></a>
      </div>
      <!-- photo 2 -->
      <div>
        <a @click="goTo('/check')"><img src="../assets/2.jpg" /></a>
      </div>
    </a-carousel>

    <div class="home-body">
        <h1 class="h1">在线城市异构数据可视化系统</h1>
        <p class="text"> </p>
    </div>
  </div>
</template>



<script>
export default {
  name: 'Home',
  components: {
  },
  methods:{
    goTo(path){
          this.$router.push(path);
      }
  }
}
</script>

<style scoped>
.home{
  text-align: center;
  background-color: white;
}

.text{
  font-size: 16px;
}

.h1{
  margin-top: 30px;
  font-size: 30px;
}

.home-body{
  padding: 0 50px;
}

.ant-carousel >>> .slick-slide {
  text-align: center;
  overflow: hidden;
}

.ant-carousel >>> .slick-slide img {
  display: block;
  margin: auto;
  max-width: 100%;
}

</style>