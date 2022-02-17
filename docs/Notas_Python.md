# Notas - Programación en Python  

**Gabriel Ramírez Vilchis**  



## Markdown  

_3 de febrero de 2022_  

### ¿Qué es Markdown?  

- Lenguaje de marcado.  
- Basado en texto plano.  
- Fácil de exportar a otros formatos.  

### Buenas prácticas  

Es una buena práctica guardar un archivo de Markdown al abrirlo, antes de comenzar a escribir.  

> "Así se agrega una cita"  

Negritas usar doble guion bajo o doble asterisco.  



### Listas  

Se escribe el número seguido de un punto, un espacio y el elemento de la lista ordenada

1. d  



### Código  

Si queremos insertar una sola línea de código, podemos hacerlo `con dos acentos graves`  

También podemos agregar bloques:  



```python
/// Esto es un bloque de código
```

`` texto en **negritas**``*  





### Links  

Aquí puedes consultar el sitio de la [LCG](https://www.lcg.unam.mx).

<https://www.lcg.unam.mx/>  



Ejemplos de marcado  

| Formato   | Etiqueta |
| --------- | -------- |
| Título    | `#`      |
| Subtítulo | `##`     |





## Git  
_10y 17 de febrero de 2022_  

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

Git no controla todo lo que se almacene en el repositorio Git, por lo que hay que indicarle que lo haga usando `git add`, con lo que empezará a preparar alamacenando temporalmente los cambios, y cuando le indiquemos que confirme esos cambios usamos `git commit`

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
La rama __master__ es la empleada por defecto en Git

Git permite hacer referencia a los commits a través de cabeceras. Si se quiere hacer referencia a un commit se puede hacer por medio del identificador o de la cabecera. El commit más reciente se encuentra hasta arriba, por lo que es el HEAD. El segundo más reciente será el HEAD~1, el tercero el HEAD~2, y así sucesivamente.

### Restaurar una versión  
Para restaurar una
