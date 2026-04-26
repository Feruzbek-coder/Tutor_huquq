"""
Loyihani internet orqali boshqalarga ko'rsatish uchun skript.
1. https://ngrok.com saytida bepul hisob oching
2. Dashboard > Authtoken sahifasida tokeningizni oling
3. Quyidagi TOKEN o'rniga o'z tokeningizni kiriting
4. python start_public.py buyrug'ini ishga tushiring
"""

import threading
import time
from pyngrok import ngrok, conf

# =====================================================
# NGROK TOKENINGIZNI SHU YERGA KIRITING:
NGROK_TOKEN = "3CrWK5XAm6rlYkb5HLeYy3gvlFI_ve53fQjev2bYshhcyUHE"
# =====================================================

def run_flask():
    from app import app
    app.run(host='127.0.0.1', port=5005, debug=False, use_reloader=False)

if __name__ == '__main__':
    if NGROK_TOKEN == "bu_yerga_tokeningizni_kiriting":
        print("=" * 60)
        print("XATO: Avval ngrok tokeningizni kiriting!")
        print("1. https://ngrok.com saytiga kiring")
        print("2. Bepul hisob yarating")
        print("3. Dashboard > Your Authtoken sahifasida tokenni oling")
        print("4. start_public.py faylida NGROK_TOKEN ga o'z tokeningizni kiriting")
        print("=" * 60)
        exit(1)

    # Token sozlash
    conf.get_default().auth_token = NGROK_TOKEN

    print("=" * 60)
    print("Flask server ishga tushirilmoqda...")

    # Flask ni alohida thread da ishlatish
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    time.sleep(2)  # Flask ishga tushishini kutish

    # Ngrok tunnelini ochish
    print("Ngrok tunneli ochilmoqda...")
    tunnel = ngrok.connect(5005, "http")
    public_url = tunnel.public_url

    print("=" * 60)
    print(f"\n🚀 MUVAFFAQIYAT! Loyihangiz internetda ochiq!")
    print(f"\n🔗 PUBLIC LINK: {public_url}")
    print(f"\nShu linkni do'stlaringizga yuboring!")
    print(f"\nDiqqat: Bu kompyuteringiz yoqiq va internet bilan")
    print(f"ulangan bo'lganda ishlaydi.")
    print(f"\nDasturni to'xtatish uchun Ctrl+C bosing.")
    print("=" * 60)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDastur to'xtatildi.")
        ngrok.disconnect(tunnel.public_url)
        ngrok.kill()
