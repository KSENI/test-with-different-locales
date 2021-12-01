import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_should_see_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    # 2 секунды на загрузку страницы, если отображается поле поиска то страница считается загруженной
    button = WebDriverWait(browser, 10).until(
         EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='search']"))
     )
    assert len(browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")) == 1, "The button is not displayed or there is more than one button"
    # ожидание для ручной проверки языка кнопки
    time.sleep(10)