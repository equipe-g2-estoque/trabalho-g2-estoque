## 1. Contexto e Problema
O restaurante utiliza produtos e insumos agrícolas colhidos diretamente da horta própria ou adquiridos de fornecedores externos. Atualmente, a falta de um rastreamento centralizado dificulta o controle de saldo, gerando risco de desperdício de alimentos ou desabastecimento da cozinha nos momentos de pico.

## 2. Descrição da Solução
Desenvolvimento de uma aplicação em Python integrada a um banco de dados relacional SQLite (`estoque.db`). O sistema funcionará via CLI (interface de linha de comando) e permitirá registrar novos produtos e gerenciar movimentações contínuas de entrada (colheita/compra) e saída (consumo na cozinha).

## 3. Escopo das Alterações
- Criação das tabelas relacionais `produtos` e `movimentacoes`.
- Implementação das 4 operações fundamentais do CRUD (Create, Read, Update, Delete).
- Validação automática de saldo impredizível (bloqueio de saídas superiores ao estoque disponível).

## 4. Impacto Esperado
- Visibilidade em tempo real das giros de estoque da horta para a cozinha.
- Redução de perdas por insumos vencidos ou não registrados.
- Padronização do registro de entradas e saídas com carimbo de data/hora automatizado.