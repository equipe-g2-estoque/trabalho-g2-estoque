import sqlite3

def conectar():
    return sqlite3.connect('estoque.db')

def cadastrar_produto():
    print("\n--- CADASTRO DE NOVO PRODUTO ---")
    nome = input("Nome do produto: ").strip()
    categoria = input("Categoria (ex: Horta, Laticínios, Secos): ").strip()
    unidade = input("Unidade de medida (ex: kg, g, un, L): ").strip()
    
    if not nome or not unidade:
        print("Erro: Nome e Unidade de medida são obrigatórios!")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO produtos (nome, categoria, quantidade_estoque, unidade_medida)
        VALUES (?, ?, 0.0, ?)
    ''', (nome, categoria, unidade))
    conn.commit()
    conn.close()
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    print("\n--- SALDO ATUAL DO ESTOQUE ---")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, categoria, quantidade_estoque, unidade_medida FROM produtos')
    produtos = cursor.fetchall()
    conn.close()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'ID':<4} | {'Nome':<20} | {'Categoria':<15} | {'Estoque':<10} | {'Unidade':<8}")
    print("-" * 65)
    for p in produtos:
        print(f"{p[0]:<4} | {p[1]:<20} | {p[2]:<15} | {p[3]:<10.2f} | {p[4]:<8}")

def registrar_movimentacao():
    print("\n--- REGISTRAR MOVIMENTAÇÃO (ENTRADA / SAÍDA) ---")
    listar_produtos()
    
    try:
        produto_id = int(input("\nID do produto: "))
        tipo = input("Tipo de movimentação (E para Entrada / S para Saída): ").strip().upper()
        if tipo not in ['E', 'S']:
            print("Erro: Tipo inválido! Use 'E' para Entrada ou 'S' para Saída.")
            return

        quantidade = float(input("Quantidade: "))
        if quantidade <= 0:
            print("Erro: A quantidade deve ser maior que zero!")
            return

        observacao = input("Observação (ex: Colheita, Uso na Cozinha): ").strip()

        conn = conectar()
        cursor = conn.cursor()
        
        # Verifica saldo atual
        cursor.execute('SELECT quantidade_estoque, nome FROM produtos WHERE id = ?', (produto_id,))
        res = cursor.fetchone()
        
        if not res:
            print("Erro: Produto não encontrado!")
            conn.close()
            return

        saldo_atual, nome_produto = res
        tipo_db = 'ENTRADA' if tipo == 'E' else 'SAIDA'

        # Validação de estoque suficiente para saída
        if tipo_db == 'SAIDA' and quantidade > saldo_atual:
            print(f"Erro: Saldo insuficiente! Estoque atual de '{nome_produto}': {saldo_atual:.2f}")
            conn.close()
            return

        # Atualiza saldo no produto
        novo_saldo = saldo_atual + quantidade if tipo_db == 'ENTRADA' else saldo_atual - quantidade
        cursor.execute('UPDATE produtos SET quantidade_estoque = ? WHERE id = ?', (novo_saldo, produto_id))

        # Registra a movimentação no histórico
        cursor.execute('''
            INSERT INTO movimentacoes (produto_id, tipo, quantidade, observacao)
            VALUES (?, ?, ?, ?)
        ''', (produto_id, tipo_db, quantidade, observacao))

        conn.commit()
        conn.close()
        print(f"Movimentação de {tipo_db} registrada com sucesso! Novo saldo: {novo_saldo:.2f}")

    except ValueError:
        print("Erro: Digite valores numéricos válidos para ID e Quantidade.")

def deletar_produto():
    print("\n--- REMOVER PRODUTO ---")
    listar_produtos()
    try:
        produto_id = int(input("\nID do produto a ser removido: "))
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT nome FROM produtos WHERE id = ?', (produto_id,))
        res = cursor.fetchone()

        if not res:
            print("Erro: Produto não encontrado!")
            conn.close()
            return

        confirmar = input(f"Tem certeza que deseja deletar '{res[0]}'? (S/N): ").strip().upper()
        if confirmar == 'S':
            cursor.execute('DELETE FROM movimentacoes WHERE produto_id = ?', (produto_id,))
            cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
            conn.commit()
            print(f"Produto '{res[0]}' removido com sucesso!")
        else:
            print("Operação cancelada.")
        conn.close()
    except ValueError:
        print("Erro: Digite um ID numérico válido.")

def menu():
    while True:
        print("\n==========================================")
        print("  GESTÃO DE ESTOQUE (HORTA & RESTAURANTE) ")
        print("==========================================")
        print("1. Cadastrar Novo Produto")
        print("2. Listar Produtos e Saldo Atual")
        print("3. Registrar Entrada/Saída de Estoque")
        print("4. Remover Produto")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            registrar_movimentacao()
        elif opcao == '4':
            deletar_produto()
        elif opcao == '5':
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print("Opção inválida! Digite um número de 1 a 5.")

if __name__ == "__main__":
    menu()
