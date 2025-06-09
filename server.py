import asyncio
import websockets
import subprocess
from datetime import datetime
import json
import os

# Ayarları config.json'dan oku
with open("config.json", encoding="utf-8") as f:
    config = json.load(f)
SIFRE = config.get("sifre")
HOST = config.get("host")
PORT = config.get("port")

# İzinli komutları dosyadan oku
if os.path.exists("izinli_komutlar.txt"):
    with open("izinli_komutlar.txt", encoding="utf-8") as f:
        izinli_komutlar = [line.strip() for line in f if line.strip()]

async def baglantiyi_yonet(websocket, path="/"):
    ip = websocket.remote_address[0] if websocket.remote_address else "Bilinmiyor"
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{zaman}] Bağlantı: {ip}\n")
    await websocket.send("🔐 Lütfen şifre girin:")
    girilen = await websocket.recv()

    if girilen != SIFRE:
        await websocket.send("❌ Hatalı şifre. Bağlantı kapatılıyor.")
        await websocket.close()
        return

    await websocket.send("✅ Giriş başarılı. Komut girebilirsiniz.")

    while True:
        try:
            mesaj = await websocket.recv()
            komut = mesaj.strip().split()[0]

            # Güvenlik kontrolü
            if komut not in izinli_komutlar:
                await websocket.send(f"⚠️ Bu komuta izin verilmiyor: {komut}")
                continue

            try:
                sonuc = subprocess.getoutput(mesaj)
            except Exception as e:
                sonuc = f"❌ Komut çalıştırılırken hata oluştu: {e}"

            await websocket.send(sonuc)

            # Komut logu
            with open("log.txt", "a", encoding="utf-8") as f:
                zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{zaman}] {ip}\nKOMUT: {mesaj}\nCEVAP:\n{sonuc}\n\n")

        except websockets.exceptions.ConnectionClosed:
            print(f"❗ İstemci bağlantıyı kapattı. ({ip})")
            break

async def baslat():
    print(f"🌐 WebSocket sunucusu başlatılıyor... ({HOST}:{PORT})")
    # Eğer HTTPS/WSS kullanmak isterseniz sertifika dosyalarını ekleyin:
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # ssl_context.load_cert_chain(certfile="sertifika.pem", keyfile="anahtar.key")
    # async with websockets.serve(baglantiyi_yonet, host=HOST, port=PORT, ssl=ssl_context):
    async with websockets.serve(baglantiyi_yonet, host=HOST, port=PORT):
        await asyncio.Future()

asyncio.run(baslat())