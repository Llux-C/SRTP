<template>
  <div class="check" style="minHeight:calc(100vh - 139px)">
      <a-row style="minHeight:300px">
          <a-col :span="12">
            <A1 />
          </a-col>
          <a-col :span="12">
            <A2 />
          </a-col>
      </a-row>
  </div>
</template>

<script>
import A1 from '../components/A1'
import A2 from '../components/A2'

export default{
    name: 'calculate',
    components: {
        'A1':A1,
        'A2':A2,
  }
}
</script>


<style scoped>
.check{
  background-color: white;
}
</style>