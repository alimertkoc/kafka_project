# OSS Proje Ödevi

Python dilini kullanarak Apache Kafka’ya bir JSON mesajı üreten ve bu mesajları tüketen (consumer) bir uygulama geliştirilmiştir.


## Dosya ve klasörler

 - Dockerfile-A
 - Dockerfile-B
 - docker-compose.yml
 - consumer.py
 - producer.py

## Kurulum
`docker compose up` komutu ile konteynırlar koşturulabilir. 

`curl http://127.0.0.1:5000/ -X POST -H "Content-Type: application/json" -d '{"isim":"soyisim"}'` gibi örnek bir POST metodu kullanımıyla test edilebilir.

