from pystyle import Colorate, Colors, Write
import json
import pyautogui
import time
import sys
import random


# No soy muy bueno programando y este codigo en su mayoria fue hecho con IA puede tener bugs y errores.

colorate = Colorate()


Banner = r"""
__    __     ______        __  __     ______     ______     __  __         
/\ "-./  \   /\  ___\      /\ \_\ \   /\  __ \   /\  ___\   /\ \/ /         
\ \ \-./\ \  \ \___  \     \ \  __ \  \ \  __ \  \ \ \____  \ \  _"-.       
 \ \_\ \ \_\  \/\_____\     \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\      
  \/_/  \/_/   \/_____/      \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/                              
"""
Write.Print(f"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", Colors.cyan_to_green, interval=0.005)
Write.Print(Banner, Colors.purple_to_blue, interval=0.005)
Write.Print(f"              Microsoft Rewards Hacks Version 1.0.1 \n", Colors.white_to_red, interval=0.05)
Write.Print(f"- - - - - - - - - - - - / / Made by spyro \\ \\ - - - - - - - - - - - - - - \n", Colors.cyan_to_green, interval=0.005)
Write.Print("                       Configuraciones: \n ", Colors.white_to_blue, interval=0.05)
while True:
    inter_type = Write.Input("Sleccione el modo: \n (P) Predeterminado [Alto Riesgo] \n (R) Random [Bajo Riesgo] \n (I) Intermitente rango aleatorio [Riesgo Medio] \n $>", Colors.purple_to_red, interval=0.0025)
    if inter_type in ["P", "R", "I"]:
        break
    else:
        Write.Print(f"Error: Opción incorrecta. Inténtalo nuevamente.", Colors.red_to_yellow, interval=0.05)

if inter_type == "P":
    pred_timer = Write.Input(r"Has seleccionado Predeterminado. Ingrese el tiempo: ", Colors.green_to_cyan, interval=0.0025)
elif inter_type == "R":
    Write.Print(r"Has seleccionado aleatorio.", Colors.green_to_cyan, interval=0.0025)
elif inter_type == "I":
    random_range_x = Write.Input("Has seleccionado intermitente. Ingresa el inicio del rango: ", Colors.green_to_cyan, interval=0.0025)
    random_range_y = Write.Input("Ingresa el final del rango: ", Colors.green_to_cyan, interval=0.0025)
    Write.Print(f"Tu rango de aleatoriedad sera del {random_range_x} al {random_range_y}", Colors.green_to_cyan, interval=0.0025)

print(""" 
      Advertencia: Esta herramienta esta creada por un total inexperto en la programacion puede tener 
      errores y bugs ademas que puedes ser baneado
      del programa de Microsoft Rewards aunque nosotros tratamos de hacer que no sea asi. 
      No me hago responsable de nada y descargo toda la responsabilidad
      a el usuario de la misma.
    """)
input("\nPresiona Enter para continuar...")
print("Acomoda el mouse arriba de la barra de busqueda tienes 10 segundos.")


def cuenta_regresiva(segundos):
    for i in range(segundos, 0, -1):
        print(f"Cuenta regresiva {i} segundos...", end="\r")
        time.sleep(1)


cuenta_regresiva(10)
print("\n")
def escribir_preguntas(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
        preguntas = datos.get('preguntas', [])
        leido_stat = datos.get('leido')
        if leido_stat == True:
            print("Parece que estas preguntas de busqueda ya fueron usadas, genera otras y cambia el valor a FALSE")
            sys.exit()
            


        for pregunta in preguntas:
            if inter_type == "P":
                print(f"Esperando {str(pred_timer)} segundos")
                time.sleep(int(pred_timer))
            elif inter_type == "R":
                randomtime = random.randint(0, 100)
                print(f"Esperando: {str(randomtime)} segundos")
                time.sleep(int(randomtime))
                print(pregunta)
            elif inter_type == "I":
                randomtimeI= random.randint(int(random_range_x), int(random_range_y))
                print(f"Esperando: {str(randomtimeI)} segundos")
                time.sleep(int(randomtimeI))
                print(f"Pregunta: " + pregunta)
            pyautogui.click()
            time.sleep(random.randint(1,3))
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(random.randint(1,2))
            pyautogui.press('delete')
            pyautogui.click()
            
            for letra in pregunta:
                pyautogui.typewrite(letra)
                time.sleep(0.1)  
            pyautogui.press('enter')  
        
      
        datos['leido'] = True

    
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)


escribir_preguntas('preguntas.json')
