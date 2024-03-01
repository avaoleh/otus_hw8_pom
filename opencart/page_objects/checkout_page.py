from selenium.webdriver.common.by import By

from opencart.page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_FORM = By.CSS_SELECTOR, "#checkout-checkout"
    CHECKOUT_PAYMENT_FORM = By.CSS_SELECTOR, "#checkout-payment-method"
    LOGIN_PAGE_LINK = By.XPATH, "//strong[text()='login page']"

    def click_login_page_link(self):
        self.click(self.LOGIN_PAGE_LINK)

    def wait_page_load(self):
        self.get_element(self.CHECKOUT_FORM)

    def wait_payment_form(self):
        self.get_element(self.CHECKOUT_PAYMENT_FORM)
