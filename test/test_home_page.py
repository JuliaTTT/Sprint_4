import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pages.home import ImportantQuestions
from pages.base import BasePage
from pages.home import HomePage


class TestHomePage:

    @allure.title('Инициализируем драйвер')
    def setup(self):
        self.driver = webdriver.Firefox()

    @allure.title('Проверка вопросов о важном #1')
    @allure.description('Проверяем первый вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_to_question_1(self):
        answer = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        click = ImportantQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_question_1()
        assert click.click_answer_1() == answer

    @allure.title('Проверка вопросов о важном #2')
    @allure.description('Проверяем второй вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_to_question_2(self):
        answer = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        click = ImportantQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_question_2()
        assert click.click_answer_2() == answer

    @allure.title('Проверка вопросов о важном #3')
    @allure.description('Проверяем третий вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_to_question_3(self):
        answer = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        click = ImportantQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_question_3()
        assert click.click_answer_3() == answer

    @allure.title('Проверка вопросов о важном #4')
    @allure.description('Проверяем четвертый вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_to_question_4(self):
        answer = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        click = ImportantQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_question_4()
        assert click.click_answer_4() == answer

    @allure.title('Проверка вопросов о важном #5')
    @allure.description('Проверяем пятый вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_to_question_5(self):
        answer = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        click = ImportantQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_question_5()
        assert click.click_answer_5() == answer

    @allure.title('Проверка вопросов о важном #6')
    @allure.description('Проверяем шестой вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_to_question_6(self):
        answer = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        click = ImportantQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_question_6()
        assert click.click_answer_6() == answer

    @allure.title('Проверка вопросов о важном #7')
    @allure.description('Проверяем седьмой вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_to_question_7(self):
        answer = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        click = ImportantQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_question_7()
        assert click.click_answer_7() == answer

    @allure.title('Проверка вопросов о важном #8')
    @allure.description('Проверяем восьмой вопрос и его ответ на соответствие')
    @allure.step('Сравниваем ожидаемые и актуальные данные')
    def test_answer_to_question_8(self):
        answer = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        click = ImportantQuestions(self.driver)
        base = BasePage(self.driver)
        base.open_home_page()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]')))
        click.scroll_to_header()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[text()="Вопросы о важном"]')))
        click.click_question_8()
        assert click.click_answer_8() == answer

    @allure.description('Проверяем переход на главную страницу сервера по клику на лого Самокат')
    @allure.title('Нажимаем на логотип Самокат')
    def test_click_scooter_logo(self):
        home_page_objects = HomePage(self.driver)
        home_page_objects.click_in_logo_scooter()
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/img')))
        assert self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/img')

    @allure.description('Проверяем переход на страницу Дзен по клику на логотип Яндекса')
    @allure.title('Нажимаем на логотип Яндекса')
    def test_click_yandex_logo(self):
        home_page = HomePage(self.driver)
        home_page.open_page_scooter()

        handles_before = self.driver.window_handles
        home_page.click_yandex_link()
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(len(handles_before) + 1))

        handles_current = self.driver.window_handles
        new_window = None
        for window in handles_current:
            if window not in handles_before:
                new_window = window
                break

        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://dzen.ru/?yredirect=true'))

        assert self.driver.title == 'Дзен'

    @allure.title('Закрываем драйвер')
    def teardown(self):
        self.driver.quit()