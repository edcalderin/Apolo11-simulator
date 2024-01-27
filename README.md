# Apollo 11 Simulator

## Table of contents
<!--ts-->

* [Problem statement](#problem-statement)
* [Directory layout](#directory-layout)
* [Architecture](#architecture)
* [Setup](#setup)
* [Running the app](#running-the-app)
    * [Generator](#generator)
    * [Reporter](#reporter)
* [Checkpoints](#checkpoints)
* [About the authors](#about-the-authors)
* [References](#references)
<!--te-->

## Problem statement
El propósito central de este proyecto es evaluar nuestras destrezas y competencias en Python, focalizándonos lo aprendido en los niveles 3 y 4 del Bootcamp.

Como estudiantes, nos enfrentamos al desafío emocionante de colaborar en cuatro proyectos visionarios de la NASA: OrbitOne, ColonyMoon, VacMars y GalaxyTwo. Conscientes de la importancia de evitar errores, estamos contribuyendo al desarrollo de un sistema de monitoreo que opera cada 20 segundos, permitiéndonos tener un control minucioso de los dispositivos empleados en cada misión.

Hemos sido convocados como ingenieros en jefe, y se nos ha asignado la tarea de crear el programa "Apolo-11". Este programa, operado manualmente por el comandante, desempeñará un papel crucial en el éxito de estas trascendentales iniciativas científicas y exploratorias. Nos sentimos honrados de ser parte de este proyecto significativo que contribuirá al avance de la exploración espacial y a la seguridad de los astronautas y turistas involucrados.

## Directory layout
```
.
├── images              # Assets
├── apollo11_simulator  # Code
│   ├── config          # Configuration files
│   └── models          # Classes
│       ├── generator   # Generator classes
│       └── reporter    # Reporter classes
└── tests               # Tests

7 directories
```

## Architecture

![Alt text](./images/classes_diagram.png)

El programa "Apolo-11" consta de dos componentes principales:

### Generator:
* Responsable de la simulación de datos entre componentes.
* Genera registros en archivos siguiendo especificaciones dadas.
* Utiliza la periodicidad de ejecución establecida.

### Reporter:
* Encargado de la generación de reportes y manejo de archivos.
* Analiza eventos, gestiona desconexiones, consolida misiones, calcula porcentajes y genera informes.
* Proporciona informes estadísticos para la toma de decisiones.

## Setup
Steps to reproduce this project

1. Step 1
2. Step 2
3. Step 3

## Running the app
El programa "APOLLO11-SIMULATOR" consta de dos partes principales que se ejecutan de manera independiente.

### Generator
Ejecute el siguiente comando para iniciar la simulación de datos:

python -m apollo11_simulator generate_events

### Reporter
Ejecute el siguiente comando para generar reportes y realizar el manejo de archivos:

python -m apollo11_simulator generate-report

## Checkpoints
- [x] Problem description
- [x] Inheritance
- [x] Class methods
- [x] File managements
- [x] Logging
- [x] Other
- [ ] Tests
- [ ] Other

## About the authors

### Erick
Text here

### Ana
Text here

### Pablo
Text here



## References
* Reference 1
* Reference 2
* Reference n


