import sys
sys.path.insert(0,"\Users\Lorenzo\Documents\programacion\2.Desarrollo_OO\El_ordenador_sabe_leer\codigo_cap13")
sys.path.insert(0,"\Users\Lorenzo\Documents\programacion\2.Desarrollo_OO\El_ordenador_sabe_leer\codigo_cap13/aprendizaje")
#Importaciones de directorios
from aprendizaje import aprendizaje
from lectura_etapa_1 import lectura_etapa_1
from lectura_etapa_2 import lectura_etapa_2
from lectura_etapa_3 import lectura_etapa_3
from creacion import creacion
from preparacion_imagenes import preparacion_imagenes
from red_convolucioal import red_convolucional


def iniciar():
    while True:
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Aprendizaje")
        print("[2] Lectura_etapa_1")
        print("[3]  Lectura_etapa_2")
        print("[4]  Lectura_etapa_3")
        print("[5] Cerrar el Manager ")
        print("========================")
        opcion = input("> ")
        if opcion == "1":
            print("Ejercicio 1")
            while True:
                print("========================")
                print("[1] Aprendizaje")
                print("[2] Creacion")
                print("[3] Preparacion_imagenes")
                print("[4] red_convolucional")
                print("[5] Salida")
                print("========================")
                opcion2 = input("> ")
                if opcion2 == "1":
                    aprendizaje()
                elif opcion2 == "2":
                    creacion()
                elif opcion2 == "3":
                    preparacion_imagenes()
                elif opcion2 == "4":
                    red_convolucional()
                elif opcion2 == "5":
                    print("Volviendo al menu principal")
                    break

        elif opcion == "2":
            lectura_etapa_1()          

        elif opcion == "3":
            lectura_etapa_2()

        elif opcion == "4":
            lectura_etapa_3()
            
        elif opcion == "5":
            print("Saliendo...")
            break
