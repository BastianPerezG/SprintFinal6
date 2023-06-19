# SprintFinal6
En este repositorio se guardará el proyecto FINAL con todo el aprendizaje adquirido durante el módulo 6 (Desarrollo de Aplicaciones Web Python Django) del Bootcamp Full Stack Python

Documentación de uso.

-Descargar el Zip desde el github -Descomprimir y abrir a través de su editor de código preferido -Ingresar a la carpeta sistemaVentas, abrir un terminal y correr el comando python manage.py runserver -Luego ingresar desde un navegador web al localhost http://127.0.0.1:8000/ -Una vez dentro debería poder visualizar la landing page.

Proceso de autenticación

En la landing page a un navbar con el botón de login, dentro de esa página usted podrá ingresar a la aplicación con los siguientes usuarios (por default):

ejohnson odavis awilson

y la clave de todos estas cuentas es hola.123

Al autenticarse se redirigirá a la landing page pero en el navbar aparecerá un nueva opción en el navbar llamada Productos, esa página solo puede ser accedida una vez logueado. En esa página podrá ver la bienvenida personalizada al usuario y además del catálogo de productos.

En la opción registrarse podrá crear un nuevo usuario, esto tiene su respectivo formulario y vista y esta podrá agregar una foto de perfil (no obligatorio, si no quiere agregarla hay una foto de perfil por default), escoger a que grupo de usuarios pertenece. En este proyecto existen 2 tipos de grupos, los trabajadores y los clientes, cada uno de ellos tiene acceso a distintos permisos.

Por otro lado, en este sprint final también se hizo dinámico todos los templates, por ejemplo, el template de paginaRestringida que es la que muestra los productos. Además, de reduccion de código que ya no se utiliza que viene de los desafíos anteriores del mismo módulo.

Por último, se adjuntan las librerías que se utilizaron en este proyecto destacar PILLOW, que fue la que me permitió subir fotos de perfil para los usuarios.
Package                Version
---------------------- ---------
asgiref                3.7.2
brotlipy               0.7.0
certifi                2022.12.7
cffi                   1.15.1
charset-normalizer     2.0.4
colorama               0.4.5
conda                  22.11.1
conda-content-trust    0.1.3
conda-package-handling 1.9.0
cryptography           38.0.1
distlib                0.3.6
Django                 4.2.2
filelock               3.12.0
idna                   3.4
menuinst               1.4.19
Pillow                 9.5.0
pip                    22.3.1
platformdirs           3.5.1
pluggy                 1.0.0
pycosat                0.6.4
pycparser              2.21
pyOpenSSL              22.0.0
PySocks                1.7.1
requests               2.28.1
ruamel.yaml            0.17.21
ruamel.yaml.clib       0.2.6
setuptools             65.5.0
six                    1.16.0
sqlparse               0.4.4
toolz                  0.12.0
tqdm                   4.64.1
typing_extensions      4.6.3
tzdata                 2023.3
urllib3                1.26.13
virtualenv             20.23.0
wheel                  0.37.1
win-inet-pton          1.1.0
wincertstore           0.2
