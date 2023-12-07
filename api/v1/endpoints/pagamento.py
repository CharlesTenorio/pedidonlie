from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_session
from schemas.pagamento_schema import PagamentoSchema
from model.pagamento import PagamentodoModel
from core.configs import settings

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PagamentoSchema)
async def processar_pagamento(db: AsyncSession = Depends(get_session)):
    try:
        # Consumir mensagem da fila
        mensagem_fila = settings.consume_message_from_queue()
        if mensagem_fila:
            # Parse da mensagem para PagamentoSchema
            pagamento_dados = PagamentoSchema(**mensagem_fila)
            
            # Criação do objeto PagamentodoModel
            novo_pagamento = PagamentodoModel(
                id_pedido=pagamento_dados.id_pedido,
                data_pagamento=pagamento_dados.data_pagamento,
                total_pago=pagamento_dados.total_pago,
                status='pagamento realizado com sucesso'
            )

            # Salvando no banco de dados
            db.add(novo_pagamento)
            await db.commit()
            await db.refresh(novo_pagamento)

            return novo_pagamento

        else:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Nenhuma mensagem na fila")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))