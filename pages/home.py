from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from pages.base import BasePage


class ImportantQuestions:

    header = [By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]']
    question_1 = [By.CSS_SELECTOR, '#accordion__heading-0']
    question_2 = [By.CSS_SELECTOR, '#accordion__heading-1']
    question_3 = [By.CSS_SELECTOR, '#accordion__heading-2']
    question_4 = [By.CSS_SELECTOR, '#accordion__heading-3']
    question_5 = [By.CSS_SELECTOR, '#accordion__heading-4']
    question_6 = [By.CSS_SELECTOR, '#accordion__heading-5']
    question_7 = [By.CSS_SELECTOR, '#accordion__heading-6']
    question_8 = [By.CSS_SELECTOR, '#accordion__heading-7']

    answer_1 = [By.CSS_SELECTOR, '#accordion__panel-0 > p']
    answer_2 = [By.CSS_SELECTOR, '#accordion__panel-1 > p']
    answer_3 = [By.CSS_SELECTOR, '#accordion__panel-2 > p']
    answer_4 = [By.CSS_SELECTOR, '#accordion__panel-3 > p']
    answer_5 = [By.CSS_SELECTOR, '#accordion__panel-4 > p']
    answer_6 = [By.CSS_SELECTOR, '#accordion__panel-5 > p']
    answer_7 = [By.CSS_SELECTOR, '#accordion__panel-6 > p']
    answer_8 = [By.CSS_SELECTOR, '#accordion__panel-7 > p']

    @allure.step('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем заголовок "Вопросы о важном"')
    def get_header(self):
        return self.driver.find_element(*self.header)

    @allure.step('Делаем скролл к списку вопросов')
    def scroll_to_header(self):
        header = self.get_header()
        self.driver.execute_script('arguments[0].scrollIntoView();', header)

    @allure.step('Нажимаем на первый вопрос')
    def click_question_1(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.question_1)))
        self.driver.find_element(*self.question_1).click()

    @allure.step('Получаем ответ на первый вопрос')
    def click_answer_1(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.answer_1)))
        return self.driver.find_element(*self.answer_1).text

    @allure.step('Нажимаем на второй вопрос')
    def click_question_2(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.question_2)))
        self.driver.find_element(*self.question_2).click()

    @allure.step('Получаем ответ на второй вопрос')
    def click_answer_2(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.answer_2)))
        return self.driver.find_element(*self.answer_2).text

    @allure.step('Нажимаем на третий вопрос')
    def click_question_3(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.question_3)))
        self.driver.find_element(*self.question_3).click()

    @allure.step('Получаем ответ на третий вопрос')
    def click_answer_3(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.answer_3)))
        return self.driver.find_element(*self.answer_3).text

    @allure.step('Нажимаем на четвертый вопрос')
    def click_question_4(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.question_4)))
        self.driver.find_element(*self.question_4).click()

    @allure.step('Получаем ответ на четвертый вопрос')
    def click_answer_4(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.answer_4)))
        return self.driver.find_element(*self.answer_4).text

    @allure.step('Нажимаем на пятый вопрос')
    def click_question_5(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.question_5)))
        self.driver.find_element(*self.question_5).click()

    @allure.step('Получаем ответ на пятый вопрос')
    def click_answer_5(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.answer_5)))
        return self.driver.find_element(*self.answer_5).text

    @allure.step('Нажимаем на шестой вопрос')
    def click_question_6(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.question_6)))
        self.driver.find_element(*self.question_6).click()

    @allure.step('Получаем ответ на шестой вопрос')
    def click_answer_6(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.answer_6)))
        return self.driver.find_element(*self.answer_6).text

    @allure.step('Нажимаем на седьмой вопрос')
    def click_question_7(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.question_7)))
        self.driver.find_element(*self.question_7).click()

    @allure.step('Получаем ответ на седьмой вопрос')
    def click_answer_7(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.answer_7)))
        return self.driver.find_element(*self.answer_7).text

    @allure.step('Нажимаем на восьмой вопрос')
    def click_question_8(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.question_8)))
        self.driver.find_element(*self.question_8).click()

    @allure.step('Получаем ответ на восьмой вопрос')
    def click_answer_8(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.answer_8)))
        return self.driver.find_element(*self.answer_8).text


class OrderByButton:

    button = [By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/button[1]']

    @allure.step('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*self.button).click()


# class Cookies:
#
#     cookie_button = [By.ID, 'rcc-confirm-button']
#     cookies = None
#
#     @allure.step('Инициализируем драйвер')
#     def __init__(self, driver):
#         self.driver = driver
#
#     @allure.step('Находим кнопку для установки cookies и кликаем по ней')
#     def click_consent_button(self):
#         self.driver.find_element(*self.cookie_button).click()
#
#     @allure.step('Сохраняем куки')
#     def get_cookies(self):
#         self.click_consent_button()
#         return self.driver.get_cookies()


class HomePage:
    button_order = [By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/button[1]']
    scooter_link = [By.XPATH, '/html/body/div/div/div[1]/div[1]/a[2]/img']
    yandex_link = [By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[1]/a[1]/img']

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    @allure.step('Открываем главную страницу заказа самоката')
    def open_page_scooter(self):
        base = BasePage(self.driver)
        base.open_home_page()

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()

    @allure.step('Нажимаем по логотипу Самокат')
    def click_logo_scooter(self):
        self.driver.find_element(*self.scooter_link).click()

    @allure.step('Нажимаем по логотипу Яндекса')
    def click_yandex_link(self):
        self.driver.find_element(*self.yandex_link).click()

    @allure.step('Создаем шаг для нажатия на логотип самоката')
    def click_in_logo_scooter(self):
        self.open_page_scooter()
        self.click_button_order()
        self.click_logo_scooter()