from selenium.webdriver.common.by import By
def test_check_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_to_basket_button = browser.find_elements(By.XPATH, '//*[@id="ad11d_to_basket_form"]/button')
    assert add_to_basket_button, "Button not found"