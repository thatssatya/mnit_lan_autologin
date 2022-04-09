from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from enum import Enum
import yaml, os, time, requests, glob



os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOG'] = '0'
os.environ['WDM_LOCAL'] = '1'
# os.environ['WDM_SSL_VERIFY'] = '0'
os.environ['WDM_PRINT_FIRST_LINE'] = 'False'

class Browser(Enum):
   CHROME = 1
   BRAVE = 2
   MSEDGE = 3

class Arch(Enum):
   x64 = 1
   x86 = 2

class LAN:

   def __init__(self):

      # self.loginSiteUrl = 'http://172.16.1.3:8002/index.php?zone=mnit'
      self.loginSiteUrl = 'http://mnit.ac.in'
      self.usernameXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[2]/td[2]/input'
      self.passwordXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[3]/td[2]/input'
      self.submit_buttonXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[5]/td/center/input'

      self.root = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir)

      self.browser_details_path = os.path.join(self.root, 'config', 'browser_details.yml')
      self.login_details_path = os.path.join(self.root, 'config', 'login_details.yml')

      self.browser = self.getBrowser()
      self.browser_arch = self.getBrowserArch()
      self.username, self.password = self.getLoginDetails()
      self.driver = self.getWebDriver()

   def getLoginDetails(self):
      conf = yaml.load(open(self.login_details_path), Loader = yaml.BaseLoader)
      username = conf['lanUser']['collegeId']
      password = conf['lanUser']['password']

      return (username, password)

   def getWebDriver(self):

      def getOptions():
         options_catalogue = {
            Browser.CHROME: webdriver.ChromeOptions(),
            Browser.BRAVE: webdriver.ChromeOptions(),
            Browser.MSEDGE: webdriver.EdgeOptions()
         }
         
         opt = options_catalogue.get(self.browser)
         opt.binary_location = self.getBrowserPath()

         opt.add_argument("--headless")
         opt.add_experimental_option("excludeSwitches", ["enable-logging"])

         return (opt)

      def getExecutablePath():
         try:
            if self.browser == Browser.CHROME:
               return (ChromeDriverManager().install())
            elif self.browser == Browser.BRAVE:
               return (ChromeDriverManager(chrome_type = ChromeType.BRAVE).install())
            elif self.browser == Browser.MSEDGE:
               return (EdgeChromiumDriverManager().install())

         except requests.exceptions.ConnectionError as ce:
            if os.path.exists(os.path.join(os.path.abspath(__file__), os.pardir, '.wdm')):
               if self.browser == Browser.CHROME or self.browser == Browser.BRAVE:
                  return (os.path.join(self.root, glob.glob(os.path.join('.', 'scripts', \
                           '.wdm', 'drivers', 'chromedriver', '*', '*', 'chromedriver.exe'))[0]))
               elif self.browser == Browser.MSEDGE:
                  return (os.path.join(self.root, glob.glob(os.path.join('.', 'scripts', \
                           '.wdm', 'drivers', 'edgedriver', '*', '*', 'msedgedriver.exe'))[0]))
            
            else:
               raise Exception('No webdriver found in cache!')

      def getService():
         if self.browser == Browser.CHROME or self.browser == Browser.BRAVE:
            return (ChromeService(executable_path = getExecutablePath()))
         elif self.browser == Browser.MSEDGE:
            return (EdgeService(executable_path = getExecutablePath()))

      
      if self.browser == Browser.CHROME or self.browser == Browser.BRAVE:
         return (webdriver.Chrome(service = getService(), options = getOptions()))
      elif self.browser == Browser.MSEDGE:
         return (webdriver.Edge(service = getService(), options = getOptions()))


   def getBrowser(self):

      browser_details = yaml.load(open(self.browser_details_path), Loader = yaml.BaseLoader)

      try:
         return Browser[(browser_details['browser']['name']).upper()]
      except Exception as e:
         raise Exception('Invalid browser name!')

   def getBrowserArch(self):

      browser_details = yaml.load(open(self.browser_details_path), Loader = yaml.BaseLoader)

      try:
         return Arch[(browser_details['browser']['arch']).lower()]
      except Exception as e:
         raise Exception('Invalid browser architecture!')

   def getBrowserPath(self):
      browser_path = r'C:\Program Files{}\{}\Application\{}.exe'

      browser_folder = {
         Browser.CHROME: r'Google\Chrome',
         Browser.MSEDGE: r'Microsoft\Edge',
         Browser.BRAVE: r'BraveSoftware\Brave-Browser'
      }

      browser_arch_folder = {
         Arch.x64: '',
         Arch.x86: ' (x86)'
      }

      return (browser_path.format(browser_arch_folder.get(self.browser_arch), \
         browser_folder.get(self.browser), self.browser.name.lower()))
   

   def login(self):
      try:
         print('Trying logging into LAN...')
         
         self.driver.get(self.loginSiteUrl)

         self.driver.find_element(By.XPATH, self.usernameXpath).send_keys(self.username)
         self.driver.find_element(By.XPATH, self.passwordXpath).send_keys(self.password)
         print('Entered username and password...')
         
         self.driver.find_element(By.XPATH, self.submit_buttonXpath).click()
         print('You\'re logged in now!')

      except Exception as e:
         self.driver.quit()
         if isinstance(e, NoSuchElementException):
            print('You\'re already logged in!')
         else:
            print('Exception occurred!', e)
      
      time.sleep(0.5)

if __name__ == '__main__':
   
   LAN().login()
   