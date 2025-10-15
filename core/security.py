from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_senha(senha: str, senha_hash: str) -> bool:
    """
    Função para verificar se a senha está correta, comparando a senha
    em texto puro, informada pelo usuário, e o hash da senha que estará
    salvo no banco de dados durante a criação da conta
    """
    return CRIPTO.verify(senha, senha_hash)

def gerar_hash_senha(senha: str) -> str:
    """
    Função para gerar o hash da senha, que será salvo no banco de dados
    durante a criação da conta
    """
    return CRIPTO.hash(senha)