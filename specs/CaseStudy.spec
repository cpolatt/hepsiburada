CaseStudy Specification
===================
Kullanıcı girişi yapılarak sepete ürün eklenmesi
------------------------------------------------
Kullanıcı Hepsiburada.com sitesini ziyaret eder
* Go to "https://www.hepsiburada.com/"

Kullanıcı giriş işlemi yapılır
* Login as "polat.cem22@gmail.com" "Y2VtcG9sYXQ3NTQxMjk="

Kullanıcı, burada satın almak istediği ürün için arama yapacaktır.
* Search as "kitap"

Kullanıcı, Arama sonucunda ekrana gelen ürün listesinden (veya tek bir sonuç da dönmüş
olabilir) ürün seçer
* Click element by xpath "(//li[@class='search-item col lg-1 md-1 sm-1  custom-hover not-fashion-flex'])[1]"

Seçilen ürün için 2 tane farklı satıcıdan ürün seçilip sepete eklenir
* Click element by xpath "//button[@id='addToCart']"
* Wait "10" seconds
* Click element by xpath "//a[@class='checkoutui-Modal-2iZXl']"
* Click element by xpath "(//div[@class='addToCart'])[1]"
* Wait "10" seconds

Kullanıcı girişi yapılmadan belirtilen ürünü sepete ekleme
----------------------------------------------------------
Kullanıcı Hepsiburada.com sitesini ziyaret eder
* Go to "https://www.hepsiburada.com/"

Kullanıcı, Kitap, Müzik, Film, Hobi kategorisine gelir. 
* Hover "//span[text()='Kitap, Müzik, Film, Hobi']" texts
* Wait "2" seconds

Uzaktan Kumandalı Arabalar sekmesine tıklar.
* Click element by xpath "//a[@class='sf-ChildMenuItems-3R6bj item-2124']"

Drone yedek parçaları kategorisini seçer.
* Scroll by visible element "(//div[@class='content-contentRoot content-child content-vertical'])[9]"
* Click element by xpath "(//div[@class='content-contentRoot content-child content-vertical'])[9]"
* Wait "2" seconds

Ürün seçer.
* Hover "//li[@id='i0']" texts
* Wait "2" seconds

Sepete ekler.
* Click element by xpath "//button[@data-test-id='product-info-button']"
* Wait "5" seconds
