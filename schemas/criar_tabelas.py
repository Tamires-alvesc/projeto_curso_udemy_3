from core.configs import settings
from core.database import engine


async def create_tables() -> None:
    import models.__all_models
    print("Iniciando processo de criação das tabelas...")
        
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Processo de criação das tabelas finalizado!")

if __name__ == "__main__":
    import asyncio
    
    asyncio.run(create_tables())
 
  