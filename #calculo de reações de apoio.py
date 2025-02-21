
carga_1 = float(input("valor da força 1 : "))
distancia_da_carga1 = float(input("Digite a distancia da carga1 até Ra: "))
carga_2 = float(input("valor da força 2 : ")) 
distancia_da_carga2 = float(input("Digite a distancia da carga2 até Ra: "))
viga_Ra_or_Rb = float(input("Distancia da viga Rb a viga Ra: "))
Resultado = float(carga_1 * distancia_da_carga1 + carga_2 * distancia_da_carga2 / viga_Ra_or_Rb)
Rb= Resultado
print (f"Resultado: Rb={Resultado}")
print (Resultado)
Resultado_de_Ra = Rb - carga_1 - carga_2
Ra = Resultado_de_Ra  
print(f"Resultado de Ra : {Ra}")



