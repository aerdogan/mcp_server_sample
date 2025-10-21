# School API - FastAPI + SQLite + FastMCP

Bu proje, **FastAPI** ve **SQLite** kullanarak oluşturulmuş bir okul yönetimi API’sidir.  
Ayrıca, **FastMCP** ile MCP (Model Context Protocol) uyumlu bir sunucuya dönüştürülmüştür.

Projede **Sınıf (Classroom)** ve **Öğrenci (Student)** modelleri vardır ve hem CRUD hem de sınıf-öğrenci ilişkisi yönetilebilir.

---

## 📦 Özellikler

- **FastAPI** tabanlı REST API
- **SQLite** veritabanı (otomatik oluşturulur)
- **SQLAlchemy ORM** kullanımı
- **CRUD** işlemleri: Sınıf ve Öğrenci
- **Sınıf ile öğrencileri birlikte yönetme** endpoint’leri
- **MCP Server** olarak çalışabilir
- Swagger UI ve ReDoc dokümantasyonu destekler

---

## ⚙️ Kurulum

1. Projeyi klonlayın veya indirin
2. Virtual environment oluşturun (opsiyonel ama önerilir):

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# veya
source .venv/bin/activate  # Linux/Mac
```
