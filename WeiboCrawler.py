import time
import codecs
import configparser
from selenium import webdriver

#使用谷歌浏览器,需要Chrome存在于系统路径中
driver = webdriver.Chrome()
file = codecs.open("result.txt","a","utf-8")

#登陆微博获取权限
def LoginWeibo(username, password):
    driver.get("https://passport.weibo.cn/signin/login")
    time.sleep(3)
    user = driver.find_element_by_id("loginName").send_keys(username)
    keyword = driver.find_element_by_id("loginPassword").send_keys(password)
    submit = driver.find_element_by_id("loginAction").click()

#爬虫主程序
def Crawler(user_id):
    driver.get("https://m.weibo.cn/u/"+user_id)
    time.sleep(3)
    VIPname = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div[1]/div[1]/div/div[3]/div[1]/span/span").text
    file.write("ID:"+VIPname+"\r\n"+"\r\n")
    driver.get("https://m.weibo.cn/u/"+user_id+"?filter=0")
    time.sleep(3)
    #下拉页面
    js = "window.scrollTo(0, document.body.scrollHeight)"
    for i in range(1000000):
        driver.execute_script(js)
        time.sleep(0.5)
        #判断是否拉到底
        if(i%120==0):
            test = driver.find_elements_by_xpath("//*[@id=\"app\"]/div[1]/div[1]/div[contains(@class,'card m-panel card9')]/div/div/article")
            for j in range(20):
                driver.execute_script(js)
                time.sleep(0.5)
            now = driver.find_elements_by_xpath("//*[@id=\"app\"]/div[1]/div[1]/div[contains(@class,'card m-panel card9')]/div/div/article")
            time.sleep(3)
            if(len(test)==len(now)):
                break
    #获取并写入微博信息
    text=driver.find_elements_by_xpath("//*[@id=\"app\"]/div[1]/div[1]/div[contains(@class,'card m-panel card9')]/div/div/article")
    date=driver.find_elements_by_xpath("//*[@id=\"app\"]/div[1]/div[1]/div[contains(@class,'card m-panel card9')]/div/div/header/div/div/h4/span[1]")
    comments=driver.find_elements_by_xpath("//*[@id=\"app\"]/div[1]/div[1]/div[contains(@class,'card m-panel card9')]/div/div/footer/div[2]/h4")
    repos=driver.find_elements_by_xpath("//*[@id=\"app\"]/div[1]/div[1]/div[contains(@class,'card m-panel card9')]/div/div/footer/div[1]/h4")
    for i,j,m,n in zip(text,date,comments,repos):
        if(m.text=="评论" and n.text=="转发"):
            file.write(j.text + "     Comments:" +"0"+ "     Repos:" +"0"+ "\r\n" + i.text + "\r\n" + "\r\n")
        elif(m.text=="评论"):
            file.write(j.text + "     Comments:" + "0" + "     Repos:" + n.text + "\r\n" + i.text + "\r\n" + "\r\n")
        elif(n.text=="转发"):
            file.write(j.text + "     Comments:" + m.text + "     Repos:" + "0" + "\r\n" + i.text + "\r\n" + "\r\n")
        else:
            file.write(j.text + "     Comments:" + m.text + "     Repos:" + n.text + "\r\n" + i.text + "\r\n" + "\r\n")
    file.close()
    #用微博发送结果
    driver.get("https://m.weibo.cn/compose")
    time.sleep(3)
    content = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div[1]/div/span/textarea[1]").send_keys("Crawled down %d weibos of %s"%(len(text),VIPname))
    time.sleep(2)
    send = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/header/div[3]/a").click()

#程序入口
if __name__ == '__main__':
    conf = configparser.ConfigParser()
    conf.read("ID.conf")
    #用户输入user_id
    user_id=input("Input the user_id of mobile weibo:\n")
    username =conf.get("ID1","id")
    password = conf.get("ID1","keys")
    LoginWeibo(username, password)
    Crawler(user_id)

