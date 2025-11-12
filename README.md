# School MCP Api+ SQLite + FastMCP

Ayrıca, **FastMCP** ile MCP (Model Context Protocol) uyumlu bir sunucuya dönüştürülmüştür.
Projede **Sınıf (Classroom)** ve **Öğrenci (Student)** modelleri vardır ve hem CRUD hem de sınıf-öğrenci ilişkisi yönetilebilir.

## 📦 Özellikler

- **SQLite** veritabanı (otomatik oluşturulur)
- **SQLAlchemy ORM** kullanımı
- **CRUD** işlemleri: Sınıf ve Öğrenci
- **Sınıf ile öğrencileri birlikte yönetme** endpoint’leri

## ⚙️ Kurulum

1. Projeyi klonlayın veya indirin
2. Virtual environment oluşturun (opsiyonel ama önerilir):

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# veya
source .venv/bin/activate  # Linux/Mac
```

3. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt

```

🚀 Sunucuyu Çalıştırma

Server’ı başlatmak için:

```bash
python main.py

```

# Postman ile test Görüntüsü
<img src="server.png" />

🚀 Test Çalıştırma

```bash
python test.py

```