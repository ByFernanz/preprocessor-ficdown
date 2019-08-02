# Prop: Un preprocesador para Ficdown

**Prop:** *Un preprocesador para Ficdown creado por Ricardo Monascal. Ampliado por Billy Fernández.*

Se establece una cabecera en el archivo .md donde se pueden declarar constantes, establecer la configuracion de ficdown y usar algunas macros especiales.

ejemplo:
```
---
@format: epub
@template: archivos/plantilla
@images: archivos/imagenes
@author: Billy Fernández
@bookid: 99999999999999
@language: es
@debug: 1
@scene_header: esto aparece al inicio de la escena
@scene_footer: esto aparece al final de la escena
@action_header: esto aparece al inicio de la accion
@action_footer: esto aparece al final de la accion
NOMBRE: Pedro Arturo
EDAD: 57 años
PALABRA: prueba
---

# [hola mundo](/hola)

Tu nombre es __NOMBRE__, tu edad es __EDAD__.

## Hola

Hola. Esto es una __PALABRA__.
```

Si quieres usar una constante en el codigo debe estar referenciada rodeada de doble rayita abajo.
<<<<<<< HEAD

## TODO:

- Macro  para lugares donde no apareceran el header o el footer
- Macro para mostrar fecha de compilacion.
- Añadir exportación para JS-NEW o JS o PDF o DOT o MOBI
- Incluir soporte para pandoc
- Parser par convertir el codigo a Squiffy
- Filtros (buscar y reemplazar cualquier cosa del texto, se puede especificar segun la salida tambien. Ejem: @filter(epub): ".gif" ".jpg"
- Soporte para kindlegen
=======
>>>>>>> f00b8aa90803e70e9ac794d3998eff5f7ff2739a
