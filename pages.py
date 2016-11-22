# -*- coding: utf-8 -*-

from io import BytesIO
from urllib.request import urlopen

from page_object import PageObject, PageElement, PageElements
from page_object.elements import Button, Checkbox, Link, Radio, Select, Textbox
from pytesseract import image_to_string

try:
    from PIL import Image
except ImportError:
    from pil import Image


def resolve_captcha(url):
    response = urlopen(url)
    img = Image.open(BytesIO(response.read()))

    return image_to_string(img, config="-psm 8")


class KaskoCalcPage(PageObject):
    URL = 'http://www.reso.ru/Retail/Motor/Calculator/'

    another_sk = Checkbox(id="AnotherSK")
    previous_sk = Select(id="dictPreviousSK")
    pay_period = Select(name="payPeriod")
    face = Select(name="face")
    is_bank = Checkbox(id="isBank")
    dtp_count = Textbox(name="CarDamageQuanityManual")
    auto_race = Checkbox(id="autoRace")
    price = Textbox(name="price")
    year = Select(name="year")
    purchase_date = Textbox(name="purchaseDate")
    add_driver = Button(name="addDriver")
    steal_device = Select(name="stealDevice")
    is_thf_mech_device = Checkbox(id="isThfMechDevice")
    captcha = PageElement(xpath="//img[@class='code']")
    code = Textbox(name="codeImage")
    calculation = Button(name="calculation")

    def brand_model(self, brand, model):
        Button(xpath=("//input[@name='modelName']"
                      "/../input[@type='button']")).__get__(
                          self, self.__class__).click()

        self.webdriver.switch_to_window(
            self.webdriver.window_handles[1])

        Link(xpath=("//table/tbody/tr"
                    "/td[contains(text(), '%s')]/.."
                    "/td/span[contains(text(), '%s')]") %
             (brand, model)).__get__(self, self.__class__).click()

        self.webdriver.switch_to_window(
            self.webdriver.window_handles[0])

    def territory_name(self, value):
        Button(xpath=("//input[@name='territoryName']"
                      "/../input[@type='button']")).__get__(
                          self, self.__class__).click()

        self.webdriver.switch_to_window(
            self.webdriver.window_handles[1])

        Link(xpath=("//table/tbody/tr"
                    "/td/span[contains(text(), '%s')]") % value).__get__(
                        self, self.__class__).click()

        self.webdriver.switch_to_window(
            self.webdriver.window_handles[0])

    def owner_address(self, value):
        Button(xpath=("//input[@name='ownerAddressName']"
                      "/../input[@type='button']")).__get__(
                          self, self.__class__).click()

        self.webdriver.switch_to_window(
            self.webdriver.window_handles[1])

        Link(xpath=("//table/tbody/tr"
                    "/td/span[contains(text(), '%s')]") % value).__get__(
                        self, self.__class__).click()

        self.webdriver.switch_to_window(
            self.webdriver.window_handles[0])

    def driver_list(self, value):
        Radio(xpath=("//label/a[contains(text(), '%s')]"
                     "/../../input") % value).__get__(
                         self, self.__class__).click()

    def driver_age(self, index, value):
        Textbox(name="driverAge%d" % index).__set__(self, value)

    def driver_stage(self, index, value):
        Textbox(name="driverStage%d" % index).__set__(self, value)

    def driver_sex(self, index, value):
        Select(name="driverSex%d" % index).__set__(self, value)

    def payment(self, value):
        Radio(xpath=("//label[contains(text(), '%s')]"
                     "/../input") % value).__get__(
                         self, self.__class__).click()

    @property
    def error(self):
        return PageElement(id="error").__get__(self, self.__class__).text

    @property
    def result(self):
        rows = PageElements(xpath="//table[@id='result']/tbody/tr").__get__(
            self, self.__class__)[9:18]

        return [(row.find_element_by_xpath(".//td[1]").text,
                 row.find_element_by_xpath(".//td[2]").text)
                for row in rows]
