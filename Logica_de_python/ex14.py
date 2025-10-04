'''O preço do "Iphone" no dicionário precos_produtos foi atualizado para 2500. Altere o valor da chave "Iphone" para este novo preço e imprima apenas o novo preço do "Iphone".

Saída Esperada: 2500'''


precos_produtos=  {
    "Ipad": 1000,
    "Iphone": 2000,
    "Notebook": 5000,
    }



novo_preço = precos_produtos["Iphone"] = 2500

print(novo_preço)