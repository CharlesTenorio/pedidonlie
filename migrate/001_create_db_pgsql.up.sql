-- Criação da tabela 'clientes'
CREATE TABLE public.clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE
);

-- Criação da tabela 'produtos'
CREATE TABLE public.produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE,
    valor DECIMAL(10, 2)
);

-- Criação da tabela 'pedidos'
CREATE TABLE public.pedidos (
    id serial4 NOT NULL,
    id_cliente int4 NULL,
    data_pedido timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    total numeric(10, 2) NULL,
    descricao varchar(100) NULL,
    statuspedido varchar(30) NULL,
    produtos jsonb NULL,  -- Adicionando um campo do tipo JSON
    CONSTRAINT pedidos_pkey PRIMARY KEY (id)
);
-- Criação da tabela 'detalhes_pedidos'
CREATE TABLE public.detalhes_pedidos (
    id SERIAL PRIMARY KEY,
    id_pedido INTEGER REFERENCES pedidos(id),
    id_produto INTEGER REFERENCES produtos(id),
    quantidade INTEGER,
    valor DECIMAL(10, 2),
    subtotal DECIMAL(10, 2),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id),
    FOREIGN KEY (id_produto) REFERENCES produtos(id)
);
