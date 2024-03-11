import os
import time
from opencart.page_objects.main_page import MainPage
from opencart.page_objects.user_page import UserPage
from opencart.page_objects.product_page import ProductPage
from opencart.page_objects.cart_page import CartPage
from opencart.page_objects.checkout_page import CheckoutPage
from opencart.page_objects.comparison_page import ComparisonPage
from opencart.page_objects.wish_list_page import WishListPage
from opencart.page_objects.alert_element import AlertSuccessElement

from opencart.utils.helpers import Client
from dotenv import load_dotenv

load_dotenv()
USER_EMAIL = os.getenv("EMAIL")
USER_PASSWORD = os.getenv("PASSWORD")


user = Client()
FIRSTNAME_TEST = user.first_name
LASTNAME_TEST = user.last_name
EMAIL_TEST = user.email
PASSWORD_TEST = user.password


def test_authorisation(browser):
    UserPage(browser).authorized(
        FIRSTNAME_TEST, LASTNAME_TEST, EMAIL_TEST, PASSWORD_TEST
    )


def test_login(browser):
    UserPage(browser).login(USER_EMAIL, USER_PASSWORD)


def test_check_cash(browser):
    UserPage(browser).check_cash()


def test_add_to_wish_list(browser):
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    ProductPage(browser).add_to_wish_list()
    AlertSuccessElement(browser).login.click()
    UserPage(browser).login_by_proccesing(
        USER_EMAIL, USER_PASSWORD
    ).wait_logged_in().click_wish_list()
    WishListPage(browser).wait_for_product_in_wish_list(product_name)


def test_add_to_cart(browser):
    product_name = MainPage(browser).get_featured_product_name(1)
    MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_cart()
    AlertSuccessElement(browser).shopping_cart.click()
    CartPage(browser).wait_for_product_in_cart(product_name).click_checkout()
    CheckoutPage(browser).click_login_page_link()
    UserPage(browser).login_by_proccesing(USER_EMAIL, USER_PASSWORD)
    CheckoutPage(browser).wait_page_load()


def test_add_to_cart_from_comparison(browser):
    product_name = MainPage(browser).get_featured_product_name()
    MainPage(browser).click_featured_product()
    ProductPage(browser).add_to_comparison()
    AlertSuccessElement(browser).comparison.click()
    ComparisonPage(browser).wait_for_product_in_comparison(product_name).click_confirm()
    AlertSuccessElement(browser).shopping_cart.click()
    CartPage(browser).wait_for_product_in_cart(product_name).click_checkout()
    CheckoutPage(browser).click_login_page_link()
    UserPage(browser).login_by_proccesing(USER_EMAIL, USER_PASSWORD)
    CheckoutPage(browser).wait_payment_form()
