from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# 크롬 드라이버 경로 설정
chromedriver_path = "chromedriver"

# 크롬 드라이버 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# 크롬 브라우저 실행
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# 구글 검색 페이지 열기
driver.get("https://www.google.com")

# 검색창에 검색어 입력 후 검색
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.RETURN)

# 검색 결과 가져오기
results = driver.find_elements(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div[1]/div/a')

# 검색 결과 출력
for result in results:
    print(result.get_attribute("href"))

# 브라우저 종료
driver.quit()