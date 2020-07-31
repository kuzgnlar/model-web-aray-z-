<img src="assets/header_background.jpg" height ="38%" width="38%"></img> 

# Kuzgunlar Model Web Arayüzü

![Python 3](https://img.shields.io/badge/Python-3-yellow.svg)
![Dash Plotly](https://img.shields.io/badge/Dash-1.14-turquoise.svg)
![GPL 3.0](https://img.shields.io/badge/license-GPLv3-red.svg)

Bu paket Kuzgunlar Doğal Dil İşleme modellerinin son kullanıcılar tarafından kolayca kullanılabilmesi için hazırlanmıştır.

## :exclamation: Gereksinimler

 * Python3.4 veya daha üst bir Python sürümü.
 * Python paketlerini kurmak için pip veya benzeri bir araç. Lütfen göz [atın](https://pip.pypa.io/en/stable/installing/).

## ⚙ Kurulum

 * Öncelikle bu repoyu indirin.
 * Daha sonra requirements.txt dosyasında ismi geçen paketleri kurmak için şu komutu kullanın.
 ```bash 
  python3 -m pip install -r requirements.txt
```

 :exclamation: ÖNEMLİ UYARI -- Her bir model ~450mb boyutundadır ve ilk çalıştırılma sırasında otomatik olarak indirilecektir. Bu yüzden ilk çalıştırma uzun sürebilir.

 * Kurulum videosu:

![animated](assets/kurulum.gif)

## :video_game: Web Arayüzünün Kullanımı

Web arayüzü son kullanıcının modelleri test edip kullanabilmesi için çok kolay bir ortam sağlar.

 * Arayüzü çalıştırmak için tek yapmanız gereken şu komutu çalıştırmaktır.
 ```bash 
  python3 dash_app.py
```
 * Daha sonra Q&A ve NER modellerini http://127.0.0.1:8050 adresine tarayıcınız ile giderek kullanabilirsiniz.
 * Kuzgunlar web arayüzü https://huggingface.co/models adresindeki diğer tüm modelleri denemenize izin vermektedir.

 * Kullanım videosu:

![animated](assets/web_arayuz.gif)

## :video_game: Web API Kullanımı

Web API büyük veriler ile hızlı çalışmanız gerektiği zamanlarda işe yaramaktadır.

 * Arayüzü çalıştırmak için tek yapmanız şu komutu çalıştırmaktır.
 ```bash 
  python3 api.py
```
 * Daha sonra hangi modeli kullanmak istiyorsanız o modelin URL'ine POST isteği atmalısınız.
 * REST isteği atmak için şayet curl kullanıyorsanız:
 
 NER Modeli için
  ```bash 
   curl http://127.0.0.1:5000/ner -H 'Content-Type: application/json' -d '{"context": "Samsun, büyükşehir statüsündeki otuz ilden biridir."}'
```

 Soru Cevap (Q&A) Modeli için
  ```bash 
   curl http://127.0.0.1:5000/qa -H 'Content-Type: application/json' -d '{"context": "Mehteran birliği 1365 yılında kuruldu.", "question": "Mehteran ne zaman kuruldu?"}'
```

 Duygu Analizi (Sentiment Analysis) Modeli için
  ```bash 
   curl http://127.0.0.1:5000/sentiment -H 'Content-Type: application/json' -d '{"context": "Bu ürün çok başarılı."}'
```

 Sınıflandırma (Classification) Modeli için
  ```bash 
   curl http://127.0.0.1:5000/classification -H 'Content-Type: application/json' -d '{"context": "Intel yeni bir işlemci tanıttı."}'
```

Yazmanız yeterli olacaktır.

 * Kullanım videosu:

![animated](assets/web_api.gif)
 
