from core.configs import settings
from core.database import engine


async def create_tables() -> None:
    import models.__all_models
    print("Iniciando processo de criação das tabelas...")
    print(f"URL do banco de dados: {settings.DB_URL}")
    
    try:
        print("Tentando conectar ao banco de dados...")
        async with engine.begin() as conn:
            print("Conexão estabelecida com sucesso!")
            
            # Verificar se o modelo foi registrado
            print(f"Tabelas no metadata: {list(settings.DBBaseModel.metadata.tables.keys())}")
            
            print("Executando DROP de todas as tabelas...")
            await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
            print("DROP executado com sucesso!")
            
            print("Executando CREATE de todas as tabelas...")
            await conn.run_sync(settings.DBBaseModel.metadata.create_all)
            print("CREATE executado com sucesso!")
            
    except Exception as e:
        print(f"ERRO durante a criação das tabelas: {e}")
        print(f"Tipo do erro: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        raise
    
    print("Processo de criação das tabelas finalizado!")

 
  