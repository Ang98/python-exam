**Prueba de ingreso OpenLab - Grupo de Freelancers y asesorías - Django**

Estimados postulantes, el siguiente examen tiene como objetivo medir sus siguientes capacidades respecto a los requerimientos del grupo de Freelancers y asesorías de OpenLab.

Se evaluará: detalle de respuestas, capacidad, rol que desempeñan (hay espacio por cada rol), manejo de funciones, framework que usen. Deberán crear un FORK de este repositorio y resolver en el readme.me las preguntas así como linkear las resoluciones a los problemas de programación por este medio

1. **Responda las siguientes preguntas sobre las siguientes tecnologías: Docker, git, postman.**

- ¿Sabes que es?
- ¿Sabes para qué sirve?
- ¿Sabes cómo se usa?

RESPUESTAS:

GIT:
¿Sabes que es?

Si , es un sistema que nos ayuda a controlar las version de un proyecto de software

¿Sabes para qué sirve?

Si , sirve para guardar cambios hechos en el proyecto en un instante dado, tener todo un registro de los cambios hechos, observar los cambios desde otras versiones y poder regresar a los cambios.
Tambien ayuda a repartir la carga de trabajo si es que se trabaja con otras personas y detectar los avances propios de estos.

¿Sabes cómo se usa?

Si lo he utilizado casi siempre desde que lo conoci, Tiene varios comandos que ayudan a realizar el guardado de cambios,reparticion de tareas, subida a un repositorio remoto,etc.

DOCKER:
¿Sabes que es?

Si , es un sistema de creacion y control de contenedores. Un contenedor es como una maquina virtual solo que sin el sistema operativo, ya que este se basa en el sistema operativo de la computadora que se esta utilizando, en el contenedor se almacenan procesos y sirve de ambiente de trabajo para el alojamiento de un proyecto de software.

¿Sabes para qué sirve?

Si , Sirve mas para la arquitectura de microservicios , en la que cada contenedor representaria un servicio de estos. Ayuda en distribucion de carga de pesos en los proyectos ya que cada contenedor puede estar alojado en diferentes servidores y asi conectarse con los demas microservicios.

¿Sabes cómo se usa?

Si pero lo he utilizado poco, Es una tecnologia muy util a la hora de desplegar proyectos en los diferentes servidores.

POSTMAN:

¿Sabes que es?

Si , es una interfaz para la probar las APIs

¿Sabes para qué sirve?

Si, sirve para probar las apis con las peticiones correspondientes, verificando si estas funcionan o arrojan errores

¿Sabes cómo se usa?

Si, es muy util al momento de pasar un proyecto a la fase de desarrollo.


1. **Responda las siguientes preguntas**

- ¿Tienes experiencia en hackatones, concursos, freelancer, laboral?
- ¿Cuéntanos sobre tu experiencia?
- ¿Qué rubro del desarrollar software te gustaría desempeñar?
  - QA
  - Desarrollo
  - Product Owner
- ¿Tienes ideas de apps o algo propio que quieras desarrollar? (ya sea como startup o libre para la comunidad)

RESPUESTAS:

¿Tienes experiencia en hackatones, concursos, freelancer, laboral?

he participado en la ultima hackaton que ocurrio en la FISI (facultad de ingenieria de sistemas e formatica) de la UNMSM, participe en la opcion de educacion infantil , mi propuesta fue la de un sistema de reforzamiento de aprendizaje a nivel primario , que consistia en que cuando un profesor finalice su clase de un tema de un curso , este podra tomar una evaluacion a todos sus alumnos con lo cual los alumnos aplicarian lo aprendido en la clase reciente y el profesor podria ayudar a aquellos que no obtuvieron una buena nota.

¿Cuéntanos sobre tu experiencia?

En el 2018 empeze un proyecto para la biblioteca de la FISI con algunos alumnos de esta misma escuela, el proyecto consitia en controlar la asistencia de los alumnos en la biblioteca , registrar su estancia y cuanto tiempo utilizaron la biblioteca, este proyecto se realizo en spring boot utilizando la arquitectura MVC . En el año 2019 conoci el framework django de python el cual me ayudo a realizar varios proyecto de los cursos del ciclo universitario. Llegue a conocer la libreria Django Rest Framework con la cual pude realizar APIs Rest y utilizarlos en un FrontEnd con Angular y React. Utilice Github para el alojamiento de backend y Heroku para el desplieue en fase de desarrollo de mis proyectos.

¿Qué rubro del desarrollar software te gustaría desempeñar?

Me gustaria desarrollar el rubro de Desarrollador porque es la rama en la que estos ultimos años he estado viendo , pero tambien me gustaria conocer y aprender sobre las otras ramas.

¿Tienes ideas de apps o algo propio que quieras desarrollar? (ya sea como startup o libre para la comunidad)

Si , me gustaria desarrollar una app propia que consiste en utilizar las notas o evaluaciones de estudiantes para apostar, es como un juego.


**Resuelva las siguientes preguntas en un repositorio aparte y linkealas en tu readme.md**
## Problema 1 - Python: Para los siguientes arreglos
1. [1,1,1,0,2,1,0,0,2,0,1,0]
2. [1,1,1,0,2,1,0,0,2,0,0,0,1]
3. [0,2,2,2,0,0,0,1,2,1,1,0,0,0]
4. [3,3,3,3,3,3,3,1,0,0,0,1]

Cada arreglo representa una parcela, que tiene en cada posición una regadera. Dicha regadera tiene un valor que representa su alcance, por ejemplo en la parcela: [0,0,0,1] la regadera de la posición &quot;4&quot; puede regar 1 espacio más aparte de su misma ubicación ![](https://res.cloudinary.com/openlab-pe/image/upload/v1601789562/temporal/2.png) .

Nota:

- Cada valor &quot;X&quot; indica que una regadera puede regar una distancia &quot;X&quot; hacia ambas direcciones (Derecha e izquierda) como indica la figura.
- El cero indica que solo se riega así misma.

![](https://res.cloudinary.com/openlab-pe/image/upload/v1601789532/temporal/1.png)

El objetivo de este problema es crear un algoritmo que me indique por cada arreglo presentado, la cantidad mínima de regaderas que se necesita prender para regar toda la parcela.

Si tienen una duda sobre este problema, pueden comunicarse con Edwin Deza al 987645213 y él resolverá sus dudas.

## Problema 2 - Django:

Hacer un proyecto Django con las siguientes características

- Ruteo:
  - /
    - Debe tener un texto que de la hora del sistema en el siguiente formato: DD-MM-AA - Hora - Segundos
  - /Nosotros
    - lorem ipsum
  - /Servicios
    - 4 Servicios renderizados de manera dinámica
      - Servicio:
        - Nombre
        - Descripción
        - Imagen.
- Ruteo API:
  - /usuarios - GET
    - Listado de 5 usuarios
      - Usuario:
        - Nombres
        - Apellido paterno
        - Apellido materno
        - Edad
  - /usuarios/${id} - GET
  - /crear-usuarios - POST
  - /editar-usuarios/${id} - PUT
  - /borrar-usuarios/${id} - DELETE
- Debe tener un menú con las 4 opciones de las rutas
- Se debe usar una BD SQLite