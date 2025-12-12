# High Availability & Load Balancing Simulation with Docker

## Projenin Amacı
Bu proje, kurumsal sistemlerdeki "Süreklilik" (High Availability) ve "Yük Dengeleme" (Load Balancing) prensiplerini simüle etmek amacıyla hazırlanmıştır. Monolitik bir yapı yerine, konteyner mimarisi kullanılarak yatayda ölçeklenebilir (horizontally scalable) bir yapı kurulmuştur.

## Kullanılan Teknolojiler
*   **Docker & Docker Compose**: Orkestrasyon ve izolasyon için.
*   **Nginx**: Reverse Proxy ve Load Balancer olarak.
*   **Python (Flask)**: Mikroservis simülasyonu için.

## Mimari Şema (Architecture)
Client Request -> Nginx (Load Balancer) -> [Container A] / [Container B] / [Container C]

## Temel Kazanımlar
1.  **Fault Tolerance (Hata Toleransı)**: Konteynerlerden biri çökse bile Nginx trafiği diğerlerine yönlendirerek hizmetin kesilmemesini sağlar.
2.  **Scalability (Ölçeklenebilirlik)**: `docker-compose up --scale app=10 -d` komutu ile saniyeler içinde sunucu sayısı 3'ten 10'a çıkarılabilir.
3.  **Resource Efficiency (Kaynak Verimliliği)**: Sanal makineler yerine hafif konteyner yapısı kullanılarak sistem kaynakları optimize edilmiştir.

## Nasıl Çalıştırılır?

Projeyi ayağa kaldırmak için terminalde şu komutu çalıştırın:

```bash
docker-compose up --build
```

### Test Etme
1.  Tarayıcınızda `http://localhost` adresine gidin.
2.  Sayfayı yenileyin. Her yenilemede "Ben [ID] isimli sunucuyum" kısmındaki ID'nin değiştiğini göreceksiniz. Bu, yükün farklı sunuculara dağıtıldığını gösterir.

### Simülasyon Senaryoları
*   **Yedeklilik Testi**: Farklı bir terminalde `docker ps` ile çalışan konteynerleri listeleyin. `docker kill [CONTAINER_ID]` komutuyla birini öldürün. Sayfayı yenilediğinizde sitenin hala çalıştığını göreceksiniz.
*   **Scale Testi**: `docker-compose up --scale app=5 -d` komutuyla sunucu sayısını 5'e çıkarın.
