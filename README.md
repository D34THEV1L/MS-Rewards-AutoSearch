# MS-Rewards-AutoSearch

Facilita tus busquedas de bing con mayor seguridad que otros metodos

## Como Funciona

Las preguntas o busqueda las haces tu, las puedes hacer con inteligencia artificial eligiendo temas o simplemente escribiendolas tu puedes hacer de
1 a 60, mi recomendacion es variar el numero de preguntas por dia, despues pones las preguntas en el formato json ya hecho. Si leido esta en true significa que esas preguntas ya se
usaron, crea mas y cambialo a true, despues lanzas la aplicacion seleccionas un modo y dejas que se encargue de tus busquedas, la computadora no la toques hasta que el programa
pare por si solo.

Ejemplo del json:
```json
{
    "leido": false,
    "preguntas": [
        "Pregunta de busqueda 1",
        "Pregunta de busqueda dos"
    ]
}
```
## Como Generar preguntas con la IA
```
Generame <Numero de preguntas> lo mas humanamente posible, no uses caracteres
especiales que unaconsola no soporte y trata que las
preguntas sean diferentes y humanas y una inteligencia artificial no pueda detectarlo,
 estos son los temas para
las preguntas: <tema1> <tema2> <tema3> . . .
Y quieroque utilizes este formato de json
{
    "leido": false,
    "preguntas": [
        "Pregunta de busqueda 1",
        "Pregunta de busqueda dos"
    ]
}
```
Para mayor seguridad humaniza tus preguntas
https://writehuman.ai/
## Instalacion

* Descarga el repositorio
* Instala los requerimientos

```cmd
pip install requirements.txt -r
```
* Inicia el programa
```cmd
python AutoMicrosoftRewards.py
```
Nota: Tambien puedes usar el open.bat



## Imágenes

![image](https://github.com/D34THEV1L/MS-Rewards-AutoSearch/assets/87221905/46893365-256e-4703-b190-a0e97dd00966)


![image](https://github.com/D34THEV1L/MS-Rewards-AutoSearch/assets/87221905/8055ddd1-eace-43f4-b707-5812da6130d2)

