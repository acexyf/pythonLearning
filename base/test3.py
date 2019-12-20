from pyquery import PyQuery as pq

html = '''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>人人电影网 迅雷下载 百度云资源</title>
<meta name="description" content="人人电影网是国内最优秀的电影迅雷下载、百度云资源网站，免费提供电影、韩剧、美剧、日剧资源，你想看的片片，这里都有。" />
<meta name="keywords" content="人人电影网 迅雷下载 百度云资源" />


<meta name="viewport" content="width=device-width, initial-scale=1">

<link rel="stylesheet" href="/static/css/pure-min.css">

<link rel="stylesheet" href="/static/css/grids-responsive-min.css">

<link href="/static/css/app.css" rel="stylesheet" type="text/css">
<link href="/static/css/iconfont.css" rel="stylesheet" type="text/css">
<script src="/static/js/jquery.min.js" type="text/javascript"></script>
<script src="/static/js/jquery.cookie.min.js" type="text/javascript"></script>
<script src="/static/js/jquery.lazyload.min.js" type="text/javascript"></script>
<style>
body {/*background: url(/static/images/a561b538ly1fgzuu34f4nj21jk0m8dok.jpg) repeat-x fixed center top;*/color: #333;}
</style>
<script src="/static/js/jquery.easing.min.js" type="text/javascript"></script>
<script src="/static/js/jquery.easing.compatibility.min.js" type="text/javascript"></script>
</head>
<body>
<!--头部开始-->
<!-- member -->

<script language="javascript" type="text/javascript" src="/include/dedeajax2.js"></script>

<script language="javascript" type="text/javascript">

function CheckLogin(){

    var taget_obj = document.getElementById('_userlogin');

    myajax = new DedeAjax(taget_obj,false,false,'','','');

    myajax.SendGet2("/member/ajax_loginsta.php");

    DedeXHTTP = null;

  }

</script>

<!-- member --end-->







<script>



var _hmt = _hmt || [];



(function() {



  var hm = document.createElement("script");



  hm.src = " https://hm.baidu.com/hm.js?4c18eb2a34373fa783fa1713d0697753 ";



  var s = document.getElementsByTagName("script")[0]; 



  s.parentNode.insertBefore(hm, s);



})();



</script>



<div id="top" class="top" style="height: auto;">



    <div class="clearfix">



        <div class="float-left">



            <a href="/" class="logo"><img src="/static/picture/logo.png" height="22px"></a>



        </div>





<style type="text/css">

.top form{float: left;}

</style>

        



        <div class="topbar-user float-right">





<!-- 会员登陆 -->

<style type="text/css">

.huiyuan{float: right;}

</style>

              <div class="huiyuan" style="display:none;">

              

                <div id="_userlogin">

   [<a title="登录" href="/member/login.php">登录</a>] [<a title="注册" href="/member/index_do.php?fmdo=user&dopost=regnew">注册</a>]

     <script language="javascript" type="text/javascript">CheckLogin();</script>

</div>

              </div>

<!-- 会员登陆--end -->







            <form class="pure-form" action="/plus/search.php" target="_blank">



                <input type="text"  name="q" class="search-box"   placeholder="电影 / 电视剧" style="color: #000;">



                <input type="hidden" name="pagesize" value="10" />



                <button type="submit" name="submit"  class="pure-button pure-button-primary">搜索</button>



            </form>











        </div>







        <div class="topbar-search float-right small-show">



            <a href="/plus/search.php?q=NULL" class="top-search"><i class="icon iconfont icon-search"></i></a>



        </div>











        <div class="clear"></div>



        <div class="float-left" style="  line-height: 46px;">



<a href="/">首页</a>



            



            <a href="/movie/">电影</a>



           



            <a href="/dianshiju/">电视剧</a>



           



            <a href="/zongyi/">综艺</a>



           



            <a href="/dongman/">动漫</a>



           



            <a href="/plus/list.php?tid=2&splxa=News">预告</a>



           



        </div>



        



    </div>



</div>



<style>



.clear{ clear:both;}



@media screen and (min-width: 1201px) { 



.float-left a{color: #fff;font-size:20px; padding:0 10px;}



} 



@media screen and (max-width: 1200px) { 



.float-left{ float:left; margin-left:10px;}



.float-left a{color: #fff;font-size:14px; margin-right:20px;}



} 



@media screen and (max-width: 400px) { 



.float-left{ float:left; margin-left:10px;}



.float-left a{color: #fff;font-size:14px; margin-right:10px;}



} 



</style>



<script>



    function dropdown(handle, entity) {



        var flag = 1;



        var topmore = $(handle);



        var listmore = $(entity);



        topmore.mouseenter(function(){



            listmore.show();



        }).mouseleave(function(){



            setTimeout(function(){



                if(flag){



                    listmore.hide();



                }



            },100);



        });



        listmore.mouseleave(function(){



            listmore.hide();



            flag = 1;



        }).mouseenter(function(){



            flag = 0;



        });



    }



    dropdown('#topmore', '.top-more');



    dropdown('#tophead', '.top-head');



    </script>




<!--头部结束-->


<!--导航下的广告-->
<style>
	.adv-1{
		border-left: 25px solid rgba(255,255,255,0.2);
		border-right: 25px solid rgba(255,255,255,0.2);
		border-top: 10px solid rgba(255,255,255,0.2);
		border-bottom: 10px solid rgba(255,255,255,0.2);
	}
	.adv_f{
		position: fixed;
		bottom: 0px;
		width: 100%;
		z-index:999999;
		display:none;
	}
	.adv_f img{
		width:100%;
	}
	@media  screen and (max-width: 768px) ,screen and (max-device-width: 768px){ 
		.adv-1{
			display:none;
		}
		.adv_f{
			display:none;
		}
	}
</style>
<div class="adv-1" style="width:950px;height:90px;margin:10px auto;position: relative;display: none;">


<a class="close-adv1" href="javascript:void(0)" style="position: absolute;width: 20px;height: 20px;background: #fff;right: 0px;top: 2px;font-size: 24px;text-align: center;line-height: 16px;">x</a>
</div>
<script>
   $('.close-adv1').click(function(){
	$('.adv-1').css('display','none');
});
</script>

<div class="adv_f">

</div>
<!--结束-->
<style>
@media screen and (min-width: 1201px) { 
.nrtop { margin-top:60px;} 
}
@media screen and (max-width: 1200px) { 
.nrtop { margin-top:20px;} 
}  
</style>
<div class="wrapper masking nrtop">
	<div class="pure-g">
		<div class="pure-u-1 pure-u-md-17-24">
			<div class="pure-g filter">
				<div class="pure-u-sm-3-5 pure-u-1-3"><i style="color:#ccc">筛选：</i></div>
				<div class="pure-u-sm-1-5 pure-u-1-3"></div>
				<div class="pure-u-sm-1-5 pure-u-1-3">
					<div class="condition text-right">
						<a class="drop-down" href="###">按类型</a>
						<div class="drop-down-menu shadow"><a style="float: left;
    display: block; width: 80px;  height: 24px;  line-height: 24px;  padding: 3px 0;    font-weight: bold;   color: #EB444C;  text-align: center;">全部</a><a class="transition" title="剧情" href="/plus/list.php?tid=2&splxa=%E5%89%A7%E6%83%85">剧情</a><a class="transition" title="喜剧" href="/plus/list.php?tid=2&splxa=%E5%96%9C%E5%89%A7">喜剧</a><a class="transition" title="惊悚" href="/plus/list.php?tid=2&splxa=%E6%83%8A%E6%82%9A">惊悚</a><a class="transition" title="动作" href="/plus/list.php?tid=2&splxa=%E5%8A%A8%E4%BD%9C">动作</a><a class="transition" title="爱情" href="/plus/list.php?tid=2&splxa=%E7%88%B1%E6%83%85">爱情</a><a class="transition" title="犯罪" href="/plus/list.php?tid=2&splxa=%E7%8A%AF%E7%BD%AA">犯罪</a><a class="transition" title="恐怖" href="/plus/list.php?tid=2&splxa=%E6%81%90%E6%80%96">恐怖</a><a class="transition" title="冒险" href="/plus/list.php?tid=2&splxa=%E5%86%92%E9%99%A9">冒险</a><a class="transition" title="悬疑" href="/plus/list.php?tid=2&splxa=%E6%82%AC%E7%96%91">悬疑</a><a class="transition" title="科幻" href="/plus/list.php?tid=2&splxa=%E7%A7%91%E5%B9%BB">科幻</a><a class="transition" title="奇幻" href="/plus/list.php?tid=2&splxa=%E5%A5%87%E5%B9%BB">奇幻</a><a class="transition" title="家庭" href="/plus/list.php?tid=2&splxa=%E5%AE%B6%E5%BA%AD">家庭</a><a class="transition" title="动画" href="/plus/list.php?tid=2&splxa=%E5%8A%A8%E7%94%BB">动画</a><a class="transition" title="纪录片" href="/plus/list.php?tid=2&splxa=%E7%BA%AA%E5%BD%95%E7%89%87">纪录片</a><a class="transition" title="战争" href="/plus/list.php?tid=2&splxa=%E6%88%98%E4%BA%89">战争</a><a class="transition" title="历史" href="/plus/list.php?tid=2&splxa=%E5%8E%86%E5%8F%B2">历史</a><a class="transition" title="传记" href="/plus/list.php?tid=2&splxa=%E4%BC%A0%E8%AE%B0">传记</a><a class="transition" title="音乐" href="/plus/list.php?tid=2&splxa=%E9%9F%B3%E4%B9%90">音乐</a><a class="transition" title="运动" href="/plus/list.php?tid=2&splxa=%E8%BF%90%E5%8A%A8">运动</a><a class="transition" title="歌舞" href="/plus/list.php?tid=2&splxa=%E6%AD%8C%E8%88%9E">歌舞</a><a class="transition" title="西部" href="/plus/list.php?tid=2&splxa=%E8%A5%BF%E9%83%A8">西部</a><a class="transition" title="同性" href="/plus/list.php?tid=2&splxa=%E5%90%8C%E6%80%A7">同性</a><a class="transition" title="短片" href="/plus/list.php?tid=2&splxa=%E7%9F%AD%E7%89%87">短片</a><a class="transition" title="古装" href="/plus/list.php?tid=2&splxa=%E5%8F%A4%E8%A3%85">古装</a><a class="transition" title="情色" href="/plus/list.php?tid=2&splxa=%E6%83%85%E8%89%B2">情色</a><a class="transition" title="武侠" href="/plus/list.php?tid=2&splxa=%E6%AD%A6%E4%BE%A0">武侠</a><a class="transition" title="灾难" href="/plus/list.php?tid=2&splxa=%E7%81%BE%E9%9A%BE">灾难</a><a class="transition" title="儿童" href="/plus/list.php?tid=2&splxa=%E5%84%BF%E7%AB%A5">儿童</a><a class="transition" title="黑色电影" href="/plus/list.php?tid=2&splxa=%E9%BB%91%E8%89%B2%E7%94%B5%E5%BD%B1">黑色电影</a><a class="transition" title="真人秀" href="/plus/list.php?tid=2&splxa=%E7%9C%9F%E4%BA%BA%E7%A7%80">真人秀</a><a class="transition" title="舞台艺术" href="/plus/list.php?tid=2&splxa=%E8%88%9E%E5%8F%B0%E8%89%BA%E6%9C%AF">舞台艺术</a><a class="transition" title="惊栗" href="/plus/list.php?tid=2&splxa=%E6%83%8A%E6%A0%97">惊栗</a><a class="transition" title="鬼怪" href="/plus/list.php?tid=2&splxa=%E9%AC%BC%E6%80%AA">鬼怪</a><a class="transition" title="Reality-TV" href="/plus/list.php?tid=2&splxa=Reality-TV">Reality-TV</a><a class="transition" title="News" href="/plus/list.php?tid=2&splxa=News">News</a><br/> </div>
					</div>
				</div>
			</div>
               <div class="clear"></div>
                   

                <div class="clear"></div>
			<div class="list">
				<ul id="movielist">
				 
				  
				  
				  <li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/1206/6902.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="http://pic.iask.cn/fimg/485212532362_516.jpg" alt="《婚姻故事》百度云电影-在线观看-超清BD1080P|英" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="《婚姻故事》百度云电影-在线观看-超清BD1080P|英" href="/movie/2019/1206/6902.html">《婚姻故事》百度云电影-在线观看-超清BD1080P|英
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">导演: 诺亚鲍姆巴赫 编剧: 诺亚鲍姆巴赫 资源类型：婚姻故事百度云网盘 在线观看 迅雷下载 主演: 斯嘉丽约翰逊 / 亚当德赖弗 / 劳拉邓恩 / 梅里特韦弗 / 雷利奥塔 / 马克奥布莱恩 / 阿...</div>
						<div class="tags">2019-12-18
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b>8.9</b></a>
						</div>
						<div class="imdb">IMDB：<b>8.3</b></div>
						
					  </div>
					</div>
				  </li><li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/1218/7170.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="https://bbs.djicdn.com/data/attachment/album/201912/18/103154kzfsn7znnjkl1k17.jpg" alt="《洛杉矶大逃亡》百度云电影-在线观看-超清BD" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="《洛杉矶大逃亡》百度云电影-在线观看-超清BD" href="/movie/2019/1218/7170.html">《洛杉矶大逃亡》百度云电影-在线观看-超清BD
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">导演: 约翰卡朋特 编剧: 黛布拉希尔 / 约翰卡朋特 / 库尔特拉塞尔 资源类型：洛杉矶大逃亡百度云网盘 在线观看 迅雷下载 主演: 库尔特拉塞尔 / 史蒂夫布西密 / 彼得方达 / 克里夫罗伯...</div>
						<div class="tags">2019-12-18
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b>6.4</b></a>
						</div>
						<div class="imdb">IMDB：<b>5.7</b></div>
						
					  </div>
					</div>
				  </li><li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/1218/7169.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="https://bbs.djicdn.com/data/attachment/album/201912/18/102551a3tlnleeke5z6ed6.jpg" alt="《御天神兽》百度云电影-在线观看-超清BD1080P|国" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="《御天神兽》百度云电影-在线观看-超清BD1080P|国" href="/movie/2019/1218/7169.html">《御天神兽》百度云电影-在线观看-超清BD1080P|国
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">导演: 武文光 主演: 张冰倩 / 张子文 / 李子雄 资源类型：御天神兽百度云网盘 在线观看 迅雷下载 类型: 奇幻 / 古装 制片国家/地区: 中国大陆 语言: 汉语普通话 上映日期: 2019-12-11(中国...</div>
						<div class="tags">2019-12-18
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b></b></a>
						</div>
						<div class="imdb">IMDB：<b></b></div>
						
					  </div>
					</div>
				  </li><li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/1218/7168.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="https://bbs.djicdn.com/data/attachment/album/201912/18/102113dygn6hizgbz5czhz.jpg" alt="《霍家拳之精武英雄》百度云电影-在线观看-超清" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="《霍家拳之精武英雄》百度云电影-在线观看-超清" href="/movie/2019/1218/7168.html">《霍家拳之精武英雄》百度云电影-在线观看-超清
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">导演: 戴维 编剧: 金成 资源类型：霍家拳之精武英雄百度云网盘 在线观看 迅雷下载 主演: 王文杰 / 赵晨宇 / 吴恒 类型: 剧情 / 动作 制片国家/地区: 中国大陆 语言: 汉语普通话 上映日期...</div>
						<div class="tags">2019-12-18
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b></b></a>
						</div>
						<div class="imdb">IMDB：<b></b></div>
						
					  </div>
					</div>
				  </li><li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/1218/7167.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="https://bbs.djicdn.com/data/attachment/album/201912/18/101431wjbkx9rx99rxd96x.jpg" alt="《木鸢迷踪》百度云电影-在线观看-超清BD1080P|国" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="《木鸢迷踪》百度云电影-在线观看-超清BD1080P|国" href="/movie/2019/1218/7167.html">《木鸢迷踪》百度云电影-在线观看-超清BD1080P|国
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">导演: 张津涛 编剧: 张津涛 资源类型：木鸢迷踪百度云网盘 在线观看 迅雷下载 主演: 孙耀威 / 周睿君 类型: 剧情 / 动作 制片国家/地区: 中国大陆 语言: 汉语普通话 上映日期: 1980-04-0...</div>
						<div class="tags">2019-12-18
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b></b></a>
						</div>
						<div class="imdb">IMDB：<b></b></div>
						
					  </div>
					</div>
				  </li><li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/1218/7166.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="https://bbs.djicdn.com/data/attachment/album/201912/18/100904w3vavkiizz2zhyxf.jpg" alt="《白银帝国》百度云电影-在线观看-超清BD1080P|国" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="《白银帝国》百度云电影-在线观看-超清BD1080P|国" href="/movie/2019/1218/7166.html">《白银帝国》百度云电影-在线观看-超清BD1080P|国
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">导演: 姚树华 编剧: 姚树华 / 成一 资源类型：白银帝国百度云网盘 在线观看 迅雷下载 主演: 郭富城 / 郝蕾 / 张铁林 / 詹妮弗提莉 / 金士杰 / 恬妞 / 丁志城 / 雷镇语 / 吕中 / 李依晓 类型...</div>
						<div class="tags">2019-12-18
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b>6.3</b></a>
						</div>
						<div class="imdb">IMDB：<b>6.1</b></div>
						
					  </div>
					</div>
				  </li><li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/0920/5502.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="https://ask.qcloudimg.com/draft/3504130/e5v7l6sb6w.jpg" alt="<b>《小丑》百度云网盘 迅雷下载 超清.HD1080P.英语中</b>" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="<b>《小丑》百度云网盘 迅雷下载 超清.HD1080P.英语中</b>" href="/movie/2019/0920/5502.html"><b>《小丑》百度云网盘 迅雷下载 超清.HD1080P.英语中</b>
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">導演: 托德菲利普斯 編劇: 托德菲利普斯 / 斯科特西爾弗 主演: 傑昆菲尼克斯 / 羅伯特德尼羅 / 馬克馬龍 / 莎姬貝茲 / 謝惠根姆 / 弗蘭西絲康羅伊 / 布萊恩考倫 / 布萊恩泰裏亨利 / 布萊...</div>
						<div class="tags">2019-12-18
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b>9.4</b></a>
						</div>
						<div class="imdb">IMDB：<b>9.5</b></div>
						
					  </div>
					</div>
				  </li><li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/0921/5549.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="http://pic.iask.cn/fimg/630111839373_516.jpg" alt="《小丑回魂2》百度云网盘 迅雷下载 超清.HD1080" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="《小丑回魂2》百度云网盘 迅雷下载 超清.HD1080" href="/movie/2019/0921/5549.html">《小丑回魂2》百度云网盘 迅雷下载 超清.HD1080
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">片名：小丑回魂2百度云盘It: Chapter Two它：第二章(台) / It 2 導演: 安德斯穆斯切蒂 編劇: 加裏多伯曼 / 斯蒂芬金 類型: 恐怖 制片國家/地區: 美國 語言: 英語 上映日期: 2019-09-06(美國) 片長...</div>
						<div class="tags">2019-12-17
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b>6.6</b></a>
						</div>
						<div class="imdb">IMDB：<b>6.9</b></div>
						
					  </div>
					</div>
				  </li><li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/1217/7165.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="https://bbs.djicdn.com/data/attachment/album/201912/17/204957snzb2eccec6zyee7.jpg" alt="<b>《长安道》百度云电影-在线观看-超清BD1080P|国语</b>" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="<b>《长安道》百度云电影-在线观看-超清BD1080P|国语</b>" href="/movie/2019/1217/7165.html"><b>《长安道》百度云电影-在线观看-超清BD1080P|国语</b>
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">导演: 李骏 编剧: 李骏 / 丁小洋 / 海岩 资源类型：长安道百度云网盘 在线观看 迅雷下载 主演: 范伟 / 宋洋 / 焦俊艳 / 陈数 类型: 剧情 / 悬疑 / 犯罪 制片国家/地区: 中国大陆 语言: 汉语...</div>
						<div class="tags">2019-12-17
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b>6.6</b></a>
						</div>
						<div class="imdb">IMDB：<b>5.0</b></div>
						
					  </div>
					</div>
				  </li><li class="pure-g shadow">
					<div class="pure-u-5-24">
					  <a class="movie-thumbnails" target="_blank" href="/movie/2019/1217/7164.html">
						<img class="pure-img" src="/static/picture/grey.gif" data-original="https://bbs.djicdn.com/data/attachment/album/201912/17/203928fyv9yikrzp0wmuk9.jpg" alt="《燃烧女子的肖像》百度云电影-在线观看-超清" /></a>
					</div>
					<div class="pure-u-19-24">
					  <div class="intro">
						<h2>
						  <a target="_blank" title="《燃烧女子的肖像》百度云电影-在线观看-超清" href="/movie/2019/1217/7164.html">《燃烧女子的肖像》百度云电影-在线观看-超清
							<i>免费电影下载</i>
						  </a>
						</h2>
						<div class="brief">导演: 瑟琳席安玛 编剧: 瑟琳席安玛 资源类型：燃烧女子的肖像百度云网盘 在线观看 迅雷下载 主演: 诺米梅兰特 / 阿黛拉哈内尔 / 瓦莱丽亚戈利诺 / Armande Boulanger / Luna Bajrami / Christel...</div>
						<div class="tags">2019-12-17
						
						<div class="dou">
						  <a target="_blank" rel="nofollow" href="">豆瓣：<b>8.4</b></a>
						</div>
						<div class="imdb">IMDB：<b>8.3</b></div>
						
					  </div>
					</div>
				  </li>
				  
				  
				  
				</ul>
			</div>
<!--当评分为空时设置默认值-->
<script type="text/javascript">
window.onload = function () {
  $("#movielist .dou").each(function(){
	  var lebs = $.trim($(this).find("a b").html()).length;
	  if(lebs == 0){
		  $(this).find("a").attr("href","https://movie.douban.com/subject/0/"); 
		  $(this).find("a b").html("0.0");
	  }
  })
  $("#movielist .imdb").each(function(){
	  var qlebs = $.trim($(this).find("b").html()).length;
	  if(qlebs == 0){
		  $(this).find("b").html("0.0"); 
	  } 
  })
}
</script>   
<!--页码样式-->
<style>
.pagea{padding-BOTTOM: 25px; MARGIN: 10px auto 0px; WIDTH: 100%; PADDING-TOP: 10px; TEXT-ALIGN: center;background: #fff;}
.pagea li{display: inline; BORDER-RIGHT: #ccc 1px solid; PADDING-RIGHT: 8px! important; padding-left: 8px; BORDER-TOP: #ccc 1px solid; PADDING- LEFT: 8px! important; PADDING-BOTTOM: 4px! important; MARGIN: 2px; BORDER-LEFT: #ccc 1px solid; COLOR: #333; PADDING-TOP: 4px! important; BORDER-BOTTOM: #ccc 1px solid; TEXT-DECORATION: none! important} 
.pagea li a{color: #000;}
.pagea li.thisclass{background-color: #a7090a; border-color: #a7090a; color: #fff;border-radius: 5px;font-weight: bold;}
.pagea li.thisclass a{color: #fff;}
	
.pageqq{background: #fff;padding-BOTTOM: 25px; MARGIN: 10px auto 0px; WIDTH: 100%; PADDING-TOP: 10px; TEXT-ALIGN: center; display: none;}
.pageqq li{display: inline; BORDER-RIGHT: #ccc 1px solid; PADDING-RIGHT: 8px! important; padding-left: 4px; BORDER-TOP: #ccc 1px solid; PADDING- LEFT: 8px! important; PADDING-BOTTOM: 4px! important; MARGIN: 2px; BORDER-LEFT: #ccc 1px solid; COLOR: #333; PADDING-TOP: 4px! important; BORDER-BOTTOM: #ccc 1px solid; TEXT-DECORATION: none! important} 
.pageqq li.thisclass{background-color: #a7090a; border-color: #a7090a; color: #fff;}
.pageqq li a{color: #000;}
.pageqq li.thisclass a{color: #fff;}
	
@media screen and (max-width: 767px) {
.pageqq{display: block;}
.pagea{display: none;}
}
	
</style>      
<div class="pagea"><li><a href='list_2_1.html'>首页</a></li>
<li><a href='list_2_3.html'>上一页</a></li>
<li><a href='list_2_1.html'>1</a></li>
<li><a href='list_2_2.html'>2</a></li>
<li><a href='list_2_3.html'>3</a></li>
<li class="thisclass">4</li>
<li><a href='list_2_5.html'>5</a></li>
<li><a href='list_2_6.html'>6</a></li>
<li><a href='list_2_7.html'>7</a></li>
<li><a href='list_2_5.html'>下一页</a></li>
<li><a href='list_2_561.html'>末页</a></li>
<li><select name='sldd' style='width:54px' onchange='location.href=this.options[this.selectedIndex].value;'>
<option value='list_2_1.html'>1</option>
<option value='list_2_2.html'>2</option>
<option value='list_2_3.html'>3</option>
<option value='list_2_4.html' selected>4</option>
<option value='list_2_5.html'>5</option>
<option value='list_2_6.html'>6</option>
<option value='list_2_7.html'>7</option>
<option value='list_2_8.html'>8</option>
<option value='list_2_9.html'>9</option>
<option value='list_2_10.html'>10</option>
<option value='list_2_11.html'>11</option>
<option value='list_2_12.html'>12</option>
<option value='list_2_13.html'>13</option>
<option value='list_2_14.html'>14</option>
<option value='list_2_15.html'>15</option>
<option value='list_2_16.html'>16</option>
<option value='list_2_17.html'>17</option>
<option value='list_2_18.html'>18</option>
<option value='list_2_19.html'>19</option>
<option value='list_2_20.html'>20</option>
<option value='list_2_21.html'>21</option>
<option value='list_2_22.html'>22</option>
<option value='list_2_23.html'>23</option>
<option value='list_2_24.html'>24</option>
<option value='list_2_25.html'>25</option>
<option value='list_2_26.html'>26</option>
<option value='list_2_27.html'>27</option>
<option value='list_2_28.html'>28</option>
<option value='list_2_29.html'>29</option>
<option value='list_2_30.html'>30</option>
<option value='list_2_31.html'>31</option>
<option value='list_2_32.html'>32</option>
<option value='list_2_33.html'>33</option>
<option value='list_2_34.html'>34</option>
<option value='list_2_35.html'>35</option>
<option value='list_2_36.html'>36</option>
<option value='list_2_37.html'>37</option>
<option value='list_2_38.html'>38</option>
<option value='list_2_39.html'>39</option>
<option value='list_2_40.html'>40</option>
<option value='list_2_41.html'>41</option>
<option value='list_2_42.html'>42</option>
<option value='list_2_43.html'>43</option>
<option value='list_2_44.html'>44</option>
<option value='list_2_45.html'>45</option>
<option value='list_2_46.html'>46</option>
<option value='list_2_47.html'>47</option>
<option value='list_2_48.html'>48</option>
<option value='list_2_49.html'>49</option>
<option value='list_2_50.html'>50</option>
<option value='list_2_51.html'>51</option>
<option value='list_2_52.html'>52</option>
<option value='list_2_53.html'>53</option>
<option value='list_2_54.html'>54</option>
<option value='list_2_55.html'>55</option>
<option value='list_2_56.html'>56</option>
<option value='list_2_57.html'>57</option>
<option value='list_2_58.html'>58</option>
<option value='list_2_59.html'>59</option>
<option value='list_2_60.html'>60</option>
<option value='list_2_61.html'>61</option>
<option value='list_2_62.html'>62</option>
<option value='list_2_63.html'>63</option>
<option value='list_2_64.html'>64</option>
<option value='list_2_65.html'>65</option>
<option value='list_2_66.html'>66</option>
<option value='list_2_67.html'>67</option>
<option value='list_2_68.html'>68</option>
<option value='list_2_69.html'>69</option>
<option value='list_2_70.html'>70</option>
<option value='list_2_71.html'>71</option>
<option value='list_2_72.html'>72</option>
<option value='list_2_73.html'>73</option>
<option value='list_2_74.html'>74</option>
<option value='list_2_75.html'>75</option>
<option value='list_2_76.html'>76</option>
<option value='list_2_77.html'>77</option>
<option value='list_2_78.html'>78</option>
<option value='list_2_79.html'>79</option>
<option value='list_2_80.html'>80</option>
<option value='list_2_81.html'>81</option>
<option value='list_2_82.html'>82</option>
<option value='list_2_83.html'>83</option>
<option value='list_2_84.html'>84</option>
<option value='list_2_85.html'>85</option>
<option value='list_2_86.html'>86</option>
<option value='list_2_87.html'>87</option>
<option value='list_2_88.html'>88</option>
<option value='list_2_89.html'>89</option>
<option value='list_2_90.html'>90</option>
<option value='list_2_91.html'>91</option>
<option value='list_2_92.html'>92</option>
<option value='list_2_93.html'>93</option>
<option value='list_2_94.html'>94</option>
<option value='list_2_95.html'>95</option>
<option value='list_2_96.html'>96</option>
<option value='list_2_97.html'>97</option>
<option value='list_2_98.html'>98</option>
<option value='list_2_99.html'>99</option>
<option value='list_2_100.html'>100</option>
<option value='list_2_101.html'>101</option>
<option value='list_2_102.html'>102</option>
<option value='list_2_103.html'>103</option>
<option value='list_2_104.html'>104</option>
<option value='list_2_105.html'>105</option>
<option value='list_2_106.html'>106</option>
<option value='list_2_107.html'>107</option>
<option value='list_2_108.html'>108</option>
<option value='list_2_109.html'>109</option>
<option value='list_2_110.html'>110</option>
<option value='list_2_111.html'>111</option>
<option value='list_2_112.html'>112</option>
<option value='list_2_113.html'>113</option>
<option value='list_2_114.html'>114</option>
<option value='list_2_115.html'>115</option>
<option value='list_2_116.html'>116</option>
<option value='list_2_117.html'>117</option>
<option value='list_2_118.html'>118</option>
<option value='list_2_119.html'>119</option>
<option value='list_2_120.html'>120</option>
<option value='list_2_121.html'>121</option>
<option value='list_2_122.html'>122</option>
<option value='list_2_123.html'>123</option>
<option value='list_2_124.html'>124</option>
<option value='list_2_125.html'>125</option>
<option value='list_2_126.html'>126</option>
<option value='list_2_127.html'>127</option>
<option value='list_2_128.html'>128</option>
<option value='list_2_129.html'>129</option>
<option value='list_2_130.html'>130</option>
<option value='list_2_131.html'>131</option>
<option value='list_2_132.html'>132</option>
<option value='list_2_133.html'>133</option>
<option value='list_2_134.html'>134</option>
<option value='list_2_135.html'>135</option>
<option value='list_2_136.html'>136</option>
<option value='list_2_137.html'>137</option>
<option value='list_2_138.html'>138</option>
<option value='list_2_139.html'>139</option>
<option value='list_2_140.html'>140</option>
<option value='list_2_141.html'>141</option>
<option value='list_2_142.html'>142</option>
<option value='list_2_143.html'>143</option>
<option value='list_2_144.html'>144</option>
<option value='list_2_145.html'>145</option>
<option value='list_2_146.html'>146</option>
<option value='list_2_147.html'>147</option>
<option value='list_2_148.html'>148</option>
<option value='list_2_149.html'>149</option>
<option value='list_2_150.html'>150</option>
<option value='list_2_151.html'>151</option>
<option value='list_2_152.html'>152</option>
<option value='list_2_153.html'>153</option>
<option value='list_2_154.html'>154</option>
<option value='list_2_155.html'>155</option>
<option value='list_2_156.html'>156</option>
<option value='list_2_157.html'>157</option>
<option value='list_2_158.html'>158</option>
<option value='list_2_159.html'>159</option>
<option value='list_2_160.html'>160</option>
<option value='list_2_161.html'>161</option>
<option value='list_2_162.html'>162</option>
<option value='list_2_163.html'>163</option>
<option value='list_2_164.html'>164</option>
<option value='list_2_165.html'>165</option>
<option value='list_2_166.html'>166</option>
<option value='list_2_167.html'>167</option>
<option value='list_2_168.html'>168</option>
<option value='list_2_169.html'>169</option>
<option value='list_2_170.html'>170</option>
<option value='list_2_171.html'>171</option>
<option value='list_2_172.html'>172</option>
<option value='list_2_173.html'>173</option>
<option value='list_2_174.html'>174</option>
<option value='list_2_175.html'>175</option>
<option value='list_2_176.html'>176</option>
<option value='list_2_177.html'>177</option>
<option value='list_2_178.html'>178</option>
<option value='list_2_179.html'>179</option>
<option value='list_2_180.html'>180</option>
<option value='list_2_181.html'>181</option>
<option value='list_2_182.html'>182</option>
<option value='list_2_183.html'>183</option>
<option value='list_2_184.html'>184</option>
<option value='list_2_185.html'>185</option>
<option value='list_2_186.html'>186</option>
<option value='list_2_187.html'>187</option>
<option value='list_2_188.html'>188</option>
<option value='list_2_189.html'>189</option>
<option value='list_2_190.html'>190</option>
<option value='list_2_191.html'>191</option>
<option value='list_2_192.html'>192</option>
<option value='list_2_193.html'>193</option>
<option value='list_2_194.html'>194</option>
<option value='list_2_195.html'>195</option>
<option value='list_2_196.html'>196</option>
<option value='list_2_197.html'>197</option>
<option value='list_2_198.html'>198</option>
<option value='list_2_199.html'>199</option>
<option value='list_2_200.html'>200</option>
<option value='list_2_201.html'>201</option>
<option value='list_2_202.html'>202</option>
<option value='list_2_203.html'>203</option>
<option value='list_2_204.html'>204</option>
<option value='list_2_205.html'>205</option>
<option value='list_2_206.html'>206</option>
<option value='list_2_207.html'>207</option>
<option value='list_2_208.html'>208</option>
<option value='list_2_209.html'>209</option>
<option value='list_2_210.html'>210</option>
<option value='list_2_211.html'>211</option>
<option value='list_2_212.html'>212</option>
<option value='list_2_213.html'>213</option>
<option value='list_2_214.html'>214</option>
<option value='list_2_215.html'>215</option>
<option value='list_2_216.html'>216</option>
<option value='list_2_217.html'>217</option>
<option value='list_2_218.html'>218</option>
<option value='list_2_219.html'>219</option>
<option value='list_2_220.html'>220</option>
<option value='list_2_221.html'>221</option>
<option value='list_2_222.html'>222</option>
<option value='list_2_223.html'>223</option>
<option value='list_2_224.html'>224</option>
<option value='list_2_225.html'>225</option>
<option value='list_2_226.html'>226</option>
<option value='list_2_227.html'>227</option>
<option value='list_2_228.html'>228</option>
<option value='list_2_229.html'>229</option>
<option value='list_2_230.html'>230</option>
<option value='list_2_231.html'>231</option>
<option value='list_2_232.html'>232</option>
<option value='list_2_233.html'>233</option>
<option value='list_2_234.html'>234</option>
<option value='list_2_235.html'>235</option>
<option value='list_2_236.html'>236</option>
<option value='list_2_237.html'>237</option>
<option value='list_2_238.html'>238</option>
<option value='list_2_239.html'>239</option>
<option value='list_2_240.html'>240</option>
<option value='list_2_241.html'>241</option>
<option value='list_2_242.html'>242</option>
<option value='list_2_243.html'>243</option>
<option value='list_2_244.html'>244</option>
<option value='list_2_245.html'>245</option>
<option value='list_2_246.html'>246</option>
<option value='list_2_247.html'>247</option>
<option value='list_2_248.html'>248</option>
<option value='list_2_249.html'>249</option>
<option value='list_2_250.html'>250</option>
<option value='list_2_251.html'>251</option>
<option value='list_2_252.html'>252</option>
<option value='list_2_253.html'>253</option>
<option value='list_2_254.html'>254</option>
<option value='list_2_255.html'>255</option>
<option value='list_2_256.html'>256</option>
<option value='list_2_257.html'>257</option>
<option value='list_2_258.html'>258</option>
<option value='list_2_259.html'>259</option>
<option value='list_2_260.html'>260</option>
<option value='list_2_261.html'>261</option>
<option value='list_2_262.html'>262</option>
<option value='list_2_263.html'>263</option>
<option value='list_2_264.html'>264</option>
<option value='list_2_265.html'>265</option>
<option value='list_2_266.html'>266</option>
<option value='list_2_267.html'>267</option>
<option value='list_2_268.html'>268</option>
<option value='list_2_269.html'>269</option>
<option value='list_2_270.html'>270</option>
<option value='list_2_271.html'>271</option>
<option value='list_2_272.html'>272</option>
<option value='list_2_273.html'>273</option>
<option value='list_2_274.html'>274</option>
<option value='list_2_275.html'>275</option>
<option value='list_2_276.html'>276</option>
<option value='list_2_277.html'>277</option>
<option value='list_2_278.html'>278</option>
<option value='list_2_279.html'>279</option>
<option value='list_2_280.html'>280</option>
<option value='list_2_281.html'>281</option>
<option value='list_2_282.html'>282</option>
<option value='list_2_283.html'>283</option>
<option value='list_2_284.html'>284</option>
<option value='list_2_285.html'>285</option>
<option value='list_2_286.html'>286</option>
<option value='list_2_287.html'>287</option>
<option value='list_2_288.html'>288</option>
<option value='list_2_289.html'>289</option>
<option value='list_2_290.html'>290</option>
<option value='list_2_291.html'>291</option>
<option value='list_2_292.html'>292</option>
<option value='list_2_293.html'>293</option>
<option value='list_2_294.html'>294</option>
<option value='list_2_295.html'>295</option>
<option value='list_2_296.html'>296</option>
<option value='list_2_297.html'>297</option>
<option value='list_2_298.html'>298</option>
<option value='list_2_299.html'>299</option>
<option value='list_2_300.html'>300</option>
<option value='list_2_301.html'>301</option>
<option value='list_2_302.html'>302</option>
<option value='list_2_303.html'>303</option>
<option value='list_2_304.html'>304</option>
<option value='list_2_305.html'>305</option>
<option value='list_2_306.html'>306</option>
<option value='list_2_307.html'>307</option>
<option value='list_2_308.html'>308</option>
<option value='list_2_309.html'>309</option>
<option value='list_2_310.html'>310</option>
<option value='list_2_311.html'>311</option>
<option value='list_2_312.html'>312</option>
<option value='list_2_313.html'>313</option>
<option value='list_2_314.html'>314</option>
<option value='list_2_315.html'>315</option>
<option value='list_2_316.html'>316</option>
<option value='list_2_317.html'>317</option>
<option value='list_2_318.html'>318</option>
<option value='list_2_319.html'>319</option>
<option value='list_2_320.html'>320</option>
<option value='list_2_321.html'>321</option>
<option value='list_2_322.html'>322</option>
<option value='list_2_323.html'>323</option>
<option value='list_2_324.html'>324</option>
<option value='list_2_325.html'>325</option>
<option value='list_2_326.html'>326</option>
<option value='list_2_327.html'>327</option>
<option value='list_2_328.html'>328</option>
<option value='list_2_329.html'>329</option>
<option value='list_2_330.html'>330</option>
<option value='list_2_331.html'>331</option>
<option value='list_2_332.html'>332</option>
<option value='list_2_333.html'>333</option>
<option value='list_2_334.html'>334</option>
<option value='list_2_335.html'>335</option>
<option value='list_2_336.html'>336</option>
<option value='list_2_337.html'>337</option>
<option value='list_2_338.html'>338</option>
<option value='list_2_339.html'>339</option>
<option value='list_2_340.html'>340</option>
<option value='list_2_341.html'>341</option>
<option value='list_2_342.html'>342</option>
<option value='list_2_343.html'>343</option>
<option value='list_2_344.html'>344</option>
<option value='list_2_345.html'>345</option>
<option value='list_2_346.html'>346</option>
<option value='list_2_347.html'>347</option>
<option value='list_2_348.html'>348</option>
<option value='list_2_349.html'>349</option>
<option value='list_2_350.html'>350</option>
<option value='list_2_351.html'>351</option>
<option value='list_2_352.html'>352</option>
<option value='list_2_353.html'>353</option>
<option value='list_2_354.html'>354</option>
<option value='list_2_355.html'>355</option>
<option value='list_2_356.html'>356</option>
<option value='list_2_357.html'>357</option>
<option value='list_2_358.html'>358</option>
<option value='list_2_359.html'>359</option>
<option value='list_2_360.html'>360</option>
<option value='list_2_361.html'>361</option>
<option value='list_2_362.html'>362</option>
<option value='list_2_363.html'>363</option>
<option value='list_2_364.html'>364</option>
<option value='list_2_365.html'>365</option>
<option value='list_2_366.html'>366</option>
<option value='list_2_367.html'>367</option>
<option value='list_2_368.html'>368</option>
<option value='list_2_369.html'>369</option>
<option value='list_2_370.html'>370</option>
<option value='list_2_371.html'>371</option>
<option value='list_2_372.html'>372</option>
<option value='list_2_373.html'>373</option>
<option value='list_2_374.html'>374</option>
<option value='list_2_375.html'>375</option>
<option value='list_2_376.html'>376</option>
<option value='list_2_377.html'>377</option>
<option value='list_2_378.html'>378</option>
<option value='list_2_379.html'>379</option>
<option value='list_2_380.html'>380</option>
<option value='list_2_381.html'>381</option>
<option value='list_2_382.html'>382</option>
<option value='list_2_383.html'>383</option>
<option value='list_2_384.html'>384</option>
<option value='list_2_385.html'>385</option>
<option value='list_2_386.html'>386</option>
<option value='list_2_387.html'>387</option>
<option value='list_2_388.html'>388</option>
<option value='list_2_389.html'>389</option>
<option value='list_2_390.html'>390</option>
<option value='list_2_391.html'>391</option>
<option value='list_2_392.html'>392</option>
<option value='list_2_393.html'>393</option>
<option value='list_2_394.html'>394</option>
<option value='list_2_395.html'>395</option>
<option value='list_2_396.html'>396</option>
<option value='list_2_397.html'>397</option>
<option value='list_2_398.html'>398</option>
<option value='list_2_399.html'>399</option>
<option value='list_2_400.html'>400</option>
<option value='list_2_401.html'>401</option>
<option value='list_2_402.html'>402</option>
<option value='list_2_403.html'>403</option>
<option value='list_2_404.html'>404</option>
<option value='list_2_405.html'>405</option>
<option value='list_2_406.html'>406</option>
<option value='list_2_407.html'>407</option>
<option value='list_2_408.html'>408</option>
<option value='list_2_409.html'>409</option>
<option value='list_2_410.html'>410</option>
<option value='list_2_411.html'>411</option>
<option value='list_2_412.html'>412</option>
<option value='list_2_413.html'>413</option>
<option value='list_2_414.html'>414</option>
<option value='list_2_415.html'>415</option>
<option value='list_2_416.html'>416</option>
<option value='list_2_417.html'>417</option>
<option value='list_2_418.html'>418</option>
<option value='list_2_419.html'>419</option>
<option value='list_2_420.html'>420</option>
<option value='list_2_421.html'>421</option>
<option value='list_2_422.html'>422</option>
<option value='list_2_423.html'>423</option>
<option value='list_2_424.html'>424</option>
<option value='list_2_425.html'>425</option>
<option value='list_2_426.html'>426</option>
<option value='list_2_427.html'>427</option>
<option value='list_2_428.html'>428</option>
<option value='list_2_429.html'>429</option>
<option value='list_2_430.html'>430</option>
<option value='list_2_431.html'>431</option>
<option value='list_2_432.html'>432</option>
<option value='list_2_433.html'>433</option>
<option value='list_2_434.html'>434</option>
<option value='list_2_435.html'>435</option>
<option value='list_2_436.html'>436</option>
<option value='list_2_437.html'>437</option>
<option value='list_2_438.html'>438</option>
<option value='list_2_439.html'>439</option>
<option value='list_2_440.html'>440</option>
<option value='list_2_441.html'>441</option>
<option value='list_2_442.html'>442</option>
<option value='list_2_443.html'>443</option>
<option value='list_2_444.html'>444</option>
<option value='list_2_445.html'>445</option>
<option value='list_2_446.html'>446</option>
<option value='list_2_447.html'>447</option>
<option value='list_2_448.html'>448</option>
<option value='list_2_449.html'>449</option>
<option value='list_2_450.html'>450</option>
<option value='list_2_451.html'>451</option>
<option value='list_2_452.html'>452</option>
<option value='list_2_453.html'>453</option>
<option value='list_2_454.html'>454</option>
<option value='list_2_455.html'>455</option>
<option value='list_2_456.html'>456</option>
<option value='list_2_457.html'>457</option>
<option value='list_2_458.html'>458</option>
<option value='list_2_459.html'>459</option>
<option value='list_2_460.html'>460</option>
<option value='list_2_461.html'>461</option>
<option value='list_2_462.html'>462</option>
<option value='list_2_463.html'>463</option>
<option value='list_2_464.html'>464</option>
<option value='list_2_465.html'>465</option>
<option value='list_2_466.html'>466</option>
<option value='list_2_467.html'>467</option>
<option value='list_2_468.html'>468</option>
<option value='list_2_469.html'>469</option>
<option value='list_2_470.html'>470</option>
<option value='list_2_471.html'>471</option>
<option value='list_2_472.html'>472</option>
<option value='list_2_473.html'>473</option>
<option value='list_2_474.html'>474</option>
<option value='list_2_475.html'>475</option>
<option value='list_2_476.html'>476</option>
<option value='list_2_477.html'>477</option>
<option value='list_2_478.html'>478</option>
<option value='list_2_479.html'>479</option>
<option value='list_2_480.html'>480</option>
<option value='list_2_481.html'>481</option>
<option value='list_2_482.html'>482</option>
<option value='list_2_483.html'>483</option>
<option value='list_2_484.html'>484</option>
<option value='list_2_485.html'>485</option>
<option value='list_2_486.html'>486</option>
<option value='list_2_487.html'>487</option>
<option value='list_2_488.html'>488</option>
<option value='list_2_489.html'>489</option>
<option value='list_2_490.html'>490</option>
<option value='list_2_491.html'>491</option>
<option value='list_2_492.html'>492</option>
<option value='list_2_493.html'>493</option>
<option value='list_2_494.html'>494</option>
<option value='list_2_495.html'>495</option>
<option value='list_2_496.html'>496</option>
<option value='list_2_497.html'>497</option>
<option value='list_2_498.html'>498</option>
<option value='list_2_499.html'>499</option>
<option value='list_2_500.html'>500</option>
<option value='list_2_501.html'>501</option>
<option value='list_2_502.html'>502</option>
<option value='list_2_503.html'>503</option>
<option value='list_2_504.html'>504</option>
<option value='list_2_505.html'>505</option>
<option value='list_2_506.html'>506</option>
<option value='list_2_507.html'>507</option>
<option value='list_2_508.html'>508</option>
<option value='list_2_509.html'>509</option>
<option value='list_2_510.html'>510</option>
<option value='list_2_511.html'>511</option>
<option value='list_2_512.html'>512</option>
<option value='list_2_513.html'>513</option>
<option value='list_2_514.html'>514</option>
<option value='list_2_515.html'>515</option>
<option value='list_2_516.html'>516</option>
<option value='list_2_517.html'>517</option>
<option value='list_2_518.html'>518</option>
<option value='list_2_519.html'>519</option>
<option value='list_2_520.html'>520</option>
<option value='list_2_521.html'>521</option>
<option value='list_2_522.html'>522</option>
<option value='list_2_523.html'>523</option>
<option value='list_2_524.html'>524</option>
<option value='list_2_525.html'>525</option>
<option value='list_2_526.html'>526</option>
<option value='list_2_527.html'>527</option>
<option value='list_2_528.html'>528</option>
<option value='list_2_529.html'>529</option>
<option value='list_2_530.html'>530</option>
<option value='list_2_531.html'>531</option>
<option value='list_2_532.html'>532</option>
<option value='list_2_533.html'>533</option>
<option value='list_2_534.html'>534</option>
<option value='list_2_535.html'>535</option>
<option value='list_2_536.html'>536</option>
<option value='list_2_537.html'>537</option>
<option value='list_2_538.html'>538</option>
<option value='list_2_539.html'>539</option>
<option value='list_2_540.html'>540</option>
<option value='list_2_541.html'>541</option>
<option value='list_2_542.html'>542</option>
<option value='list_2_543.html'>543</option>
<option value='list_2_544.html'>544</option>
<option value='list_2_545.html'>545</option>
<option value='list_2_546.html'>546</option>
<option value='list_2_547.html'>547</option>
<option value='list_2_548.html'>548</option>
<option value='list_2_549.html'>549</option>
<option value='list_2_550.html'>550</option>
<option value='list_2_551.html'>551</option>
<option value='list_2_552.html'>552</option>
<option value='list_2_553.html'>553</option>
<option value='list_2_554.html'>554</option>
<option value='list_2_555.html'>555</option>
<option value='list_2_556.html'>556</option>
<option value='list_2_557.html'>557</option>
<option value='list_2_558.html'>558</option>
<option value='list_2_559.html'>559</option>
<option value='list_2_560.html'>560</option>
<option value='list_2_561.html'>561</option>
</select></li>
</div>
<div class="pageqq"><li><a href='list_2_1.html'>首页</a></li>
<li><a href='list_2_3.html'>上一页</a></li>
<li><a href='list_2_5.html'>下一页</a></li>
<li><a href='list_2_561.html'>末页</a></li>
</div>


		</div>
		
		<!--右侧开始-->
		<div class="pure-u-1 pure-u-md-7-24">
<div class="side-bar">
								<!-- items -->
<style>
.item-third-dl{padding:0;overflow:hidden;margin: 0 0 15px;}
.item-third-box{position: fixed;   top: 50px;width: 260px;display:none;}
.item-third {box-sizing: border-box;width: 100%;float: left;display: block;cursor: pointer;	color:#555;}
.item-third:hover {color: #f84e4e;text-decoration: none;}
.item-third .item-third-container {width: 100%;background: #fff;border-radius: 4px}
.item-third .item-third-cover {width: 100%;padding-top: 100%;background-size: cover;border-radius: 4px 4px 0 0}
.item-third .item-third-info-container {border-top: 0}
.item-third .item-third-name {padding-left: 10px;padding-right: 10px;text-overflow: ellipsis;white-space: nowrap;
	overflow: hidden;font-size:14px;}
.item-third .item-third-info {padding: 5px 10px;padding-bottom: 2px;overflow: hidden}
.item-third .item-third-info .item-third-price {float: left;color:#555;}
.item-third .item-third-info .item-third-price b {color: #f84e4e;font-size:20px;}
.item-third .item-third-info .item-third-fav-count {color: #979797;float: right;line-height:30px;}
.item-third .item-third-info .item-third-fav-count i {display: block;margin-top: 9px;margin-right: 2px;float: left;
	width: 15px;height: 13px;background: url(/static/images/icon_favorite_78d7777.png);background-size: 15px;}
.item-third .item-third-info .item-third-fav-count i.like {background: url(/static/images/icon_favorites_selected_35f43f3.png);background-size: 15px}
.item-third .item-third-info .item-third-fav-count p {margin-left: 20px;	line-height: 22px}
.mall-data{outline: 0px;   display: block;   padding-right: 0px;   float: right;color: rgb(51, 51, 51);margin-top: 6px; font-size: 12px;   line-height: 14px;}
.card-btn-deep{outline: 0px;  display: block;   padding-right: 0px;  float: right;  width: 68px;  height: 28px;  margin-left: 10px;   border-radius: 3px;
    line-height: 28px;   text-align: center;   font-size: 12px;   background-color: rgb(240, 72, 72);   color: rgb(255, 255, 255);}
.tag-coupon{height: 16px;   width: 16px;  text-align: center;  line-height: 16px;  display: inline-block;  vertical-align: middle;  margin-right: 6px;}
.tag-quan{width: auto;}
.icon-quan{width: 17px;   height: 16px;   display: inline-block;  vertical-align: top;  background-image: url(/static/images/icon-q.png);
    background-image: -webkit-image-set(url(/static/images/icon-q.png) 1x,url(/static/images/icon-q2.png) 2x);
    background-image: -moz-image-set(url(/static/images/icon-q.png) 1x,url(/static/images/icon-q2.png) 2x);
    background-image: -ms-image-set(url(/static/images/icon-q.png) 1x,url(/static/images/icon-q2.png) 2x);
    background-image: -o-image-set(url(/static/images/icon-q.png) 1x,url(/static/images/icon-q2.png) 2x);}
.quan-money {   border: 1px solid #f50;   border-left: none;   display: inline-block;   vertical-align: top;  height: 14px;   line-height: 14px;
background-color: #FFF;   border-radius: 0 2px 2px 0;   padding: 0 3px;   color: #E64D00;}
</style>
					
<dl class="item-third-dl">
  <div>
    <div class="item-third">
     <div class="item-third-container" onclick="window.open('http://www.renrendianyingwang.cn/movie/2019/0916/5408.html')">
        <div class="item-third-cover" style="background: url(https://ae01.alicdn.com/kf/H477a697117324f37bdd10cd2cbc8619fx.jpg); background-size: cover;"></div>
        <div class="item-third-info-container">
          <p class="item-third-name">打开支付宝搜“532393058”领红包，</p>
          <div class="item-third-info">
            <div class="item-third-price">¥<b></b>券后价</div>
            <div class="mall-data">
              <span class="tag-coupon tag-quan">
                <span class="icon-quan"></span>
                <span class="quan-money">
                  <span></span>元</span></span>
            </div>
          </div>
          <div class="item-third-info">
            <div class="item-third-fav-count">
              <i class="like-item-icon"></i>
              <span>8722</span></div>
          </div>
        </div>
      </div>

    </div>
  </div>
</dl>	
					
<!-- items end -->	
<div class="box shadow" style="padding: 10px;color:#999;font-size:12px; line-height:20px;    display: none;">
    <b style="color:#c00">现在迅雷屏蔽资源比较严重</b>，<br>
    是迅雷软件的问题！解决办法：<br>
    1.<a href="https://pan.baidu.com/download" target="_blank">百度网盘离线下载</a><br>
    2.<a href="https://pan.baidu.com/s/1nvT6eE1" target="_blank">使用早期版本迅雷5.8下载</a> 密码: vi2g<br>
	3.<a href="https://pan.baidu.com/s/1kVQSszd" target="_blank">使用utorrent下载</a> 密码: ygm3<br>
    4.使用115网盘，BitComet等软件下载。
</div>
<div class="box shadow clearfix">
    <div class="tit">关注微信公众号</div>
    
    <div class="float-left" style="width: 45%; padding: 2%">
       <img class="float-left" alt="商务合作" src="https://ae01.alicdn.com/kf/HTB19D99bcnrK1RkHFrdq6xCoFXaJ.jpg" width="100%">

    </div>
    <div class="float-right" style="width: 45%;  padding: 2%">
        <a class="float-right" href="http://weibo.com/dcmovie" target="_blank" rel="nofollow">
        <img alt="官方微信公众号" src="https://s1.ax1x.com/2018/11/07/iTJ3LD.jpg" width="100%">

   		</a>
    </div>
</div>
<div class="box shadow" style="padding:5px">
    <a target="_blank" href="http://bbs.mnw.cn/" class="tutorial text-center transition">福利【升级中】<i>(点击进入)</i></a>
</div>


<div class="box shadow" style="padding:15px">
    <a href="http://www.rrzyw.cn" target="_blank">人人资源网</a>
    <a target="_blank" href="http://www.15166.com/"></a>
</div>			
</div>
</div>
		<!--结束-->
	</div>
</div>
<script>
	$(function() {
		// 异步加载图片
		$("#movielist img").lazyload({
			effect: "fadeIn"
		});
		// 下拉选选
		var t = true;
		$('.drop-down').click(function () {
			$(this).focus();
			var obj = $(this).parent().find('.drop-down-menu');
			var h = obj.height();
			obj.css('height','0');
			obj.show().animate({height:h}, {duration: 400, easing: 'easeOutBounce'});
		}).blur(function () {
			if(t) {
				var obj = $(this).parent().find('.drop-down-menu');
				obj.animate({height:0}, 200, 'easeInQuart', function () {
					obj.hide();
					obj.css('height','auto');
				});
			}
		});
		$('.drop-down-menu a').mouseover(function () {
			t = false;
		}).mouseout(function () {
			t = true;
		});
	});
</script>


	
</body>
</html>




'''


doc = pq(html)
li_list = doc.find('.pure-g.shadow')
for item in li_list.items():
    temp_href = item.find('.movie-thumbnails').attr.href
    imdb = item.find('.imdb').eq(1).text()
    print(temp_href,imdb)
