<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" width="120" height="120" align="right" />

# Notas - Programación en Python  

**Gabriel Ramírez Vilchis**  

Licenciatura en Ciencias Genómicas

## Markdown  

_3 de febrero de 2022_  

### ¿Qué es Markdown?  

- Es un **lenguaje de marcado** ligero.  
- Permite agregar **formatos** como:  
  - Encabezados  
  - Negritas  
  - Cursivas  
  - Listas  
  - ¡Y mucho más!  
- Basado en **texto plano**.  
- Es **minimalista**.
- Fácil de exportar a **otros formatos**.  

#### ¿Por qué usar Markdown?  

- Es **rápido y cómodo**.  
- Sintaxis sencilla.  
- Editores de texto **minimalistas**.  
- Se puede **compartir** con otros dispositivos.  

#### Editores de Markdown

##### Windows  

- MarkdownPad  
- DownMarker  
- MarkPad  

##### MacOS  

- Typora  
- MacDown  

##### Linux  

- Springseed  
- Remarkable  

### Tomar notas con Markdown  

Es una buena práctica guardar un archivo de Markdown al abrirlo, antes de comenzar a escribir.  

#### Encabezados  

Para insertar un encabezado se utiliza el caracter '#' al inicio del texto. Por cada '#' adicional se entiende que dicho encabezado está subordinado a cierto nivel en la estructura del texto.  Por ejemplo:

Sintaxis: `# Título`  

# Título  

Sintaxis: `## Subtítulo`  

## Subtítulo  

Sintaxis: `### Sub-subtítulo`  

### Sub-subtítulo  

¡Así se pueden tener notas mejor organizadas!  

#### Formatos  

##### Negritas  

Hay dos opciones para escribir en **negritas**. La primera es usar `**dos asteriscos**` rodeando la palabra o frase a resaltar, mientras que la segunda es utilizar `__dos guiones bajos__` de la misma manera.  

##### Cursivas  

Para escribir en _cursivas_ también pueden usarse guiones bajos o asteriscos, pero de manera sencilla; es decir, `*con asteriscos*` o `_con guiones bajos_`.  

##### Citas  

Para agregar una cita se coloca el caracter '>' antes del texto que corresponde a la cita.  

> "Así se agrega una cita"  

##### Saltos de línea  

Para agregar saltos de línea deben agregarse dos espacios en blanco al final de cada línea.  

#### Listas  

En Markdown pueden usarse listas desordenadas u ordenadas.

##### Listas desordenadas  

Para crear **listas desordenadas** se escribe un guión, un espacio y el elemento de la lista.  

- Elemento 1  
- Elemento 2  
- Elemento 3  

##### Listas ordenadas

Para crear **listas ordenadas** se escribe el número seguido de un punto, un espacio y el elemento de la lista ordenada.  

1. Elemento 1  
2. Elemento 2  
3. Elemento 3  

#### Código  

Si queremos insertar una sola línea de código, podemos hacerlo `con dos acentos graves` alrededor de la línea de código.  

También podemos agregar bloques de código al colocar tres acentos graves seguidos de un salto de línea:  

```python
# Esto es un bloque de código  
```

#### Links  

Se puede agregar un link que funcione al hacer click sobre un texto con la sintaxis `[Texto](url)`. Por ejemplo:  

Aquí puedes consultar el sitio de la [LCG](https://www.lcg.unam.mx).  

También puede colocarse el link sin ninguna palabra o frase relacionada con la sintaxis `<url>`. Por ejemplo:  

<https://www.lcg.unam.mx/>  

#### Imágenes  

Para agregar imágenes podemos utilizar alguna de las siguientes sintaxis:

1. Usando la URL en donde se encuentra la imagen: `![LogoMarkdown](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Markdown")`  

   ![LogoMarkdown](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Markdown")

2. Indicando la ruta en donde se encuentra la imagen: `![](./img/facebook_icon.png "logo fb")`  

3. Usando código HTML para definir el tamaño de la imagen: `<img src="./img/logoMarkdown.png" width="50" height="50" />`  

#### Tablas  

Se usan pipes '|' y guiones '-' para generar el formato de tabla. Por ejemplo:  

| Formato   | Etiqueta |
| --------- | -------- |
| Título    | `#`      |
| Subtítulo | `##`     |

## Git  

_10, 17 y 24 de febrero de 2022_  

### Introducción  

#### ¿Qué queremos lograr con el desarrollo de un software?  

Es importante saber cuál es el problema a resolver. Debemos codificar de tal manera que si se lo pasamos a a alguien más, esa persona pueda continuar con nuestro código.  

#### ¿Cómo lograrlo?  

Hay estándares que son básicos para escribir código, lo cual permite codificar de una manera adecuada.  

- Usar estándares de codificación.  
  - Para Python se usa PEP8 para Python.  
- Usar notaciones o estándares de nombrado.  
  - Camel case.  
  - Upper case.  
- Buenas prácticas.  
- Control de versiones de código.  

Al desarrollar software buscamos:

- Resolver problema

La solución debe tener prácticas y características que permitan recordar o que otras personas lo entiendan

### Buenas prácticas

Se basa en lineamientos que usan muchos programadores alrededor del mundo.

- Encabezado de programas

- Documentación interna. Pocas líneas que nos ayuden a recordar con palabras claves lo que hace una línea de código.
- Nombres adecuados de variables y métodos/funciones
- Nombre adecuado de programas.

Debemos tener un control (automatizado o manual) de las versiones del código

Sirve para identificar lo que fue cambiando en un documento de código.

Para el control de versiones es importante

#### Control de versiones

##### Forma manual

El versionamiento está constituido por dos dígitos, versiones primarias y secundarias (X.Y). Cada quien decide cómo versionar sus documentos.

v1.8 major y minor

minor es para cambios menores

###### Reglas

- Major
- Minor

- Ejemplo: myScript_v0.1.py

##### Forma automática

Se hace por medio de un sistema de control de versiones.

Ejemplos:

- Git

#### ¿Qué es un sistema de control de versiones?

- Herramienta encargada de controlar todos los cambios realizados en los programas, creando deferentes versiones de nuestros archivos.
- Commit: es un registro de un cambio de interés.
- Los controladores existen desde inicios de 1980.

#### ¿Para qué?

- Se conserva toda la historia de los cambios en nuestro código.
- Permite que varias personas trabajen en paralelo.

### ¿Qué es Git?

Git es un sistema de control de versiones que permite el trabajo colaborativo.

#### Git de manera local

- Acceso sólo desde el dispositivo (privado)
- Control desde computadora
- Uso personal

#### Git + GitHub

- Trabajar conjuntamente
- Comunidad por un fin común
- Contribución para mejoras
- Acceso de otras personas al código sin afectarlo

#### Trabajar con Git

1. Instalar y configurar
2. Esquema de trabajo

### Comandos importantes

`git --version`Devuelve la versión de Git instalada

`git config --global user.name "[TuNombre]"`

### Esquema de trabajo

Git no controla todo lo que se almacene en el repositorio Git, por lo que hay que indicarle que lo haga usando `git add`, con lo que empezará a preparar almacenando temporalmente los cambios, y cuando le indiquemos que confirme esos cambios usamos `git commit`

Repositorio: carpeta que contiene el seguimiento de los cambios que se realicen en el código.

### Crear un repositorio

- Definir la ruta de trabajo
- Crear una carpeta

#### Buenas prácticas

Seguir una estructura de organización de carpetas y archivos para proyectos.

- docs
- lib
- src
- test

¡No meterse con .git!

Git es el controlador de versiones

git init

git add

git commit -m "Mensaje"

### Mensaje para el commit

Escribir un mensaje que describa con precisión los cambios que se han realizado. Alrededor de 50 caracteres.

### Ramas de Git  

La rama **master** es la empleada por defecto en Git

Git permite hacer referencia a los commits a través de cabeceras. Si se quiere hacer referencia a un commit se puede hacer por medio del identificador o de la cabecera. El commit más reciente se encuentra hasta arriba, por lo que es el HEAD. El segundo más reciente será el HEAD\~1, el tercero el HEAD\~2, y así sucesivamente.

### Restaurar una versión  

Para restaurar una versión usamos `git checkout [HEAD|IdCommit] [file]`

git log

git log -N

git log --oneline

git diff HEAD ~#

El archivo **.gitignore** le indica a Git cuáles son los archivos que debe ignorar.

## GitHub  

_24 de febrero y 3 de marzo de 2022_  

GitHub es una plataforma web que permite alojar proyectos basados en Git, haciendo

### GitHub Desktop

GitHub Desktop es la interfaz gráfica de GitHub, que permite la interacción con la plataforma desde nuestra plataforma.

Pull baja información y push la sube

`git credential-oskeychain erase` borra las credenciales previas.  



Se usan casos de uso para describir los problemas.

- Usar estándar PEP8
- No escribir "código spaghetti o repetir"
  - Refactorizar: Q
- Comentar el código, iniciando con un encabezado
  - TITLE
  - VERSION
  - AUTHOR
  - DESCRIPTION
  - CATHEGORY
  - USAGE
  - ARGUMENTS
- La primera versión que se sube a GitHub debe tener el algoritmo de lo que se desea hacer sin codificar.



## Introducción a Python

Python es un lenguaje interpretado, por lo que lee las instrucciones y las ejecuta en tiempo real.

### Filosofía de Python

Se espera que podamos entender el código de cualquier persona, y que cualquier persona pueda entender nuestro código, es decir, se busca que sea legible para los humanos. Python fue creado por Guido van Rossum buscando desarrollar un lenguaje más sencillo para los programadores. Los principales objetivos al crear Python eran un lenguaje amigable.

### Versiones de Python

No son recomendables las versiones beta.

Es preferible usar Python 3 porque tiene soporte por parte del equipo de desarrollo, sólo usamos Python 2 cuando el programa ya estaba hecho en Python 2 y es complicado pasarlo a Python 3

### Comandos sistema



### Ecosistema de Python

d

### Tipos de datos

#### Números y sus operadores

Python sirve como una calculadora

#### Strings

Son cadenas de caracteres y pueden estar encerradas entre comillas simples ('...') o comillas dobles ("...")



En Python, cada dato en un programa es un objeto.

- Dato es un valor
  - Enteros
  - Flotantes
  - Cadenas
- Objeto tiene
  - Identificador
  - Tipo
  - Valor
- Funcionalidades por tipo de objeto definidas por Python: métodos
- Funciones no están vinculadas a objetos



- Input: Dar una variable

  - input(): Ingresar un valor
  - open(): Lee archivos
  - Argumentos: Pasar argumentos por medio de la línea de comandos

  ```python
  dna = input('Dame una secuencia de DNA:\n')
  print(dna)
  ```

  



## Comentarios

Tienes unos apuntes muy ordenados <3
