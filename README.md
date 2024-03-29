# 1. S.O.L.I.D.

## 1.1 SRP - The Single Responsability Principle

Conway's law - Qualquer organização que projeta um sistema (definido de forma ampla) produzirá um projeto cuja estrutura é uma cópia da estrutura de comunicação da organização.

Quando fizermos uma feature deve se ater aos processo que a própria organização utiliza

Um módulo deve ser responsável por um e apenas um ator

Um módulo é um conjunto coeso de funções e estruturas de dados

## 1.2 OCP - The Open-Closed Principle

Para sistemas de software serem fáceis de mudar, eles devem ser projetados para permitir o comportamento desses sistemas a serem alterados pela adição de novo código, em vez de alterar os códigos existentes

O módulo será considerado fechado se estiver disponível para uso por outros módulos

modulo aberto, esta disponível para expansao

Conceito de aberto e fechado esta relacionado se a classe esta preparada para receber um tipo de dado que se voce colocar outro tipo, você não tem que incluir no código pois o sistema prevê tipos infinitos

Entradas diferentes, geram ações diferentes

fragilidade, o elemento deve ter o método da classe executora, por isso se usa herança e interface

## 1.3 LSP - Liskov Substitution Principle

Para construir um sistema de software a partir de partes intercambiáveis, essas partes devem aderir a um contrato que permite que essas partes sejam substituídas umas pelas outras.

É contra o principio de polimorfismo

Herança deve ser uma complementação

## 1.4 ISP - Interface Segregation Principle

Evitar depender de coisas que não utilizamos

heranca no qual os filhos estao com metodos alem daqueles que ele precisariam da classe pai

Segregação das interfaces, tornando elas mais específicas

## 1.5 DIP - Dependency Inversion Principle

Interfaces realizam a inversão de dependência

Politica é como os métodos das interfaces são entendidos


# 2. Interfaces

classe abstrata com metodos abstratos

sempre que tiver uma heranca (implementacao), temos que implementar o metodo abstrato