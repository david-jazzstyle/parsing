import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


if __name__ == "__main__":
	print("Hello World")

	req = requests.get("http://www.shilladfs.com/estore/kr/ko/Skin-Care/Basic-Skin-Care/Skin-Toner/c/79?actr=1#url")
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')

	# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
	driver = webdriver.Chrome('/Users/hwangheeseung/Documents/Workspace/chromedriver')
	# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
	# driver_phantom = webdriver.PhantomJS('/Users/hwangheeseung/Documents/Workspace/phantomjs')

	driver.implicitly_wait(3)

	driver.get('https://www.shilladfs.com/estore/kr/ko/login')
	driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div/div[2]/div/a').click()
	driver.get('https://www.shilladfs.com/estore/kr/ko/login')

	driver.switch_to.frame(driver.find_element_by_id("ne_tgmiframe_0"))
	# driver.switch_to.frame('google_conversion_frame')
	# driver.implicitly_wait(3)
	driver.find_element_by_name('j_username').send_keys('heeseungh')
	driver.find_element_by_name('j_password').send_keys('Tlsfk12#')

	driver.find_element_by_xpath('//*[@id="loginForm"]/div/div/div/div[2]/div[1]/a').click()
	# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

	# price = driver_chrome.find_element_by_css_selector('#container > div.sub_category > div.product_list_wrap.facet_module > div.facet-product-list > ul:nth-child(1) > li:nth-child(1) > div > div.product_off > div.pr_info')

	# print(price)
	# my_titles = soup.select(
	# 	'#best_selling1 > div.best_box > ul > li.list_01 > div > div.product_off > div.pr_info > div.price > span.sale'
	# 	)



	# for title in my_titles:

	# 	print(title.t

	# //*[@id="loginForm"]/div/div/div/div[2]/div[1]/a

	# <a href="javascript:void(0)" onclick="javascript:formSubmit();" class="btn_red">로그인</a>

	# #loginForm > div > div > div > div.cont > div.login_write > a

	# //*[@id="loginForm"]/div/div/div/div[2]/div[1]/a
	# //*[@id="frmNIDLogin"]/fieldset/input
