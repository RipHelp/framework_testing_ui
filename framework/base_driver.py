"""
    Базовый класс
"""

from typing import Union

from attrdict import AttrDict
from selenium import webdriver

class BaseDriver:
    def __init__(self, driver: Union[webdriver.Remote, webdriver.Chrome], config: AttrDict):
        self.driver = driver
        self.config = config

    def kill(self):
        """Закрыть браузер"""
        self.driver.quit()