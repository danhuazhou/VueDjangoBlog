<template>
  <div>
    <div class="nav">
      <slot></slot>   //插槽
    </div>
  </div>
</template>

<script>
  export default {
    name: "nav-bottom"
  }
</script>

<style scoped>
  .nav {
    display: flex;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #7b7b7b;
    height: 49px;
    text-align: center;
  }
</style>
