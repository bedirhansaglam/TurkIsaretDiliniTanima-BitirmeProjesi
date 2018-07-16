

# Leap Motion Sensör İle Türk İşaret Dilini Tanıma
Bedirhan Sağlam, Emre Yarar, Gülsüm Balci, Abdulkadir Karacı <br />
Bilgisayar Mühendisliği Bölümü, Kastamonu Üniversitesi, Kastamonu, Türkiye <br />
bedirhanssaglam@gmail.com, emreyarar25@gmail.com, gulsumbalci14@gmail.com, akaraci@kastamonu.edu.tr 

**Özet:**  Toplumumuzda işaret dili bilmeyen insanların sayısı fazladır. Bu durum işitme engelli insanlar ile toplumun arasındaki iletişimi azaltmaktadır hatta işitme engelli insanların toplumdan soyutlanmasına neden olmaktadır. Bu çalışma ile işaret dili bilen insanlar ile işaret dili bilmeyen insanlar arasındaki iletişimi sağlamak ve bu engelli insanları topluma kazandırmak amaçlanmaktadır. Bu amaçla Türk Dili Kurumunun (TDK) hazırladığı Türk İşaret Dili sözlüğü referans alınarak işaret dili alfabesi Leap Motion cihazı ile tanıtılmıştır. Tasarlanan bu sistem ile hem sağ hem de sol el verileri üzerinde çalışılmıştır. İki bireyden ilk önce 10 harf için toplam 1000 örnek ve daha sonra 28 harf için toplam 2800 örnek alınarak verilerin %70’i eğitim verisi %30’u test verisi olarak ayrılmıştır. Bu veri kümelerine makine öğrenmesi algoritmalarından Rastgele Orman ( Random Forest), Yapay Sinir Ağları (Neural Network), Navie Bayes ve Destek Vektör Makineleri (Support Vector Machine) algoritmaları uygulanıp test edilerek çevrimdışı (offline) ve gerçek zamanlı (online) başarım sonuçları elde edilmiştir. Başarım sonuçları karşılaştırılarak detaylı analiz yapılmıştır.  Çevrimdışı testte her iki örnek verisi için de en iyi sonucu %100 doğru başarım ile Rastgele Orman (Random Forest) algoritması vermektedir.

<br />**Anahtar Kelime:** işaret dili sözlüğü, leap motion, makine öğrenmesi metotları, çevrimdışı test, gerçek zamanlı test
<br /><br />**Abstract:**  There are more people in our society who do not know the sign language. This reduces the communication between people with hearing impairment and society, and even causes the hearing impaired people to be isolated from society. Through this study, it is aimed to provide communication between people who know sign language and people who do not speak sign language and to bring people with disabilities to community. For this purpose, with reference to the Turkish Sign Language, prepared by the Turkish Language Institute (TDK), the sign language alphabet was introduced with the Leap Motion device. With this system designed, both right and left hands were worked on. For two individuals, first a total of 1000 samples for 10 letters and then a total of 2800 samples for 28 letters, 70% of the data were divided into training data and 30% as test data. By applying and testing the algorithms of machine learning algorithms to these data sets, Random Forest, Neural Network, Navie Bayes and Support Vector Machine algorithms, (online) performance results were obtained. Detailed analysis was made by comparing the results of the achievement. The best result for both sample data in the offline test is the Random Forest algorithm with 100% correct performance
