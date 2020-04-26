#coding:utf-8
from pyquery import PyQuery as pq
import re
import time
html = '''

<!DOCTYPE html>
<html lang="zh-CN" class="ua-windows ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <title>
        复仇者联盟4：终局之战 (豆瓣)
</title>
    
    <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
    <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img3.doubanio.com/f/shire/3e5dfc68b0f376484c50cf08a58bbca3700911dc/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css" rel="stylesheet">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/5ecaf46d6954d5a30bc7d99be86ae34031646e00/js/douban.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js"></script>
    
    <meta name="keywords" content="复仇者联盟4：终局之战,Avengers: Endgame,复仇者联盟4：终局之战影评,剧情介绍,电影图片,预告片,影讯,在线购票,论坛">
    <meta name="description" content="复仇者联盟4：终局之战电影简介和剧情介绍,复仇者联盟4：终局之战影评、图片、预告片、影讯、论坛、在线购票">
    <meta name="mobile-agent" content="format=html5; url=http://m.douban.com/movie/subject/26100958/"/>
    <link rel="alternate" href="android-app://com.douban.movie/doubanmovie/subject/26100958/" />
    <link rel="stylesheet" href="https://img3.doubanio.com/dae/cdnlib/libs/LikeButton/1.0.5/style.min.css">
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript">
      Do.add('dialog', {path: 'https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js', type: 'js'});
      Do.add('dialog-css', {path: 'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css', type: 'css'});
      Do.add('handlebarsjs', {path: 'https://img3.doubanio.com/f/movie/3d4f8e4a8918718256450eb6e57ec8e1f7a2e14b/js/movie/lib/handlebars.current.js', type: 'js'});
    </script>
    
  <script type='text/javascript'>
  var _vwo_code = (function() {
    var account_id = 249272,
      settings_tolerance = 0,
      library_tolerance = 2500,
      use_existing_jquery = false,
      // DO NOT EDIT BELOW THIS LINE
      f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return settings_timer;}};}());

  +function () {
    var bindEvent = function (el, type, handler) {
        var $ = window.jQuery || window.Zepto || window.$
       if ($ && $.fn && $.fn.on) {
           $(el).on(type, handler)
       } else if($ && $.fn && $.fn.bind) {
           $(el).bind(type, handler)
       } else if (el.addEventListener){
         el.addEventListener(type, handler, false);
       } else if (el.attachEvent){
         el.attachEvent("on" + type, handler);
       } else {
         el["on" + type] = handler;
       }
     }

    var _origin_load = _vwo_code.load
    _vwo_code.load = function () {
      var args = [].slice.call(arguments)
      bindEvent(window, 'load', function () {
        _origin_load.apply(_vwo_code, args)
      })
    }
  }()

  _vwo_settings_timer = _vwo_code.init();
  </script>


    


<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "name": "复仇者联盟4：终局之战 Avengers: Endgame",
  "url": "/subject/26100958/",
  "image": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2552058346.webp",
  "director": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1321812/",
      "name": "安东尼·罗素 Anthony Russo"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1320870/",
      "name": "乔·罗素 Joe Russo"
    }
  ]
,
  "author": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1276125/",
      "name": "克里斯托弗·马库斯 Christopher Markus"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1276126/",
      "name": "斯蒂芬·麦克菲利 Stephen McFeely"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1013888/",
      "name": "斯坦·李 Stan Lee"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1050183/",
      "name": "杰克·科比 Jack Kirby"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1360715/",
      "name": "吉姆·斯特林 Jim Starlin"
    }
  ]
,
  "actor": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1016681/",
      "name": "小罗伯特·唐尼 Robert Downey Jr."
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1017885/",
      "name": "克里斯·埃文斯 Chris Evans"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1040505/",
      "name": "马克·鲁弗洛 Mark Ruffalo"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1021959/",
      "name": "克里斯·海姆斯沃斯 Chris Hemsworth"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1054453/",
      "name": "斯嘉丽·约翰逊 Scarlett Johansson"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1013770/",
      "name": "杰瑞米·雷纳 Jeremy Renner"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1002667/",
      "name": "保罗·路德 Paul Rudd"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1036344/",
      "name": "凯伦·吉兰 Karen Gillan"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1053573/",
      "name": "唐·钱德尔 Don Cheadle"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1027194/",
      "name": "布丽·拉尔森 Brie Larson"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1013757/",
      "name": "布莱德利·库珀 Bradley Cooper"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1027395/",
      "name": "泰莎·汤普森 Tessa Thompson"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1325351/",
      "name": "汤姆·赫兰德 Tom Holland"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1129847/",
      "name": "伊丽莎白·奥尔森 Elizabeth Olsen"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1009405/",
      "name": "本尼迪克特·康伯巴奇 Benedict Cumberbatch"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1025152/",
      "name": "蒂尔达·斯文顿 Tilda Swinton"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1018985/",
      "name": "格温妮斯·帕特洛 Gwyneth Paltrow"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1004610/",
      "name": "蕾妮·罗素 Rene Russo"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1022661/",
      "name": "约翰·斯拉特里 John Slattery"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1327680/",
      "name": "查德维克·博斯曼 Chadwick Boseman"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1027217/",
      "name": "安东尼·麦凯 Anthony Mackie"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1021985/",
      "name": "塞巴斯蒂安·斯坦 Sebastian Stan"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1017967/",
      "name": "克里斯·帕拉特 Chris Pratt"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1004596/",
      "name": "汤姆·希德勒斯顿 Tom Hiddleston"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1047985/",
      "name": "佐伊·索尔达娜 Zoe Saldana"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1308787/",
      "name": "丹娜·奎里拉 Danai Gurira"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1301179/",
      "name": "本尼迪克特·王 Benedict Wong"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1313255/",
      "name": "庞·克莱门捷夫 Pom Klementieff"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1014003/",
      "name": "戴夫·巴蒂斯塔 Dave Bautista"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1356810/",
      "name": "利蒂希娅·赖特 Letitia Wright"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1021963/",
      "name": "伊万杰琳·莉莉 Evangeline Lilly"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1027164/",
      "name": "乔恩·费儒 Jon Favreau"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1000051/",
      "name": "海莉·阿特维尔 Hayley Atwell"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1054454/",
      "name": "娜塔莉·波特曼 Natalie Portman"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1047974/",
      "name": "玛丽莎·托梅 Marisa Tomei"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1076354/",
      "name": "塔伊加·维迪提 Taika Waititi"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1025214/",
      "name": "安吉拉·贝塞特 Angela Bassett"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1053620/",
      "name": "迈克尔·道格拉斯 Michael Douglas"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1035642/",
      "name": "米歇尔·菲佛 Michelle Pfeiffer"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1031849/",
      "name": "威廉·赫特 William Hurt"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1000018/",
      "name": "寇碧·史莫德斯 Cobie Smulders"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1022552/",
      "name": "肖恩·古恩 Sean Gunn"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1362864/",
      "name": "温斯顿·杜克 Winston Duke"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1010545/",
      "name": "琳达·卡德里尼 Linda Cardellini"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1339359/",
      "name": "马克斯米利亚诺·赫尔南德斯 Maximiliano Hernández"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1100321/",
      "name": "弗兰克·格里罗 Frank Grillo"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1027879/",
      "name": "真田广之 Hiroyuki Sanada"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1332428/",
      "name": "汤姆-沃恩-劳勒 Tom Vaughan-Lawlor"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1049713/",
      "name": "詹姆斯·达西 James D&#39;Arcy"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1376777/",
      "name": "雅各布·巴特朗 Jacob Batalon"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1041020/",
      "name": "范·迪塞尔 Vin Diesel"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1053617/",
      "name": "罗伯特·雷德福 Robert Redford"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1004568/",
      "name": "乔什·布洛林 Josh Brolin"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1054408/",
      "name": "塞缪尔·杰克逊 Samuel L. Jackson"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1210466/",
      "name": "伊薇特·尼科尔·布朗 Yvette Nicole Brown"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392731/",
      "name": "卡梅伦·布鲁姆布罗 Cameron Brumbelow"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392730/",
      "name": "蒂莫西·卡尔 Timothy Carr"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1013874/",
      "name": "凯瑞·康顿 Kerry Condon"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392741/",
      "name": "迈克尔·A·库克 Michael A. Cook"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1342808/",
      "name": "凯莉·库恩 Carrie Coon"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1321687/",
      "name": "艾玛·福尔曼 Emma Fuhrmann"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392734/",
      "name": "雷纳·加拉赫 Renah Gallagher"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392732/",
      "name": "丹妮拉·加斯基 Daniela Gaskie"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1275017/",
      "name": "郑肯 Ken Jeong"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392722/",
      "name": "小弗洛伊德·安东尼·约翰 Floyd Anthony Johns Jr."
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1013888/",
      "name": "斯坦·李 Stan Lee"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1348037/",
      "name": "罗斯·马昆德 Ross Marquand"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392739/",
      "name": "布伦特·麦吉 Brent McGee"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392737/",
      "name": "迈克尔·皮耶里诺·米勒 Michael Pierino Miller"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1126747/",
      "name": "卡兰·马尔韦 Callan Mulvey"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1341026/",
      "name": "泰瑞·诺塔里 Terry Notary"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1133195/",
      "name": "吉米·雷·皮肯斯 Jimmy Ray Pickens"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1344984/",
      "name": "迈克尔·詹姆斯·肖 Michael James Shaw"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1322702/",
      "name": "泰·辛普金斯 Ty Simpkins"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392736/",
      "name": "格雷格·蒂芬 Greg Tiffan"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1415181/",
      "name": "艾娃·罗素 Ava Russo"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1320870/",
      "name": "乔·罗素 Joe Russo"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392738/",
      "name": "玛丽亚·Z·威尔逊 Maria Z. Wilson"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392735/",
      "name": "本杰明·韦弗 Benjamin Weaver"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392728/",
      "name": "劳尔·阿尔坎塔 Raul Alcantar"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392727/",
      "name": "雅各布·埃文斯 Jacob Evans"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1411163/",
      "name": "何塞·阿尔弗雷多·费尔南德斯 José Alfredo Fernandez"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392726/",
      "name": "布伦特·莫雷尔·加斯金斯 Brent Moorer Gaskins"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1266890/",
      "name": "安东尼·B·哈里斯 Anthony B. Harris"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392740/",
      "name": "肖恩·麦克米伦 Shaun McMillan"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392724/",
      "name": "罗伯特·佩恩 Robert Payen"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392725/",
      "name": "麦克斯威尔·海史密斯 Maxwell Highsmith"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1402482/",
      "name": "罗伯特·廷斯利 Robert Tinsley"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1393240/",
      "name": "费斯·洛根 Faith Logan"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392723/",
      "name": "保罗·皮尔斯伯里 Paul Pillsbury"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392752/",
      "name": "特拉维斯·汤普森 Travis Thompson"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1415276/",
      "name": "亚历珊德拉‧瑞秋·拉贝 Alexandra Rachael Rabe"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392777/",
      "name": "贾迈尔·钱伯斯 Jamel Chambers"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1412334/",
      "name": "杰克逊·艾顿 Jackson A. Dunn"
    }
  ]
,
  "datePublished": "2019-04-24",
  "genre": ["\u52a8\u4f5c", "\u79d1\u5e7b", "\u5947\u5e7b", "\u5192\u9669"],
  "duration": "PT3H1M",
  "description": "一声响指，宇宙间半数生命灰飞烟灭。几近绝望的复仇者们在惊奇队长（布丽·拉尔森 Brie Larson 饰）的帮助下找到灭霸（乔什·布洛林 Josh Brolin 饰）归隐之处，却得知六颗无限宝石均被销...",
  "@type": "Movie",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingCount": "828154",
    "bestRating": "10",
    "worstRating": "2",
    "ratingValue": "8.5"
  }
}
</script>


    <style type="text/css">
  
</style>
    <style type="text/css">img { max-width: 100%; }</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/77480d92e534c81c.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>
  
    <script type="text/javascript">var _body_start = new Date();</script>

    
    



    <link href="//img3.doubanio.com/dae/accounts/resources/1f8d15e/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://accounts.douban.com/passport/login?source=movie" class="nav-login" rel="nofollow">登录/注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="on">
      <a href="https://movie.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/1f8d15e/shire/bundle.js" defer="defer"></script>




    



    <link href="//img3.doubanio.com/dae/accounts/resources/1f8d15e/movie/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-movie" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;movie.douban.com">豆瓣电影</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;search.douban.com&#47;movie/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1002" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://movie.douban.com/cinema/nowplaying/"
     >影讯&购票</a>
    </li>
    <li    ><a href="https://movie.douban.com/explore"
     >选电影</a>
    </li>
    <li    ><a href="https://movie.douban.com/tv/"
     >电视剧</a>
    </li>
    <li    ><a href="https://movie.douban.com/chart"
     >排行榜</a>
    </li>
    <li    ><a href="https://movie.douban.com/tag/"
     >分类</a>
    </li>
    <li    ><a href="https://movie.douban.com/review/best/"
     >影评</a>
    </li>
    <li    ><a href="https://movie.douban.com/annual/2019?source=navigation"
     >2019年度榜单</a>
    </li>
    <li    ><a href="https://m.douban.com/standbyme/annual2019?source=navigation"
            target="_blank"
     >2019书影音报告</a>
    </li>
  </ul>
</div>

    <a href="https://movie.douban.com/annual/2019?source=movie_navigation" class="movieannual"></a>
  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= img}}" width="40" />
            <p>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                {{if sub_title}}
                    <br /><span>{{= sub_title}}</span>
                {{/if}}
                {{if address}}
                    <br /><span>{{= address}}</span>
                {{/if}}
                {{if episode}}
                    {{if episode=="unknow"}}
                        <br /><span>集数未知</span>
                    {{else}}
                        <br /><span>共{{= episode}}集</span>
                    {{/if}}
                {{/if}}
            </p>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/1f8d15e/movie/bundle.js" defer="defer"></script>





    
    <div id="wrapper">
        

        
    <div id="content">
        

    <div id="dale_movie_subject_top_icon"></div>
    <h1>
        <span property="v:itemreviewed">复仇者联盟4：终局之战 Avengers: Endgame</span>
            <span class="year">(2019)</span>
    </h1>

        <div class="grid-16-8 clearfix">
            

            
            <div class="article">
                
    

    





        <div class="indent clearfix">
            <div class="subjectwrap clearfix">
                <div class="subject clearfix">
                    



<div id="mainpic" class="">
    <a class="nbgnbg" href="https://movie.douban.com/subject/26100958/photos?type=R" title="点击看更多海报">
        <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2552058346.webp" title="点击看更多海报" alt="Avengers: Endgame" rel="v:image" />
   </a>
</div>

                    


<div id="info">
        <span ><span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1321812/" rel="v:directedBy">安东尼·罗素</a> / <a href="/celebrity/1320870/" rel="v:directedBy">乔·罗素</a></span></span><br/>
        <span ><span class='pl'>编剧</span>: <span class='attrs'><a href="/celebrity/1276125/">克里斯托弗·马库斯</a> / <a href="/celebrity/1276126/">斯蒂芬·麦克菲利</a> / <a href="/celebrity/1013888/">斯坦·李</a> / <a href="/celebrity/1050183/">杰克·科比</a> / <a href="/celebrity/1360715/">吉姆·斯特林</a></span></span><br/>
        <span class="actor"><span class='pl'>主演</span>: <span class='attrs'><a href="/celebrity/1016681/" rel="v:starring">小罗伯特·唐尼</a> / <a href="/celebrity/1017885/" rel="v:starring">克里斯·埃文斯</a> / <a href="/celebrity/1040505/" rel="v:starring">马克·鲁弗洛</a> / <a href="/celebrity/1021959/" rel="v:starring">克里斯·海姆斯沃斯</a> / <a href="/celebrity/1054453/" rel="v:starring">斯嘉丽·约翰逊</a> / <a href="/celebrity/1013770/" rel="v:starring">杰瑞米·雷纳</a> / <a href="/celebrity/1002667/" rel="v:starring">保罗·路德</a> / <a href="/celebrity/1036344/" rel="v:starring">凯伦·吉兰</a> / <a href="/celebrity/1053573/" rel="v:starring">唐·钱德尔</a> / <a href="/celebrity/1027194/" rel="v:starring">布丽·拉尔森</a> / <a href="/celebrity/1013757/" rel="v:starring">布莱德利·库珀</a> / <a href="/celebrity/1027395/" rel="v:starring">泰莎·汤普森</a> / <a href="/celebrity/1325351/" rel="v:starring">汤姆·赫兰德</a> / <a href="/celebrity/1129847/" rel="v:starring">伊丽莎白·奥尔森</a> / <a href="/celebrity/1009405/" rel="v:starring">本尼迪克特·康伯巴奇</a> / <a href="/celebrity/1025152/" rel="v:starring">蒂尔达·斯文顿</a> / <a href="/celebrity/1018985/" rel="v:starring">格温妮斯·帕特洛</a> / <a href="/celebrity/1004610/" rel="v:starring">蕾妮·罗素</a> / <a href="/celebrity/1022661/" rel="v:starring">约翰·斯拉特里</a> / <a href="/celebrity/1327680/" rel="v:starring">查德维克·博斯曼</a> / <a href="/celebrity/1027217/" rel="v:starring">安东尼·麦凯</a> / <a href="/celebrity/1021985/" rel="v:starring">塞巴斯蒂安·斯坦</a> / <a href="/celebrity/1017967/" rel="v:starring">克里斯·帕拉特</a> / <a href="/celebrity/1004596/" rel="v:starring">汤姆·希德勒斯顿</a> / <a href="/celebrity/1047985/" rel="v:starring">佐伊·索尔达娜</a> / <a href="/celebrity/1308787/" rel="v:starring">丹娜·奎里拉</a> / <a href="/celebrity/1301179/" rel="v:starring">本尼迪克特·王</a> / <a href="/celebrity/1313255/" rel="v:starring">庞·克莱门捷夫</a> / <a href="/celebrity/1014003/" rel="v:starring">戴夫·巴蒂斯塔</a> / <a href="/celebrity/1356810/" rel="v:starring">利蒂希娅·赖特</a> / <a href="/celebrity/1021963/" rel="v:starring">伊万杰琳·莉莉</a> / <a href="/celebrity/1027164/" rel="v:starring">乔恩·费儒</a> / <a href="/celebrity/1000051/" rel="v:starring">海莉·阿特维尔</a> / <a href="/celebrity/1054454/" rel="v:starring">娜塔莉·波特曼</a> / <a href="/celebrity/1047974/" rel="v:starring">玛丽莎·托梅</a> / <a href="/celebrity/1076354/" rel="v:starring">塔伊加·维迪提</a> / <a href="/celebrity/1025214/" rel="v:starring">安吉拉·贝塞特</a> / <a href="/celebrity/1053620/" rel="v:starring">迈克尔·道格拉斯</a> / <a href="/celebrity/1035642/" rel="v:starring">米歇尔·菲佛</a> / <a href="/celebrity/1031849/" rel="v:starring">威廉·赫特</a> / <a href="/celebrity/1000018/" rel="v:starring">寇碧·史莫德斯</a> / <a href="/celebrity/1022552/" rel="v:starring">肖恩·古恩</a> / <a href="/celebrity/1362864/" rel="v:starring">温斯顿·杜克</a> / <a href="/celebrity/1010545/" rel="v:starring">琳达·卡德里尼</a> / <a href="/celebrity/1339359/" rel="v:starring">马克斯米利亚诺·赫尔南德斯</a> / <a href="/celebrity/1100321/" rel="v:starring">弗兰克·格里罗</a> / <a href="/celebrity/1027879/" rel="v:starring">真田广之</a> / <a href="/celebrity/1332428/" rel="v:starring">汤姆-沃恩-劳勒</a> / <a href="/celebrity/1049713/" rel="v:starring">詹姆斯·达西</a> / <a href="/celebrity/1376777/" rel="v:starring">雅各布·巴特朗</a> / <a href="/celebrity/1041020/" rel="v:starring">范·迪塞尔</a> / <a href="/celebrity/1053617/" rel="v:starring">罗伯特·雷德福</a> / <a href="/celebrity/1004568/" rel="v:starring">乔什·布洛林</a> / <a href="/celebrity/1054408/" rel="v:starring">塞缪尔·杰克逊</a> / <a href="/celebrity/1210466/" rel="v:starring">伊薇特·尼科尔·布朗</a> / <a href="/celebrity/1392731/" rel="v:starring">卡梅伦·布鲁姆布罗</a> / <a href="/celebrity/1392730/" rel="v:starring">蒂莫西·卡尔</a> / <a href="/celebrity/1013874/" rel="v:starring">凯瑞·康顿</a> / <a href="/celebrity/1392741/" rel="v:starring">迈克尔·A·库克</a> / <a href="/celebrity/1342808/" rel="v:starring">凯莉·库恩</a> / <a href="/celebrity/1321687/" rel="v:starring">艾玛·福尔曼</a> / <a href="/celebrity/1392734/" rel="v:starring">雷纳·加拉赫</a> / <a href="/celebrity/1392732/" rel="v:starring">丹妮拉·加斯基</a> / <a href="/celebrity/1275017/" rel="v:starring">郑肯</a> / <a href="/celebrity/1392722/" rel="v:starring">小弗洛伊德·安东尼·约翰</a> / <a href="/celebrity/1013888/" rel="v:starring">斯坦·李</a> / <a href="/celebrity/1348037/" rel="v:starring">罗斯·马昆德</a> / <a href="/celebrity/1392739/" rel="v:starring">布伦特·麦吉</a> / <a href="/celebrity/1392737/" rel="v:starring">迈克尔·皮耶里诺·米勒</a> / <a href="/celebrity/1126747/" rel="v:starring">卡兰·马尔韦</a> / <a href="/celebrity/1341026/" rel="v:starring">泰瑞·诺塔里</a> / <a href="/celebrity/1133195/" rel="v:starring">吉米·雷·皮肯斯</a> / <a href="/celebrity/1344984/" rel="v:starring">迈克尔·詹姆斯·肖</a> / <a href="/celebrity/1322702/" rel="v:starring">泰·辛普金斯</a> / <a href="/celebrity/1392736/" rel="v:starring">格雷格·蒂芬</a></span></span><br/>
        <span class="pl">类型:</span> <span property="v:genre">动作</span> / <span property="v:genre">科幻</span> / <span property="v:genre">奇幻</span> / <span property="v:genre">冒险</span><br/>
        <span class="pl">官方网站:</span> <a href="http://www.marvel.com/movies/avengers-endgame" rel="nofollow" target="_blank">www.marvel.com/movies/avengers-endgame</a><br/>
        <span class="pl">制片国家/地区:</span> 美国<br/>
        <span class="pl">语言:</span> 英语 / 日语 / 科萨语<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="2019-04-24(中国大陆)">2019-04-24(中国大陆)</span> / <span property="v:initialReleaseDate" content="2019-04-26(美国)">2019-04-26(美国)</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content="181">181分钟</span><br/>
        <span class="pl">又名:</span> 复仇者联盟3：无尽之战(下) / 复联4 / Avengers: Infinity War - Part II / The Avengers 3: Part 2 / The Avengers 4: Endgame / AVG4<br/>
        <span class="pl">IMDb链接:</span> <a href="https://www.imdb.com/title/tt4154796" target="_blank" rel="nofollow">tt4154796</a><br>

</div>




                </div>
                    


<div id="interest_sectl">
    <div class="rating_wrap clearbox" rel="v:rating">
        <div class="clearfix">
          <div class="rating_logo ll">豆瓣评分</div>
          <div class="output-btn-wrap rr" style="display:none">
            <img src="https://img3.doubanio.com/f/movie/692e86756648f29457847c5cc5e161d6f6b8aaac/pics/movie/reference.png" />
            <a class="download-output-image" href="#">引用</a>
          </div>
          
          
        </div>
        



<div class="rating_self clearfix" typeof="v:Rating">
    <strong class="ll rating_num" property="v:average">8.5</strong>
    <span property="v:best" content="10.0"></span>
    <div class="rating_right ">
        <div class="ll bigstar bigstar45"></div>
        <div class="rating_sum">
                <a href="collections" class="rating_people">
                    <span property="v:votes">828178</span>人评价
                </a>
        </div>
    </div>
</div>
<div class="ratings-on-weight">
    
        <div class="item">
        
        <span class="stars5 starstop" title="力荐">
            5星
        </span>
        <div class="power" style="width:64px"></div>
        <span class="rating_per">46.6%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars4 starstop" title="推荐">
            4星
        </span>
        <div class="power" style="width:48px"></div>
        <span class="rating_per">35.4%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars3 starstop" title="还行">
            3星
        </span>
        <div class="power" style="width:21px"></div>
        <span class="rating_per">15.3%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars2 starstop" title="较差">
            2星
        </span>
        <div class="power" style="width:2px"></div>
        <span class="rating_per">1.9%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars1 starstop" title="很差">
            1星
        </span>
        <div class="power" style="width:1px"></div>
        <span class="rating_per">0.8%</span>
        <br />
        </div>
</div>

    </div>
        <div class="rating_betterthan">
            好于 <a href="/typerank?type_name=科幻&type=17&interval_id=100:90&action=">95% 科幻片</a><br/>
            好于 <a href="/typerank?type_name=动作&type=5&interval_id=100:90&action=">97% 动作片</a><br/>
        </div>
</div>


                
            </div>
                




<div id="interest_sect_level" class="clearfix">
        
            <a href="https://www.douban.com/reason=collectwish&amp;ck=" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-26100958-wish">
                <span>想看</span>
            </a>
            <a href="https://www.douban.com/reason=collectcollect&amp;ck=" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-26100958-collect">
                <span>看过</span>
            </a>
        <div class="ll j a_stars">
            
    
    评价:
    <span id="rating"> <span id="stars" data-solid="https://img3.doubanio.com/f/shire/5a2327c04c0c231bced131ddf3f4467eb80c1c86/pics/rating_icons/star_onmouseover.png" data-hollow="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" data-solid-2x="https://img3.doubanio.com/f/shire/7258904022439076d57303c3b06ad195bf1dc41a/pics/rating_icons/star_onmouseover@2x.png" data-hollow-2x="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png">

            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26100958-1">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star1" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26100958-2">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star2" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26100958-3">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star3" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26100958-4">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star4" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-26100958-5">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star5" width="16" height="16"/></a>
    </span><span id="rateword" class="pl"></span>
    <input id="n_rating" type="hidden" value=""  />
    </span>

        </div>
    

</div>


            

















<div class="gtleft">
    <ul class="ul_subject_menu bicelink color_gray pt6 clearfix">
        
    
        
                <li> 
    <img src="https://img3.doubanio.com/f/shire/cc03d0fcf32b7ce3af7b160a0b85e5e66b47cc42/pics/short-comment.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_cmnt_login'})" class="j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">写短评</a>
 </li>
                    <li> 
    
    <img src="https://img3.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_rv_login'})" class="j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">写影评</a>
 </li>
                <li> 
    



 </li>
                <li> 
   

   
    
    <span class="rec" id="电影-26100958">
    <a href= "#"
        data-type="电影"
        data-url="https://movie.douban.com/subject/26100958/"
        data-desc="电影《复仇者联盟4：终局之战 Avengers: Endgame》 (来自豆瓣) "
        data-title="电影《复仇者联盟4：终局之战 Avengers: Endgame》 (来自豆瓣) "
        data-pic="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2552058346.jpeg"
        class="bn-sharing ">
        分享到
    </a> &nbsp;&nbsp;
    </span>

    <script>
        if (!window.DoubanShareMenuList) {
            window.DoubanShareMenuList = [];
        }
        var __cache_url = __cache_url || {};

        (function(u){
            if(__cache_url[u]) return;
            __cache_url[u] = true;
            window.DoubanShareIcons = 'https://img3.doubanio.com/f/shire/d15ffd71f3f10a7210448fec5a68eaec66e7f7d0/pics/ic_shares.png';

            var initShareButton = function() {
                $.ajax({url:u,dataType:'script',cache:true});
            };

            if (typeof Do == 'function' && 'ready' in Do) {
                Do(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js',
                    initShareButton
                );
            } else if(typeof Douban == 'object' && 'loader' in Douban) {
                Douban.loader.batch(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js'
                ).done(initShareButton);
            }

        })('https://img3.doubanio.com/f/movie/32be6727ed3ad8f6c4a417d8a086355c3e7d1d27/js/movie/lib/sharebutton.js');
    </script>


  </li>
            

    </ul>

    <script type="text/javascript">
        $(function(){
            $(".ul_subject_menu li.rec .bn-sharing").bind("click", function(){
                $.get("/blank?sbj_page_click=bn_sharing");
            });
            $(".ul_subject_menu .create_from_menu").bind("click", function(e){
                e.preventDefault();
                var $el = $(this);
                var glRoot = document.getElementById('gallery-topics-selection');
                if (window.has_gallery_topics && glRoot) {
                    // 判断是否有话题
                    glRoot.style.display = 'block';
                } else {
                    location.href = $el.attr('href');
                }
            });
        });
    </script>
</div>




                




    <style type="text/css">
        
.suggestions-list li { position: relative; left: 0; top: 0; margin-bottom: 7px; height: 35px }
.suggestions-list li .user-thumb { display: inline-block; *display: inline; float: left; margin: 2px 5px 0 0; vertical-align: top }
.suggestions-list li .user-thumb img { width: 25px; height: 25px }
.suggestions-list li .user-name-info { display: inline-block; *display: inline; line-height: 1.4em }
.suggestions-list li .user-name-info .user-profile-link { color: #333; font-weight: 800 }
.suggestions-list li .user-name-info .user-profile-link:hover { color: #4b8dc5 }
.suggestions-list li .user-name-info p { color: #999 }
.suggestions-list li .user-name-info b { color: #4b8dc5; font-weight: normal; cursor: pointer }
.suggestions-list li .user-name-info b:hover { text-decoration: underline }
.suggestions-list li .dismiss { position: absolute }
.suggestions-list li .dismiss { color: #aaa; margin: 0 0 0 10px; top: 0; right: 0 }
.suggestions-list li .dismiss:hover { color: #333; text-decoration: none }


.suggest-overlay { position: absolute; z-index: 99; width: auto; background: #fff; border: 1px solid #c5c7d2;
    -moz-border-radius : 3px;
    -webkit-border-radius : 3px;
    border-radius: 3px
}
.suggest-overlay .bd { min-width: 220px; line-height: 1; background: #fafafa; color: #b3b3b3; padding: 5px;
    -moz-border-radius : 3px;
    -webkit-border-radius : 3px;
    border-radius: 3px
}
.suggest-overlay ul { color: #999; padding: 3px 0; min-width: 214px }
.suggest-overlay li { cursor: pointer; padding: 3px 7px }
.suggest-overlay li b { font-weight: bold }
.suggest-overlay li .username { color: #333 }
.suggest-overlay img { margin-right: 5px; width: 20px; height: 20px; vertical-align: middle }
.suggest-overlay .on { background: #e9f0f8 }

.mentioned-highlighter { font: 14px/20px "Helvetica Neue",Helvetica,Arial,sans-serif; position: absolute; left: 4px; top: 4px; font-size: 14px; height: 60px; width: 98.5%; overflow: hidden; background: #fff; white-space: pre-wrap; word-wrap: break-word; color: transparent }
.mentioned-highlighter b { font-weight: normal; background-color: #d2e1f3; color: transparent;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  border-radius: 2px
}

        .movie-share-dialog .bn-flat input {
    font-size: 14px;
}
.movie-share-dialog {
    z-index: 100;
}
.movie-share-dialog .form-ft-inner{
    text-align: right;
}
.movie-share-dialog div.bd {
    padding: 0;
}

.movie-share .form-bd .input-area {
    position: relative;
    margin: 15px;
    height: 91px;
    zoom: 1;
}

.movie-share-no-media .form-bd {
    height: 140px;
}

.movie-share-dialog .share-text {
    height: 85px;
    position: absolute;
    z-index: 9;
    background: transparent;
    font: 14px/18px "Helvetica Neue",Helvetica,Arial,sans-serif;
    width: 98%;
    -webkit-border-radius: 4px 4px 4px 4px;
    border-radius: 4px 4px 4px 4px;
}

.movie-share-dialog .mentioned-highlighter {
    width: 483px;
    padding: 3px 4px 4px;
    color: white;
    position: absolute;
    top:0;
    left:0;
    z-index: 0;
}

.movie-share-dialog .mentioned-highlighter code {
    color: #D2E1F3;
    background: #D2E1F3;
    border-radius: 2px;
    padding-right: 1px;
    display: inline-block;
    font: 14px/18px "Helvetica Neue",Helvetica,Arial,sans-serif;
}


.movie-share .form-ft {
    background: #e9eef2;
    height: 25px;
    padding-top: 10px;
    padding-bottom: 10px;
}

.movie-share .form-ft-inner {
    height: 25px;
    padding-left: 15px;
    padding-right: 15px;
}

.movie-share-dialog .dialog-only-text {
    text-align: center;
    font-size: 14px;
    line-height: 1.5;
    padding-top: 30px;
    padding-bottom: 30px;
    color: #0c7823;
}

.movie-share-dialog .ll {
    float: left;
    display: inline;
}
.movie-share-dialog .share-label {
    width: auto;
    display: inline;
    float: none;
}

.movie-share-dialog .leading-label {
    _vertical-align: -2px;
}
.movie-share-dialog .media {
    float: left;
    margin-right: 10px;
    max-width: 100px;
    max-height: 100px;
    *width: 100px;
}
.movie-share-dialog .info-area{
    overflow: hidden;
    zoom: 1;
    margin: 0 15px 15px;
    height: 100px;
}
.movie-share-dialog .info-area strong{
    font-weight: bold;
}
.movie-share-dialog .info-area p{
    margin: 3px 0;
    color: #999;
}

.movie-share-dialog #sync-setting {
    _vertical-align: -5px;
    margin-left: 10px;
}

.movie-share-dialog .info-area .server-error {
    position: absolute;
    bottom: 45px;
    right: 15px;
    color: red;
}

.movie-share-dialog .avail-num-indicator {
    color: #aaa;
    font-weight: 800;
    padding-right: 3px;
}

.movie-share-dialog .bottom-setting {
    width: 432px;
}
.movie-share-dialog .input-checkbox {
    vertical-align: -2px;
    _vertical-align: -1px;
}

.movie-share-dialog #sync-setting img {
    _vertical-align: 2px;
}



.suggest-overlay {
    z-index: 2000;
}

.movie-bar {
    position: relative;
    margin-top: 10px;
}

.movie-bar-fav {
    position: absolute;
    top: 0;
    right: 0;
}

    </style>
    <script src="https://img3.doubanio.com/f/shire/a40c5220b3f40ce737b366c0030ecf810b37bfea/js/lib/mustache.js" type="text/javascript"></script>
    <script src="https://img3.doubanio.com/f/shire/1d985568f3cc434b145983919d9954e2ca627e9c/js/lib/textarea-mention.js" type="text/javascript"></script>
    <script src="https://img3.doubanio.com/f/movie/230795bbf6a9a7700cc6f395067493d5dcc572ad/js/movie/share.js" type="text/javascript"></script>

<div class="rec-sec">
<span class="rec">
    <script id="movie-share" type="text/x-html-snippet">
        
    <form class="movie-share" action="/j/share" method="POST">
        <div class="clearfix form-bd">
            <div class="input-area">
                <textarea name="text" class="share-text" cols="72" data-mention-api="https://api.douban.com/shuo/in/complete?alt=xd&amp;callback=?"></textarea>
                <input type="hidden" name="target-id" value="26100958">
                <input type="hidden" name="target-type" value="0">
                <input type="hidden" name="title" value="复仇者联盟4：终局之战 Avengers: Endgame‎ (2019)">
                <input type="hidden" name="desc" value="导演 安东尼·罗素 主演 小罗伯特·唐尼 / 克里斯·埃文斯 / 美国 / 8.5分(828178评价)">
                <input type="hidden" name="redir" value=""/>
                <div class="mentioned-highlighter"></div>
            </div>

            <div class="info-area">
                    <img class="media" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2552058346.webp" />
                <strong>复仇者联盟4：终局之战 Avengers: Endgame‎ (2019)</strong>
                <p>导演 安东尼·罗素 主演 小罗伯特·唐尼 / 克里斯·埃文斯 / 美国 / 8.5分(828178评价)</p>
                <p class="error server-error">&nbsp;</p>
            </div>
        </div>
        <div class="form-ft">
            <div class="form-ft-inner">
                



                <span class="avail-num-indicator">140</span>
                <span class="bn-flat">
                    <input type="submit" value="推荐" />
                </span>
            </div>
        </div>
    </form>
    
    <div id="suggest-mention-tmpl" style="display:none;">
        <ul>
            {{#users}}
            <li id="{{uid}}">
              <img src="{{avatar}}">{{{username}}}&nbsp;<span>({{{uid}}})</span>
            </li>
            {{/users}}
        </ul>
    </div>


    </script>

        
        <a href="/accounts/register?reason=recommend"  class="j a_show_login lnk-sharing" 
            share-id="26100958" 
            data-mode="plain" data-name="复仇者联盟4：终局之战 Avengers: Endgame‎ (2019)" 
            data-type="movie" data-desc="导演 安东尼·罗素 主演 小罗伯特·唐尼 / 克里斯·埃文斯 / 美国 / 8.5分(828178评价)" 
            data-href="https://movie.douban.com/subject/26100958/" data-image="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2552058346.webp" 
            data-properties="{}" 
            data-redir="" data-text="" 
            data-apikey="" data-curl="" 
            data-count="10" data-object_kind="1002" 
            data-object_id="26100958" data-target_type="rec" 
            data-target_action="0" 
            data-action_props="{&#34;subject_url&#34;:&#34;https:\/\/movie.douban.com\/subject\/26100958\/&#34;,&#34;subject_title&#34;:&#34;复仇者联盟4：终局之战 Avengers: Endgame‎ (2019)&#34;}">推荐</a>
</span>


</div>






            <script type="text/javascript">
                $(function() {
                    $('.collect_btn', '#interest_sect_level').each(function() {
                        Douban.init_collect_btn(this);
                    });
                    $('html').delegate(".indent .rec-sec .lnk-sharing", "click", function() {
                        moreurl(this, {
                            from : 'mv_sbj_db_share'
                        });
                    });
                });
            </script>
        </div>
            


    <div id="collect_form_26100958"></div>


        



<div class="related-info" style="margin-bottom:-10px;">
    <a name="intro"></a>
    
        
            
            
    <h2>
        <i class="">复仇者联盟4：终局之战的剧情简介</i>
              · · · · · ·
    </h2>

            <div class="indent" id="link-report">
                    
                        <span property="v:summary" class="">
                                　　一声响指，宇宙间半数生命灰飞烟灭。几近绝望的复仇者们在惊奇队长（布丽·拉尔森 Brie Larson 饰）的帮助下找到灭霸（乔什·布洛林 Josh Brolin 饰）归隐之处，却得知六颗无限宝石均被销毁，希望彻底破灭。如是过了五年，迷失在量子领域的蚁人（保罗·路德 Paul Rudd 饰）意外回到现实世界，他的出现为幸存的复仇者们点燃了希望。与美国队长（克里斯·埃文斯 Chris Evans 饰）冰释前嫌的托尼（小罗伯特·唐尼 Robert Downey Jr. 饰）找到了穿越时空的方法，星散各地的超级英雄再度集结，他们分别穿越不同的时代去搜集无限宝石。而在这一过程中，平行宇宙的灭霸察觉了他们的计划。
                                    <br />
                                　　注定要载入史册的最终决战，超级英雄们为了心中恪守的信念前仆后继……
                        </span>
                        <span class="pl"><a href="https://movie.douban.com/help/movie#t0-qs">&copy;豆瓣</a></span>
            </div>
</div>


    <div id="dale_movie_subject_banner_after_intro"></div>

    








<div id="celebrities" class="celebrities related-celebrities">

  
    <h2>
        <i class="">复仇者联盟4：终局之战的演职员</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="/subject/26100958/celebrities">全部 140</a>
            )
            </span>
    </h2>


  <ul class="celebrities-list from-subject __oneline">
        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1321812/" title="安东尼·罗素 Anthony Russo" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1555672594.77.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1321812/" title="安东尼·罗素 Anthony Russo" class="name">安东尼·罗素</a></span>

      <span class="role" title="导演">导演</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1320870/" title="乔·罗素 Joe Russo" class="has-account">
      <div class="avatar has-account" style="background-image: url(https://img3.doubanio.com/f/movie/14960825e118267b5857fc0ae9f306ef8c74da8f/pics/movie/has_douban@2x.png), url(https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1525505053.79.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1320870/" title="乔·罗素 Joe Russo" class="name">乔·罗素</a></span>

      <span class="role" title="导演">导演</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1016681/" title="小罗伯特·唐尼 Robert Downey Jr." class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p56339.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1016681/" title="小罗伯特·唐尼 Robert Downey Jr." class="name">小罗伯特·唐尼</a></span>

      <span class="role" title="饰 钢铁侠 Tony Stark / Iron Man">饰 钢铁侠 Tony Stark / Iron Man</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1017885/" title="克里斯·埃文斯 Chris Evans" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1359877729.49.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1017885/" title="克里斯·埃文斯 Chris Evans" class="name">克里斯·埃文斯</a></span>

      <span class="role" title="饰 美国队长 Steve Rogers / Captain America">饰 美国队长 Steve Rogers / Captain America</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1040505/" title="马克·鲁弗洛 Mark Ruffalo" class="">
      <div class="avatar" style="background-image: url(https://img9.doubanio.com/view/celebrity/s_ratio_celebrity/public/p15885.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1040505/" title="马克·鲁弗洛 Mark Ruffalo" class="name">马克·鲁弗洛</a></span>

      <span class="role" title="饰 浩克 Bruce Banner / Hulk">饰 浩克 Bruce Banner / Hulk</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1021959/" title="克里斯·海姆斯沃斯 Chris Hemsworth" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1425725663.63.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1021959/" title="克里斯·海姆斯沃斯 Chris Hemsworth" class="name">克里斯·海姆斯沃斯</a></span>

      <span class="role" title="饰 雷神 Thor">饰 雷神 Thor</span>

    </div>
  </li>


  </ul>
</div>


    


<link rel="stylesheet" href="https://img3.doubanio.com/f/verify/16c7e943aee3b1dc6d65f600fcc0f6d62db7dfb4/entry_creator/dist/author_subject/style.css">
<div id="author_subject" class="author-wrapper">
    <div class="loading"></div>
</div>
<script type="text/javascript">
    var answerObj = {
      ISALL: 'False',
      TYPE: 'movie',
      SUBJECT_ID: '26100958',
      USER_ID: 'None'
    }
</script>
<script type="text/javascript" src="https://img3.doubanio.com/f/movie/61252f2f9b35f08b37f69d17dfe48310dd295347/js/movie/lib/react/15.4/bundle.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/verify/ac140ef86262b845d2be7b859e352d8196f3f6d4/entry_creator/dist/author_subject/index.js"></script>


    









    
    <div id="related-pic" class="related-pic">
        
    
    
    <h2>
        <i class="">复仇者联盟4：终局之战的视频和图片</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/26100958/trailer#trailer">预告片21</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/26100958/trailer#short_video">视频评论8</a>&nbsp;·&nbsp;<a href="/video/create?subject_id=26100958">添加</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/26100958/all_photos">图片3170</a>&nbsp;·&nbsp;<a href="https://movie.douban.com/subject/26100958/mupload">添加</a>
            )
            </span>
    </h2>


        <ul class="related-pic-bd  wide_videos">
                <li class="label-trailer">
                    <a class="related-pic-video" href="https://movie.douban.com/trailer/244458/#content" title="预告片" style="background-image:url(https://img3.doubanio.com/img/trailer/medium/2550759113.jpg?)">
                    </a>
                </li>
                
                <li class="label-short-video">
                    <a class="related-pic-video" href="https://movie.douban.com/video/104036/" title="视频评论" style="background-image:url(https://img9.doubanio.com/view/photo/photo/public/p2568556885.webp?)">
                    </a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2553240846/"><img src="https://img9.doubanio.com/view/photo/sqxs/public/p2553240846.webp" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2552111742/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p2552111742.webp" alt="图片" /></a>
                </li>
        </ul>
    </div>




    
    



<style type="text/css">
.award li { display: inline; margin-right: 5px }
.awards { margin-bottom: 20px }
.awards h2 { background: none; color: #000; font-size: 14px; padding-bottom: 5px; margin-bottom: 8px; border-bottom: 1px dashed #dddddd }
.awards .year { color: #666666; margin-left: -5px }
.mod { margin-bottom: 25px }
.mod .hd { margin-bottom: 10px }
.mod .hd h2 {margin:24px 0 3px 0}
</style>


<div class="mod">
    <div class="hd">
        
    <h2>
        <i class="">复仇者联盟4：终局之战的获奖情况</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/26100958/awards/">全部</a>
            )
            </span>
    </h2>

    </div>
        
        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/Oscar/92/">第92届奥斯卡金像奖</a>
            </li>
            <li>最佳视觉效果(提名)</li>
            <li><a href='https://movie.douban.com/celebrity/1282937/' target='_blank'>拉塞尔·厄尔</a>&nbsp;/&nbsp;<a href='https://movie.douban.com/celebrity/1388220/' target='_blank'>丹·德里伍</a>&nbsp;/&nbsp;<a href='https://movie.douban.com/celebrity/1276892/' target='_blank'>Matt Aitken</a>&nbsp;/&nbsp;<a href='https://movie.douban.com/celebrity/1298615/' target='_blank'>丹尼尔·萨迪克</a></li>
        </ul>
        
        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/bafta/73/">第73届英国电影学院奖</a>
            </li>
            <li>电影奖 最佳特殊视觉效果(提名)</li>
            <li></li>
        </ul>
        
        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/annie/47/">第47届动画安妮奖</a>
            </li>
            <li>最佳真人电影动画角色</li>
            <li></li>
        </ul>
</div>

    








    <div id="recommendations" class="">
        
        
    <h2>
        <i class="">喜欢这部电影的人也喜欢</i>
              · · · · · ·
    </h2>

        
    
    <div class="recommendations-bd">
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/24773958/?from=subject-page" >
                    <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2517753454.webp" alt="复仇者联盟3：无限战争" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/24773958/?from=subject-page" class="" >复仇者联盟3：无限战争</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1432146/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p725871968.webp" alt="钢铁侠" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1432146/?from=subject-page" class="" >钢铁侠</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/25820460/?from=subject-page" >
                    <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2332503406.webp" alt="美国队长3" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/25820460/?from=subject-page" class="" >美国队长3</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/4920389/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2516578307.webp" alt="头号玩家" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/4920389/?from=subject-page" class="" >头号玩家</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/10485647/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2181156848.webp" alt="X战警：逆转未来" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/10485647/?from=subject-page" class="" >X战警：逆转未来</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/26213252/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2546360443.webp" alt="惊奇队长" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/26213252/?from=subject-page" class="" >惊奇队长</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1866475/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2517193090.webp" alt="无敌浩克" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1866475/?from=subject-page" class="" >无敌浩克</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1866473/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2266823371.webp" alt="蚁人" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1866473/?from=subject-page" class="" >蚁人</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/6560058/?from=subject-page" >
                    <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2156839164.webp" alt="雷神2：黑暗世界" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/6560058/?from=subject-page" class="" >雷神2：黑暗世界</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/7065154/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2198455702.webp" alt="银河护卫队" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/7065154/?from=subject-page" class="" >银河护卫队</a>
            </dd>
        </dl>
    </div>

    </div>



        


<script type="text/x-handlebar-tmpl" id="comment-tmpl">
    <div class="dummy-fold">
        {{#each comments}}
        <div class="comment-item" data-cid="id">
            <div class="comment">
                <h3>
                    <span class="comment-vote">
                            <span class="votes">{{votes}}</span>
                        <input value="{{id}}" type="hidden"/>
                        <a href="javascript:;" class="j {{#if ../if_logined}}a_vote_comment{{else}}a_show_login{{/if}}">有用</a>
                    </span>
                    <span class="comment-info">
                        <a href="{{user.path}}" class="">{{user.name}}</a>
                        {{#if rating}}
                        <span class="allstar{{rating}}0 rating" title="{{rating_word}}"></span>
                        {{/if}}
                        <span>
                            {{time}}
                        </span>
                        <p> {{content_tmpl content}} </p>
                    </span>
            </div>
        </div>
        {{/each}}
    </div>
</script>












    

    <div id="comments-section">
        <div class="mod-hd">
            
            
        <a class="comment_btn j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">
            <span>我要写短评</span>
        </a>

            
    <h2>
        <i class="">复仇者联盟4：终局之战的短评</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/26100958/comments?status=P">全部 254586 条</a>
            )
            </span>
    </h2>

            
        </div>
        <div class="mod-bd">
                

    <div class="tab-hd">
        <a id="hot-comments-tab" href="comments" data-id="hot" class="on">热门</a>&nbsp;/&nbsp;
            <a id="new-comments-tab" href="comments?sort=time" data-id="new">最新</a>&nbsp;/&nbsp;
        <a id="following-comments-tab" href="follows_comments" data-id="following"  class="j a_show_login">好友</a>
    </div>

    <div class="tab-bd">
        <div id="hot-comments" class="tab">
            
    
        
        <div class="comment-item" data-cid="1364011224">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">35950</span>
                <input value="1364011224" type="hidden"/>
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/146803809/" class="">棠枫海</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2019-04-24 02:23:59">
                    2019-04-24
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">如果你不喜欢这部电影，说明他不是为你准备的，故事的终章是为读过故事的人准备的</span>
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1762730748">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">9700</span>
                <input value="1762730748" type="hidden"/>
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/123229428/" class="">雁落孤山</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2019-04-24 02:52:20">
                    2019-04-24
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">I AM IRONMAN.</span>
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1762727048">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">9368</span>
                <input value="1762727048" type="hidden"/>
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/145575037/" class="">梅西</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2019-04-24 02:40:40">
                    2019-04-24
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">凡人之躯 比肩神明 最后真的泪目</span>
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1762708307">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">2744</span>
                <input value="1762708307" type="hidden"/>
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/3677758/" class="">感谢政府感谢党</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2019-04-24 01:46:26">
                    2019-04-24
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">三个小时剧情太拖沓，成了七龙珠寻宝了，堆砌拼凑的剧情，真是不知道浪费睡觉时间来看首映。</span>
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="922792980">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">1891</span>
                <input value="922792980" type="hidden"/>
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/49136180/" class="">哆啦A梦你在吗</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2019-04-24 02:51:09">
                    2019-04-24
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">我爱 小罗伯特·唐尼 / 克里斯·埃文斯 / 克里斯·海姆斯沃斯 / 杰瑞米·雷纳 / 马克·鲁弗洛 / 斯嘉丽·约翰逊  以及漫威所有的人！十年青春，感谢有你，此生不悔！！！</span>
                
                <a class="source-icon" href="https://www.douban.com/doubanapp/" target="_blank"><img src="https://img3.doubanio.com/f/shire/c541f3cbc321589b29d7c7b6d00e620243f224d9/pics/comment/iphone.png" title="发自iPhone" alt="iPhone" rel="v:image"/></a>
        </p>
    </div>

        </div>



                
                &gt; <a href="comments?sort=new_score&status=P" >
                    更多短评
                        254586条
                </a>
        </div>
        <div id="new-comments" class="tab">
            <div id="normal">
            </div>
            <div class="fold-hd hide">
                <a class="qa" href="/help/opinion#t2-q0" target="_blank">为什么被折叠？</a>
                <a class="btn-unfold" href="#">有一些短评被折叠了</a>
                <div class="qa-tip">
                    评论被折叠，是因为发布这条评论的帐号行为异常。评论仍可以被展开阅读，对发布人的账号不造成其他影响。如果认为有问题，可以<a href="https://help.douban.com/help/ask?category=movie">联系</a>豆瓣电影。
                </div>
            </div>
            <div class="fold-bd">
            </div>
            <span id="total-num"></span>
        </div>
        <div id="following-comments" class="tab">
            
    


        <div class="comment-item">
            你关注的人还没写过短评
        </div>

        </div>
    </div>


            
            
        </div>
    </div>



        

<link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/1e4177a528d7c149.css">

<section class="topics mod">
    <header>
        <h2>
            复仇者联盟4：终局之战的话题 · · · · · ·
            <span class="pl">( <span class="gallery_topics">全部 <span id="topic-count"></span> 条</span> )</span>
        </h2>
    </header>

    




<section class="subject-topics">
    <div class="topic-guide" id="topic-guide">
        <img class="ic_question" src="//img3.doubanio.com/f/ithildin/b1a3edea3d04805f899e9d77c0bfc0d158df10d5/pics/export/icon_question.png">
        <div class="tip_content">
            <div class="tip_title">什么是话题</div>
            <div class="tip_desc">
                <div>无论是一部作品、一个人，还是一件事，都往往可以衍生出许多不同的话题。将这些话题细分出来，分别进行讨论，会有更多收获。</div>
            </div>
        </div>
        <img class="ic_guide" src="//img3.doubanio.com/f/ithildin/529f46d86bc08f55cd0b1843d0492242ebbd22de/pics/export/icon_guide_arrow.png">
        <img class="ic_close" id="topic-guide-close" src="//img3.doubanio.com/f/ithildin/2eb4ad488cb0854644b23f20b6fa312404429589/pics/export/close@3x.png">
    </div>

    <div id="topic-items"></div>

    <script>
        window.subject_id = 26100958;
        window.join_label_text = '写影评参与';

        window.topic_display_count = 4;
        window.topic_item_display_count = 1;
        window.no_content_fun_call_name = "no_topic";

        window.guideNode = document.getElementById('topic-guide');
        window.guideNodeClose = document.getElementById('topic-guide-close');
    </script>
    
        <link rel="stylesheet" href="https://img3.doubanio.com/f/ithildin/f731c9ea474da58c516290b3a6b1dd1237c07c5e/css/export/subject_topics.css">
        <script src="https://img3.doubanio.com/f/ithildin/d3590fc6ac47b33c804037a1aa7eec49075428c8/js/export/moment-with-locales-only-zh.js"></script>
        <script src="https://img3.doubanio.com/f/ithildin/c600fdbe69e3ffa5a3919c81ae8c8b4140e99a3e/js/export/subject_topics.js"></script>

</section>

    <script>
        function no_topic(){
            $('#content .topics').remove();
        }
    </script>
</section>
    <section class="reviews mod movie-content">
        <header>
            <a href="new_review" rel="nofollow" class="create-review comment_btn "
                data-isverify="False"
                data-verify-url="https://www.douban.com/accounts/phone/verify?redir=http://movie.douban.com/subject/26100958/new_review">
                <span>我要写影评</span>
            </a>
            <h2>
                复仇者联盟4：终局之战的影评 · · · · · ·
                <span class="pl">( <a href="reviews">全部 5798 条</a> )</span>
            </h2>
        </header>

        

<style>
#gallery-topics-selection {
  position: fixed;
  width: 595px;
  padding: 40px 40px 33px 40px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 16px 0 rgba(0, 0, 0, 0.2);
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  z-index: 9999;
}
#gallery-topics-selection h1 {
  font-size: 18px;
  color: #007722;
  margin-bottom: 36px;
  padding: 0;
  line-height: 28px;
  font-weight: normal;
}
#gallery-topics-selection .gl_topics {
  border-bottom: 1px solid #dfdfdf;
  max-height: 298px;
  overflow-y: scroll;
}
#gallery-topics-selection .topic {
  margin-bottom: 24px;
}
#gallery-topics-selection .topic_name {
  font-size: 15px;
  color: #333;
  margin: 0;
  line-height: inherit;
}
#gallery-topics-selection .topic_meta {
  font-size: 13px;
  color: #999;
}
#gallery-topics-selection .topics_skip {
  display: block;
  cursor: pointer;
  font-size: 16px;
  color: #3377AA;
  text-align: center;
  margin-top: 33px;
}
#gallery-topics-selection .topics_skip:hover {
  background: transparent;
}
#gallery-topics-selection .close_selection {
  position: absolute;
  width: 30px;
  height: 20px;
  top: 46px;
  right: 40px;
  background: #fff;
  color: #999;
  text-align: right;
}
#gallery-topics-selection .close_selection:hover{
  background: #fff;
  color: #999;
}
</style>




            <div class="review_filter">
                <a href="javascript:;;" class="cur" data-sort="">热门</a href="javascript:;;"> /
                <a href="javascript:;;" data-sort="time">最新</a href="javascript:;;"> /
                <a href="javascript:;;" data-sort="follow">好友</a href="javascript:;;">
                
            </div>


            



<div class="review-list  ">
        
    

        
    
    <div data-cid="10133071">
        <div class="main review-item" id="10133071">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/lingrui1995/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/u63688511-18.jpg">
        </a>

        <a href="https://www.douban.com/people/lingrui1995/" class="name">凌睿</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2019-04-24" class="main-meta">2019-04-24 07:17:48</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10133071/">《复联4》以及MCU剧情、人物、彩蛋全解（2.8万字长文）</a></h2>

                <div id="review_10133071_short" class="review-short" data-rid="10133071">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        从2008年的《钢铁侠1》到2019年的《复联4》，11年时间，22部电影，构成了这个雄伟壮阔的漫威电影宇宙。 说到MCU，每个人的观感不尽相同。 有人被它震撼的视觉效果所征服，有人喜欢那些猝不及防的幽默瞬间； 有人被复仇者们保卫世界的责任感所打动，有人理解灭霸、埃里克等每位...

                        &nbsp;(<a href="javascript:;" id="toggle-10133071-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10133071_full" class="hidden">
                    <div id="review_10133071_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10133071" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-10133071">
                                21647
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10133071" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-10133071">
                                859
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10133071/#comments" class="reply ">1446回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10134635">
        <div class="main review-item" id="10134635">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/busanmovie/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/u134916477-8.jpg">
        </a>

        <a href="https://www.douban.com/people/busanmovie/" class="name">不散</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2019-04-24" class="main-meta">2019-04-24 18:28:30</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10134635/">《复联4》最全100个彩蛋，我们给你找齐了</a></h2>

                <div id="review_10134635_short" class="review-short" data-rid="10134635">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        4月24日，《复联4》在国内上映，中国大陆也首次早于北美，成为全球最早上映的国家地区之一。这一次，终于轮到我们给外国网友剧透了。 对于这样的福利，国内影迷也拿出百分百热情。光是昨晚零点场，就有上百万观众走进电影院，共同第一时间见证一个时代的终结。 历时11年，经过2...

                        &nbsp;(<a href="javascript:;" id="toggle-10134635-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10134635_full" class="hidden">
                    <div id="review_10134635_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10134635" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-10134635">
                                8280
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10134635" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-10134635">
                                306
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10134635/#comments" class="reply ">1422回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10133679">
        <div class="main review-item" id="10133679">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/174806215/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/u174806215-7.jpg">
        </a>

        <a href="https://www.douban.com/people/174806215/" class="name">..elv</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2019-04-24" class="main-meta">2019-04-24 12:15:59</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10133679/">可爱的女人与让人生厌的女神</a></h2>

                <div id="review_10133679_short" class="review-short" data-rid="10133679">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        妇联4不是一部失败之作，甚至可以说是巅峰之作，至少这一部里人终于有了人样，而不是为了市场喜好定制的人设。 但在视觉奇观的兴奋退却后，最让我越发不适的不是逻辑崩坏带来的困惑，而是电影里两位女性的诠释，黑寡妇和惊奇队长，一个女人，和一个“女神”。 先谈谈娜塔莎，说...

                        &nbsp;(<a href="javascript:;" id="toggle-10133679-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10133679_full" class="hidden">
                    <div id="review_10133679_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10133679" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-10133679">
                                4421
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10133679" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-10133679">
                                426
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10133679/#comments" class="reply ">879回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10132877">
        <div class="main review-item" id="10132877">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/68608189/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u68608189-3.jpg">
        </a>

        <a href="https://www.douban.com/people/68608189/" class="name">启真湖千纸鹤</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2019-04-24" class="main-meta">2019-04-24 04:32:32</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10132877/">复联4剧情梳理（剧透慎入，简洁易懂）</a></h2>

                <div id="review_10132877_short" class="review-short" data-rid="10132877">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        真剧透慎入！ 真剧透慎入！ 真剧透慎入！ 回车够多了，准备好了吗？Let us begin. 1. 鹰眼在教女儿射箭，一回头爱人孩子俱为土灰。 2. 漫威经典开头动画 3. 钢铁侠和星云在宇宙漂流，钢铁侠对小辣椒说了真挚的心里话，被惊奇队长救起，托着飞船直接回到地球复仇者联盟总部。 4....

                        &nbsp;(<a href="javascript:;" id="toggle-10132877-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10132877_full" class="hidden">
                    <div id="review_10132877_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10132877" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-10132877">
                                1534
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10132877" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-10132877">
                                143
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10132877/#comments" class="reply ">1295回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="9363635">
        <div class="main review-item" id="9363635">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/159334651/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u159334651-2.jpg">
        </a>

        <a href="https://www.douban.com/people/159334651/" class="name">陆小虾</a>


        <span content="2018-05-13" class="main-meta">2018-05-13 10:38:24</span>

            <a class="rel-topic" target="_blank" href="//www.douban.com/gallery/topic/《复仇者联盟4》情节猜想">#《复仇者联盟4》情节猜想</a>

    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/9363635/">根据复联3的细节完美推理复联4剧情</a></h2>

                <div id="review_9363635_short" class="review-short" data-rid="9363635">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        翻遍了豆瓣的评论，发现对于复联4的剧情推论都是各偏一词，没有很强的逻辑说服力，现在通过对复联3的细节推理来对复联4的剧情进行合理的解剖，希望这是终结篇。 首先网上之前爆出的号称复联4现场剧照是位于纽约大战现场，于是大部分网友都认为是利用时间宝石穿梭回了过去来改变...

                        &nbsp;(<a href="javascript:;" id="toggle-9363635-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_9363635_full" class="hidden">
                    <div id="review_9363635_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="9363635" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-9363635">
                                697
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="9363635" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-9363635">
                                55
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/9363635/#comments" class="reply ">729回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10135191">
        <div class="main review-item" id="10135191">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/3056342/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u3056342-2.jpg">
        </a>

        <a href="https://www.douban.com/people/3056342/" class="name">Royma</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2019-04-24" class="main-meta">2019-04-24 22:19:48</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10135191/">撕开情怀的外衣</a></h2>

                <div id="review_10135191_short" class="review-short" data-rid="10135191">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        从另一条时间线穿越过来的灭霸指挥飞船，直接用导弹直接摧毁复仇者联盟总部。那一刻，我忍不住惊呼：“神作！” 反套路的经典！我好像看到昆汀在罗素兄弟身上灵魂附体：角色当死即死，一点都不含糊，哪怕最具人气的复仇者联盟初代团队都集合于此。 然而当浩克开始扛着巨石，、...

                        &nbsp;(<a href="javascript:;" id="toggle-10135191-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10135191_full" class="hidden">
                    <div id="review_10135191_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10135191" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-10135191">
                                1547
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10135191" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-10135191">
                                235
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10135191/#comments" class="reply ">544回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10133044">
        <div class="main review-item" id="10133044">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/ballteda/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u45134592-73.jpg">
        </a>

        <a href="https://www.douban.com/people/ballteda/" class="name">掉线</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2019-04-24" class="main-meta">2019-04-24 06:41:02</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10133044/">一个几乎完美的穿越故事。</a></h2>

                <div id="review_10133044_short" class="review-short" data-rid="10133044">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        【 只接受非盈利目的个人社交平台免费转载（带原文链接），谢谢合作 】 电影本身懒得费力评价了，纯粹表扬下这个剧本。 时空题材的电影很多，能做到严谨，自洽的很少，而商业大片能做到的就更少了。 仅从穿越逻辑来说，《复联4》几乎没有漏洞 故事剧情大概是这样的。 【A宇宙】...

                        &nbsp;(<a href="javascript:;" id="toggle-10133044-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10133044_full" class="hidden">
                    <div id="review_10133044_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10133044" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-10133044">
                                1711
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10133044" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-10133044">
                                318
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10133044/#comments" class="reply ">1326回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10132848">
        <div class="main review-item" id="10132848">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/182939940/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u182939940-12.jpg">
        </a>

        <a href="https://www.douban.com/people/182939940/" class="name">啊呜一大口</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2019-04-24" class="main-meta">2019-04-24 04:24:23</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10132848/">填坑能手 梗王大佬漫威  故事完结 我来搞个新鲜剧透/并不</a></h2>

                <div id="review_10132848_short" class="review-short" data-rid="10132848">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        补个细节！！ hope他爹汉克博士  在蚁人说他以前和霍德华史塔克闹翻，是因为霍德华不承认偷了他的皮姆粒子。 其实是队长偷的..... 霍华德：我是真的冤 ～～～～ 评论区补充@隔壁老王： 葬礼上哈皮问摩根想吃啥，摩根说爱芝士汉堡，瞬间泪目，看了无数遍钢1的我瞬间想起来，托尼...

                        &nbsp;(<a href="javascript:;" id="toggle-10132848-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10132848_full" class="hidden">
                    <div id="review_10132848_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10132848" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-10132848">
                                346
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10132848" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-10132848">
                                27
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10132848/#comments" class="reply ">163回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10133259">
        <div class="main review-item" id="10133259">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/EverybodyFool/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u37142357-10.jpg">
        </a>

        <a href="https://www.douban.com/people/EverybodyFool/" class="name">彩蛋君KL</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2019-04-24" class="main-meta">2019-04-24 09:45:32</span>

            <a class="rel-topic" target="_blank" href="//www.douban.com/gallery/topic/《复仇者联盟4》会如何联结之前漫威的21部电影？">#《复仇者联盟4》会如何联结之前漫威的21部电影？</a>

    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10133259/">《复联4：终局之战》终极彩蛋指南</a></h2>

                <div id="review_10133259_short" class="review-short" data-rid="10133259">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        无限传奇完美终结！ 漫威用美妙的方式串联起前21部影片，每个我们熟悉的人物都散发着前所未有的光芒，感觉复联4不是一部电影，而是一场属于英雄们的授勋典礼。 Nuff Said，奉上彩蛋。 托尼给小辣椒的录音信息中，说到“It&#39;s always you”（一直都是你）。在《钢铁侠2》中托尼任...

                        &nbsp;(<a href="javascript:;" id="toggle-10133259-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10133259_full" class="hidden">
                    <div id="review_10133259_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10133259" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-10133259">
                                845
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10133259" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-10133259">
                                73
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10133259/#comments" class="reply ">169回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10133022">
        <div class="main review-item" id="10133022">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/149238384/" class="avator">
            <img width="24" height="24" src="https://img9.doubanio.com/icon/u149238384-4.jpg">
        </a>

        <a href="https://www.douban.com/people/149238384/" class="name">光影痕迹</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2019-04-24" class="main-meta">2019-04-24 06:06:28</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10133022/">这是初代最完美的谢幕，但是漫威这次搞砸了————《复联4》不负责任非深度个人感受加少少分析</a></h2>

                <div id="review_10133022_short" class="review-short" data-rid="10133022">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        刚刚看了《小蜘蛛:离家日》的预告，内心满满的感触。预告中铁人的几个镜头和几句关于托尼的话，催泪程度爆表。 ——————————————最后一次更新———————————————————— 额。。。第一次写正文的时候，已经是凌晨四五点了，随便记录了自己当时的观影...

                        &nbsp;(<a href="javascript:;" id="toggle-10133022-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10133022_full" class="hidden">
                    <div id="review_10133022_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10133022" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-10133022">
                                1389
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10133022" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-10133022">
                                534
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10133022/#comments" class="reply ">1351回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>




    

    

    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/418fa12b33d072cf.js"></script>
    <!-- COLLECTED CSS -->
</div>








                <p class="pl">
                    &gt;
                    <a href="reviews">
                        更多影评
                            5798篇
                    </a>
                </p>
    </section>
<!-- COLLECTED JS -->

    <br/>

                
    <div class="section-discussion">
        <div class="hd-ops">
            <a class="comment_btn j a_show_login" href="https://www.douban.com/register?reason=discussion" rel="nofollow"><span>发起新的讨论</span></a>
        </div>
        <div class="mod-hd">
            
    <h2>
        小组讨论
         &nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;
    </h2>

        </div>
        
  <table class="olt"><tr><td><td><td><td></tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/172394886/" title="看的第5遍">看的第5遍</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/162526337/">Smile</a></td>
          <td class="pl"><span>1 回应</span></td>
          <td class="pl"><span>2020-04-22</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/171579655/" title="复仇者联盟4到哪可以看，好久没看了想要回味一下">复仇者联盟4到哪可以看，好久没看了想要回味一下</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/215240371/">随缘এ᭄</a></td>
          <td class="pl"><span>7 回应</span></td>
          <td class="pl"><span>2020-04-21</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/144534353/" title="复仇者联盟英雄实力排名">复仇者联盟英雄实力排名</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/152525743/">卖高仿童鞋宝妈</a></td>
          <td class="pl"><span>23 回应</span></td>
          <td class="pl"><span>2020-04-18</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/139181410/" title="感觉漫威宇宙下一阶段要由女英雄开始挑大梁了">感觉漫威宇宙下一阶段要由女英雄开始挑大梁了</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/8638493/">ekingling</a></td>
          <td class="pl"><span>5 回应</span></td>
          <td class="pl"><span>2020-04-16</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/170768709/" title="漫威的影迷看过来">漫威的影迷看过来</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/185248885/">Milton</a></td>
          <td class="pl"><span>10 回应</span></td>
          <td class="pl"><span>2020-04-15</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/170066209/" title="太奇怪了！">太奇怪了！</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/213461064/">萌萌的小考拉</a></td>
          <td class="pl"><span>5 回应</span></td>
          <td class="pl"><span>2020-04-14</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/171447573/" title="我为三巨头P的海报">我为三巨头P的海报</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/183694369/">豆56</a></td>
          <td class="pl"><span></span></td>
          <td class="pl"><span>2020-04-14</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/169064321/" title="【设定集】复联3的原版设定集 想出（低价）">【设定集】复联3的原版设定集 想出（低价）</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/153804636/">七海缘</a></td>
          <td class="pl"><span>1 回应</span></td>
          <td class="pl"><span>2020-04-14</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/171124888/" title="银河护卫队版防疫指南">银河护卫队版防疫指南</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/214871789/">❤️甜甜❤️</a></td>
          <td class="pl"><span>1 回应</span></td>
          <td class="pl"><span>2020-04-12</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://www.douban.com/group/topic/168861565/" title="这个问题一定新颖，进来吧。">这个问题一定新颖，进来吧。</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/189872166/">24 K Pyre Hands</a></td>
          <td class="pl"><span>4 回应</span></td>
          <td class="pl"><span>2020-04-12</span></td>
        </tr>
  </table>

        
        <p class="pl" align="right">
            <a href="//www.douban.com/group/659897#topics" rel="nofollow">
                &gt; 去这部电影的小组讨论（全部4676条）
            </a>
        </p>
    </div>


        
    
        
                





<div id="askmatrix">
    <div class="mod-hd">
        <h2>
            关于《复仇者联盟4：终局之战》的问题
            · · · · · ·
            <span class="pl">
                (<a href='https://movie.douban.com/subject/26100958/questions/?from=subject'>
                    全部175个
                </a>)
            </span>
        </h2>


        
    
    <a class='j a_show_login comment_btn'
        href='https://movie.douban.com/subject/26100958/questions/ask/?from=subject'>我来提问</a>

    </div>

    <div class="mod-bd">
        <ul class="">
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/26100958/questions/829415/?from=subject" class="">
                            为什么美国队长在片尾只需穿越一次就能把6颗无限宝石都还上了？
                    </a>
                </span>
                <span class="meta">
                    13人回答
                </span>
            </li>
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/26100958/questions/829437/?from=subject" class="">
                            最后灭霸的宝石怎么跑到钢铁侠手里的？？？
                    </a>
                </span>
                <span class="meta">
                    14人回答
                </span>
            </li>
        </ul>

        <p>&gt;
            <a href='https://movie.douban.com/subject/26100958/questions/?from=subject'>
                全部175个问题
            </a>
        </p>

    </div>
</div>



            


    <script type="text/javascript">
        $(function(){if($.browser.msie && $.browser.version == 6.0){
            var $info = $('#info'),
                maxWidth = parseInt($info.css('max-width'));
            if($info.width() > maxWidth) {
                $info.width(maxWidth);
            }
        }});
    </script>


            </div>
            <div class="aside">
                


    









    <!-- douban ad begin -->
    <div id="dale_movie_subject_top_right"></div>
    <div id="dale_movie_subject_top_middle"></div>
    <!-- douban ad end -->

    



<style type="text/css">
    .m4 {margin-bottom:8px; padding-bottom:8px;}
    .movieOnline {background:#FFF6ED; padding:10px; margin-bottom:20px;}
    .movieOnline h2 {margin:0 0 5px;}
    .movieOnline .sitename {line-height:2em; width:160px;}
    .movieOnline td,.movieOnline td a:link,.movieOnline td a:visited{color:#666;}
    .movieOnline td a:hover {color:#fff;}
    .link-bt:link,
    .link-bt:visited,
    .link-bt:hover,
    .link-bt:active {margin:5px 0 0; padding:2px 8px; background:#a8c598; color:#fff; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; display:inline-block;}
</style>



    







    
    <div class="tags">
        
        
    <h2>
        <i class="">豆瓣成员常用的标签</i>
              · · · · · ·
    </h2>

        <div class="tags-body">
                <a href="/tag/漫威" class="">漫威</a>
                <a href="/tag/超级英雄" class="">超级英雄</a>
                <a href="/tag/科幻" class="">科幻</a>
                <a href="/tag/美国" class="">美国</a>
                <a href="/tag/2019" class="">2019</a>
                <a href="/tag/情怀" class="">情怀</a>
                <a href="/tag/动作" class="">动作</a>
                <a href="/tag/漫画改编" class="">漫画改编</a>
        </div>
    </div>


    <div id="dale_movie_review_right_guess_you_like"></div>
    <div id="dale_movie_subject_inner_middle"></div>
    <div id="dale_movie_subject_download_middle"></div>
        








<div id="subject-doulist">
    
    
    <h2>
        <i class="">以下豆列推荐</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/26100958/doulists">全部</a>
            )
            </span>
    </h2>


    
    <ul>
            <li>
                <a href="https://www.douban.com/doulist/27868/" target="_blank">【内牛满面】</a>
                <span>(影志)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/114465/" target="_blank">{北美电影票房总排行}</a>
                <span>(荔枝超人)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/30299/" target="_blank">豆瓣电影【口碑榜】2020-04-17 更新</a>
                <span>(影志)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/16002/" target="_blank">带你进入不正常的世界</a>
                <span>(DK奔小驰)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/11568/" target="_blank">【科幻】太空、外星人、时空、超能量</a>
                <span>(卡特兰)</span>
            </li>
    </ul>

</div>

            








<div id="subject-others-interests">
    
    
    <h2>
        <i class="">谁在看这部电影</i>
              · · · · · ·
    </h2>

    
    <ul class="">
            
            <li class="">
                <a href="https://www.douban.com/people/183574396/" class="others-interest-avatar">
                    <img src="https://img3.doubanio.com/icon/u183574396-1.jpg" class="pil" alt="昨昨昨昨">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/183574396/" class="">昨昨昨昨</a>
                    <div class="">
                        刚刚
                        看过
                        
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/190142289/" class="others-interest-avatar">
                    <img src="https://img3.doubanio.com/icon/u190142289-1.jpg" class="pil" alt="田刚">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/190142289/" class="">田刚</a>
                    <div class="">
                        刚刚
                        看过
                        
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/214234349/" class="others-interest-avatar">
                    <img src="https://img3.doubanio.com/icon/u214234349-1.jpg" class="pil" alt="小可爱">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/214234349/" class="">小可爱</a>
                    <div class="">
                        1分钟前
                        看过
                        
                    </div>
                </div>
            </li>
    </ul>

    
    <div class="subject-others-interests-ft">
        
            <a href="https://movie.douban.com/subject/26100958/collections">1394178人看过</a>
                &nbsp;/&nbsp;
            <a href="https://movie.douban.com/subject/26100958/wishes">161457人想看</a>
    </div>

</div>



    
    

<!-- douban ad begin -->
<div id="dale_movie_subject_middle_right"></div>
<script type="text/javascript">
    (function (global) {
        if(!document.getElementsByClassName) {
            document.getElementsByClassName = function(className) {
                return this.querySelectorAll("." + className);
            };
            Element.prototype.getElementsByClassName = document.getElementsByClassName;

        }
        var articles = global.document.getElementsByClassName('article'),
            asides = global.document.getElementsByClassName('aside');

        if (articles.length > 0 && asides.length > 0 && articles[0].offsetHeight >= asides[0].offsetHeight) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_middle_right');
        }
    })(this);
</script>
<!-- douban ad end -->



    <br/>

    
<p class="pl">订阅复仇者联盟4：终局之战的评论: <br/><span class="feed">
    <a href="https://movie.douban.com/feed/subject/26100958/reviews"> feed: rss 2.0</a></span></p>


            </div>
            <div class="extra">
                
    
<!-- douban ad begin -->
<div id="dale_movie_subject_bottom_super_banner"></div>
<script type="text/javascript">
    (function (global) {
        var body = global.document.body,
            html = global.document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
        if (height >= 2000) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_bottom_super_banner');
        }
    })(this);
</script>
<!-- douban ad end -->


            </div>
        </div>
    </div>

        
    <div id="footer">
            <div class="footer-extra"></div>
        
<span id="icp" class="fleft gray-link">
    &copy; 2005－2020 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about/legal">法律声明</a>
    
    · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

    </div>

    </div>
    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/5e78ef1ba3f087b6.js"></script>
        
        
    <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css" />
    <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/movie/4aca95d66d37ec0712b3d19973b5d8feb75f2f05/css/movie/mod/reg_login_pop.css" />
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js"></script>
    <script type="text/javascript">
        var HTTPS_DB='https://www.douban.com';
var account_pop={open:function(o,e){e?referrer="?referrer="+encodeURIComponent(e):referrer="?referrer="+window.location.href;var n="",i="",t=448;n="用户登录",i="https://accounts.douban.com/passport/login_popup?source=movie";var r=document.location.protocol+"//"+document.location.hostname,a=dui.Dialog({width:340,title:n,height:t,cls:"account_pop",isHideTitle:!0,modal:!0,content:"<iframe scrolling='no' frameborder='0' width='340' height='"+t+"' src='"+i+"' name='"+r+"'></iframe>"},!0),c=a.node;if(c.undelegate(),c.delegate(".dui-dialog-close","click",function(){var o=$("body");o.find("#login_msk").hide(),o.find(".account_pop").remove()}),$(window).width()<478){var d="";"reg"===o?d=HTTPS_DB+"/accounts/register"+referrer:"login"===o&&(d=HTTPS_DB+"/accounts/login"+referrer),window.location.href=d}else a.open();$(window).bind("message",function(o){"https://accounts.douban.com"===o.originalEvent.origin&&(c.find("iframe").css("height",o.originalEvent.data),c.height(o.originalEvent.data),a.update())})}};Douban&&Douban.init_show_login&&(Douban.init_show_login=function(o){var e=$(o);e.click(function(){var o=e.data("ref")||"";return account_pop.open("login",o),!1})}),Do(function(){$("body").delegate(".pop_register","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("reg",e),!1}),$("body").delegate(".pop_login","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("login",e),!1})});
    </script>

    
    
    
    




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = '0vRdXfffwRc',
            criteria = '7:情怀|7:杰瑞米·雷纳|7:漫威|7:蒂尔达·斯文顿|7:动作|7:查德维克·博斯曼|7:格温妮斯·帕特洛|7:感动|7:约翰·斯拉特里|7:马克·鲁弗洛|7:安东尼·罗素|7:漫画改编|7:本尼迪克特·康伯巴奇|7:伊丽莎白·奥尔森|7:泰莎·汤普森|7:2019|7:布丽·拉尔森|7:保罗·路德|7:超级英雄|7:克里斯·埃文斯|7:乔·罗素|7:史诗|7:克里斯·海姆斯沃斯|7:汤姆·赫兰德|7:凯伦·吉兰|7:布莱德利·库珀|7:冒险|7:蕾妮·罗素|7:奇幻|7:科幻|7:美国|7:唐·钱德尔|7:小罗伯特·唐尼|7:斯嘉丽·约翰逊|3:/subject/26100958/',
            preview = '',
            debug = false,
            adSlots = ['dale_movie_subject_top_icon', 'dale_movie_subject_top_right', 'dale_movie_subject_top_middle', 'dale_movie_subject_inner_middle', 'dale_movie_subject_download_middle', 'dale_movie_subject_banner_after_intro', 'dale_movie_review_right_guess_you_like'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', '//img1.doubanio.com/eDRjYjNvdi9mL2FkanMvZTQ2YTNkMjgwYjBiMzc2OWE4YTI3MWFhMzI0NTQwMTBlMWY3OTYzMy9hZC5yZWxlYXNlLmpz');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>











    
  









<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-19', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id]);
      _gaq.push([method('_setSampleRate'), '5']);

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}

  gaWithNamespace(function(method) {
    _gaq.push([method('_setAccount'), 'UA-59230-10'])
    
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

    _gaq.push([method('_setDomainName'), '.douban.com'])
    _gaq.push([method('_trackPageview')]);
  }, 't1')

;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>

<script src="https://img3.doubanio.com/js/boomerang.js?09" type="text/javascript"></script>
<script type="text/javascript">
BOOMR.init({
    user_ip: "122.192.49.194",
    beacon_url: "/beacon.gif",
    site_domain: ".douban.com",
    BW: {
        enabled: false
    }
});
BOOMR.subscribe('before_beacon', function(o) {
    if(o.t_done && o.t_done > 0 && o.t_done < 30) {
        _gaq.push(['t1._trackEvent', 'Performance', 'done', '/subject/-/', o.t_done]);
    }
});
var _now = new Date();
if (typeof(_head_start)==typeof(_now)) {
    var t_head = _now-_head_start;
    var t_body = _now-_body_start;
    if (t_head < 1000*60 && t_head > 0){
        var _slow = t_head > 10*1000 ? 'slow ' : '';
        _gaq.push(['t1._trackEvent', 'Performance', _slow + 'head', '/subject/-/', _now-_head_start]);
        _gaq.push(['t1._trackEvent', 'Performance', _slow + 'body', '/subject/-/', _now-_body_start]);
        BOOMR.plugins.RT.setTimer('t_head', t_head).setTimer('t_body', t_body);
    }
}
</script>







      
    

    <!-- dae-web-movie--default-599f4cc99c-jhgtb-->

  <script>_SPLITTEST=''</script>
</body>

</html>




'''

save_item = {
"directors": [
"恩斯特·刘别谦"
],
"rate": "9.2",
"cover_x": 2000,
"star": "45",
"title": "你逃我也逃",
"url": "https://movie.douban.com/subject/1303418/",
"casts": [
"卡洛·朗白",
"杰克·本尼",
"罗伯特·斯塔克",
"菲利克斯·布雷萨特",
"莱昂内尔·阿特威尔"
],
"cover": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1339915772.webp",
"id": "1303418",
"cover_y": 3000
}


doc = pq(html)

content_block = doc.find('#content')

title_spans = content_block.find('h1')
title_span = title_spans.find('span').eq(0)
year_span = title_spans.find('span').eq(1)


film_name = save_item['title']
film_name_full = title_span.text()
douban_id = save_item['id']
film_year_pre = year_span.text()
cover = save_item['cover']
cover_x = save_item['cover_x']
cover_y = save_item['cover_y']
url = save_item['url']

info_div = content_block.find('#info')

director = info_div('span').eq(2).text()


writer_span = info_div('span').eq(3)
writer = []
for writer_elem in writer_span.find('a').items():
    writer.append(writer_elem.text())



actors_span = info_div('span.actor')
actors = []
for actor_elem in actors_span.find('a').items():
    actors.append(actor_elem.text())

types = []
release_date_pre = []
film_length_pre = []

for span_elem in info_div('span').items():
    propertys =span_elem.attr('property')
    if propertys == 'v:genre':
        types.append(span_elem.text())
    elif propertys == 'v:initialReleaseDate':
        release_date_pre.append(span_elem.text())
    elif propertys == 'v:runtime':
        film_length_pre.append(span_elem.text())

raw_html = info_div.html()
raw_html_parse = raw_html.encode('utf-8')


make_country_match = re.search("制片国家/地区:</span>\s?(.*)?<br/>",raw_html_parse)
make_country = ''

if make_country_match is None:
    pass
else:
    make_country = make_country_match.group(1)
    
    
languages_match = re.search("语言:</span>\s?(.*)?<br/>",raw_html_parse)
languages = ''
if languages_match is None:
    pass
else:
    languages = languages_match.group(1)
    
alias_match = re.search("又名:</span>\s?(.*)?<br/>",raw_html_parse)
alias = ''
if alias_match is None:
    pass
else:
    alias = alias_match.group(1)


interest_sectl_div = content_block('#interest_sectl')

score_pre = interest_sectl_div('.rating_num').text()
rate_perple_pre = interest_sectl_div('.rating_people span').text()
now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

index = 0
star_five = ''
star_four = ''
star_three = ''
star_two = ''
star_one = ''

for rate_elem in interest_sectl_div('.rating_per').items():
    if index == 0:
        star_five = rate_elem.text()
    elif index == 1:
        star_four = rate_elem.text()
    elif index == 2:
        star_three = rate_elem.text()
    elif index == 3:
        star_two = rate_elem.text()
    elif index == 4:
        star_one = rate_elem.text()

    index = index + 1


better_than = []
for better_item in interest_sectl_div('.rating_betterthan a').items():
    better_than.append(better_item.text())

plot = ''
if len(content_block('#link-report .all')) >= 1:
    plot = content_block('#link-report .all').text()
else:
    plot = content_block('#link-report span').eq(0).text()
