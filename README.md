# Samarqand bo‘limi hisobot web-dasturi

## Imkoniyatlar
- Login/parol orqali kirish; parollar xavfsiz hash ko‘rinishida saqlanadi.
- Administrator bo‘lim va foydalanuvchilarni qo‘shadi.
- Oylik ma’lumotlar: tushum, qiyoslov, reja va amaldagi xulosa.
- 2025 va 2026-yil ko‘rsatkichlari hamda foizlar.
- PDF va PowerPoint eksporti.
- Standart holatda SQLite ma’lumotlar bazasi; hostingda PostgreSQL `DATABASE_URL` orqali sozlanishi mumkin.

## Mahalliy kompyuterda ishga tushirish
1. Python 3.11 yoki undan yangi versiyani o‘rnating.
2. Terminalda loyiha papkasiga kiring.
3. Virtual muhit yarating: `python -m venv .venv`
4. Faollashtiring (Windows): `.venv\\Scripts\\activate` (macOS/Linux: `source .venv/bin/activate`).
5. Kutubxonalarni o‘rnating: `pip install -r requirements.txt`
6. `.env.example` dagi qiymatlarni muhit o‘zgaruvchilari sifatida kiriting. `ADMIN_USERNAME` va `ADMIN_PASSWORD` ni albatta o‘zingizga moslab belgilang.
7. Ishga tushiring: `python app.py`
8. Brauzerda `http://127.0.0.1:5000` manzilini oching.

## Eslatma
Bu manba kodi loyihasi; u hali internetga joylashtirilmagan. Ommaviy internetga chiqarishdan oldin kuchli `SECRET_KEY`, kuchli administrator paroli, HTTPS va doimiy ma’lumotlar bazasi sozlanishi kerak. `ADMIN_PASSWORD` ni kod ichiga yozmang.
