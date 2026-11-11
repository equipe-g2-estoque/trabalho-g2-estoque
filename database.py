import sqlite3

def criar_banco():
    # Conecta ao banco de dados (cria o arquivo se não existir)
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    # Tabela 1: produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT,
            quantidade_estoque REAL DEFAULT 0.0,
            unidade_medida TEXT NOT NULL
        )
    ''')

    # Tabela 2: movimentacoes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            tipo TEXT NOT NULL CHECK(tipo IN ('ENTRADA', 'SAIDA')),
            quantidade REAL NOT NULL,
            data_movimentacao DATETIME DEFAULT CURRENT_TIMESTAMP,
            observacao TEXT,
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados 'estoque.db' e tabelas criados com sucesso!")

if __name__ == "__main__":
    criar_banco()