<template>
  <div class="calculate" style="minHeight:calc(100vh - 139px)">
      <A1 />
  </div>
</template>

<script>

import A1 from '../components/A1'

export default {
  name: 'calculate',
  components: {
    'A1':A1,
  }
}
</script>

<style scoped>
.calculate{
  text-align: center;
  background-color: white;
}
</style>