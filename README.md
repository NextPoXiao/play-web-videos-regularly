# open_tv
适用于二中晚修电视节目

### 使用说明
首次使用会在程序所在目录创建配置文件'set_up.json',   
其中包含基本信息:
> today_opentv——今天是否运行程序，'yes'或'no'  
> opentv_time——程序自动运行的时间，例如'20:45'  
> week_opentv——周末是否运行（用于调休的时候），'yes'或'no'  
> run_now——是否立即运行（调试的时候开启），'yes'或'no'  
> use_browse——使用的浏览器，'chrome'或'edge'  
> opentv_url——电视节目的网址，例如<http://10.23.26.242/#/videos/>  
> opentv_video_class_name——电视节目选项的图片  
> opentv_Play_xpath——播放按纽  
> opentv_maximize_xpath——放大按纽  

需要将浏览器驱动(webdriver)放在与程序同一目录下；
### chrome webdriver：
> 在浏览器设置中查看浏览器版本  
> 根据版本号（只看大版本）下载对应文件  
> [chrome_114及之前的版本](https://chromedriver.storage.googleapis.com/index.html)  
> [chrome_116版本点击直接下载](https://storage.googleapis.com/chrome-for-testing-public/116.0.5845.96/win64/chromedriver-win64.zip)  
> [chrome_117/118/119版本](https://googlechromelabs.github.io/chrome-for-testing/)  

### edge webdriver：
> 在浏览器设置中查看浏览器版本  
> 根据版本号（只看大版本）下载对应文件  
> [edge webdriver](https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/?form=MA13LH)

如果程序找不到网页元素，说明网页元素属性已更新，请自行定位元素并修改配置文件  
#### 本程序制作时间2024年9月15日

