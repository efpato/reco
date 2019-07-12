# -*- coding: utf-8 -*-

import logging
from time import sleep

from page_object.ui.jquery import Select as S
from page_object.ui.jquery import SelectWrapper as SW
from page_object.ui.jquery import Textbox, TextboxWrapper


logger = logging.getLogger(__name__)


class AutocompleteTextboxWrapper(TextboxWrapper):
    def enter_text(self, value):
        logger.info("%r entering text `%s` ...", self, value)
        self._el.parent.execute_script(
            """
            $("{0}").next().val('{1}').trigger('input');
            setTimeout(function () {{
                $("li.ui-menu-item div:contains('{1}')").click();
            }}, 1000);
            """.format(self._locator[1], value))
        sleep(1)


class AutocompleteTextbox(Textbox):
    def __get__(self, instance, owner):
        el = AutocompleteTextboxWrapper(
            self.find(instance.webdriver), self._locator)
        el.move_to_self()
        return el


class SelectWrapper(SW):
    def select_by_text(self, text):
        logger.info('%r selecting by text "%s" ...', self, text)
        self._el.parent.execute_script(
            """
            var el = $("{} + div.selectize-control");
            el.find("div.selectize-input").click();
            setTimeout(function () {{
                el.find("div.selectize-dropdown div:contains('{}')").click();
            }}, 1000);
            """.format(self._locator[1], text))
        sleep(1)


class Select(S):
    def __get__(self, instance, owner):
        el = SelectWrapper(self.find(instance.webdriver), self._locator)
        el.move_to_self()
        return el
