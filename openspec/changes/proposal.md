# Proposta de Mudança: Sistema de Gestão de Estoque (Horta & Restaurante)

## 1. Por que esta mudança é necessária?
É necessário criar um sistema simples e eficiente para controlar o fluxo de produtos e insumos agrícolas da horta e seu consumo no restaurante, evitando desperdícios e garantindo o rastreamento do estoque.

## 2. O que será alterado?
Será criado um sistema CRUD em Python com banco de dados SQLite contendo 2 tabelas relacionadas:
- `produtos`: cadastro dos itens e saldo atual.
- `movimentacoes`: histórico detalhado de entradas e saídas de produtos.

## 3. Qual o impacto esperado?
O sistema permitirá consultar saldos em tempo real, cadastrar novos produtos, editar registros e impedir a saída de itens sem saldo suficiente.