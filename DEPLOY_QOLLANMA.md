# Samarqand Hisobot — internetga joylashtirish uchun

## Eng sodda yo‘l
1. ZIP faylni oching.
2. Ichidagi `samarqand_hisobot_web_deploy` papkasidagi fayllarni GitHub repozitoriyiga yuklang.
3. Render kabi Python web-hosting xizmatida yangi Web Service yarating va GitHub repozitoriyingizni ulang.
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`
6. Environment Variables bo‘limida quyidagilarni kiriting:
   - `SECRET_KEY` — uzun, tasodifiy maxfiy qiymat
   - `ADMIN_USERNAME` — administrator uchun o‘zingiz tanlagan login
   - `ADMIN_PASSWORD` — kuchli, noyob parol
   - `DATABASE_URL` — doimiy PostgreSQL bazasi manzili
7. Deploy tugagach hosting bergan `https://....` manzilini oching. Alohida domen hozircha shart emas.

## Muhim xavfsizlik va ma’lumotlar
- `ADMIN_PASSWORD` yoki `SECRET_KEY` ni GitHub kodiga yozmang.
- Doimiy ma’lumotlar bazasi ulang; bepul hostingning vaqtinchalik diskiga muhim hisobotlarni ishonib topshirmang.
- Deploydan oldin login, hisobot saqlash, PDF va PPTX eksportini sinab ko‘ring.
- Bu ZIP hostingga tayyorlash uchun moslashtirilgan loyiha kodi; internetga o‘zi joylashtirilmagan.
