Funcionamiento de los endpoints de la api:

Primero debes tener iniciado el servidor de python con la api, si no lo has echo mira primero el README.md principal.

Una vez tengas el servidor iniciado utiliza la url: http://127.0.0.1:8000/ (en el caso de que no hayamos cambiado el puerto por defecto)

Esta api tiene las siguientes aplicaciones: 

 - categoria
    Los campos de categoria son: id y nombre

    Puedes utilizar un crud completo con la siguiente información:

    Para realizar un get de todas las categorias utilizaremos la ruta http://127.0.0.1:8000/categoria y utilizamos el 
    método http get, este endpoint te devolverá un array con todos los campos y una respuesta 302_FOUND

    Para realizar un get por id necesitas utilizar la url de antes además de /<id> escribiendo en <id> el id de la categoria que deseas,
    además utilizaremos el método get como antes.
    En este caso te peude devolver 2 respuestas un 404_NOT_FOUND en el caso de no encontrar la categoria y un 302_FOUND en el caso de que
    se encuentre además del json con los campos

    Para realizar un POST(creación) de una categoria basta con utilizar la ruta http://127.0.0.1:8000/categoria y el método POST.
    En este caso te devolverá un 201_CREATED en caso de que se guarde correctamente, en el caso de que no se cree te enviará un 400_BAD_REQUEST

    En el caso de que quieras eliminar una categoria utiliza http://127.0.0.1:8000/categoria/<id> con el método DELETE, en este caso también es 
    necesario especificar el id en <id>, este método te devolverá 202_ACCEPTED en caso de que se elimine y 404_NOT_FOUND en el caso de que 
    no se encuentre la categoria que has puesto



    

