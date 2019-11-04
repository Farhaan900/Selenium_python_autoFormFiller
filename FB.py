'''
Created on Nov 1, 2019

@author: farhaan
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def build_chrome_options():

        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_untrusted_certs = True
        chrome_options.assume_untrusted_cert_issuer = True
        # chrome configuration
        # More: https://github.com/SeleniumHQ/docker-selenium/issues/89
        # And: https://github.com/SeleniumHQ/docker-selenium/issues/87
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-impl-side-painting")
#         chrome_options.add_argument("--disable-setuid-sandbox")
#         chrome_options.add_argument("--disable-seccomp-filter-sandbox")
#         chrome_options.add_argument("--disable-breakpad")
#         chrome_options.add_argument("--disable-client-side-phishing-detection")
#         chrome_options.add_argument("--disable-cast")
#         chrome_options.add_argument("--disable-cast-streaming-hw-encoding")
#         chrome_options.add_argument("--disable-cloud-import")
#         chrome_options.add_argument("--disable-popup-blocking")
#         chrome_options.add_argument("--ignore-certificate-errors")
#         chrome_options.add_argument("--disable-session-crashed-bubble")
#         chrome_options.add_argument("--disable-ipv6")
#         chrome_options.add_argument("--allow-http-screen-capture")
        chrome_options.add_argument("--start-maximized")

        return chrome_options 

def main():
    
    options = build_chrome_options()
    driver = webdriver.Chrome('usr/bin/chromedriver',options=options)
    
    user_name = "yourUserName"
    password = "yourPassword"
    driver.get("https://www.facebook.com")
    element = driver.find_element_by_id("email")
    element.send_keys(user_name)
    element = driver.find_element_by_id("pass")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    element.close()

if __name__ == "__main__":
    main()