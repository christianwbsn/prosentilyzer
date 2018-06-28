import csv
import re
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


def get_review(driver):
    content = []
    soup = BeautifulSoup(driver.page_source, 'lxml')
    reviews = soup.select(".item .content")
    for review in reviews:
        rev = review.text.strip()
        content.append(rev)
    return content
        
def get_rating(driver):
    rating = []
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for stars in soup.select(".item .top .container-star"):
        star = str(stars)
        yellow_pattern = "//laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png"
        yellow_star = re.findall(yellow_pattern, star)
        rating.append(len(yellow_star))
    return rating

def get_data(driver):
    data = []
    for x,y in zip(get_rating(driver), get_review(driver)):
        data.append((x,y))
    return data

urls = [ 
        "https://www.lazada.co.id/products/xiaomi-redmi-5a-grey-snapdragron-425-quad-core-i336294944-s346595741.html?spm=a2o4j.searchlist.list.10.c8eff239My5xSA&search=1", 
        "https://www.lazada.co.id/products/xiaomi-redmi-5a-rose-gold-snapdragron-425-quad-core-i169447311-s198910690.html?spm=a2o4j.searchlist.list.7.c8eff239EHeeBF&search=1",
        "https://www.lazada.co.id/products/xiaomi-redmi-5a-blue-snapdragron-425-quad-core-i169447310-s198910689.html?spm=a2o4j.searchlist.list.4.c8eff239dmynjm&search=1",
        "https://www.lazada.co.id/products/xiaomi-redmi-5a-gold-snapdragron-425-quad-core-i160043545-s181917409.html?spm=a2o4j.searchlist.list.4.3e784bca9NR55Q&search=1",
        "https://www.lazada.co.id/products/samsung-galaxy-j2-prime-hitam-i160028701-s181884089.html?spm=a2o4j.searchlist.list.5.4f31509cK655eZ&search=1",
        "https://www.lazada.co.id/products/samsung-galaxy-j7-2016-sm-j710-emas-i160027967-s181882650.html?spm=a2o4j.searchlist.list.1.79913ad49TyC4v&search=1",
        "https://www.lazada.co.id/products/samsung-galaxy-j2-prime-sm-g532-silver-i160028249-s181883052.html?spm=a2o4j.searchlist.list.3.4f31509cK655eZ&search=1",
        "https://www.lazada.co.id/products/case-anti-shock-anti-crack-elegant-softcase-for-xiaomi-redmi-5a-white-clear-free-tempered-glass-i160714927-s183461134.html?spm=a2o4j.searchlistcategory.list.17.56e255988JPvFD&search=1",
        "https://www.lazada.co.id/products/flashdisk-hp-64gb-silver-i154704976-s174866180.html?spm=a2o4j.searchlistcategory.list.1.677a60f12FiFVl&search=1",
        "https://www.lazada.co.id/products/xiaomi-mi-headset-hifi-35mm-stereo-in-ear-headphones-basic-hitam-i170863366-s200925990.html?spm=a2o4j.searchlistcategory.list.9.72581147ed3oGd&search=1",
        "https://www.lazada.co.id/products/headset-bluetooth-7star-wireless-s530-mini-portabel-41-nirkabel-colokan-charger-i191439429-s233415202.html?spm=a2o4j.searchlistcategory.list.56.72581147ed3oGd&search=1",
        "https://www.lazada.co.id/products/onix-cognos-zgpax-smartwatch-u9-dz09-gsm-sim-card-termasuk-box-strap-karet-i8593586-s375324746.html?spm=a2o4j.searchlistcategory.list.4.1d3b66ectSpozx&search=1"
        ]

review_data = []

if __name__ == "__main__":
    webdriver_path = '/usr/lib/chromium-browser/chromedriver'
    driver = webdriver.Chrome(webdriver_path)
    for url in urls:
        driver.implicitly_wait(80)
        driver.get(url)
        review_data += get_data(driver)
        while True :
            driver.implicitly_wait(20)
            button_xpath = "//button[@class='next-btn next-btn-normal next-btn-medium next-pagination-item next']"
            next_button = driver.find_element_by_xpath(button_xpath)
            if not next_button.is_enabled():
                break
            driver.execute_script("arguments[0].click();", next_button)
            driver.implicitly_wait(100)
            review_data += get_data(driver)
        with open('../../input/raw/lazada_review.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            for datum in review_data:
                writer.writerow([datum[0], datum[1]])
    driver.quit()
