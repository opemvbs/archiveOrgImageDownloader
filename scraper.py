from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import os
import threading
import shutil

email = input("Your archive.org email account: ")
password = input("Your archive.org password: ")
url = input("Your archive.org book link: ")
dir = input("Your download directory/folder (relative to your current working directory): ")
pages = input("Your pages that will be downloaded: ")
quality = input("Your quality of images, from 0-10 (lower is better): ")
print("Starting...")

quality = int(quality)
pages = int(pages)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")  
driver = webdriver.Chrome("./chromedriver", options=chrome_options)
driver.get("https://archive.org/account/login")
print("Logging in...")

user = driver.find_element_by_name("username")
pwd = driver.find_element_by_name("password")

user.send_keys(email)
pwd.send_keys(password+"\n")
time.sleep(0.5)

s = requests.Session()
def Download(url, directory, bookname, pagenum):
    if(os.path.exists(directory)):
        pass
    else:
        os.mkdir(directory)
    time.sleep(0.5)
    r = requests.get(url, cookies=cookies_dict, stream=True)
    r.raw.decode_content = True
    if r.status_code == 200:
        time.sleep(1)
        print("Downloading page: " + str(pagenum))
        with open(directory + "/" + str(pagenum) + ".jpg", 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
            pass
        #print("Done downloading page: " + str(pagenum))
    else:
        print("Error " + r.status_code + " while downloading page: " + str(pagenum))
        driver.quit()
    driver.quit()


def split(string):
    splitstring = []
    for i in str(string):
        splitstring.append(i)
    return splitstring


def join(array):
    result = ""
    for i in array:
        result += str(i)
    return result


def FloatToString(float, digits):
    float = split(str(float))[1:digits]
    float = "".join(float)
    float = float.replace(".", "")
    if(len(split(float)) != 4):
        float = "0" + float
    return float


def GetPagesArray(srcurl, maxpages):
    pages = []
    srcurl = srcurl.split("&scale=4")
    tmp = split(srcurl[0])
    tmp[len(tmp)-1] = "2&scale=" + str(quality)
    tmp = "".join(tmp)
    srcurl = str(tmp)
    modurl = srcurl
    i = 0.0001
    while(len(split(str(maxpages))) != 4):
        maxpages = "0" + str(maxpages)
    if(len(split(maxpages)) == 4):
        maxpages = "0." + str(maxpages)
    maxpages = float(maxpages)
    while(i < maxpages):
        modurl = modurl.split(".jp2")
        spliturl = split(modurl[0])
        spliturl = spliturl[:len(spliturl)-4]
        value = split(FloatToString(i, 6))
        spliturl += value
        modurl = "".join(spliturl) + ".jp2" + "&scale=" + str(quality)
        modurl = "".join(modurl)
        pages.append(modurl)
        modurl = srcurl
        i += 0.0001
    time.sleep(0.5)
    return pages


def GetBaseUrl(bookurl, num = 0):
    success = 0
    while(success != 1):
        if(num == 0):
            driver.get(bookurl)
        try:
            base = driver.find_elements_by_class_name("BRpageimage")[1].get_attribute("src")
            success = 1
        except Exception:
            num = num+1
            pass
    cookies = driver.get_cookies()
    global cookies_dict
    cookies_list = {}
    for cookie in cookies:
       cookies_list[cookie['name']] = cookie['value']
    cookies_dict = dict(cookies_list)
    time.sleep(0.5)
    return base


print("Finding pages...")
download = GetPagesArray(GetBaseUrl(url), pages)
print("Downloading pages...")
for i in range(len(download)):
    threading.Thread(target=Download, args=(download[i], dir, "", i)).start()
    time.sleep(0.5)