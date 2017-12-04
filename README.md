# Sina-Crawler
爬取新浪微博的微博信息等相关  
**组员： 姚博文 黄青刚 魏志航 郑浩然 周一帆**   
**实现功能：**  
1.爬取输入用户的所有微博、对应微博的转发、评论  
2.自动发微博显示结果  
**实现途径：**      
Selenium+Python  
通过移动端微博不断下拉将用户所有微博先显示出来，最后一次性读取微博内容。  
**使用说明：**    
1.提示输入用户ID，为移动端的如下图地址：  
![](/GetID.png)  
2.需要在系统变量下设置浏览器路径（默认用的Chrome）   
3.需要在ID.conf中填入登入账号和密码  
![](/IDConfig.png)  
4.完成后会生成一个txt（例子中result.txt为局座招忠的所有微博）和你的登陆账号发一条微博  
![](/WeiboSent.png) 
**存在的问题：**    
1.账号需要取消安全防护（以便通过账号密码登陆)    
2.下拉过程中网速不稳定可能导致下拉失败，只能读取到部分微博  
3.实现思路的限制导致速度较慢  
4.对于需要点击跳转加载全文的微博还没有进行处理
