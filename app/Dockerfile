# Base imaj olarak Python 3.9 kullanıyoruz
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Portu dışarı aç
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "app.py"]
