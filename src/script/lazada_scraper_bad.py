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
        if x <= 3:
            data.append((x,y))
    return data

urls = [ 
        "https://www.lazada.co.id/products/squishy-bakpao-warna-ukuran-kecilmini-gantungan-kunci-5cm-warna-random-1pcs-i144290848-s158479610.html?spm=a2o4j.searchlist.list.1.12943522AahAs1&search=1",
        "https://www.lazada.co.id/products/squishy-bun-panda-warna-7-cm-i110343133-s112384405.html?spm=a2o4j.searchlist.list.43.578d3522EMeAVH&search=1",
        "https://www.lazada.co.id/products/case-anti-shock-anti-crack-elegant-softcase-for-xiaomi-redmi-4x-white-clear-i108849519-s110628132.html?spm=a2o4j.searchlistcategory.list.5.70967b3cwhId6O&search=1",
        "https://www.lazada.co.id/products/powerbank-8800mah-otg-micro-untuk-semua-tipe-hp-i141180771-s152116140.html?spm=a2o4j.searchlistcategory.list.7.72f15a4b3XalHH&search=1",
        "https://www.lazada.co.id/products/cognos-garansi-18-bulan-power-bank-polymer-battery-real-capacity-with-lcd-10000-mah-i113795393-s117189238.html?spm=a2o4j.searchlistcategory.list.32.72f15a4b3XalHH&search=1",
        "https://www.lazada.co.id/products/powerbank-universal-slim-99000-mah-free-kabel-data-usb-warna-random-i207742782-s254052162.html?spm=a2o4j.searchlistcategory.list.59.72f15a4b3XalHH&search=1",
        "https://www.lazada.co.id/products/tempered-glass-screen-protector-for-xiaomi-redmi-note-4x-i103380446-s103889955.html?spm=a2o4j.searchlistcategory.list.21.1ecc6bfeddHIA1&search=1",
        "https://www.lazada.co.id/products/tempered-glass-screen-protector-for-xiaomi-redmi-note-4-i100060068-s100082444.html?spm=a2o4j.searchlistcategory.list.47.1bb76bfeFIp9lI&search=1",
        "https://www.lazada.co.id/products/onix-cognos-u-watch-u8-smartwatch-original-termasuk-box-hitam-i459738-s560025.html?spm=a2o4j.searchlistcategory.list.7.6baa27a3KYOvqr&search=1",
        "https://www.lazada.co.id/products/cognos-u-watch-u8-smartwatch-original-tanpa-box-hitam-i6888315-s8765058.html?spm=a2o4j.searchlistcategory.list.43.6baa27a3KYOvqr&search=1",
        "https://www.lazada.co.id/products/onix-cognos-smartwatch-u9-dz09-termasuk-box-gold-smart-watch-i419781-s511297.html?spm=a2o4j.searchlistcategory.list.40.6baa27a3KYOvqr&search=1",
        "https://www.lazada.co.id/products/onix-cognos-zgpax-smartwatch-u9-dz09-termasuk-box-hitam-strap-karet-i8723684-s11153133.html?spm=a2o4j.searchlistcategory.list.23.6baa27a3KYOvqr&search=1",
        "https://www.lazada.co.id/products/tongsis-3-in-1-tongsis-tripod-bluetooth-with-remote-acces-selfie-stick-i171960266-s202841704.html?spm=a2o4j.searchlistcategory.list.5.4e953728pz1LPh&search=1",
        "https://www.lazada.co.id/products/tongsis-mini-selfie-stick-dengan-remote-shutter-biru-i7163569-s9138582.html?spm=a2o4j.searchlistcategory.list.11.4e953728pz1LPh&search=1",
        "https://www.lazada.co.id/products/mini-fan-usb-kipas-angin-mini-handphone-portable-i101263047-s101448132.html?spm=a2o4j.searchlistcategory.list.136.27094896xRLLl9&search=1",
        "https://www.lazada.co.id/products/vr-box-generesi-ke-3-3d-virtual-reality-for-smartphone-ukuran-lebih-kecil-putih-i100009196-s100014538.html?spm=a2o4j.searchlistcategory.list.27.c5df42b5LT0qKp&search=1",
        "https://www.lazada.co.id/products/vr-box-generesi-ke-3-3d-virtual-reality-for-smartphone-ukuran-lebih-kecil-biru-i106163640-s107023961.html?spm=a2o4j.searchlistcategory.list.29.c5df42b5LT0qKp&search=1",
        "https://www.lazada.co.id/products/jam-tangan-led-jam-tangan-pria-dan-wanita-strap-karet-hitam-emas-pink-apple_black_rosegold-i102545830-s102897342.html?spm=a2o4j.searchlistcategory.list.13.112fc35aV4X87m&search=1",
        "https://www.lazada.co.id/products/santorini-jam-tangan-wanita-kulit-pu-fashion-stainless-steel-analog-quartz-women-lady-leather-watch-i108840140-s110617500.html?spm=a2o4j.searchlistcategory.list.31.112fc35aYWEmbr&search=1",
        "https://www.lazada.co.id/products/jam-tangan-quartz-1-pair-pria-dan-wanita-strap-kulit-pu-men-women-stainless-steel-leather-couple-watch-i7714227-s9815108.html?spm=a2o4j.searchlistcategory.list.21.3ac5c35afrr9md&search=1",
        "https://www.lazada.co.id/products/geneva-jam-tangan-wanita-analog-fashion-casual-women-strap-stainless-steel-wrist-quartz-watch-rose-gold-i7802633-s9928471.html?spm=a2o4j.searchlistcategory.list.79.3ac5c35afrr9md&search=1",
        "https://www.lazada.co.id/products/trisonic-stand-mixer-com-mixer-berdiri-putih-i6361492-s8020018.html?spm=a2o4j.searchlistcategory.list.5.79773168I8J2cb&search=1",
        "https://www.lazada.co.id/products/xtreamer-bien-3-set-top-box-stb-dvb-t2-and-media-player-televisi-film-foto-musik-tv-siaran-digital-support-full-hd-1080p-tv-tabung-lcd-led-plasma-bening-bebas-semut-kualitas-gambar-bagus-antena-uhf-teknologi-biasa-aksesoris-audio-video-k015-hitam-i105359581-s106157874.html?spm=a2o4j.searchlistcategory.list.1.18a96a4avwS86x&search=1",
        "https://www.lazada.co.id/products/dozn-celana-blackhawk-tactical-outdoor-blk-i106111252-s116099223.html?spm=a2o4j.searchlistcategory.list.12.1c505e7cTgntmB&search=1",
        "https://www.lazada.co.id/products/garuda-dompet-pria-men-long-wallet-zipper-credits-cards-mobile-phone-holder-hitam-i166468535-s194303895.html?spm=a2o4j.searchlistcategory.list.13.50943bd1s4C0sI&search=1",
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
        with open('../../input/raw/lazada_negative_review.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            for datum in review_data:
                writer.writerow([datum[0], datum[1]])
    driver.quit()
