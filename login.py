
import time
import pytesseract
from PIL import Image, ImageEnhance
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import base64
import json
import requests
from selenium.webdriver.common.action_chains import ActionChains
url="https://passport.hualala.com/login?redirectURL=https%3A%2F%2Fshop.hualala.com"
driver=webdriver.Chrome("D:\softinstall\chrome1109\chromedriver_win32\chromedriver.exe")
driver.get(url)
code=""
driver.maximize_window()
sleep(5)
driver.save_screenshot("D://coder/untitled2/01.png")
sleep(2)
ran=Image.open("D://coder/untitled2/01.png")
box=(1416,490,1524,530)
ran.crop(box).save("D://coder/untitled2/02.png")
sleep(2)
imagecode=Image.open("D://coder/untitled2/02.png")
sleep(2)
sharp_img=ImageEnhance.Contrast(imagecode).enhance(2.0)
sleep(2)
sharp_img.save("D://coder/untitled2/03.png")#保存图像增强，二值化之后的验证码图片
sharp_img.load()  # 对比度增强
print(sharp_img)#打印图片的信息

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""



if __name__ == "__main__":
    img_path = "03.png"
    code = base64_api(uname='simtwo', pwd='xxx123456', img=img_path, typeid=1)
    print(code)
mainAccount=driver.find_element_by_css_selector("[data-i18nid='account-enterprise']").send_keys("984701981")
sleep(2)
username=driver.find_element_by_css_selector("[data-i18nid='account-personal']").send_keys("19938022004")
sleep(2)
password=driver.find_element_by_css_selector("[data-i18nid='account-password']").send_keys("x022004")
sleep(2)
accountcode=driver.find_element_by_css_selector("[data-i18nid='account-code']").send_keys(code)
sleep(2)
# 登录
driver.find_element_by_css_selector("[data-i18nid='account-submit']").click()
sleep(10)

notices=driver.find_element_by_css_selector("[class='Notices_noticesKnow__3pXP0']")
if notices:
    notices.click()
else:
    print("null")
sleep(2)
#视角切换
driver.find_element_by_css_selector("[class='ant-btn viewpoint_dropButton__rHX51']").click()
sleep(2)
#切换到配送中心视角选择
driver.find_element_by_css_selector("[href='#4F']").click()
sleep(2)
#切换到配送中心
driver.find_element_by_css_selector("[data-id='3_61808407']").click()
sleep(4)
#报表视图
driver.find_element_by_xpath("/html/body/div/div/div/div/div/ul/li[9]").click()
sleep(5)
driver.get("https://report.hualala.com/#/tab/0")
sleep(2)
# driver.get("https://report.hualala.com/#/tab/CP_caipinqudao_2410")
sleep(2)
# driver.find_element_by_link_text("菜品销售报表").click()
driver.find_element_by_link_text("241菜品渠道表").click()
# driver.find_element_by_css_selector("[title='241菜品渠道表']").click()
# sleep(2)
# print( driver.execute_script("return document.documentElement.outerHTML"))


# ActionChains(driver).move_to_element(driver.find_element_by_xpath("//span[contains(text(),'菜品销售报表')]"))
# sleep(2)
# driver.find_element_by_css_selector("class='anticon anticon-down'").click()
# sleep(2)
# js = 'document.getElementsByClassName("ant-picker-input ant-picker-input-active")[0].removeAttribute("readOnly")'
# js = 'document.getElementsByClassName("ant-picker-input")[0].removeAttribute("readOnly")'
# #js = "document.getElementByClassName('ant-picker-input ant-picker-input-active').removeAttribute('readonly')"
# # js = "$('input[placeholder=开始日期]').attr('readonly',’ ‘)"
# # js = "$('input[placeholder=结束日期]').attr('readonly',’ ‘)"
# driver.execute_script(js)
# sleep(2)
# driver.find_element_by_class_name("ant-picker-input ant-picker-input-active").send_keys("2020-5-6")
# driver.find_element_by_class_name("ant-picker-input").send_keys("2020-5-6")
