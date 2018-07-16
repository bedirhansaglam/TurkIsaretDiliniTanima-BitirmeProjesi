

# Leap Motion Sensör İle Türk İşaret Dilini Tanıma
Bedirhan Sağlam, Emre Yarar, Gülsüm Balci, Abdulkadir Karacı <br />
Bilgisayar Mühendisliği Bölümü, Kastamonu Üniversitesi, Kastamonu, Türkiye <br />
bedirhanssaglam@gmail.com, emreyarar25@gmail.com, gulsumbalci14@gmail.com, akaraci@kastamonu.edu.tr 

**Özet:**  Toplumumuzda işaret dili bilmeyen insanların sayısı fazladır. Bu durum işitme engelli insanlar ile toplumun arasındaki iletişimi azaltmaktadır hatta işitme engelli insanların toplumdan soyutlanmasına neden olmaktadır. Bu çalışma ile işaret dili bilen insanlar ile işaret dili bilmeyen insanlar arasındaki iletişimi sağlamak ve bu engelli insanları topluma kazandırmak amaçlanmaktadır. Bu amaçla Türk Dili Kurumunun (TDK) hazırladığı Türk İşaret Dili sözlüğü referans alınarak işaret dili alfabesi Leap Motion cihazı ile tanıtılmıştır. Tasarlanan bu sistem ile hem sağ hem de sol el verileri üzerinde çalışılmıştır. İki bireyden ilk önce 10 harf için toplam 1000 örnek ve daha sonra 28 harf için toplam 2800 örnek alınarak verilerin %70’i eğitim verisi %30’u test verisi olarak ayrılmıştır. Bu veri kümelerine makine öğrenmesi algoritmalarından Rastgele Orman ( Random Forest), Yapay Sinir Ağları (Neural Network), Navie Bayes ve Destek Vektör Makineleri (Support Vector Machine) algoritmaları uygulanıp test edilerek çevrimdışı (offline) ve gerçek zamanlı (online) başarım sonuçları elde edilmiştir. Başarım sonuçları karşılaştırılarak detaylı analiz yapılmıştır.  Çevrimdışı testte her iki örnek verisi için de en iyi sonucu %100 doğru başarım ile Rastgele Orman (Random Forest) algoritması vermektedir.

<br />**Anahtar Kelime:** işaret dili sözlüğü, leap motion, makine öğrenmesi metotları, çevrimdışı test, gerçek zamanlı test
<br /><br />**Abstract:**  There are more people in our society who do not know the sign language. This reduces the communication between people with hearing impairment and society, and even causes the hearing impaired people to be isolated from society. Through this study, it is aimed to provide communication between people who know sign language and people who do not speak sign language and to bring people with disabilities to community. For this purpose, with reference to the Turkish Sign Language, prepared by the Turkish Language Institute (TDK), the sign language alphabet was introduced with the Leap Motion device. With this system designed, both right and left hands were worked on. For two individuals, first a total of 1000 samples for 10 letters and then a total of 2800 samples for 28 letters, 70% of the data were divided into training data and 30% as test data. By applying and testing the algorithms of machine learning algorithms to these data sets, Random Forest, Neural Network, Navie Bayes and Support Vector Machine algorithms, (online) performance results were obtained. Detailed analysis was made by comparing the results of the achievement. The best result for both sample data in the offline test is the Random Forest algorithm with 100% correct performance

## ÇALIŞMA ORTAMI

### A-Verilerin Kayıt Edilmesi

![save data calisma ortami-min](https://user-images.githubusercontent.com/21055045/42748794-1f644e8a-88ea-11e8-95b7-c2222aca85fc.png)
![save data](https://user-images.githubusercontent.com/21055045/42748800-23f11794-88ea-11e8-8373-7c659572aa38.png)

### B-Gerçek Zamanlı Test
![save data calisma ortami-min](https://user-images.githubusercontent.com/21055045/42748794-1f644e8a-88ea-11e8-95b7-c2222aca85fc.png)
![gercek zamanli test uygulama ekrani](https://user-images.githubusercontent.com/21055045/42748822-332fac2a-88ea-11e8-95da-10a4cb4b0138.png)

### C-Çevrimdışı Test
##### C1-Verileri Yükle
![1- verileri yukle](https://user-images.githubusercontent.com/21055045/42748838-40ef9cda-88ea-11e8-80af-b2bc6dc570be.png)
##### C2-Sınıflandırıcı Seç
![2-siniflandirici sec](https://user-images.githubusercontent.com/21055045/42748839-410ebade-88ea-11e8-949e-2bfd6477a95e.png)
##### C3-Eğitim ve Test Yüzdesi Belirle , Test Et
![3- egitim ve test yuzdesi belirle ve test et](https://user-images.githubusercontent.com/21055045/42748840-412f5d0c-88ea-11e8-9bad-c74af9dd4fe5.png)
##### C4 - Başarı Oranı
![4-basari orani](https://user-images.githubusercontent.com/21055045/42748841-415e7b96-88ea-11e8-8d75-797e9840d6c6.png)
##### C5 - Eğitim Verisi
![5-egitim verisi](https://user-images.githubusercontent.com/21055045/42748842-417e47d2-88ea-11e8-9d21-fc9ad925c1d5.png)
##### C6 - Eğitim Verisi Hedef Etiketler
![6-egitim verisi hedef etiketler](https://user-images.githubusercontent.com/21055045/42748844-41c46c3a-88ea-11e8-8ace-5f23eec64725.png)
##### C7 - Test Verisi
![7-test verisi](https://user-images.githubusercontent.com/21055045/42748845-41ea7dda-88ea-11e8-877e-ae685c611ff5.png)
##### C8 - Test Verisi Hedef Etiketler
![8-test verisi hedef etiketler](https://user-images.githubusercontent.com/21055045/42748846-42296004-88ea-11e8-96d2-9de7edd88f27.png)
##### C9 - Karmaşıklık Matrisi
![9-karmasiklik matrisi](https://user-images.githubusercontent.com/21055045/42748847-425ac4f0-88ea-11e8-9c9f-a4703104a2d9.png)
##### C10 - Karmaşıklık Matrisi Tam Boyut
![10-karmasiklik matrisi tam boyut](https://user-images.githubusercontent.com/21055045/42748848-427a0b76-88ea-11e8-92cf-64c9a802af71.png)


