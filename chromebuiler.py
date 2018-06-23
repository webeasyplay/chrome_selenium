from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os,time
class CHROME:
    pbundle_dir = ""
    chrome_driver = None

    def __init__(self,pbundle_dir,proxy=None):
        self.pbundle_dir = pbundle_dir
        CHROMEDRIVER_PATH = pbundle_dir + "/" + "chromedriver.exe"  # driver 路径
        WINDOW_SIZE = "1920,1048"  # 窗体大小
        chrome_op = Options()
        chrome_op.add_argument('--ignore-certificate-errors-spki-list')
        chrome_op.add_argument('--mute-audio')
        chrome_op.add_argument('--disable-gpu')
        chrome_op.add_argument('--disable-blink-features')
        chrome_op.add_argument('--disable-app-list-dismiss-on-blur')
        chrome_op.add_argument('--disable-core-animation-plugins')
        # chrome_op.add_argument(f'user-data-dir={desk_path}')
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_op.add_experimental_option("prefs", prefs)
        if proxy:
            chrome_op.add_argument('--proxy-server=%s' % proxy)

        # chrome_op.add_argument('--headless')
        chrome_op.add_argument('--ignore-ssl-errors')
        chrome_op.add_argument("--window-size=%s" % WINDOW_SIZE)
        self.chrome_driver = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_op
        )

if __name__ == '__main__':
    driver = CHROME(os.getcwd()).chrome_driver
    driver.get("https://google.com")
    time.sleep(5)
    driver.quit()


