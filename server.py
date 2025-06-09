import asyncio
import websockets
import subprocess

async def baglantiyi_yonet(websocket):
    print("İstemci bağlandı.")
    try:
        async for mesaj in websocket:
            print(f"Gelen komut: {mesaj}")

            # Komutu sistemde çalıştır
            try:
                sonuc = subprocess.check_output(mesaj, shell=True, stderr=subprocess.STDOUT, text=True)
            except subprocess.CalledProcessError as e:
                sonuc = f"HATA: {e.output}"

            # Sonucu istemciye gönder
            await websocket.send(sonuc)
    except websockets.exceptions.ConnectionClosed:
        print("İstemci bağlantıyı kapattı.")

async def baslat():
    print("WebSocket komut sunucusu başlatılıyor...")
    async with websockets.serve(baglantiyi_yonet, "localhost", 8765):
        await asyncio.Future()

asyncio.run(baslat())
