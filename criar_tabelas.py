from core.configs import settings
from core.database import engine

async def create_tables()-> Nome:
    import model.__all_models
    print('criando as tbls no banco de dados....')
    
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('tabelas cirado com sucesso')  


if __name__== '__main__':
    import asyncio
    asyncio.run(create_tables)      