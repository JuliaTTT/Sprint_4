from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from pages.base import BasePage


class PersonalData:

    name = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/input']
    surname = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/input']
    address = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/input']
    station = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div/input']
    station_names_1 = [By.XPATH, '//li[@class="select-search__row"][1]']
    station_names_2 = [By.XPATH, '//li[@class="select-search__row"][2]']
    phone = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[5]/input']
    next_button = [By.XPATH, '//div[@id="root"]//button[text()="Далее"]']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем сайт Заказа Самоката')
    def open_site(self):
        base = BasePage(self.driver)
        base.open_order_page()

    @allure.step('Вводим имя')
    def set_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    @allure.step('Вводим фамилию')
    def set_surname(self, surname):
        self.driver.find_element(*self.surname).send_keys(surname)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.driver.find_element(*self.address).send_keys(address)

    @allure.step('Нажимаем на поле метро')
    def click_station_field(self):
        self.driver.find_element(*self.station).click()

    @allure.step('Указываем станцию метро для первого заказа')
    def station_selection_1(self):
        self.driver.find_element(*self.station_names_1).click()

    @allure.step('Указываем станцию метро для второго заказа')
    def station_selection_2(self):
        self.driver.find_element(*self.station_names_2).click()

    @allure.step('Вводим телефон')
    def set_phone(self, phone):
        self.driver.find_element(*self.phone).send_keys(phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_next(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Создаем шаг для первого заказа')
    def first_order(self, name, surname, address, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_station_field()
        self.station_selection_1()
        self.set_phone(phone)
        self.click_next()

    @allure.step('Создаем шаг для второго заказа')
    def second_order(self, name, surname, address, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_station_field()
        self.station_selection_2()
        self.set_phone(phone)
        self.click_next()


class RentScooter():

    header = [By.XPATH, '//*[@id="root"]/div/div[2]/div[1]']
    data_input = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]"]
    date_for_scooter_1 = [By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[6]"]
    date_for_scooter_2 = [By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[6]"]
    period_dropdown = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]']
    period_dropdown_scooter_1 = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[4]']
    period_dropdown_scooter_2 = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[6]']
    color_scooter_1 = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/label[1]']
    color_scooter_2 = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/label[2]']
    comment = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/input']
    order_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[2]']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем заголовок формы ввода параметров аренды')
    def find_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header))

    @allure.step('Нажимаем на поле дата')
    def click_date_field(self):
        self.driver.find_element(*self.data_input).click()

    @allure.step('Выбираем дату для первого заказа')
    def click_date_scooter_1(self):
        self.driver.find_element(*self.date_for_scooter_1).click()

    @allure.step('Выбираем дату для второго заказа')
    def click_date_scooter_2(self):
        self.driver.find_element(*self.date_for_scooter_2).click()

    @allure.step('Нажимаем на поле периода аренды')
    def click_period_dropdown(self):
        self.driver.find_element(*self.period_dropdown).click()

    @allure.step('Выбираем период аренды для первого заказа')
    def set_period_scooter_1(self):
        self.driver.find_element(*self.period_dropdown_scooter_1).click()

    @allure.step('Выбираем период аренды для второго заказа')
    def set_period_scooter_2(self):
        self.driver.find_element(*self.period_dropdown_scooter_2).click()

    @allure.step('Выбираем цвет для первого заказа')
    def set_color_scooter_1(self):
        self.driver.find_element(*self.color_scooter_1).click()

    @allure.step('Выбираем цвет для второго заказа')
    def set_color_scooter_2(self):
        self.driver.find_element(*self.color_scooter_2).click()

    @allure.step('Пишем комментарий курьеру')
    def set_comment(self, comment):
        self.driver.find_element(*self.comment).send_keys(comment)

    @allure.step('Нажимаем на кнопку заказа')
    def click_button_order(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Создаем шаг аренды для первого заказа')
    def first_scooter(self, comment):
        self.find_header()
        self.click_date_field()
        self.click_date_scooter_1()
        self.click_period_dropdown()
        self.set_period_scooter_1()
        self.set_color_scooter_1()
        self.set_comment(comment)
        self.click_button_order()

    @allure.step('Создаем шаг аренды для второго заказа')
    def second_scooter(self, comment):
        self.find_header()
        self.click_date_field()
        self.click_date_scooter_2()
        self.click_period_dropdown()
        self.set_period_scooter_2()
        self.set_color_scooter_2()
        self.set_comment(comment)
        self.click_button_order()


class OrderConfirmationWindow():

    header = [By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[1]']
    yes_button = [By.XPATH, '//button[text()="Да"]']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем заголовок окна подтверждения заказа')
    def find_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header))

    @allure.step('Нажимаем на кнопку "Да"')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Создаем шаг подтверждения первого заказа ')
    def order_confirmation_1(self):
        self.find_header()
        self.click_yes_button()

    @allure.step('Создаем шаг подтверждения второго заказа ')
    def order_confirmation_2(self):
        self.find_header()
        self.click_yes_button()


class WindowOfCompletedOrder():

    header = [By.XPATH, '//div[text()="Заказ оформлен"]']
    status_button = [By.XPATH, '//button[text()="Посмотреть статус"]']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем заголовок модального окна номера заказа')
    def find_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header))

    @allure.step('Кликаем кнопку Посмотреть статус')
    def click_status_button(self):
        self.driver.find_element(*self.status_button).click()

    @allure.step('Создание шага для просмотра статуса первого заказа')
    def completed_order_1(self):
        self.find_header()
        self.click_status_button()

    @allure.step('Создание шага для просмотра статуса первого заказа')
    def completed_order_2(self):
        self.find_header()
        self.click_status_button()

