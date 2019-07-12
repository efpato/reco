# -*- coding: utf-8 -*-

from page_object import PageObject, PageElements
from page_object.ui.jquery import Button, Checkbox, Textbox

from elements import AutocompleteTextbox, Select


class KaskoCalcPage(PageObject):
    pay_period = Select(css="select[name='payPeriod']")

    car_brand = AutocompleteTextbox(css="input[name='carBrand']")
    car_model = AutocompleteTextbox(css="input[name='carModel']")
    car_year = Select(css="select[name='year']")
    price = Textbox(css="input[name='price']")
    steal_device = AutocompleteTextbox(css="input[name='stealDevice']")
    is_thf_mech_device = Checkbox(css="input#isThfMechDevice")
    auto_race = Checkbox(css="input#autoRace")
    is_bank = Checkbox(css="input#isBank")
    dtp_count = Textbox(css="input[name='CarDamageQuanityManual']")
    purchase_date = Textbox(css="input[name='purchaseDate']")

    region = AutocompleteTextbox(css="input[name='region']")
    owner_address = AutocompleteTextbox(css="input[name='ownerAddress']")

    face = Select(css="select[name='face']")
    drivers_unlimit = Button(css="input#driverList-0")
    drivers_limit = Button(css="input#driverList-1")
    drivers_unlimit_22 = Button(css="input#driverList-3")
    add_driver = Button(css="input[name='driverCount'] + a")

    payment_1 = Button(css="input#payment-1")
    payment_2 = Button(css="input#payment-2")

    another_sk = Checkbox(css="input#AnotherSK")
    previous_sk = Select(css="select[name='prevInsurantID']")

    calculation = Button(css="input[value='Рассчитать']")

    code = Textbox(css="input[name='code']")
    confirm = Button(css="input[value='Подтвердить']")

    def driver_age(self, index, value):
        Textbox(name="driverAge%d" % index).__set__(self, value)

    def driver_stage(self, index, value):
        Textbox(name="driverStage%d" % index).__set__(self, value)

    def driver_sex(self, index, value):
        if value.lower() == 'мужчина':
            Button(css="input[name='driverSex%d'][value='M']" % index).__get__(
                self, self.__class__).click()
        if value.lower() == 'женщина':
            Button(css="input[name='driverSex%d'][value='F']" % index).__get__(
                self, self.__class__).click()

    def resolve_recaptcha(self, phone, recaptcha_response):
        self.webdriver.execute_script(
            """
            $("input[name='phone']").val('%s');
            $("textarea#g-recaptcha-response").html("%s");
            ajaxSendCode();
            """ % (phone, recaptcha_response))

    @property
    def result(self):
        services = PageElements(
            xpath="//div[@class='service_item'][./div[@class='service_value']]"
        ).__get__(self, self.__class__)

        res = []
        for service in services:
            label = service.find_element_by_xpath(
                "./div[@class='service_label']").text.replace(
                    '\n', '').strip()
            value = service.find_element_by_xpath(
                "./div[@class='service_value']").text.replace(
                    '\n', ';').strip()
            res.append((label, value))

        return res
