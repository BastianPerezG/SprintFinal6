# SprintFinal6
En este repositorio se guardará el proyecto FINAL con todo el aprendizaje adquirido durante el módulo 6 (Desarrollo de Aplicaciones Web Python Django) del Bootcamp Full Stack Python

Documentación de uso.

-Descargar el Zip desde el github -Descomprimir y abrir a través de su editor de código preferido -Ingresar a la carpeta sistemaVentas, abrir un terminal y correr el comando python manage.py runserver -Luego ingresar desde un navegador web al localhost http://127.0.0.1:8000/ -Una vez dentro debería poder visualizar la landing page.

Proceso de autenticación

En la landing page a un navbar con el botón de login, dentro de esa página usted podrá ingresar a la aplicación con los siguientes usuarios (por default):

ejohnson odavis awilson

y la clave de todos estas cuentas es hola.123

Al autenticarse se redirigirá a la landing page pero en el navbar aparecerá un nueva opción en el navbar llamada Productos, esa página solo puede ser accedida una vez logueado. En esa página podrá ver la bienvenida personalizada al usuario y además del catálogo de productos.

En la opción registrarse podrá crear un nuevo usuario, esto tiene su respectivo formulario y vista y esta podrá agregar una foto de perfil (no obligatorio, si no quiere agregarla hay una foto de perfil por default), escoger a que grupo de usuarios pertenece. En este proyecto existen 2 tipos de grupos, los trabajadores y los clientes, cada uno de ellos tiene acceso a distintos permisos. Por ejemplo, solo los trabajadores pueden entrar a la vista de todos los usuarios del sistema

De manera predeterminada, puede probar con odavis o awilson como clientes y csupanta o mbrown como trabajadores

Por otro lado, en este sprint final también se hizo dinámico todos los templates, por ejemplo, el template de paginaRestringida que es la que muestra los productos. Además, de reduccion de código que ya no se utiliza que viene de los desafíos anteriores del mismo módulo.

Por último, se adjuntan las librerías que se utilizaron en este proyecto destacar PILLOW, que fue la que me permitió subir fotos de perfil para los usuarios.
