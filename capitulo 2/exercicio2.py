precoCapaLivro = 24.95
Desconto = precoCapaLivro - (precoCapaLivro * 0.40)
custoFretePrimeiroExemplar = Desconto + 3.00
custoFreteRestanteExemplares = Desconto + 0.75
custoTotalAtacado = custoFretePrimeiroExemplar + (custoFreteRestanteExemplares * 59.00)

print("O preco total do atacado para 60 exemplares é de:",custoTotalAtacado)