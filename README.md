# Raspberry Pi AI Kiti Projeleri

Bu depo, **Raspberry Pi AI Kiti** proje kitabındaki örnek kodları içermektedir. Projeler, Raspberry Pi kullanarak nesne tanıma, görüntü segmentasyonu, poz tespiti ve diğer yapay zeka tabanlı uygulamaları kapsamaktadır.

![Raspberry Pi AI Kit](https://www.raspberrypi.com/documentation/accessories/images/ai-kit.jpg?hash=b707e971611c4b204c24f05e938bcf7d)
## AI Kit Yazılım Kurulum Adımları
Raspbian işletim sisteminin en güncel versiyonunu kurmak için aşağıdaki komutu çalıştırın. Bu komut Raspbian yazılımını günceller.

```bash
sudo apt update && sudo apt full-upgrade
```
Raspberry Pi ‘mizde hangi aygıt yazılımının çalıştığını öğrenmek için aşağıdaki komut satırını çalıştırınız. 
```bash
sudo rpi-eeprom-update
```
Komutu çalıştırdığımızda, aşağıdaki gibi bir çıktı üretecektir. Eğer ki aşağıdaki çıktıda 6 aralık 2023 ve daha sonraki bir tarih görürseniz aşağıdaki adımları takip ediniz. 

## Proje Listesi

1. **Nesne Tanıma**: Önceden eğitilmiş bir modeli kullanarak görüntülerdeki nesneleri tanımlama.
   
   ![Nesne Tanıma Örneği](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/nesne-tanima.png?raw=true)

2. **Görüntü Segmentasyonu**: Bir görüntünün her pikselini belirli kategorilere ayırma.
   
   ![Görüntü Segmentasyonu](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/goruntu-bolumlendirme.png?raw=true)

3. **Poz Algılama**: Gerçek zamanlı olarak insan pozlarını ve işaretlerini algılama.
   
   ![Poz Algılama](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/poz-alg%C4%B1lama.png?raw=true)

4. **Özel Nesne Tanıma Projesi**: Nesne tanıma modülünün ek işlevler ve geliştirmeler içeren değiştirilmiş versiyonu.
![Nesne Tanıma](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/proje4-03.png?raw=true)
## Başlarken

Bu projeleri çalıştırmak için ihtiyacınız olanlar:

- Raspberry Pi 5 veya üstü
- Raspberry Pi AI Kiti
- Raspberry Pi'de kurulu Python 3.x
- TensorFlow, OpenCV ve NumPy gibi gerekli kütüphaneler

### Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/kullanıcıadınız/depo-adı.git
