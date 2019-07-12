# -*- coding: utf-8 -*-

import time
import logging
from datetime import datetime

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


logger = logging.getLogger(__name__)


def get_sms(phone, from_='', timestamp=0):
    logger.info("Getting sms from=%s", from_)

    options = ChromeOptions()
    options.add_argument('headless')
    driver = None
    try:
        driver = Chrome(chrome_options=options)
        driver.get('https://smska.us/')
        locator = (By.XPATH,
                   "//div[@class='phone_body %s']/div[@class='bodysms']" %
                   phone.replace('+7', ''))
        res = []
        for el in driver.find_elements(*locator):
            number = el.find_element_by_xpath(
                "./div[@class='smsnumber']").text.strip()
            date = el.find_element_by_xpath(
                "./div[@class='smsdate']").text.strip()
            ts = datetime.strptime(
                date, '%Y-%m-%d %H:%M:%S').timestamp()
            message = el.find_element_by_xpath(
                "./div[@class='textsms']").text.strip()
            res.append((number, ts, message))

        if from_:
            res = list(filter(lambda o: o[0] == from_, res))

        if timestamp:
            res = list(filter(lambda o: o[1] > timestamp, res))

        return res
    finally:
        driver.quit()


def wait_for_sms(phone, from_='', timestamp=0, polling_timeout=1, timeout=300):
    code = None
    start = time.time()
    while True:
        sms = get_sms(phone, from_=from_, timestamp=timestamp)
        if sms:
            code = sms[0][2].split(':')[1].strip()
            break
        if time.time() - start > timeout:
            raise RuntimeError('Waiting for sms from "%s" timed out!')
        time.sleep(polling_timeout)

    return code
