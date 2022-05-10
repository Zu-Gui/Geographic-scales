e = int(input("Digite a escala do mapa 1: "))
c = int(input("Digite quantos cm tem no mapa: "))

a = e / 100 
b = e * c
cc = b / 1000

print("A distancia em km é {} km".format(cc))


#Escala grande 1:25.000
#Escala média 1:25.000 até 1:250.000
#Escala pequena 1:250.000 e maiores

#cm para km corta 5 zeros ou dividir por 100
#cm para m corta 2 zeros ou dividir por 100
#mm para cm adivanta uma virgula ou dividi por 10

#D = distancia real - queremos descobrir
#d = distancia do mapa - cm
#E = escala - escala do (e)

#Atualização futura / solução a entrada de dados será 1:xxxx pórem vai ter uma função excluido esse 1:
