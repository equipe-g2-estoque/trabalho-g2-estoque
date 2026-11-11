import sqlite3

def conectar_banco():
    return sqlite3.connect('estoque.db')

# --- OPERAÇÕES DO SISTEMA (CRUD & MOVIMENTAÇÕES) ---

def cadastrar_produto():
    print("\n--- Cadastrar Novo Produto ---")
    nome = input("Nome do produto: ")
    categoria = input("Categoria (ex: Horta, Restaurante, Bebidas): ")
    unidade = input("Unidade de medida (ex: kg, un, L): ")

    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO produtos (nome, categoria, unidade_medida)
        VALUES (?, ?, ?)
    ''', (nome, categoria, unidade))
    conn.commit()
    conn.close()
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    print("\n--- Lista de Produtos em Estoque ---")
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, categoria, quantidade_estoque, unidade_medida FROM produtos')
    produtos = cursor.fetchall()
    conn.close()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'ID':<4} | {'Nome':<20} | {'Categoria':<15} | {'Estoque':<10} | {'Unidade'}")
    print("-" * 65)
    for p in produtos:
        print(f"{p[0]:<4} | {p[1]:<20} | {p[2]:<15} | {p[3]:<10.2f} | {p[4]}")

def registrar_movimentacao():
    print("\n--- Registrar Entrada/Saída de Estoque ---")
    listar_produtos()
    try:
        produto_id = int(input("\nDigite o ID do produto: "))
        tipo = input("Tipo de movimentação (ENTRADA / SAIDA): ").strip().upper()
        
        if tipo not in ['ENTRADA', 'SAIDA']:
            print("Tipo inválido! Use apenas ENTRADA ou SAIDA.")
            return

        quantidade = float(input("Quantidade: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero!")
            return

        observacao = input("Observação (opcional): ")

        conn = conectar_banco()
        cursor = conn.cursor()

        # Verifica saldo atual
        cursor.execute('SELECT quantidade_estoque, nome FROM produtos WHERE id = ?', (produto_id,))
        produto = cursor.fetchone()

        if not produto:
            print("Produto não encontrado!")
            conn.close()
            return

        saldo_atual, nome_prod = produto

        # Validação de saída
        if tipo == 'SAIDA' and saldo_atual < quantidade:
            print(f"Erro: Saldo insuficiente em estoque! Saldo atual: {saldo_atual}")
            conn.close()
            return

        # Atualiza o estoque
        novo_saldo = saldo_atual + quantidade if tipo == 'ENTRADA' else saldo_atual - quantidade
        cursor.execute('UPDATE produtos SET quantidade_estoque = ? WHERE id = ?', (novo_saldo, produto_id))

        # Registra no histórico
        cursor.execute('''
            INSERT INTO movimentacoes (produto_id, tipo, quantidade, observacao)
            VALUES (?, ?, ?, ?)
        ''', (produto_id, tipo, quantidade, observacao))

        conn.commit()
        conn.close()
        print(f"Movimentação de {tipo} para '{nome_prod}' registrada com sucesso! Novo saldo: {novo_saldo}")

    except ValueError:
        print("Entrada inválida! Digite números válidos para ID e Quantidade.")

# --- MENU PRINCIPAL ---

def menu():
    while True:
        print("\n==========================================")
        print("   SISTEMA DE GESTÃO DE ESTOQUE - AMF    ")
        print("==========================================")
        print("1. Cadastrar Novo Produto")
        print("2. Listar Produtos")
        print("3. Registrar Entrada/Saída")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            registrar_movimentacao()
        elif opcao == '4':
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()