import time
from .base_page import BasePage
from .locators import BookPageLocators, AddedItemToCartLocators

class ProductPage(BasePage):
    def add_book_to_cart(self):
        assert self.is_element_present(*BookPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not presented"
        button = self.browser.find_element(*BookPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def solve_the_puzzle(self):
        self.solve_quiz_and_get_code()

    def should_be_add_message(self):
        assert self.is_element_present(*AddedItemToCartLocators.ADD_TO_CART_MESSAGE), "Added to cart message is not presented"

    def cart_cost_should_be_equal_price_of_the_book(self):
        assert self.text_of_the_element(*AddedItemToCartLocators.CART_COST) == self.text_of_the_element(*BookPageLocators.BOOK_PRICE),\
            "Prices of books are not the same"

    def names_of_books_should_be_equal(self):
        assert self.text_of_the_element(*AddedItemToCartLocators.BOOK_NAME_IN_MESSAGE) == self.text_of_the_element(*BookPageLocators.BOOK_NAME),\
            "Book names are not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddedItemToCartLocators.ADD_TO_CART_MESSAGE), "Added to cart message is presented"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*AddedItemToCartLocators.ADD_TO_CART_MESSAGE), "Added to cart message not disappeared"