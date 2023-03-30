from selenium.webdriver.common.by import By


def test_login_field_is_displayed(driver):
    driver.get("http://127.0.0.1:5000/login")
    element = driver.find_element(By.ID, "login")
    assert element.is_displayed()
