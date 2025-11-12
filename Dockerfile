# Python tabanlı bir imaj kullanıyoruz
FROM python:3.11-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Uygulama portunu expose et (örneğin 8000)
EXPOSE 8000

# Uygulamayı başlat
# Eğer `main.py` doğrudan MCP server başlatıyorsa:
CMD ["python", "main.py"]
