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

![Çıktı01](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/aiKit-01.png?raw=true)

Aşağıdaki komutu çalıştırdığımızda Raspbian’ın konfigürasyon ayarları penceresine yönlendirileceksiniz. 
```bash
sudo raspi-config
```

![çıktı02](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/aiKit-02.png?raw=true)

Aşağıdaki adımları takip ederek aygıt yazılımını son sürüme güncelleyiniz. 

Advanced Options > Bootloader Version > …Latest Bu ayarlamaları yaptıktan sonra esc yada finish butonu ile çıkış yapabilirsiniz. 

Aygıt yazılımını son sürüme güncellemek için aşağıdaki komut satırını çalıştırın. 
```bash
sudo rpi-eeprom-update -a
```
Aşağıdaki komut ile Raspberry Pi ’yi yeniden başlatın. 
```bash
sudo reboot
```
Artık Raspbian yazılımlarını AI Kit’e uygun hale getirdik. Bundan sonra yazacağımız komutlar ile AI kit için gerekli olan yapay zeka yazılımlarını işletim sistemimizin içerisine çekeceğiz.  

## AI Kit’i kullanmak için gerekli olan yazılımları yüklememizi sağlayan komut satırını çalıştıralım. 
```bash
sudo apt install hailo-all
```
Aşağıdaki komut ile Raspberry Pi ’yi yeniden başlatın. 
```bash
sudo reboot
```
Bütün adımların doğru bir şekilde yapıldığından emin olmak için aşağıdaki komut satırını çalıştırınız.
```bash
hailortcli fw-control identify
```
Aşağıdaki gibi çıktı alıyorsanız yazılım adımlarını doğru bir şekilde tamamlamlamışsınız demektedir.

![çıktı03](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/aiKit-03.png?raw=true)

# AI Kit yazılım kurulumunu başarı ile tamamladık. Artık Demo yapay zeka modellerini çalıştırabiliriz.
Raspberry Pi AI Kit yapay zeka modellerinin bulunduğu GitHub reposunu klonlamak için aşağıdaki terminal komutunu çalıştırınız. 
```bash
git clone --depth 1 https://github.com/raspberrypi/rpicam-apps.git ~/rpicam-apps
```

## Proje Listesi

1. **Nesne Tanıma**: Önceden eğitilmiş bir modeli kullanarak görüntülerdeki nesneleri tanımlama.
   
   ![Nesne Tanıma Örneği](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/nesne-tanima.png?raw=true)
```bash
rpicam-hello -t 0 --post-process-file ~/rpicam-apps/assets/hailo_yolov6_inference.json --lores-width 640 --lores-height 640
```
Diğer modellere göz atmak için kitaba göz atabilirsiniz. 

2. **Görüntü Segmentasyonu**: Bir görüntünün her pikselini belirli kategorilere ayırma.
   
   ![Görüntü Segmentasyonu](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/goruntu-bolumlendirme.png?raw=true)
```bash
rpicam-hello -t 0 --post-process-file ~/rpicam-apps/assets/hailo_yolov5_segmentation.json --lores-width 640 --lores-height 640 --framerate 20
```
3. **Poz Algılama**: Gerçek zamanlı olarak insan pozlarını ve işaretlerini algılama.
   
   ![Poz Algılama](https://github.com/Robotistan/Raspberry-Pi-AI-Kit-Project-Book/blob/main/images/poz-alg%C4%B1lama.png?raw=true)
```bash
rpicam-hello -t 0 --post-process-file ~/rpicam-apps/assets/hailo_yolov8_pose.json --lores-width 640 --lores-height 640
```
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
