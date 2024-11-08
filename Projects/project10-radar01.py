import socket

# Sunucu ayarları
host = ''  # Raspberry Pi'nin IP'si, boş bırakılırsa tüm ağ arayüzlerinden bağlantılara izin verir
port = 12345  # Bağlantıyı dinleyeceğiniz port

# Soket oluştur ve bağlantıları dinle
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))  # IP ve port numarasına bağla
    s.listen(1)  # Maksimum 1 bağlantıyı dinle
    print(f"Server listening on port {port}...")

    conn, addr = s.accept()  # Bağlantı kabul et
    with conn:
        print(f"Connection accepted from {addr}")
        while True:
            data = conn.recv(1024)  # 1024 byte'a kadar veri al
            if not data:
                break  # Eğer veri yoksa döngüden çık
            print(f"Received value: {data.decode()}")  # Alınan veriyi yazdır