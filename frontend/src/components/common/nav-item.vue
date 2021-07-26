<template>
  <div class="nav-item" :class="{isactive:isactive}">
    <div @click="change">
      <slot name="font-image"></slot>  <--!显示字体图片-->
      <slot name="font"></slot>    <--!显示文字-->
    </div>
  </div>
</template>

<script>
  export default {
    name: "nav-item",
    props: {
      path :String  // 传递路径
    },
    computed: {
      isactive () {
        return this.$route.path.indexOf(this.path) !== -1
      }
    },
    methods: {
      change () {
        if (this.isactive===false) {
          this.$router.push(this.path)
        }

      }
    }
  }
</script>

<style scoped>
  .nav-item {
    flex: 1;
  }
  .isactive {
    color: red;
  }
</style>
