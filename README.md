# Apollo 11 Simulator

## Table of contents
<!--ts-->

- [Apollo 11 Simulator](#apollo-11-simulator)
  - [Table of contents](#table-of-contents)
  - [Problem statement](#problem-statement)
  - [Directory layout](#directory-layout)
  - [Architecture](#architecture)
    - [Generator:](#generator)
    - [Reporter:](#reporter)
  - [Setup](#setup)
  - [Running the app](#running-the-app)
    - [Generator](#generator-1)
    - [Reporter](#reporter-1)
  - [Configuration](#configuration)
  - [Test](#test)
  - [About the authors](#about-the-authors)
    - [Erick Calderin:](#erick-calderin)
    - [Ana Arteaga Jimenez](#ana-arteaga-jimenez)
    - [Pablo Alarcón](#pablo-alarcón)
<!--te-->

## Problem statement
El propósito central de este proyecto es evaluar nuestras destrezas y competencias en Python, focalizándonos lo aprendido en los niveles 3 y 4 del Bootcamp.

Como estudiantes, nos enfrentamos al desafío emocionante de colaborar en cuatro proyectos visionarios de la NASA: OrbitOne, ColonyMoon, VacMars y GalaxyTwo. Conscientes de la importancia de evitar errores, estamos contribuyendo al desarrollo de un sistema de monitoreo que opera cada 20 segundos, permitiéndonos tener un control minucioso de los dispositivos empleados en cada misión.

Hemos sido convocados como ingenieros en jefe, y se nos ha asignado la tarea de crear el programa "APOLLO11-SIMULATOR". Este programa, operado manualmente por el comandante, desempeñará un papel crucial en el éxito de estas trascendentales iniciativas científicas y exploratorias. Nos sentimos honrados de ser parte de este proyecto significativo que contribuirá al avance de la exploración espacial y a la seguridad de los astronautas y turistas involucrados.

## Directory layout
```
.
├── apollo11_simulator          #Code
│   ├── config                  # Configuration files
│   └── models                  # Classes
│       ├── event_processing    # Generator classes
│       └── report_processing   # Reporter classes
├── images                      # Assets
├── input_data
└── tests                       # Tests
    └── test_data

9 directories

```


## Architecture

![Alt text](./images/classes_diagram.png)

El programa "APOLLO11-SIMULATOR" consta de dos componentes principales:

### Generator:
* Responsable de la simulación de datos entre componentes.
* Genera registros en archivos siguiendo especificaciones dadas.
* Utiliza la periodicidad de ejecución establecida.

### Reporter:
* Encargado de la generación de reportes y manejo de archivos.
* Analiza eventos, gestiona desconexiones, consolida misiones, calcula porcentajes y genera informes en un archivo plano.
* Proporciona informes estadísticos para la toma de decisiones.

## Setup
1. Instalar y configurar poetry de acuerdo a tu Sistema Operativo: https://python-poetry.org/docs/
2. Correr poetry shell para activar el ambiente
3. Correr poetry install para instalar dependencias

## Running the app
Se pueden ejecutar ambas partes, de manera independiente, de la siguiente forma:

### Generator
Ejecute el siguiente comando para iniciar la simulación de datos:

`python -m apollo11_simulator generate-events`

### Reporter
Ejecute el siguiente comando para generar reportes y realizar el manejo de eventos:

`python -m apollo11_simulator generate-report`

## Configuration

``` 
event_params:
  frequency_seconds: 2
  input_data_file: input_data/simulation.json
  devices_path: devices
  backup_path: backup
  range_of_files:
    min: 2
    max: 5
``` 

## Test
Para ejecutar los tests de la aplicación se debe ejecutar:

`pytest tests/`


## About the authors

### Erick Calderin:
Ingeniero de Sistemas, estudiante de maestría, con experiencia en desarrollo, apasionado a Python e Inteligencia Artificial.
LinkedIn:
https://www.linkedin.com/in/erick-calderin-5bb6963b/ 

### Ana Arteaga Jimenez
Administradora financiera, estudiante de inglés, experiencia en diferentes áreas administrativas, y coordinación de operaciones. Explorando el mundo de la programación.

### Pablo Alarcón
Publicista, Emprendedor y estudiante de Certified Tech Developer, con determinación para ser parte de la industria tecnologica como desarrollador BackEnd.
LinkedIn:
https://www.linkedin.com/in/pablo-alarcon-dev



