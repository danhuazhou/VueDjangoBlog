<template>

  <!--选择侧边栏的颜色-->
  <aside id="aside" class="app-aside hidden-xs bg-white">  <!--<aside>-->
    <div class="aside-wrap" layout="column">
      <div class="navi-wrap scroll-y scroll-hide" flex>
        <!-- user -->
        <div class="clearfix hidden-xs text-center hide  show" id="aside-user">
          <div class="dropdown wrapper ">
            <div ui-nav>
              <a href="https://www.ihewro.com/cross.html">
                            <span class="thumb-lg w-auto-folded avatar m-t-sm  ">
                  <img src="static/picture/863730882.jpg" class="img-full img-circle normal-shadow">
                </span>
              </a>
            </div>
            <a href="#" data-toggle="dropdown" class="dropdown-toggle hidden-folded  ">
                <span class="clear">
                  <span class="block m-t-sm">
                    <strong class="font-bold text-lt">月色真美</strong>
                    <b class="caret"></b>
                  </span>
                  <span class="text-muted text-xs block">认真生活。</span>
                </span>
            </a>
            <!-- dropdown -->
            <ul class="dropdown-menu animated fadeInRight w hidden-folded no-padder">
              <li class="wrapper b-b m-b-sm bg-info m-n">
                <span class="arrow top hidden-folded arrow-info"></span>
                <div>
                  <p>晚上好，注意早点休息</p>
                </div>
                <div class="progress progress-xs m-b-none dker">
                  <div class="progress-bar bg-white" data-toggle="tooltip" data-original-title="时间已经度过91.67%"
                       style="width: 91.67%"></div>
                </div>
              </li>
            </ul>
            <!-- / dropdown -->
          </div>
        </div>
        <!-- / user -->

        <!-- nav -->
        <nav ui-nav class="navi clearfix">
          <ul class="nav">
            <!--index-->
            <div class="line dk hidden-folded"></div>
            <li class="hidden-folded padder m-t m-b-sm text-muted text-xs">
              <span>导航</span>
            </li>
            <!--主页-->
            <li>
              <a href="https://www.ihewro.com/" class="auto">
                <span class="nav-icon"><i data-feather="home"></i></span>
                <span>首页</span>
              </a>
            </li>
            <!-- /主页 -->
            <li><a target="_self" href="https://www.ihewro.com/project.html"
                   class="auto"><span class="nav-icon"><i data-feather="github"></i></span><span>仓库</span></a></li>
            <li><a target="_self" href="https://www.ihewro.com/links.html"
                   class="auto"><span class="nav-icon"><i data-feather="heart"></i></span><span>朋友</span></a></li>
            <li><a target="_self" href="https://www.ihewro.com/category/image/"
                   class="auto"><span class="nav-icon"><i data-feather="image"></i></span><span>相册</span></a></li>
            <li><a target="_self" href="https://www.ihewro.com/category/diary/"
                   class="auto"><span class="nav-icon"><i data-feather="lock"></i></span><span>日记</span></a></li>
            <li><a target="_self" href="https://www.ihewro.com/archives.html"
                   class="auto"><span class="nav-icon"><i data-feather="archive"></i></span><span>归档</span></a></li>
            <li><a target="_self" href=""
                   class="auto"><span class="pull-right text-muted">
                    <i class="fontello icon-fw fontello-angle-right text"></i>
                    <i class="fontello icon-fw fontello-angle-down text-active"></i>
                  </span><span class="nav-icon"><i data-feather="coffee"></i></span><span>关于</span></a>
              <ul class="nav nav-sub dk">
                <li><a target="_self" href="https://www.ihewro.com/about.html"
                       class="auto"><span class="nav-icon"><i data-feather="coffee"></i></span><span>关于我</span></a></li>
                <li><a target="_self" href="https://www.ihewro.com/msg.html"
                       class="auto"><span class="nav-icon"><i data-feather="at-sign"></i></span><span>留言本</span></a>
                </li>
              </ul>
            </li>
            <li class="line dk"></li>
            <!--Components-->
            <li class="hidden-folded padder m-t m-b-sm text-muted text-xs">
              <span>组成</span>
            </li>
            <!--分类category-->
            <li>
              <a class="auto">
                  <span class="pull-right text-muted">
                    <i class="fontello icon-fw fontello-angle-right text"></i>
                    <i class="fontello icon-fw fontello-angle-down text-active"></i>
                  </span>
                <!--                  <i class="glyphicon glyphicon-th"></i>-->
                <span class="nav-icon"><i data-feather="grid"></i></span>

                <span>分类</span>
              </a>
              <ul class="nav nav-sub dk">
                <li class="nav-sub-header">
                  <a>
                    <span>分类</span>
                  </a>
                </li>
                <!--循环输出分类-->

                <li class="category-level-0 category-parent"><a href="https://www.ihewro.com/category/tech/"><b
                  class="badge pull-right">11</b>设计作品</a></li>
                <li class="category-level-0 category-parent"><a href="https://www.ihewro.com/category/share/"><b
                  class="badge pull-right">46</b>技巧杂烩</a></li>
                <li class="category-level-0 category-parent"><a href="https://www.ihewro.com/category/life/"><b
                  class="badge pull-right">99</b>生活随笔</a></li>
                <li class="category-level-0 category-parent"><a href="https://www.ihewro.com/category/null/"><b
                  class="badge pull-right">2</b>无处安放</a></li>
                <li class="category-level-0 category-parent"><a href="https://www.ihewro.com/category/diary/"><b
                  class="badge pull-right">2</b>日记心事</a></li>
                <li class="category-level-0 category-parent"><a class="auto"
                                                                href="https://www.ihewro.com/category/hobby/"><span
                  class="pull-right text-muted">
                    <i class="fontello icon-fw fontello-angle-right text"></i>
                    <i class="fontello icon-fw fontello-angle-down text-active"></i>
                  </span><span class="parent_name">兴趣爱好</span></a>
                  <ul class="nav nav-sub dk child-nav">
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/book/"><b class="badge pull-right">0</b>书评</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/movie/"><b class="badge pull-right">6</b>影评</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/music/"><b class="badge pull-right">2</b>乐评</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/hardware/"><b class="badge pull-right">3</b>硬件评测</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/software/"><b class="badge pull-right">3</b>软件评测</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/guitar/"><b class="badge pull-right">2</b>吉他学习</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/mystery/"><b class="badge pull-right">1</b>未能分类</a></li>
                  </ul>
                </li>
                <li class="category-level-0 category-parent"><a class="auto"
                                                                href="https://www.ihewro.com/category/wiki/"><span
                  class="pull-right text-muted">
                    <i class="fontello icon-fw fontello-angle-right text"></i>
                    <i class="fontello icon-fw fontello-angle-down text-active"></i>
                  </span><span class="parent_name">学习笔记</span></a>
                  <ul class="nav nav-sub dk child-nav">
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/c_plus/"><b class="badge pull-right">2</b>c++</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/java_back/"><b class="badge pull-right">2</b>java</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/php/"><b class="badge pull-right">2</b>php</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/front-end/"><b class="badge pull-right">12</b>web</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/git/"><b class="badge pull-right">1</b>git</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/acm/"><b class="badge pull-right">5</b>acm</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/python/"><b class="badge pull-right">2</b>python</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/android/"><b class="badge pull-right">2</b>android</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/typecho/"><b class="badge pull-right">13</b>typecho</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/database/"><b class="badge pull-right">1</b>数据库</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/server/"><b class="badge pull-right">5</b>服务器</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/data_structure/"><b class="badge pull-right">2</b>数据结构</a>
                    </li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/ai/"><b class="badge pull-right">2</b>人工智能</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/network/"><b class="badge pull-right">2</b>计算机网络</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/scalar/"><b class="badge pull-right">0</b>scalar</a></li>
                  </ul>
                </li>
                <li class="category-level-0 category-parent"><a class="auto"
                                                                href="https://www.ihewro.com/category/others/"><span
                  class="pull-right text-muted">
                    <i class="fontello icon-fw fontello-angle-right text"></i>
                    <i class="fontello icon-fw fontello-angle-down text-active"></i>
                  </span><span class="parent_name">都有明天</span></a>
                  <ul class="nav nav-sub dk child-nav">
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/just/"><b class="badge pull-right">1</b>胡言乱宇</a></li>
                    <li class="category-level-1 category-child category-level-odd"><a
                      href="https://www.ihewro.com/category/friday/"><b class="badge pull-right">0</b>阳光灿烂的日子</a></li>
                  </ul>
                </li>
                <li class="category-level-0 category-parent"><a href="https://www.ihewro.com/category/lock/"><b
                  class="badge pull-right">0</b>分类加密</a></li>
                <!--/循环输出分类-->

              </ul>
            </li>
            <!--独立页面pages-->
            <li>
              <a class="auto">
                  <span class="pull-right text-muted">
                    <i class="fontello icon-fw fontello-angle-right text"></i>
                    <i class="fontello icon-fw fontello-angle-down text-active"></i>
                  </span>
                <span class="nav-icon"><i data-feather="file"></i></span>
                <span>页面</span>
              </a>
              <ul class="nav nav-sub dk">
                <li class="nav-sub-header">
                  <a data-no-instant>
                    <span>页面</span>
                  </a>
                </li><!--这个字段不会被显示出来-->
                <!--循环输出独立页面-->
                <li><a href="https://www.ihewro.com/about.html"><span>关于我</span></a></li>
                <li><a href="https://www.ihewro.com/loves.html"><span>万花筒</span></a></li>
                <li><a href="https://www.ihewro.com/project.html"><span>实验室</span></a></li>
                <li><a href="https://www.ihewro.com/donate.html"><span>赞助我</span></a></li>
              </ul>
            </li>
            <!--友情链接-->
            <li>
              <a class="auto">
                  <span class="pull-right text-muted">
                    <i class="fontello icon-fw fontello-angle-right text"></i>
                    <i class="fontello icon-fw fontello-angle-down text-active"></i>
                  </span>
                <span class="nav-icon"><i data-feather="user"></i></span>
                <span>友链</span>
              </a>
              <ul class="nav nav-sub dk">
                <li class="nav-sub-header">
                  <a data-no-instant>
                    <span>友链</span>
                  </a>
                </li>
                <!--使用links插件，输出全站友链-->
                <li data-original-title="高一学生的搞事日常 " data-toggle="tooltip"
                    data-placement="top"><a rel='noopener' href="https://www.liaronce.com" target="_blank"><span>LiarOnce</span></a>
                </li>
                <li data-original-title="安静的做一个沉默中的分享、记录小站" data-toggle="tooltip"
                    data-placement="top"><a rel='noopener' href="https://www.mocurio.com/"
                                            target="_blank"><span>初夏阳光</span></a></li>
                <li data-original-title="热爱前端，喜欢编程，也会一些设计，知识杂而不精，善于折腾并乐此不疲。" data-toggle="tooltip"
                    data-placement="top"><a rel='noopener' href="https://biji.io" target="_blank"><span>设计笔记</span></a>
                </li>
                <li data-original-title="一举一动，都是承诺，会被另一个人看在眼里，记在心上的。
" data-toggle="tooltip"
                    data-placement="top"><a rel='noopener' href="https://www.moerats.com/" target="_blank"><span>Rat's Blog</span></a>
                </li>
                <li data-original-title="人若有志，万事可为！" data-toggle="tooltip"
                    data-placement="top"><a rel='noopener' href="https://www.rz.sb" target="_blank"><span>若志奕鑫的小站</span></a>
                </li>
                <li data-original-title="玺创建筑装饰工程（北京）有限公司" data-toggle="tooltip"
                    data-placement="top"><a rel='noopener' href="http://www.xichuang-china.com/" target="_blank"><span>玺创建筑</span></a>
                </li>
              </ul>
            </li>
          </ul>
        </nav>
        <!-- nav -->
      </div>
      <!--end of .navi-wrap-->
      <!--left_footer-->
      <div id="left_footer" class="footer wrapper-xs text-center nav-xs lt">

        <div class="col-xs-4 no-padder">
          <a target="_blank" class="tinav" href="https://www.ihewro.com/admin/" title="" data-toggle="tooltip"
             data-placement="top" data-original-title="后台管理">
            <span class="left-bottom-icons block"><i data-feather="settings"></i></span>
            <small class="text-muted">管理</small>
          </a>
        </div>
        <div class="col-xs-4 no-padder">
          <a target="_blank" class="tinav" href="https://www.ihewro.com/feed/" title=""
             data-toggle="tooltip" data-placement="top" data-original-title="文章RSS订阅">
            <span class="left-bottom-icons block"><i data-feather="rss"></i></span>
            <small class="text-muted">文章</small>
          </a>
        </div>
        <div class="col-xs-4 no-padder">
          <a target="_blank" href="https://www.ihewro.com/feed/comments/" title=""
             data-toggle="tooltip" data-placement="top" data-original-title="评论RSS订阅">
            <span class="left-bottom-icons block"><i data-feather="message-square"></i></span>
            <small class="text-muted">评论</small>
          </a>
        </div>
      </div>

    </div><!--.aside-wrap-->
  </aside>
</template>

<script>
export default {
  name: 'navaside'
}
</script>

<style scoped>

</style>
