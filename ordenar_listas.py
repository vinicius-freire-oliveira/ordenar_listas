# Define uma lista de dicionários, onde cada dicionário representa um produto com nome e valor
lista_produtos = [
    {'nome': 'chocolate', 'valor': 3.45},
    {'nome': 'biscoito', 'valor': 2.49},
    {'nome': 'cafe', 'valor': 3.45},
    {'nome': 'suco', 'valor': 4.3},
    {'nome': 'feijao', 'valor': 10.0},
    {'nome': 'arroz', 'valor': 8.5}
]

# Define a classe Produto
class Produto(object): 
    # Método construtor da classe, inicializa os atributos nome e valor
    def __init__(self, nome, valor): 
        self.__nome = nome 
        self.__valor = valor 

    # Método especial que define a representação do objeto como string
    def __repr__(self): 
        return "nome:%s valor:%s" % (self.__nome, self.__valor)

    # Método getter para o atributo nome
    def get_nome(self): 
        return self.__nome

    # Método getter para o atributo valor
    def get_valor(self): 
        return self.__valor

# Cria uma lista de objetos Produto a partir da lista de dicionários
produtos = [Produto(p['nome'], p['valor']) for p in lista_produtos]

# Imprime a lista de objetos Produto
print(produtos)
# Saída esperada: [nome:chocolate valor:3.45, nome:biscoito valor:2.49, nome:cafe valor:3.45, ...]

# Ordena a lista de produtos pelo valor
produtos_ordenados = sorted(produtos, key=lambda p: p.get_valor())
# Imprime a lista de produtos ordenada pelo valor
print(produtos_ordenados)
# Saída esperada: [nome:biscoito valor:2.49, nome:chocolate valor:3.45, nome:cafe valor:3.45, ...]

# Ordena a lista de produtos pelo nome
produtos_ordenados = sorted(produtos, key=lambda p: p.get_nome())
# Imprime a lista de produtos ordenada pelo nome
print(produtos_ordenados)
# Saída esperada: [nome:arroz valor:8.5, nome:biscoito valor:2.49, nome:cafe valor:3.45, ...]

# Ordena a lista de produtos pelo valor em ordem decrescente
produtos_ordenados = sorted(produtos, key=lambda p: p.get_valor(), reverse=True)
# Imprime a lista de produtos ordenada pelo valor em ordem decrescente
print(produtos_ordenados)
# Saída esperada: [nome:feijao valor:10.0, nome:arroz valor:8.5, nome:suco valor:4.3, ...]

# Ordena a lista de produtos pelo nome em ordem decrescente
produtos_ordenados = sorted(produtos, key=lambda p: p.get_nome(), reverse=True)
# Imprime a lista de produtos ordenada pelo nome em ordem decrescente
print(produtos_ordenados)
# Saída esperada: [nome:suco valor:4.3, nome:feijao valor:10.0, nome:chocolate valor:3.45, ...]

