from fastmcp import FastMCP
from data.db import engine, Base
from tools import register_tools

Base.metadata.create_all(bind=engine)

mcp = FastMCP(name="SchoolAPI-MCP", instructions="Okul yönetimi MCP sunucusu")

register_tools(mcp)

if __name__ == "__main__":
    try:
        mcp.run(transport="http", host="localhost", port=8000, log_level="info")
    except KeyboardInterrupt:
        print("\nMCP sunucusu güvenli bir şekilde kapatıldı.")
