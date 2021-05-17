<template>
  <div class="home" style="minHeight:calc(100vh - 139px)">
    <a-carousel autoplay autoplaySpeed=200>
      <!-- photo 1 -->
      <div>
        <!-- <a-button ghost  :size="large" style="position:absolute; left:18%; top:60%;" >立即体验</a-button> -->
        <a @click="goTo('/login')"><img src="" /></a>
      </div>
      <!-- photo 2 -->
      <div>
        <!-- <a-button ghost  :size="large" style="position:absolute; left:18%; top:60%;" >立即体验</a-button> -->
        <a @click="goTo('/login')"><img src="" /></a>
      </div>
    </a-carousel>
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

.g-div{
  width:50%;
  height:100%;
  float:right;
  min-width:320px;
  min-height:180px;
}

.graph{
  width:80%;
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