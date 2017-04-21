from selenium import webdriver
service_args = [ '--proxy=localhost:1080', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path="D:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.get("https://www.google.com")
print(driver.page_source)
driver.close()