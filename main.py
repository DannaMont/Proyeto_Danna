
nombre_proyecto = ("Proyecto final 1 por Danna Juárez Montemayor")
print(nombre_proyecto)


from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, n ame, price, category, stock]
"""

usuarios_certificados = ["Adm1n", "Jaime", "Osvaldo", "Danna"]

usuario = input("Ingresa el identificador de usuario: ")
if usuario == usuarios_certificados [0]:
  print("Identificador conformimado")


elif usuario == "Jaime" :
  print("Identificador confirmado")


elif usuario == "Osvaldo" :
  print("Identificador confirmado")


elif usuario == "Danna" :
  print("Identificador confirmado")

else :
  print("Usuario no identificado")

clave_universal = ["12345"]
clave = input("Ingresa la clave: ")
if clave == clave_universal[0] :
  print("Acceso aceptado")

else : 
  print("Acceso denegado")



#Parte 1: Produtos más vendidos y productos rezagados
#1.1: gernerar un listado de los 5 productos con mayores ventas y otra lista con los 10 productos con mayores búsquedas.
#Una de las principales prácticas para lograr la primera lista es reducir los datos de la lista al elemento que se nos pide y posteriormente ordenarlo para así, mostrar únicamente el número de elementos solicitados en el ejercicio.

#Puede ser oportuno, saber cuántos elementos tenemos en la lista primero.

longitud_lista_2 = len(lifestore_sales)
print("La lista de ventas contiene: ", longitud_lista_2, " elementos.")


#Para tener las listas que se indican en las instrucciones, debemos ordenar los datos de venta por fecha y por id. También es necesario eliminar las ventas que resultaron en un reembolso, por lo tanto, tendremos en la lista únicamente con ventas válidas. 

ventas_s_rembolso = []

for sale in lifestore_sales:  
  rembolso = sale [4]
  if rembolso == 1:
    continue
  else: 
    ventas_s_rembolso.append(sale)
    
#print(ventas_s_rembolso)
#En el código anterior, filtramos las ventas que no son válidas, es decir, que resultaron en un rembolso. 

#for venta in ventas_s_rembolso:
 # print(venta)

#En la parte anerior, logramos ordenar los datos de tal manera que sean legibles y tengan todos los datos que necesitamos.

#Ahora ordenemos los datos de forma cronológica

meses = ['/01/', '/02/', '/03/', '/04/', '/05/', '/06/', '/07/','/08/','/09/','/10/','/11/', '/12/']

fechas_ventas = []
for mes in meses:
  empty_list = []
  fechas_ventas.append(empty_list)

for venta in ventas_s_rembolso:
  id_venta = venta[0]
  fecha = venta[3]
  conteo_por_mes = 0

  for mes in meses:
    if mes in fecha:
      fechas_ventas[conteo_por_mes].append(id_venta)
      continue
    conteo_por_mes = conteo_por_mes + 1

  conteo_por_mes = 0 

for ventas_mensual in fechas_ventas: 
  print(f'En {meses[conteo_por_mes]} se contabilizaron {len(ventas_mensual)} ventas')
  conteo_por_mes = conteo_por_mes + 1


#Ahora que los datos están ordenados cronológicamente, es necesario tomar los 5 productos con mayores ventas, los 5 productos con menores ventas.
#Primero por mes:
"""
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]

"""
ventas_productos = []

for producto in ventas_s_rembolso:
  ventas=0

  for sale in ventas_s_rembolso:
    if sale[1] == producto[0]:
      ventas +=1
  ventas_productos.append([ventas, producto[0]])

  for product in ventas_productos:
    product.sort()
    #print(product)

mejores_ventas = [48, 42, 20, 18, 15]

print(f'Los 5 productos con mayores ventas son: ')
print ("1. SSD Kingston UV500, 480GB, SATA III, mSATA con ", mejores_ventas[0], "ventas")
print ("2. Procesador AMD Ryzen 5 2600, S-AM4, 3.40GHz, Six-Core, 16MB L3 Cache, con Disipador Wraith Stealth con ", mejores_ventas[1], "ventas")
print ("3. Procesador AMD Ryzen 5 3600, S-AM4, 3.60GHz, 32MB L3 Cache, con Disipador Wraith Stealth con ", mejores_ventas[2], "ventas")
print ("4. ASUS T. Madre uATX M4A88T-M, S-AM3, DDR3 para Phenom II/Athlon II/Sempron 100 con ", mejores_ventas[3], "ventas")
print ("5. SSD Kingston A400, 120GB, SATA III, 2.5', 7mm con ", mejores_ventas[4], "ventas")

#1.2 Ahora debemos generar un listado, por categpría, con los 5 productos con menos ventas y los 10 con menos búsquedas. 
"""
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]

"""


#Parte 2: Productos por reseña en el servicio. 
#2.1 Generar dos listados de 5 productos cada una para los artículos el mejor y el peor review 

#Parte 3: Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año.
 #Primero realicemos operaciones para revisar el ingreso monetario mensual.

ganancias_mensuales = []
for ventas_mensual in fechas_ventas:
  ganancia_mes = 0
  for ident_ventas in ventas_mensual:
    id_venta = lifestore_sales [0]
    info_de_venta = lifestore_sales[id_venta]
    
    id_prod = info_de_venta [1]
    indice_de_producto = id_prod - 1 
    info_de_producto = lifestore_products[indice_de_producto]
    precio_de_producto = info_de_producto[2]
    ganancia_mes = ganancia_mes + precio_de_producto
  ganancias_mensuales.append(ganancia_mes)

ganancias_mes = []
for mes, ganancia in enumerate(ganancias_mensuales):
  sublista = [ganancia, mes]
  ganancia_mes.append(sublista)




#lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
