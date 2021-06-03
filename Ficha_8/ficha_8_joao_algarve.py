"""
Trabalho realizado por:
        João Algarve
        PDM-B
        1º ano
        nº 45304
"""
#--------------------------------1--------------------------------
ficheiro_1 = open("ficheiro_1.txt", "r")

var = ficheiro_1.read()

print(var)

vogais_count = {}

for vogais in "aeiou":
    count = var.lower().count(vogais)
    vogais_count[vogais] = count

print("Ocorrência da Vogal A/a: {0}\n"
      "Ocorrência da Vogal E/e: {1}\n"
      "Ocorrência da Vogal I/i: {2}\n"
      "Ocorrência da Vogal O/o: {3}\n"
      "Ocorrência da Vogal U/u: {4}\n".format(vogais_count["a"],
                                            vogais_count["e"],
                                            vogais_count["i"],
                                            vogais_count["o"],
                                            vogais_count["u"]))

ficheiro_1.close()
#--------------------------------1--------------------------------


#--------------------------------2--------------------------------

ficheiro_2 = open("ficheiro_2.txt", "r")

var_2 = ficheiro_2.readline()

ficheiro_2.close()

print("Frase antiga: ",var_2)

palavras = set()
resultado = ''
for palavra in var_2.split():
    if palavra not in palavras:
        resultado = resultado + palavra + ' '
        palavras.add(palavra)
print("Frase nova: ",resultado)

ficheiro_2 = open("ficheiro_2.txt", "w")

ficheiro_2.write(resultado)

#--------------------------------2--------------------------------