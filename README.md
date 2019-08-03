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

## TODO:

- Macro  para lugares donde no apareceran el header o el footer
- Macro para mostrar fecha de compilacion.
- Añadir exportación para JS-NEW o JS o PDF o DOT o MOBI
- Incluir soporte para pandoc
- Parser par convertir el codigo a Squiffy
- Filtros (buscar y reemplazar cualquier cosa del texto, se puede especificar segun la salida tambien. Ejem: @filter(epub): ".gif" ".jpg"
- Soporte para kindlegen
- Concatenar archivos
- Macros para diseño de First Seen
- Devolver lista de variables y cantidad de escenas, acciones y palabras
- Si el formato es html, añadir la carpeta espeficiada a la url de las imagenes
- @ignore. Si esta en 1 del documento de salida sera eliminado todo lo que esté entre ~~ (ejemplo: ~~esto sera eliminado~~)
- Poder usar la cabecera del preprocesador en un documento aparte. Un archivo .prop con el mismo nombre del archivo fuente con el que se quiera trabajar. Eliminar que obligatoriamente el documento inicie con --- y finalice con ---.
- Uso de constantes que se apliquen solo en determinado formato, así podriamos tener varias constantes con el mismo nombre que pueden ser aplicadas segun el formato. Asi por ejemplo: ATRIBUTO: Facil (Se aplicará en cualquier formato). ATRIBUTO[html]: <p>Facil</p> (solo se aplicara cuando el formato sea html).
