from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import yaml, os, time

class LAN:

   def __init__(self):

      # self.loginSiteUrl = 'http://172.16.1.3:8002/index.php?zone=mnit'
      self.loginSiteUrl = 'http://mnit.ac.in'
      self.usernameXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[2]/td[2]/input'
      self.passwordXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[3]/td[2]/input'
      self.submit_buttonXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[5]/td/center/input'

      self.root = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir)

      self.browser_details_path = os.path.join(self.root, r'config\browser_details.yml')
      self.login_details_path = os.path.join(self.root, r'config\login_details.yml')

      self.username, self.password = self.getLoginDetails()
      self.driver = self.getWebDriver()

   def getLoginDetails(self):
      conf = yaml.load(open(self.login_details_path), Loader = yaml.BaseLoader)
      username = conf['lanUser']['collegeId']
      password = conf['lanUser']['password']

      return (username, password)

   def getWebDriver(self):
      option = Options()
      option.binary_location = self.getBrowserPath()
      option.add_argument("--headless")
      option.add_experimental_option("excludeSwitches", ["enable-logging"])

      return (webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = option))
      # return (webdriver.Chrome(executable_path = os.path.join(self.root, 'chromedriver', 'chromedriver.exe'), options = option))


   def getBrowserPath(self):
      browser_path = r'C:\Program Files{}\{}\Application\{}.exe'

      browser_folder = {
         'chrome': r'Google\Chrome',
         'msedge': r'Microsof\Edge',
         'brave': r'BraveSoftware\Brave-Browser'
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
         print('Trying logging into LAN...')
         print('Opening login URL...')
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
   