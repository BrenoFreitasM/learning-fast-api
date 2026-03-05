from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

app = FastAPI()

class Usuario(BaseModel):
    nome: str
    idade: int
    ativo: bool = True


@app.get("/saudar/{nome}")
async def saudar(nome: str):
    print(type(nome))
    return { "mensagem": f"Olá, {nome}" }


@app.post("/usuarios")
async def criar_usuario(usuario: Usuario):
    return {
        "messagem": "Usuario criado",
        "dados": dict(usuario)
    }

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=3001,
        reload=True
    )