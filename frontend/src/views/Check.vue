<template>
  <div class="check" style="minHeight:calc(100vh - 139px);margin:10px;padding:20px">
      <a-row style="minHeight:300px">
          <a-col :span="12">
            <A1 />
          </a-col>
          <a-col :span="12">
            <A2 />
          </a-col>
      </a-row>
      <a-row>
          <A3 />
      </a-row>
  </div>
</template>

<script>
import A1 from '../components/A1'
import A2 from '../components/A2'
import A3 from '../components/A3'

export default{
    name: 'check',
    components: {
        'A1':A1,
        'A2':A2,
        'A3':A3,
  }
}
</script>


<style scoped>
.check{
  background-color: white;
}
</style>