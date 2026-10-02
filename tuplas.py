# Etapa 1: criar a tupla com os 3 dias favoritos
dias_favoritos = ("sexta-feira", "sábado", "domingo")
print("1) Tupla original:", dias_favoritos)
print("   Tipo:", type(dias_favoritos))
 
# Etapa 2: converter a tupla em lista
dias_lista = list(dias_favoritos)
print("\n2) Convertida para lista:", dias_lista)
print("   Tipo:", type(dias_lista))
 
# Etapa 3: adicionar um novo dia (listas são mutáveis)
dias_lista.append("quinta-feira")
print("\n3) Lista com novo dia:", dias_lista)
 
# Etapa 4: converter de volta para tupla
dias_favoritos = tuple(dias_lista)
print("\n4) Convertida de volta para tupla:", dias_favoritos)
print("   Tipo:", type(dias_favoritos))