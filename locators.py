from selenium.webdriver.common.by import By

name_field = [By.XPATH, './/input[@placeholder="* Имя"]']
surname_field = [By.XPATH, './/input[@placeholder="* Фамилия"]']
address_field = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
station_field = [By.XPATH, './/input[@placeholder="* Станция метро"]']
station = [By.XPATH, ".//li[@data-index={num}]"]
phone_field = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
date_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
time_field = [By.XPATH, './/span[@class="Dropdown-arrow"]']
days = [By.XPATH, './/div[text()="двое суток"]']
comment_field = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']
color_field = [By.CLASS_NAME, 'Order_Checkboxes__3lWSI']
next_button = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
confirm_button = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]']
track_status = [By.XPATH,
                './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Посмотреть статус"]']
order_button_header = [By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[text() = "Заказать"]']
order_button_finish = [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text() = "Заказать"]']
cancel_button = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"]']
cookie_button = [By.ID, "rcc-confirm-button"]
yandex_logo = [By.XPATH, './/img[@alt="Yandex"]']
scooter_logo = [By.XPATH, './/img[@alt="Scooter"]']
dzen_logo = [By.XPATH, './/div[@class="desktop-base-header__logoContainer-3l desktop-base-header__isMorda-mX"]']

question_0 = [By.XPATH, './/div[@aria-controls="accordion__panel-0"]']
question_1 = [By.XPATH, './/div[@aria-controls="accordion__panel-1"]']
question_2 = [By.XPATH, './/div[@aria-controls="accordion__panel-3"]']
question_3 = [By.XPATH, './/div[@aria-controls="accordion__panel-3"]']
question_4 = [By.XPATH, './/div[@aria-controls="accordion__panel-4"]']
question_5 = [By.XPATH, './/div[@aria-controls="accordion__panel-5"]']
question_6 = [By.XPATH, './/div[@aria-controls="accordion__panel-6"]']
question_7 = [By.XPATH, './/div[@aria-controls="accordion__panel-7"]']

answer_0 = [By.XPATH, './/div[@aria-labelledby="accordion__heading-0"]/p']
answer_1 = [By.XPATH, './/div[@aria-labelledby="accordion__heading-1"]/p']
answer_2 = [By.XPATH, './/div[@aria-labelledby="accordion__heading-2"]/p']
answer_3 = [By.XPATH, './/div[@aria-labelledby="accordion__heading-3"]/p']
answer_4 = [By.XPATH, './/div[@aria-labelledby="accordion__heading-4"]/p']
answer_5 = [By.XPATH, './/div[@aria-labelledby="accordion__heading-5"]/p']
answer_6 = [By.XPATH, './/div[@aria-labelledby="accordion__heading-6"]/p']
answer_7 = [By.XPATH, './/div[@aria-labelledby="accordion__heading-7"]/p']

texts = [
    'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
    'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
    'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
    'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
    'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
    'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
    'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
    'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
]