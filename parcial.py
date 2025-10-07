# Lista de productos.
productos = ['Arroz', 'Fideos', 'Aceite', 'Azúcar']
# Lista de precios. El primer indice de cada una de las listas corresponde a la Tienda 1. Luego con el segundo elemento de cada una de las litas por separado es de la tienda 2 y asi sucesivamente.
precios = [
    [120, 115, 130],  # Arroz
    [80, 85, 78],     # Fideos
    [200, 210, 190],  # Aceite
    [95, 100, 90]     # Azúcar
]
bandera = True  # Variable bandera como punto de control.

menu = ('''\n*** Bienvenido al MENU de Precios ***\n\nMenu de opciones:       
    Oprima 1.\tMostrar precios de la tienda de su preferencia
    Oprima 2.\tMostrar producto con el precio mas elevado y el mas bajo de todas las tiendas
    Oprima 3.\tMostrar los productos con su precio promedio ordenada de Mayor a Menor
    Oprima 4.\tPara finalizar el programa''') # Menu de opciones (multicadena con espacios y sangria) Guardamos el menu en una varible para ser reutilizada.

print(menu) # Imprimimos el menu

while bandera: # Creamos un bucle infinito hasta que el usuario finalize el programa.
    opcion = int(input('\nIngrese una opcion (1|2|3|4): ')) # Solicitamos al usuario que ingrese una opcion del menu.

    while opcion < 1 or opcion > 4:  # Si el usuario ingresa un valor menor de 1 o mayor a 4 el programa volver a soliciarle un numero.
        print('\nError! Debe elegir las opciones que observa en pantalla!')
        opcion = int(input('\nIngrese nuevamente una opcion (1|2|3|4): '))

# Opcion 1 del programa.
    while opcion == 1: 
            print('\n\tEliga la tienda de su prefencia: | (1) Tienda 1 | (2) Tienda 2 | (3) Tienda 3 | (4) Volver al menu |') 
            tienda = (input('\nEliga una tienda: ')).lower().replace(" ", "")
            # Colocamos .lower() para forzar al programa a que el dato se ingrese en minusculas, lo mismo con el replace, por si el usuario escribe con espacios el usuario funciona de todas maneras.
            tienda_opciones_validas = ['1', 'tienda1', '2', 'tienda2', '3', 'tienda3', '4', 'volveralmenu'] 
            # Creamos una lista de todas las opciones disponibles que tiene el usuario para ingresar
            while tienda not in tienda_opciones_validas: # Si... el dato que ingresa el usuario en "tienda" no esta en la lista "tienda_opciones_validas"
                print('\n¡Error! ¡Debe elegir una tienda por numero o escribiendo el nombre!')
                tienda = (input('\nEliga una tienda: ')).lower().replace(" ", "")  # Da la oportunindad de volver a ingresar si el usuario falla.
                
            if tienda == '1' or tienda == 'tienda1': # Si el usuario ingresa tienda 1, recibira su informacion.
                print('\n¡Tienda Uno seleccionada!\n\n[Informacion]\n')
                for tienda1 in range(len(productos)): # Recorro la lista productos almacenando el recorrido en la variable "tienda1"
                    print(f'\nProducto: {productos[tienda1]}\nPrecio: ${precios[tienda1][0]}') 
                    # Imprimo el recorrido de los productos, y usando el recorrido de la lista productos, aprovecho el orden para recorrer la lista de precios utilizando unicamente el indice 0 que seria de la tienda 1.
                continuar = input('\n¿Desea continuar navegar por otras tiendas? (si/no): ').lower().strip() 
                # Pregunto al usuario si esta interesado en continuar o no. (lower para forzar si el usario escibe en mayusculas a minisculas, strip por si el usuario preciona 'espacio'.)
                
            elif tienda == '2' or tienda == 'tienda2': # Si el usuario ingresa tienda 2, recibira su informacion.
                print('\n¡Tienda Dos seleccionada!\n\n[Informacion]')
                for tienda2 in range(len(productos)):
                    print(f'\nProducto: {productos[tienda2]}\nPrecio: ${precios[tienda2][1]}')
                continuar = input('\n¿Desea continuar navegar por otras tiendas? (si/no): ').lower().strip()
                
            elif tienda == '3' or tienda == 'tienda3': # Si el usuario ingresa tienda 3, recibira su informacion.
                print('\n¡Tienda Tres seleccionada!\n\n[Informacion]')
                for tienda3 in range(len(productos)):
                    print(f'\nProducto: {productos[tienda3]}\nPrecio: ${precios[tienda3][2]}')
                continuar = input('\n¿Desea continuar navegar por otras tiendas? (si/no): ').lower().strip()

            elif tienda == '4' or tienda == 'volveralmenu':
                print(menu) # Imprimo nuevamente el menu principal.
                break  # Break para romper el bucle y poder volver al INICIO
            
            # FUNCIONAMIENTO DE CONTINUAR
            if continuar == 'no' or continuar == 'n':
                print('\nVolviendo al menu principal...')
                print(menu) # Imprimo nuevamente el menu principal para comodidad del usuario.
                break # Break para romper el bucle y poder volver al INICIO

            continuar_validacion = ['si', 's', 'no', 'n']   # Lista de validacion del continuar, solo funcionara continuar si el usuario escribe una opcion que esta dentro de la lista.

            while continuar not in continuar_validacion:
                print('\nPor favor. Coloca si o no para continuar...')
                continuar = input('\n¿Desea continuar navegar por otras tiendas? (si/no): ').lower().strip()

# Opcion 2 del programa                
    if opcion == 2:
        for tiendas in range(3): # Como son 3 tiendas, creo un range (3) para recorrer una por una. (0 al 2)
            precio_maximo = 0  # Variable para almacenar el numero maximo, cualquier numero va a ser mayor a 0.
            precio_minimo = 300 # Variable para almacenar el numero minimo, cualquier numero va a ser menor a 0.
            producto_costo_alto = '' # Variable para almacenar el producto mas caro.
            producto_costo_bajo = '' # Variable para almacenar el producto mas barato.

            for i in range(len(productos)): # Recorro los productos (0 al 3)
                if precios[i][tiendas] > precio_maximo:  # Si los precios ordenados con los productos con las todas las tiendas tiene un precio mayor a 0...
                    precio_maximo = precios[i][tiendas] # Entonces al cumplir la condicion, se almacena en "precio_maximo", el precio con el ordenamiento de los productos correspondientes... sumado al ordenamiendo de las tiendas.
                    producto_costo_alto = productos[i] # Se almacena en "producto_costo_alto" si cumple la condicion.

                elif precios[i][tiendas] < precio_minimo: # Hacemos lo mismo pero con el menor.
                    precio_minimo = precios[i][tiendas]
                    producto_costo_bajo = productos[i]
            print(f'\n\tTienda numero: {tiendas + 1}') # Al printear sumo un +1 por que sino da de 0 a 2.
            print(f'\nProducto con valor alto: {producto_costo_alto}\nPrecio: ${precio_maximo}')
            print(f'\nProducto con valor menor: {producto_costo_bajo}\nPrecio: ${precio_minimo}') # Priteamos todos los resultados que se repiten 3 veces por el range (3).
        
        print(menu) # Al terminar de mostrar todo el bucle aun continua y volvemos a mostrar las opciones para comodidad del usuario.

# Opcion 3 del programa
    elif opcion == 3:
        print('\nPromedio de los productos:')
        # Creo una variable para realizar una suma del elemento a la venta.
        suma_arroz = precios[0][0] + precios[0][1] + precios[0][2] # Accedo al numero del elemento a la venta de cada una de las tiendas y lo sumo.
        promedio_arroz = suma_arroz / len(precios[0]) 
        # Con la suma hecha, creo otra variable donde la almaceno y lo divido por la cantidad de numeros que estoy sumando en total.
        
        suma_fideos = precios[1][0] + precios[1][1] + precios[1][2]
        promedio_fideos = suma_fideos / len(precios[0])

        suma_aceite = precios[2][0] + precios[2][1] + precios[2][2]
        promedio_aceite = suma_aceite / len(precios[0])

        suma_azucar = precios[3][0] + precios[3][1] + precios[3][2]
        promedio_azucar = suma_azucar / len(precios[0])

        promedio_total = [promedio_arroz, promedio_fideos, promedio_aceite, promedio_azucar] # Junto todos los promedios en una sola variable
        promedio_total.sort() # Ordeno los numeros de los promedios de menor a mayor.
        productos.sort(reverse=True) # Ordeno los nombres de los productos de mayor a menor.
        for i in range(len(productos)): # Recorro los productos y gracias a ello puedo ordenarlo con el "promedio_total".
            print(f'\nProducto: [{productos[i]}] - Precio Promedio: [${promedio_total[i]:.1f}]') # Al imprimir el "promedio_total" utilizo el ":.1f" por si un numero tiene un float largo, lo recorte y quede mas entendible.

# Opcion 4 del programa
    elif opcion == 4:
        print('\n¡Gracias por utilizar el MENU de Precios! Hasta pronto.\n')
        bandera = False # Declaro la bandera que da inicio al While en False para que el programa termine.