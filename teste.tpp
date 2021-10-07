inteiro: tamanho
tamanho: 10

inteiro: vetor[tamanho]

inteiro particiona(inteiro: vetor[], inteiro: inicio, inteiro:final)

    inteiro: esquerda
    inteiro: direita
    inteiro: pivo
    inteiro: auxiliar

    esquerda := inicio
    direita := final
    pivo := vetor[esquerda]

    repita

        se esquerda < direita então

            repita

                se v[esquerda] <= pivo então
                    
                    esquerda := esquerda + 1
                fim
            
            até vetor[esquerda] > pivo

            repita

                se v[direita] > pivo então
                    
                    direita := direita - 1
                fim

            até v[direita] < pivo

            se esquerda < direita então
                auxiliar := vetor[esquerda]
                v[esquerda] = v[direita]
                v[direita] = auxiliar                    
            fim
        fim
    
    até esquerda >= direita

    vetor[inicio] := v[direita]
    vetor[esquerda] := v[direita]
    vetor[direita] := auxiliar
    retorna(direita)

fim

quicksort(inteiro: vetor[], inteiro: inicio, inteiro:final)

    inteiro: pivo
    
    se final > inicio então
        pivo := particiona(vetor, inicio, final)
        quicksort(vetor, inicio, pivo -1)
        quicksort(vetor, pivo + 1, final)
    fim

    retorna(0)
fim

inteiro principal()
    quicksort(vetor, 0, tamanho-1)
    i := 0
    
    repita
        escreva(vetor[i])
        i := i + 1

    até i = tamanho
    retorno(0)
fim

{aosidjoasoaisjoaji}