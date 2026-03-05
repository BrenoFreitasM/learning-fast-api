from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    idade: int
    ativo: bool = True


try: 
    usuario = Usuario(nome="Rafa", idade=30)
    print(usuario.idade) 
    
except Exception as e:
    print("Erro  de validação")
    print(e)