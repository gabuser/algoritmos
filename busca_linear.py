#precisa conter uma lista de nomes
#precisamos passar essa lista de nomes e organiza-la em uma maneira ordenada
#precisamos realizar uma busca de nomes e retornar o nome

#criaremos uma classe chamada que irá criar e organizar os dados em uma estruturas de dados
#usando o init para inicializar o estado inicial do objeto
#vamos criar uma objeto que irá realizar a busca, ele irá herdar esses valores do objeto

class lista:
    
    def __init__(self): 

        with open('nomes.txt','r') as self.nome:
            self.nomes=[n.strip() for n in self.nome]
        print(self.nomes)

class pesq(lista):

    def busca(self):
        self.valor=input('insira o nome a ser encontrado:')
        lista.__init__(self)

        for self.c in self.nomes:
            if self.valor == self.c:
                return 'valor encontrado'
            
        return 'valor não encontrado'
sistema=pesq()
print(sistema.busca())

#class controle_acesso(pesq, lista):
#
#    def acessos(self):
#        lista.__init__(self)
#        pesq.busca(self)
#
#        if self.valor == self.c:
#            print( 'acesso liberado')
#
#sistema=controle_acesso()
#
#print(sistema.acessos())