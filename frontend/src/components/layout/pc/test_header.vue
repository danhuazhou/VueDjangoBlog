<template>
  <div class="header">
    <div class="logo cp" @click="routeToHome">Wise.Wrong</div>
    <div class="nav-wrapper">
      <router-link
        class="nav cp"
        v-for="(val,index) of navs"
        :key="`nav-`"
      >{{val.name}}}</router-link>
    </div>
  </div>
</template>

<script>
  export default {
    name: "test_header"
  }
</script>

<style scoped>

</style>
