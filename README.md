# 📦 Sistema de Controle de Estoque — Horta & Restaurante (`trabalho-g2-estoque`)

Repositório oficial do trabalho de **Engenharia de Software** (Antonio Meneghetti Faculdade - AMF).  
**Equipe:** Sante Biondi, Arthur Radtke Machado e Gustavo Ellwanger.

---

## 🎯 1. O que foi solicitado pela Professora?

O objetivo do projeto é desenvolver um **MVP (Produto Mínimo Viável)** de um sistema funcional utilizando boas práticas de Engenharia de Software (documentação estruturada, controle de versão em equipe e arquitetura limpa).

**Requisitos principais:**
1. **Problema Real:** Resolver o controle de fluxo de insumos e transferências internas entre a **Horta** (produção agrícola) e a **Cozinha do Restaurante** (consumo).
2. **Documentação (Metodologia OpenSpec):** Especificar o sistema antes e durante o desenvolvimento (`proposal.md`, `design.md`, `tasks.md`).
3. **Persistência de Dados:** Armazenar produtos e histórico de movimentações de forma segura (sem perder os dados ao fechar o programa).
4. **Trabalho Colaborativo:** Uso de organização no GitHub (`equipe-g2-estoque`) com todos os integrantes participando como *Owners* e preparando a apresentação final.

---

## 🛠️ 2. O que foi feito passo a passo (Guia para a Equipe)

Para facilitar o entendimento de como o projeto foi construído e como explicá-lo na apresentação, dividimos o desenvolvimento em **5 etapas**:

### Passo 1: Configuração da Organização e Repositório
* Criamos a organização `equipe-g2-estoque` no GitHub.
* Configuramos as permissões de **Owner** para Sante, Arthur e Gustavo para que todos tenham acesso total ao código e à documentação.

### Passo 2: Documentação de Engenharia de Software (OpenSpec)
Antes de focar apenas no código, estruturamos a documentação do projeto para definir o escopo:
* **`proposal.md`**: Define o problema (falta de rastreabilidade entre o que sai da horta e entra na cozinha) e a solução proposta.
* **`design.md`**: Define a arquitetura do sistema (Python + Banco de Dados Relacional SQLite) e o modelo das tabelas.
* **`tasks.md`**: Lista de verificação (*checklist*) de todas as entregas até o dia da apresentação.

### Passo 3: Criação do Banco de Dados (`estoque.db`)
Utilizamos o **SQLite** (nativo do Python, não precisa instalar servidores externos) com duas tabelas conectadas por chave estrangeira (*Foreign Key*):
1. **`produtos`**: Guarda o cadastro base (`id`, `nome`, `categoria` [Horta ou Restaurante], `quantidade` atual e `unidade` [kg, un, l]).
2. **`movimentacoes`**: Guarda o histórico de tudo o que acontece (`id`, `produto_id`, `tipo` [ENTRADA ou SAIDA], `quantidade` e `data_hora`).

### Passo 4: Desenvolvimento da Lógica e Regras de Negócio (`database.py` / `main.py`)
Implementamos as 4 operações fundamentais (**CRUD**) e as travas de segurança:
* **Cadastrar Produto:** Insere um novo item com saldo inicial zero.
* **Listar Produtos:** Consulta o banco e exibe o saldo atualizado em tempo real.
* **Registrar Movimentação (`ENTRADA` / `SAIDA`):** 
  * *Regra de Negócio:* O sistema bloqueia automaticamente qualquer **SAÍDA** se a quantidade solicitada for maior do que o saldo disponível em estoque (evitando estoque negativo).
  * Toda movimentação atualiza o saldo na tabela `produtos` e grava um registro com data e hora na tabela `movimentacoes`.
* **Remover Produto:** Permite excluir itens cadastrados incorretamente.

### Passo 5: Interface de Terminal (CLI)
Criamos um menu interativo via linha de comando (`while True`) com tratamento de erros (`try/except`) para que o usuário possa operar o sistema facilmente sem que o programa trave caso alguém digite uma letra no lugar de um número.

---

## 💻 3. Como rodar o projeto no seu computador

1. **Clone o repositório:**
   ```bash
  git clone https://github.com/equipe-g2-estoque/trabalho-g2-estoque.git
   cd trabalho-g2-estoque