from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from com.onetest.healers import OllamaHealer
from com.onetest.utils import XPathUtils, PropertyManager


class SelfHealingDriver:
    def __init__(self, driver):
        self.driver = driver
        self.healing_enabled = PropertyManager.is_healing_enabled()
        print(self.healing_enabled)
        self.healer = OllamaHealer
        self.wait = WebDriverWait(driver, timeout=10)

    def find_element(self, locator: tuple[str, str], semantic_context: str) -> WebElement:
        try:
            # WAIT before finding
            print(f"Trying to find the element {locator[1]}")
            return self.wait.until(ec.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            if not self.healing_enabled:
                print("Healing not enabled, Raising Exception")
                raise e

            # AI healing ONLY for XPath
            if not locator[0] == By.XPATH:
                print(f"Element provided is not xpath: {locator}, AI healing currently supports only xpath.")
                raise e
            print(f"Broken XPath detected: {locator[1]}")

            broken_xpath = XPathUtils.extract_xpath(locator)
            page_source = self.driver.page_source.lstrip("<body>").rstrip("</body>")
            healed_locator = self.healer.heal(broken_xpath,page_source,semantic_context)
            print(f"Finding element with new xpath: {healed_locator}")
            # WAIT again for healed XPath
            return self.wait.until(ec.presence_of_element_located((By.XPATH,healed_locator)))

    def quit(self):
        self.driver.quit()