# Arrancar proyecto flask

## Paso 1

Debes tener inicializado el entorno virtual de python

```sh
py -m venv env
```

## Paso 2

Debes arrancar el entorno virtual, esto se hace de la siguiente manera, estando en el cmd como administrador

```sh
cd env
cd Script
activate
cd ..
cd ..
```

## Paso 3

Debes de descargar las dependencias del proyecto, esto se hace de la siguiente manera

```sh
pip install -r requirements.txt
```

## Paso 4

Debes abrir el cmd en modo administrador y escribir lo siguiente

```sh
set FLASK_APP=app\
set FLASK_DEBUG=1
set FLASK_ENV=development
flask run
```

## Paso 5

Iniciar el servidor alojado localmente con la ruta **http://127.0.0.1:5000**