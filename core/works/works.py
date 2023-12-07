
import datetime
from decimal import Decimal
import json
from model.pagamento import PagamentodoModel
from core.configs import Settings

def inc_pagamento(id_pedido, data_pagamento, total_pago, status, session) -> bool:
    novo_pagamento = PagamentodoModel(id_pedido=id_pedido, data_pagamento=data_pagamento, total_pago=total_pago, status=status)
    session.add(novo_pagamento)
    session.commit()
    return True

def ler_fila() -> dict:
    settings_instance = Settings()
    msg_fila = settings_instance.consume_message_from_queue()
    return msg_fila if msg_fila is not None else {}


def garavar_pagamento_da_fila(session):
    ler_fila_pg = ler_fila()
    pagamento = json.loads(ler_fila_pg)
    
    id_pedido = int(pagamento["id_pedido"])
    data_pagamento = datetime.fromisoformat(pagamento["data_pagamento"])
    total_pago = Decimal(str(pagamento["total_pago"]))  # Convertendo para Decimal
    status = str(pagamento["status"])
    
    inc_pagamento(id_pedido=id_pedido, data_pagamento=data_pagamento, total_pago=total_pago, status=status, session=session)
