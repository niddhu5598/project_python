from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.imdb.com/chart/top?pf_rd_m"
driver.get(url)
time.sleep(2)

driver.find_element_by_css_selector("tbody.lister-list")
print(main_area)