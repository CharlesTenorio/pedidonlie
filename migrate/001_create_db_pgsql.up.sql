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
    id SERIAL PRIMARY KEY,
    id_cliente INTEGER REFERENCES clientes(id),
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2),
    descricao VARCHAR(100)
    status_pedido VARCHAR(30) 
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
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
