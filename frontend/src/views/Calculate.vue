<template>
  <div class="calculate" style="minHeight:calc(100vh - 139px);margin:10px;padding:20px">
      <a-row style="minHeight:300px">
          <a-col :span="12">
            <B1 />
          </a-col>
          <a-col :span="12">
            <B2 />
          </a-col>
      </a-row>
  </div>
</template>

<script>
import B1 from '../components/B1'
import B2 from '../components/B2'

export default{
    name: 'calculate',
    components: {
        'B1':B1,
        'B2':B2,
  }
}
</script>


<style scoped>
.calculate{
  background-color: white;
}
</style>