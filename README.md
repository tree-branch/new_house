# new_house
此为新房数据,需要二手房数据的移步[house](https://github.com/tree-branch/house)

爬取贝壳找房、链家(、安居客、58同城未更新，用的人少的话就不更新了)的房源信息，便于广大未买房子的朋友们尽快成为房奴！！！Crawl the house informations of lianjia.com (anjvke.com, 58.com, ganji.com after the update), convenient for the majority of friends who did not buy the house as soon as to become the mortgage slave!!!

## 直接运行
修改config.ini内的mysql链接地址

python3.0及以上版本

python new_house.py

缺什么包就 pip install ***

## 个性化运行
此程序是把leancloud作为云数据库使用;在 https://leancloud.cn/ 内建立账号;修改config.ini为自己的App ID App KEY

python new_house.py

修改house.py内贝壳找房等网站的网址，查询的限定条件需要能够保存在URL内，例如链家的排序也是可以保存在URL内的，一看例子你也应该就懂了，不懂的话就再看一遍，直接给我发邮件当然是最快的办法 :-)。

## 联系方式
有想说的联系：lm521299@sina.com

![](https://img-blog.csdnimg.cn/2020071510365879.png)

# 希望发现不好用的时候邮件通知我一下，方便我尽快修改，谢谢 :-)