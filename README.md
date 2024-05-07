# MS-Rewards-AutoSearch

Facilita tus busquedas de bing con mayor seguridad que otros metodos. Ojo este programa lo hice para mis necesidades lo guardo en github para no perderlo pero
si encuentras el repositorio y lo usas ojala y te funcione bien.

## Actualizacion
10/04/2024
Ahora puedes poner una intermision para evitar que te detecten y el programa solito te avisara cuando vaya a volver a retomar las operaciones

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
Puedes usar este comando o usar el tuyo propio
```txt
Generame <Numero de preguntas> lo mas humanamente posible, no uses caracteres
especiales que una consola no soporte y trata que las
preguntas sean diferentes y humanas que una inteligencia artificial no pueda detectarlo,
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

O puedes usar: 
```
Objetivo: Generar preguntas similares a las que yo he creado a partir de un conjunto de temas predefinidos.

Instrucciones:

Proporcionar una lista de temas: La IA debe tener acceso a una lista de temas similares a los que yo he utilizado, como:

*Aprender programar desde cero: lenguajes para principiantes
*Editor de código gratuito y fácil para programar en Python
*Mejores páginas web para aprender Java: cursos gratuitos
*Libro para aprender C++ para principiantes
*Objetos vs funciones en programación: diferencia y uso
*Escribir código limpio y mantenible: trucos y consejos
*Crear aplicación para celular: lenguajes e instrumentos
*Depurar programa que no funciona: encontrar el error
*Hacer código más rápido y eficiente
*Pruebas unitarias: implementar en proyecto
*Analizar funcionamiento de programa sin código fuente
*Programa gratuito y fácil para ingeniería inversa de software
*Identificar partes de un programa: funciones y variables
*Entender flujo de un programa y cómo interactúan sus partes
*Técnicas para descompilar código a lenguaje máquina
*Modificar código de programa sin tener el original
*Riesgos de hacer ingeniería inversa: precauciones
*Legalidad de la ingeniería inversa: leyes a considerar
*Aplicaciones prácticas de la ingeniería inversa
*Cuestiones éticas en la ingeniería inversa
*Crear primera página web: HTML y CSS
*Estructura básica de una página web con HTML
*Dar estilo a página web con CSS: propiedades y selectores
*Layouts en CSS para distintos diseños de página
*Menú de navegación responsive con HTML y CSS
*Incorporar imágenes y videos en página web
*Compatibilidad de página web con diferentes navegadores y dispositivos
*Herramientas para crear y depurar sitio web
*Optimizar página web para que cargue más rápido
*Frameworks de JavaScript para páginas web interactivas
*Especificar el estilo de las preguntas: La IA debe poder generar preguntas en diferentes estilos, como:

Preguntas abiertas que inviten a la reflexión y el análisis.
Preguntas cerradas que busquen información específica.
Preguntas hipotéticas o de "qué pasaría si".
Preguntas que comparan o contrastan diferentes conceptos.
Considerar el nivel de dificultad: La IA debe poder ajustar el nivel de dificultad de las preguntas según el público objetivo.

Ejemplo de prompt:

Genera 50 preguntas similares a las de la lista proporcionada, cubriendo una variedad de temas, estilos y niveles de dificultad. Las preguntas deben ser formuladas de manera natural y coloquial, simulando el lenguaje que se utiliza en las búsquedas en internet. Evita el uso de comas y caracteres especiales.

Usa este JSON asi quiero el formato:
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

