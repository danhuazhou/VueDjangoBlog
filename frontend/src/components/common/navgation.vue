<template>
  <div class="aaa">
    <nav-item path="home" colorstyle="blue">
      <span class="iconfont" slot="font-image"></span>
      <div slot="font">首页</div>
    </nav-item>

    <nav-item path="classify" colorstyle="green">
      <span class="iconfont" slot="font-image"></span>
      <div slot="font">分类</div>
    </nav-item>

    <nav-item path="shopping" colorstyle="hotpink">
      <span class="iconfont" slot="font-image"></span>
      <div slot="font">购物车</div>
    </nav-item>

    <nav-item path="profile">
      <span class="iconfont" slot="font-image"></span>
      <div slot="font">我的</div>
    </nav-item>
  </div>
</template>

<script>
  import navItem from "./nav-item"

  export default {
    name: "navgative",
    components: {
      navItem
    }
  }
</script>

<style scoped>
  /*@import "../assets/images/style.css";*/

  /*@font-face {*/
    /*font-family: 'iconfont';*/
    /*src: url('../assets/images/fonts/icomoon.eot');*/
    /*src: url('../assets/images/fonts/icomoon.eot?#iefix') format('embedded-opentype'),*/
    /*url('../assets/images/fonts/icomoon.woff') format('woff'),*/
    /*url('../assets/images/fonts/icomoon.ttf') format('truetype'),*/
    /*url('../assets/images/fonts/icomoon.svg#iconfont') format('svg');*/
  /*}*/

  .iconfont {
    font-family: "iconfont" !important;
    font-size: 16px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.2px;
    -moz-osx-font-smoothing: grayscale;
    /*vertical-align: middle;*/
  }

  .aaa {
    display: flex;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
  }
</style>

