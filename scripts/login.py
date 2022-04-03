from selenium import webdriver
import yaml
import sys
import os

# lan_login_root = os.environ['LAN_LOGIN_ROOT']

class LAN:

   def __init__(self):

      # self.loginSiteUrl = 'http://172.16.1.3:8002/index.php?zone=mnit'
      self.loginSiteUrl = 'http://mnit.ac.in'
      self.usernameXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[2]/td[2]/input'
      self.passwordXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[3]/td[2]/input'
      self.submit_buttonXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[5]/td/center/input'

      self.chromedriver_path = 'chromedriver/chromedriver.exe'
      self.browser_details_path = 'config/browser_details.yml'
      self.login_details_path = 'config/login_details.yml'

      self.username, self.password = self.getLoginDetails()
      self.driver = self.getWebDriver()

   def getLoginDetails(self):
      conf = yaml.load(open(self.login_details_path), Loader = yaml.BaseLoader)
      username = conf['lanUser']['collegeId']
      password = conf['lanUser']['password']

      return (username, password)

   def getWebDriver(self):
      
      option = webdriver.ChromeOptions()
      option.binary_location = self.getBrowserPath()
      # option.add_argument("--incognito") OPTIONAL
      # option.add_argument("--headless") OPTIONAL

      return (webdriver.Chrome(executable_path = self.chromedriver_path, options = option))

   def getBrowserPath(self):
      browser_path = 'C:/Program Files{}/{}/Application/{}.exe'

      browser_folder = {
         'chrome': 'Google/Chrome',
         'msedge': 'Microsoft/Edge',
         'brave': 'BraveSoftware/Brave-Browser'
      }

      browser_arch_folder = {
         'x64': '',
         'x86': ' (x86)'
      }

      browser_details = yaml.load(open(self.browser_details_path), Loader = yaml.BaseLoader)
      browser_name = (browser_details['browser']['name']).lower()
      browser_arch = (browser_details['browser']['arch']).lower()

      if browser_name not in browser_folder:
         raise Exception('Invalid browser name!')

      if browser_arch not in browser_arch_folder:
         raise Exception('Invalid browser architecture!')

      return (browser_path.format(browser_arch_folder.get(browser_arch),  browser_folder.get(browser_name), browser_name))

   def login(self):
      try:
         self.driver.get(self.loginSiteUrl)

         self.driver.find_element_by_xpath(self.usernameXpath).send_keys(self.username)
         self.driver.find_element_by_xpath(self.passwordXpath).send_keys(self.password)

         self.driver.find_element_by_xpath(self.submit_buttonXpath).click()
      
      except Exception as e:
         print(e)
         self.driver.quit()

if __name__ == '__main__':

   LAN().login()