from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from pages.order import PersonalData, RentScooter, OrderConfirmationWindow, WindowOfCompletedOrder
from pages.base import BasePage


class TestOrderPage:

    driver = None

    @allure.title('Инициализируем драйвер')
    def setup(self):
        self.driver = webdriver.Firefox()

    @allure.description('Проверяем процесс первого заказа самоката с положительным сценарием')
    @allure.title('Заказ самоката #1')
    def test_order_scooter_1(self):
        base = BasePage(self.driver)
        base.open_order_page()
        order_page = PersonalData(self.driver)
        order_page.first_order('Иван', 'Иванов', 'Москва', '89111234567')

        scooter_page = RentScooter(self.driver)
        scooter_page.first_scooter('Нет')

        order_confirmation = OrderConfirmationWindow(self.driver)
        order_confirmation.order_confirmation_1()

        order_completed = WindowOfCompletedOrder(self.driver)
        order_completed.completed_order_1()
        assert self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')


    @allure.description('Проверяем процесс второго заказа самоката с положительным сценарием')
    @allure.title('Заказ самоката #2')
    def test_order_scooter_2(self):
        base = BasePage(self.driver)
        base.open_order_page()
        order_page = PersonalData(self.driver)
        order_page.second_order('Степан', 'Степанов', 'Москва', '89110000001')

        scooter_page = RentScooter(self.driver)
        scooter_page.second_scooter('Требуется подтверждение!')

        order_confirmation = OrderConfirmationWindow(self.driver)
        order_confirmation.order_confirmation_2()

        order_completed = WindowOfCompletedOrder(self.driver)
        order_completed.completed_order_2()
        assert self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/input')

    @allure.title('Закрываем драйвер')
    def teardown(self):
        self.driver.quit()