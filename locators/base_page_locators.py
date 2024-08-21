class BasePageLocators:
    TOP_PAGE_ORDER_BUTTON = ".//button[@class = 'Button_Button__ra12g']"
    BOTTOM_PAGE_ORDER_BUTTON = "//*[@id='root']/div/div/div[4]/div[2]/div[5]/button"

    LOGO_YANDEX = ".//a[@class = 'Header_LogoYandex__3TSOI']"
    LOGO_SCOOTER = ".//a[@class = 'Header_LogoYandex__3TSOI']"

    ABOUT_THE_IMPORTANT = ".//div[text() = 'Вопросы о важном']"

    WHAT_IS_THE_PRICE = ".//div[@id = 'accordion__heading-0']"
    WHAT_IS_THE_PRICE_OPEN = ".//div[@id ='accordion__panel-0']/p"
    WHAT_IS_THE_PRICE_TEXT = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    I_WANT_SEVERAL_AT_ONCE = ".//div[@id = 'accordion__heading-1']"
    I_WANT_SEVERAL_AT_ONCE_OPEN = ".//div[@id ='accordion__panel-1']/p"
    I_WANT_SEVERAL_AT_ONCE_TEXT = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    HOW_TIME_IS_CALCULATED = ".//div[@id = 'accordion__heading-2']"
    HOW_TIME_IS_CALCULATED_OPEN = ".//div[@id ='accordion__panel-2']/p"
    HOW_TIME_IS_CALCULATED_TEXT = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    POSSIBLE_TO_ORDER_FOR_TODAY = ".//div[@id = 'accordion__heading-3']"
    POSSIBLE_TO_ORDER_FOR_TODAY_OPEN = ".//div[@id ='accordion__panel-3']/p"
    POSSIBLE_TO_ORDER_FOR_TODAY_TEXT = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    POSSIBLE_TO_EXTEND_THE_ORDER = ".//div[@id = 'accordion__heading-4']"
    POSSIBLE_TO_EXTEND_THE_ORDER_OPEN = ".//div[@id ='accordion__panel-4']/p"
    POSSIBLE_TO_EXTEND_THE_ORDER_TEXT = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    DO_YOU_BRING_A_CHARGER = ".//div[@id = 'accordion__heading-5']"
    DO_YOU_BRING_A_CHARGER_OPEN = ".//div[@id ='accordion__panel-5']/p"
    DO_YOU_BRING_A_CHARGER_TEXT = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER = ".//div[@id = 'accordion__heading-6']"
    IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_OPEN = ".//div[@id ='accordion__panel-6']/p"
    IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_TEXT = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    I_LIVE_OUTSIDE_THE_MRR = ".//div[@id = 'accordion__heading-7']"
    I_LIVE_OUTSIDE_THE_MRR_OPEN = ".//div[@id ='accordion__panel-7']/p"
    I_LIVE_OUTSIDE_THE_MRR_TEXT = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
