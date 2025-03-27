listas = [1,2,3,4,5,6,7,8,9]

def sear(value:int) -> str:
    baixo= 0 # menor elemento do array
    alto = len(listas) -1 #maior elemento do array

    while baixo <= alto: # inicia a busca
        meio = (baixo + alto) // 2 # inicia a busca pela metade da lista
        chute = listas[meio] # chuta o valor da metade da lista

        if chute == value: # verifica se o chute acertou
            return "valor encontrado"
        
        if chute < value:  # verifica se o chute foi muito baixo
            baixo = meio+1  # se for, ele continua a busca pela metade maior, nesse caso do 5 pra cima
        
        else: 
            chute > value #se o valor se o chute foi muito alto
            alto = meio-1 # se for, ele continua a busca me matade menor, nesse caso 4.
    return "valor não encontrado" # se caso o valor não for encontrado, ele retorna um mesg

print(sear(6))


"""
o algoritmo funciona como um "chute inteligente", ao invés de percorrer a lista uma por uma e verificar 
se o valor corresponde ao que está dentro da lista, divide a lista pela metade e compara se o valor que 
estamos procurando está na metade da lista, se estiver, ele elimina grande parte do processo de busca e acha o valor 
em uma único processo.

se o valor que estivermos procurando for menor que o chute, então ele elimina qualquer número maior que a metade, 
se a metade é 5, todos os números acima de 5 serão eliminados

como ele faz isso? 

por exemplo, se o valor que estamos procurando na lista é 2 ele faz o seguinte, ele pega o total de números que esta na lista
nesse caso são 9 elementos e inicia a busca pela metade, ele vai dividir 9 elementos por 2 ficando 4,5, porém 
vamos arredondar esse número para 4 que representa o índice 4 elemento 5, então a metade é 5. Ele verifica se o valor é 
igual a 5, porém como estamos procurando por 2, então essa condição é falsa, logo como o número é menor que 5, o programa
entende que chutamos muito alto, e qualquer número acima de 5 é descartada, eliminando metade do processo de bsuca. 

agora o programa precisa encontrar a nova metade, porque esse algoritmo busca de matade em matade, ele vai subtrair 
o índice 4 por 1, isso para eliminar os número do 5 para frente
ficando 3, ele verifica se o número indice 3 é igual ao número que procuramos, como não é ele repete o processo de
dividir o número subtraído(índice) nesse caso 3 por 2 que dá justamente índice 1, e o número 2 é 
é representado pelo índice 1 

levando apenas 2 comparações para serem concluidas.

"""

