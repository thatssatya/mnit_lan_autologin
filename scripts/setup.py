import sys
import subprocess
import pkg_resources

def install_required_packages():
    required  = {'selenium', 'webdriver_manager', 'winshell', 'pyyaml', 'pypiwin32'} 
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        print('installing', missing)
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

if __name__ == '__main__':
    install_required_packages()

















# def download_chromedriver():
#     import os
#     import requests
#     import wget
#     import zipfile

#     def get_latestversion(version):
#         url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + str(version)
#         response = requests.get(url)
#         version_number = response.text
#         return version_number
#     def download(download_url, driver_binaryname, target_name):
        
#         latest_driver_zip = wget.download(download_url, out='chromedriver.zip')

#         with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
#             zip_ref.extractall('./chromedriver/')
        
#         os.remove(latest_driver_zip)
#         os.rename(driver_binaryname, target_name)
#         os.chmod(target_name, 755)

#     if os.name == 'nt':

#         browser_folder = {
#             'chrome': r'Google\Chrome',
#             'msedge': r'Microsoft\Edge',
#             'brave': r'BraveSoftware\Brave-Browser'
#         }

#         browser_details = yaml.load(open(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, \
#           r'config\browser_details.yml')), Loader = yaml.BaseLoader)
#         browser_name = (browser_details['browser']['name']).lower()

#         if browser_name not in browser_folder:
#             raise Exception('Invalid browser name!')

#         reg_path = r'"HKEY_CURRENT_USER\Software\{}\BLBeacon"'.format(browser_folder.get(browser_name))

#         replies = os.popen('reg query ' + reg_path + ' /v version').read()
#         replies = replies.split('\n')
#         for reply in replies:
#             if 'version' in reply:
#                 reply = reply.rstrip()
#                 reply = reply.lstrip()
#                 tokens = re.split(r"\s+", reply)
#                 fullversion = tokens[len(tokens) - 1]
#                 tokens = fullversion.split('.')
#                 version = tokens[0]
#                 break
#         target_name = './chromedriver/chromedriver-win-' + version + '.exe'
#         found = os.path.exists(target_name)
#         if not found:
#             version_number = get_latestversion(version)
            
#             download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"
#             download(download_url, './chromedriver/chromedriver.exe', target_name)

#     # elif os.name == 'posix':
#     #     reply = os.popen(r'chromium --version').read()

#     #     if reply != '':
#     #         reply = reply.rstrip()
#     #         reply = reply.lstrip()
#     #         tokens = re.split(r"\s+", reply)
#     #         fullversion = tokens[1]
#     #         tokens = fullversion.split('.')
#     #         version = tokens[0]
#     #     else:
#     #         reply = os.popen(r'google-chrome --version').read()
#     #         reply = reply.rstrip()
#     #         reply = reply.lstrip()
#     #         tokens = re.split(r"\s+", reply)
#     #         fullversion = tokens[2]
#     #         tokens = fullversion.split('.')
#     #         version = tokens[0]

#     #     target_name = './bin/chromedriver-linux-' + version
#     #     print('new chrome driver at ' + target_name)
#     #     found = os.path.exists(target_name)
#     #     if not found:
#     #         version_number = get_latestversion(version)
#     #         download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_linux64.zip"
#     #         download(download_url, './temp/chromedriver', target_name)
