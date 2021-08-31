from selenium import webdriver
import yaml
import sys

def getLoginDetails():
   conf = yaml.load(open('config/login_details.yml'))
   username = conf['lanUser']['collegeId']
   password = conf['lanUser']['password']

   return username, password

def getBrowserPath():
   browser_details = yaml.load(open('config/browser_details.yml'))
   browser_name = (browser_details['browser']['name']).lower()
   browser_arch = (browser_details['browser']['arch']).lower()

   if not ((browser_name == 'chrome' or browser_name == 'msedge' or browser_name == 'brave') and (browser_arch == 'x64' or browser_arch == 'x86')):
      print('Invalid browser details!')
      sys.exit()

   arch = ''
   browser_folder = ''

   if browser_arch == 'x86':
      arch = ' (x86)'
   if browser_name == 'chrome':
      browser_folder = 'Google/Chrome'
   elif browser_name == 'msedge':
      browser_folder = 'Microsoft/Edge'
   elif browser_name == 'brave':
      browser_folder = 'BraveSoftware/Brave-Browser'

   browser_path = 'C:/Program Files' + arch + '/' + browser_folder + '/Application/' + browser_name + '.exe'

   return browser_path

def getWebDriver():
   chromedriver_path = 'chromedriver/chromedriver.exe'
   option = webdriver.ChromeOptions()
   option.binary_location = getBrowserPath()
   # option.add_argument("--incognito") OPTIONAL
   # option.add_argument("--headless") OPTIONAL

   return webdriver.Chrome(executable_path = chromedriver_path, options = option)

def login(url, usernameXpath, username, passwordXpath, password, submit_buttonXpath):
   driver = getWebDriver()

   driver.get(url)
   driver.find_element_by_xpath(usernameXpath).send_keys(username)
   driver.find_element_by_xpath(passwordXpath).send_keys(password)
   driver.find_element_by_xpath(submit_buttonXpath).click()

if __name__ == '__main__':
   loginSiteUrl = 'http://172.16.1.3:8002/index.php?zone=mnit'
   # loginSiteUrl = 'https://cb.run/ILyB'
   usernameXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[2]/td[2]/input'
   passwordXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[3]/td[2]/input'
   submit_buttonXpath = '//*[@id=\"loginbox\"]/table/tbody/tr[5]/td/center/input'

   username, password = getLoginDetails()

   login(loginSiteUrl, usernameXpath, username, passwordXpath, password, submit_buttonXpath)