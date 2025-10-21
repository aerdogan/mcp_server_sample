# client.py
import asyncio
from fastmcp import Client

async def main():
    client = Client("http://localhost:8000/mcp")  # URL doğrudan string olmalı
    async with client:
        await client.ping()
        tools = await client.list_tools()
        print("Mevcut MCP araçları:", [t.name for t in tools])

        # Yeni sınıf oluştur
        res = await client.call_tool("create_classroom", {"name": "10-A"})
        print("Yeni sınıf:", res)

        # Öğrenci oluştur
        res = await client.call_tool("create_student", {"name": "Ahmet", "age": 16, "classroom_id": 1})
        print("Yeni öğrenci:", res)

        # Öğrencileri listele
        res = await client.call_tool("list_students", {})
        print("Tüm öğrenciler:", res)

if __name__ == "__main__":
    asyncio.run(main())
