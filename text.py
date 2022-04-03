from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
import json
import json


print("asda")
driver=webdriver.Chrome("D:\softinstall\chromedriver_win32\chromedriver.exe")
driver.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
sleep(40)
cookies=driver.get_cookies()
print(cookies)
with open('cookie.txt','w') as f:
    # 将cookies保存为json格式

    f.write(json.dumps(driver.get_cookies()))
token=driver.execute_script('window.localStorage.getItem("token")')
print(token)
with open('token.txt','w') as f:
    # 将cookies保存为json格式

    f.write(json.dumps(driver.get_cookies()))

driver.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
f1 = open('cookie.txt')
cookie = f1.read()
cookie =json.loads(cookie)
for c in cookie:
    driver.add_cookie(c)
# 刷新页面
driver.get("https://www.baidu.com/")
driver.find_element_by_css_selector("[class='s-top-login-btn c-btn c-btn-primary c-btn-mini lb']").click()
sleep(2)
driver.find_element_by_css_selector("[class='tang-pass-footerBarULogin pass-link']").click()
sleep(2)
driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("aleebb")
sleep(2)
driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("sfsf21414")
sleep(2)
driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
sleep(40)
with open('cookie.txt','w') as f:
    f.write(json.dumps(driver.get_cookies()))
driver.close()
driver.find_element_by_class_name("groupId").send_keys("14235235235")
driver.find_element_by_class_name("userId").send_keys("135")
driver.find_element_by_class_name("password").send_keys("x021352004")
driver.find_element_by_class_name("groupId").send_keys("9841355701981")
sleep(30)



