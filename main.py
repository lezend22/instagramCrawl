import os
import time
from urllib.request import urlopen
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup

#os.system("clear")

def putUrl():
    instaUrl = input("#Paste your Url : ")
    if instaUrl:
        return instaUrl
    else:
        print("Put correct Url")
        putUrl()

def singleCrawl(soup, instaUrl):
    n=1
    div = soup.select_one("._97aPb")
    imgUrl = div.select_one(".KL4Bh").img['src']
    with urlopen(imgUrl) as f:
        with open('./img/'+ str(int(time.time()))+ str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)

def doubleCrawl(ul, instaUrl):
    li = ul.select('li.Ckrof')
    n = 1
    for x in li:
        imgUrl = x.select_one('.KL4Bh').img['src']
        with urlopen(imgUrl) as f:
            with open(str(int(time.time()))+ str(n) + '.jpg', 'wb') as h:
                img = f.read()
                h.write(img)

        n += 1

def main():
    instaUrl = putUrl()
    driver = webdriver.Chrome()
    driver.get(instaUrl)
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html)
    ul = soup.select_one('ul.vi798')
    driver.close()
    if ul is None:
        singleCrawl(soup, instaUrl)
    else:
        doubleCrawl(ul, instaUrl)



main()


### instagram login
#instaLogInUrl = "https://www.instagram.com/"
#driver.get(instaLogInUrl)
#time.sleep(2)
#driver.find_element_by_name('username').send_keys('id')
#driver.find_element_by_name('password').send_keys('password')
#driver.find_element_by_name('password').submit()

