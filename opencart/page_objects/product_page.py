from selenium.webdriver.common.by import By

from opencart.page_objects.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "#button-cart"
    # ADD_TO_CART_BUTTON = By.XPATH, "//*[@id='content']/div[2]/div[2]/div/div[2]/form/div/button[1]"
    ADD_TO_COMPARISON_BUTTON = By.CSS_SELECTOR, "[title='Compare this Product']"
    ADD_TO_WISH_LIST_BUTTON = By.CSS_SELECTOR, "[title='Add to Wish List']"

    def add_to_cart(self):
        self.execute_script("arguments[0].scrollIntoView();", self.ADD_TO_CART_BUTTON)
        self.click(self.ADD_TO_CART_BUTTON)

    def add_to_comparison(self):
        self.click(self.ADD_TO_COMPARISON_BUTTON)

    def add_to_wish_list(self):
        self.click(self.ADD_TO_WISH_LIST_BUTTON)
