<template>
  <header id="header" class="app-header navbar box-shadow-bottom-lg" role="menu">
    <!-- navbar header（交集处） -->
    <div class="text-ellipsis navbar-header bg-white">
      <button class="pull-right visible-xs" ui-toggle-class="show animated animated-lento fadeIn"
              target=".navbar-collapse">
        <span class="menu-icons"><i data-feather="search"></i></span>
      </button>
      <button class="pull-left visible-xs" ui-toggle-class="off-screen animated" target=".app-aside" ui-scroll="app">
        <span class="menu-icons"><i data-feather="menu"></i></span>
      </button>
      <!-- brand -->
      <a href="https://www.ihewro.com/" class="navbar-brand text-lt">
        <span id="navbar-brand-day">
                            <img src="static/picture/logo.svg" type="image/svg+xml"
                                 style="width: 130px;height: 40px;margin-top: -18px;max-height: 40px;"/>                    </span>
        <span id="navbar-brand-dark" class="hide"> <img src="static/picture/logo_dark.svg" type="image/svg+xml"
                                                        style="width: 130px;height: 40px;margin-top: -18px;max-height: 40px;"/></span>
      </a>
      <!-- / brand -->
    </div>
    <!-- / navbar header -->

    <!-- navbar collapse（顶部导航栏） -->
    <div class="collapse pos-rlt navbar-collapse bg-white">
      <!-- statitic info-->
      <ul class="nav navbar-nav hidden-sm">
        <li class="dropdown pos-stc">
          <a id="statistic_pane" data-status="false" href="#" data-toggle="dropdown"
             class="dropdown-toggle feathericons dropdown-toggle"
             aria-expanded="false">
            <i data-feather="pie-chart"></i>
            <span class="caret"></span>
          </a>
          <div class="dropdown-menu wrapper w-full bg-white">
            <div class="row">
              <div class="col-sm-8 b-l b-light">
                <div class="m-l-xs m-t-xs m-b-sm font-bold">动态日历<span class="info-icons"><i
                  data-feather="info"
                  data-toggle="tooltip" title="统计近10个月的文章和作者评论数目"></i>
                            </span></div>
                <div class="text-center">
                  <nav class="loading-echart text-center m-t-lg m-b-lg">
                    <p class="infinite-scroll-request"><i class="animate-spin fontello fontello-refresh"></i>Loading...
                    </p>
                  </nav>
                  <div id="post-calendar" class="top-echart hide"></div>
                </div>
              </div>
              <div class="col-sm-4 b-l b-light">
                <div class="m-l-xs m-t-xs m-b-sm font-bold">分类雷达图</div>
                <div class="text-center">
                  <nav class="loading-echart text-center m-t-lg m-b-lg">
                    <p class="infinite-scroll-request"><i class="animate-spin fontello fontello-refresh"></i>Loading...
                    </p>
                  </nav>
                  <div id="category-radar" class="top-echart hide"></div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-sm-4 b-l b-light">
                <div class="m-l-xs m-t-xs m-b-sm font-bold">发布统计图</div>
                <div class="text-center">
                  <nav class="loading-echart text-center m-t-lg m-b-lg">
                    <p class="infinite-scroll-request"><i class="animate-spin fontello fontello-refresh"></i>Loading...
                    </p>
                  </nav>
                  <div id="posts-chart" class="top-echart hide"></div>
                </div>
              </div>
              <div class="col-sm-4 b-l b-light">
                <div class="m-l-xs m-t-xs m-b-sm font-bold">分类统计图</div>
                <div class="text-center">
                  <nav class="loading-echart text-center m-t-lg m-b-lg">
                    <p class="infinite-scroll-request"><i class="animate-spin fontello fontello-refresh"></i>Loading...
                    </p>
                  </nav>
                  <div id="categories-chart" class="top-echart hide"></div>
                </div>
              </div>
              <div class="col-sm-4 b-l b-light">
                <div class="m-l-xs m-t-xs m-b-sm font-bold">标签统计图</div>
                <div class="text-center">
                  <nav class="loading-echart text-center m-t-lg m-b-lg">
                    <p class="infinite-scroll-request"><i class="animate-spin fontello fontello-refresh"></i>Loading...
                    </p>
                  </nav>
                  <div id="tags-chart" class="top-echart hide"></div>
                </div>
              </div>
            </div>
          </div>
        </li>
      </ul>

      <!-- search form -->

      <form id="searchform1" class="searchform navbar-form navbar-form-sm navbar-left shift" method="post"
            role="search">
        <div class="form-group">
          <div class="input-group rounded bg-white-pure box-shadow-wrap-normal">
            <input autocomplete="off" id="search_input" type="search" name="s"
                   class="transparent rounded form-control input-sm no-borders padder" required placeholder="输入关键词搜索…">
            <!--搜索提示-->
            <ul id="search_tips_drop" class="overflow-y-auto small-scroll-bar dropdown-menu hide" style="display:
                 block;top:
                30px; left: 0px;">
            </ul>
            <span id="search_submit" class="transparent input-group-btn">
                  <button type="submit" class="transparent btn btn-sm">
                      <span class="feathericons" id="icon-search"><i data-feather="search"></i></span>
                      <span class="feathericons animate-spin  hide" id="spin-search"><i
                        data-feather="loader"></i></span>
                    <!--                      <i class="fontello fontello-search" id="icon-search"></i>-->
                    <!--                      <i class="animate-spin  fontello fontello-spinner hide" id="spin-search"></i>-->
                  </button>
              </span>
          </div>
        </div>
      </form>
      <a href="" style="display: none" id="searchUrl"></a>
      <!-- / search form -->
      <ul class="nav navbar-nav navbar-right">
        <li class="music-box hidden-xs hidden-sm" id="handsome_global_player">
          <p class="handsomePlayer-tip-loading"><span></span> <span></span> <span></span> <span></span><span></span></p>
          <div class='handsome_aplayer player-global' data-preload="false" data-autoplay="" data-listMaxHeight="200px"
               data-order="list" data-theme="#8ea9a7" data-listFolded="true" data-fix_position="true">
            <div class="handsome_aplayer_music" data-id="2935464652" data-server="netease" data-type="playlist"
                 data-auth="3010f360a9aec9f6a0d37395e1102594"></div>
          </div>
        </li>
        <li class="dropdown hidden-xs hidden-sm"><a id="global_player_toggle" class="skPlayer-list-switch dropdown-toggle
            feathericons"><i
          data-feather="disc"></i><span class="visible-xs-inline"></span></a></li>
        <!--闲言碎语-->
        <li class="dropdown">
          <a href="#" data-toggle="dropdown" class="feathericons dropdown-toggle">
            <i data-feather="twitch"></i>
            <span class="visible-xs-inline">
              闲言碎语              </span>
            <span class="badge badge-sm up bg-danger pull-right-xs"></span>
          </a>
          <!-- dropdown -->
          <div class="dropdown-menu w-xl animated fadeInUp">
            <div class="panel bg-white">
              <div class="panel-heading b-light bg-light">
                <strong>
                  闲言碎语 </strong>
              </div>
              <div class="list-group" id="smallRecording">
                <a href="https://www.ihewro.com/cross.html" class="list-group-item"><span
                  class="clear block m-b-none words_contents">所以我的时间都去哪了  生活的琐碎中  慢慢消失<br><small class="text-muted">1 星期前</small></span></a><a
                href="https://www.ihewro.com/cross.html" class="list-group-item"><span
                class="clear block m-b-none words_contents">让子弹飞会 生活上理解是  有些烦人事 不管是工作还是生活 让子弹飞会  因为有可能 它没你想的那么重要  或者缓一会  能够理清思路 更加理智的去做  又或者这件事情就是很难或者无法解决  那干脆就放弃吧  不要钻牛角尖了<br><small
                class="text-muted">1 星期前</small></span></a><a href="https://www.ihewro.com/cross.html"
                                                              class="list-group-item"><span
                class="clear block m-b-none words_contents">此条为私密说说，仅发布者可见<br><small
                class="text-muted">1 星期前</small></span></a></div>
            </div>
          </div>
        </li>
        <!--/闲言碎语-->
        <!--登录管理-->
        <li class="dropdown" id="easyLogin">
          <a onclick="return false" data-toggle="dropdown" class="dropdown-toggle clear">
            <span class="feathericons"><i data-feather="key"></i></span>
            <b class="caret"></b><!--下三角符号-->
          </a>
          <!-- dropdown(已经登录) -->
          <div class="dropdown-menu w-lg wrapper bg-white animated fadeIn" aria-labelledby="navbar-login-dropdown">
            <form id="Login_form"
                  action="https://www.ihewro.com/index.php/action/login?_=14a288339ad09b0756bf9b95bec5bf59"
                  method="post">
              <div class="form-group">
                <label for="navbar-login-user">用户名</label>
                <input type="text" name="name" id="navbar-login-user" class="form-control" placeholder="用户名或电子邮箱"></div>
              <div class="form-group">
                <label for="navbar-login-password">密码</label>
                <input autocomplete type="password" name="password" id="navbar-login-password"
                       class="form-control" placeholder="密码"></div>
              <button style="width: 100%" type="submit" id="login-submit" name="submitLogin"
                      class="btn-rounded box-shadow-wrap-lg btn-gd-primary padder-lg">
                <span>登录</span>
                <span class="text-active">登录中...</span>
                <span class="banLogin_text">刷新页面后登录</span>
                <i class="animate-spin  fontello fontello-spinner hide" id="spin-login"></i>
                <i class="animate-spin fontello fontello-refresh hide" id="ban-login"></i>
              </button>
              <!--                            -->
              <input type="hidden" name="referer" value="https://www.ihewro.com/"></form>
          </div>
        </li>
        <!--/登录管理-->
      </ul>
    </div>
    <!-- / navbar collapse -->
  </header>
</template>

<script>
export default {
  name: 'navheader'
}
</script>

<style scoped>

</style>
