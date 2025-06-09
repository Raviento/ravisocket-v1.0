import asyncio
import websockets
import subprocess
from datetime import datetime

# Şifre ve izinli komutlar
SIFRE = "raviento123" # istediğiniz şifreyi buraya yazabilirsiniz
izinli_komutlar = ["whoami", "ipconfig", "dir", "hostname", "echo"]

async def baglantiyi_yonet(websocket,  path="/"):
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

            sonuc = subprocess.getoutput(mesaj)
            await websocket.send(sonuc)

            # Log
            with open("log.txt", "a", encoding="utf-8") as f:
                zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{zaman}]\nKOMUT: {mesaj}\nCEVAP:\n{sonuc}\n\n")

        except websockets.exceptions.ConnectionClosed:
            print("❗ İstemci bağlantıyı kapattı.")
            break

# Host'u 0.0.0.0 yaparak diğer cihazlardan da erişilebilir hale getir
async def baslat():
    print("🌐 WebSocket sunucusu başlatılıyor...")
    async with websockets.serve(baglantiyi_yonet,host= "localhost",port= 8765):
        await asyncio.Future()

asyncio.run(baslat())
