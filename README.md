# ITMO Programming Winter School 2021

Este servicio está diseñado para trabajar con cualquier proveedor de servicio en la nube. Para esta documentación únicamente describiremos los pasos para ejecutar y desplegar el servicio desde GCP.
 

## Comenzando 🚀

Este proyecto

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

Requieres de tener una instalada una versión de Python3

### Instalación 🔧

Deberás instalar los siguientes paquetes introduciendo cada comando en la consola:
```
sudo apt install python3 python3-dev python3-venv
sudo apt install wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```

Una vez terminando con la configuración anterior iniciaremos con la descarga de los archivos del repositorio. Ejecuta el siguiente comando en la terminal:
```
git clone CHECK THIS
```

Esto te creara una carpeta y podrás iniciar con el despliegue o las pruebas locales.

## Ejecutando las pruebas en servidor local ⚙️

_Ahora ejecutaremos los siguientes comandos para tener un entorno de desarrollo ejecutandose desde la consola._
Tendremos que ingresar a la carpeta que se creó tras descargar el repositorio.
```
cd sso-service
```

_Si queremos iniciar el servicio de forma local deberemos ejecutar:_

```
python3 -m venv venv
source venv/bin/activate
```
_Una vez hayamos ejecutado los comandos anteriores para generar el ambiente de ejecución deberemos instalar los requisitos para el servicio:_
```
sudo pip install -r requirements.txt
```

_Por último bastará con ejecutar:_
```
sudo python3 app.py
```
_Esto hará que nuestro servicio se ejecute en localhost. Y nos mostrará el siguiente mensaje en la consola:_
```
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

_Deberemos abrir otra pestaña de la consola y tendremos que enviar las peticiones ejecutando el siguiente comando para probar el servicio._
```
curl --header "Content-Type: application/json" --request POST --data '{<json-data>}' http://0.0.0.0:8080/<function-path>
```

Mira [Service Documentation](https://documenter.getpostman.com/view/10987523/TVetcRcV) para conocer como hacer las peticiones al servicio.

## Despliegue 📦

Una vez teniendo el repositorio en la carpeta del proyecto "sso-service" bastará con ejecutar los siguientes comandos en la consola:

 ```
gcloud builds submit --tag gcr.io/<project-id>/dnaservice
```
_Para encontrar el project ID deberás ingresar a la información de de tu proyecto desde el dashboard de google console.
Mira [GService Documentation](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) para conocer en dónde encontrar esta información._

Puede que tras ejecutar el comando anterior se te muestre un mensaje como este:

![gAuth permission](https://lh5.googleusercontent.com/pcQr7q-YanHZVA7-kBJu8W-Yk0A51dMQvLvFbPtdM8_N2nL0lAXUZr8hVhOqGUxi-bMzqVGHA76rjmlWyLmj=w1600-h756-rw)

O que en la consola se te muestre algo como:
```
API [cloudbuild.googleapis.com] not enabled on project [<#Project>].
 Would you like to enable and retry (this will take a few minutes)?
(y/N)?
```
Dependiendo del caso presiona Autorizar o ingresa "y" para continuar.

Después de haber ejecutado el comando anterior deberás iniciar con el despliegue ejecutando:

```
gcloud run deploy --image gcr.io/<project-id>/dnaservice --platform managed
```

Tras ejecutar el comando anterior se te pedira que ingreses el nombre del servicio en la consola:

```
Service name (dnaservice): 
```

Puedes ingresar el mismo nombre de "sso-service" o cambiarlo. Tras haber elegido un nombre presiona enter para continuar

Tras ejecutar el comando te parecerán algunas opciones en la consola. Te recomendamos elegir una dependiendo de la cercanía a la que te encuentres del centro de datos de Google:
```
Please specify a region:
 [1] asia-east1
 [2] asia-east2
 [3] asia-northeast1
 [4] asia-northeast2
 [5] asia-northeast3
 [6] asia-south1
 [7] asia-southeast1
 [8] asia-southeast2
 [9] australia-southeast1
 [10] europe-north1
 [11] europe-west1
 [12] europe-west2
 [13] europe-west3
 [14] europe-west4
 [15] europe-west6
 [16] northamerica-northeast1
 [17] southamerica-east1
 [18] us-central1
 [19] us-east1
 [20] us-east4
 [21] us-west1
 [22] cancel
Please enter your numeric choice: 
```

Si te encuentras en México probablemente te convenga elegir la opción "18". Debes ingresar la opción deseada y presionar enter para continuar

```
Please enter your numeric choice:  18
```

Tras finalizar esta configuración te deberá aparecer el siguiente mensaje:

```
Deploying container to Cloud Run service [<service-name>] in project [<project-id>] region [us-central1]
✓ Deploying... Done.                                                           
  ✓ Creating Revision...                    
  ✓ Routing traffic...
Done.
Service [<service-name>] revision [<revision-id>] has been deployed and is serving 100 percent of traffic.
Service URL: https://<service-url>
```

El Service URL es el que ocuparemos para realizar las pruebas end-to-end de la siguiente fase.

### Analice las pruebas end-to-end 🔩

_Las pruebas se analizaron para cada elemento de funcionalidad devolviendo resultados exitosos de conexión entre el resto de servicios_

Mira [Service Documentation](https://documenter.getpostman.com/view/10987523/TVetcRcV) para ejecutar pruebas al servicio.

**Los URL de las pruebas se deben modificar dependiendo de en donde se encuentre el servicio** 

### Y las pruebas de estilo de codificación ⌨️

Velocidad y confiabilidad

La prueba al endpoint _mutation_ se ejecutan enviando una petición por un método POST. Encapsulando los parametros dentro del body de un json a un URL similar a este:
 
```
https://<api-url>/<function>
```
Mira [Service Documentation](https://documenter.getpostman.com/view/10987523/TVetcRcV) para visualizar nuestras pruebas en nuestro servicio.

**El URL puede cambiar dependiendo de en donde se encuentre el servicio** 

## Construido con 🛠️

_Las herramientas usadas para crear este proyecto_

* [Pycharm](https://www.jetbrains.com/es-es/pycharm/) - El IDE utilizado
* [Python3](https://docs.python.org/3/) - El lenguaje usado
* [Git](https://git-scm.com/doc) - Usado para manejar el versionamiento

También puedes mirar la lista de todos los [requisitos](requirements.txt) de este proyecto.

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Autores ✒️

_Este proyecto fue creado desde sus inicios por:_

* **Yoltic Cervantes Galeana** - *Análisis, Codificación y Documentación* - [YOZTiK](https://github.com/YOZTiK)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/YOZTiK/sso-service/contributors) quíenes han participado en este proyecto. 

---
⌨️ con ❤️ por [YOZTiK](https://github.com/YOZTiK) 😊
