## Lazada Product Review Data
----

## Structure
```
 input---|
         |--- dictionary <--- text dictionary for preprocessing
         |
         |--- preprocessed <--- cleaned review data
         |
         |--- raw <----- raw data scraped from Lazada
         |
         |--- pretrained vector <----- fastText wordvector in Bahasa Indonesia
```
## About the Data
Data is a product review from e-commerce Lazada Indonesia (primarily electronic, gadget).
    1. Raw data consist of 2 columns which is rating(1-5) and review(text) in Bahasa Indonesia
    2. Preprocessed data consist of 2 columns which is review(word_list) and sentiment(0 or 1) 


## Sources
1. Data used for this project are scraped from [Lazada Indonesia](https://www.lazada.co.id/)
    * Below is a list of pages that become the source of product review data
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

2. Dictionary gathered from Github [Rama Prakoso](https://github.com/ramaprakoso/analisis-sentimen)