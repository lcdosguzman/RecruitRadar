## RecruitRadar
Es una Web donde sus usuarios se pueden loguear y llenar sus datos de curriculo y/o hoja de vida. Adicionalmente los usuarios pueden publicar articulos que pueden ser vistos por los otros usuarios.

Un usuario que no esté registrado puede ver algunas partes de la web, asi como tambien las ultimas 10 publicaciones.

Otra parte donde puede ingresar es ver el perfil de los que publicaron en esas 10, con tan solo hacer clic en el autor de la publicacion.  Si quiere publicar su información o ver otros perfiles debe registrarse.

El publico es para personas que buscan empleo y reclutadores.



**El diseño está hecho para que pueda crecer en el futuro agregando mas datos al perfil y mas interacciones entre los usuarios como or ejemplo: mensajes, reacciones, etc**


## Puntos importantes para la revisión
- **Url Principal:** http://127.0.0.1:8000/appCurriculos/

- **Apps** El proyecto consta de 2 apps:
    - appCurriculos: esta app contiene toda la lógica de los curriculos y datos que se muestran en el mismo.
    - appUsers: es la que maneja la lógica de login y registro de usuarios

- **Modelos** Los modelos creados son:
    - Se hereda el modelo User para el contro de los usuarios.
    - DataUsuario: Se utiliza para manejar los datos del perfil de cada usuario y tiene una relacion de 1:1 con User. Este modelo guardará una tupla por cada User.
    - ExperienciaLaboral: Se utiliza para guardar la experiencia laboral del usuario. (En el caso del proyecto final guardará la de todos los usuarios). Tiene una relación de 1:N con User. es decir 1 user puede tener N experiencias laborales.
    - Educacion: Se utiliza para guardar los estudios del usuario. (En el caso del proyecto final guardará la de todos los usuarios). Tiene una relación de 1:N con User. es decir 1 user puede tener N estudios.
    - Idioma: Se utiliza para guardar los idiomas manejados por el usuario. (En el caso del proyecto final guardará la de todos los usuarios). Tiene una relación de 1:N con User. es decir 1 user puede tener N idiomas.
    - Skills: Se utiliza para guardar las habilidades manejadas por el usuario. (En el caso del proyecto final guardará la de todos los usuarios). Tiene una relación de 1:N con User. es decir 1 user puede tener N skills.
    - Publicacion: Se utiliza para que los user puedan crear publicaciones y compartirlas con la red. Tiene una relación de 1:N con User. es decir 1 user puede tener N publicaciones.
    - Avatar: se creo este modelo para la configuracion de la foto de perfil. Tiene una relacion de 1:1 con User. Este modelo guardará una tupla por cada User.
    
 - **Vistas basadas en clases** Para esta reentrega se tomo en cuenta el uso de vistas basadas en clases y así cumplir con una de las recomendaciones de la entrega. Para ello los siguientes modelos se trabajaron con este tipo de vista:
    - Skills
    - Idiomas
Para ambos se manejo el CRUD completo. Agregar, modificar, eliminar y ver detalle.

 - **Test Unitarios** El proyecto tiene algunos test unitarios.

 - **Archivo de Pruebas** La hoja de cálculo con las pruebas estan dentro del repositorio. Al mismo nivel que el README.


## Tomar en Cuenta
User de prueba1
usuario: korumo
pass: 1234Guatamare.

User de Prueba2
usuario: mguzman
pass 123Venezuela

