# Autores

Lizeth Isaza y Cristina Salazar

Estudiantes de Bioingeniería
Universidad de Antioquia
Trabajo Unidad 4 Informática II — 2025-2

# Descripción del Proyecto

Biomonitor es una aplicación de escritorio desarrollada en Python utilizando PyQt5.
El sistema permite registrar pacientes, visualizar y simular signos vitales, calcular niveles de riesgo clínico, generar gráficos y exportar la información.

# Objetivos

* Implementar un sistema CRUD básico aplicado a la gestión clínica.
* Utilizar interfaces gráficas creadas con PyQt5 y Qt Designer.
* Modelar pacientes mediante Programación Orientada a Objetos.
* Integrar simulación de datos fisiológicos.
* Exportar información a archivos de texto.
* Generar gráficos de signos vitales usando matplotlib.

# Arquitectura del Proyecto

El proyecto sigue una organización tipo MVC simplificada:

ProyectoBiomonitor/
│
├── controller/
│     └── controlador.py
│
├── model/
│     └── paciente.py
│
├── view/
│     ├── ventana_principal.ui
│     ├── ventana_registro.ui
│     └── ventana_grafico.ui
│
├── main.py
└── README.md

# Dependencias

El proyecto utiliza:

Python 3.11
PyQt5
matplotlib

# Instalación:

pip install PyQt5 matplotlib

# Ejecución

Ejecutar la aplicación:

python main.py

# Funcionalidades
1. Registro de Pacientes

Permite ingresar:

* Nombre
* ID
* Edad
* BPM
* SpO2
* Temperatura

(Incluye validación de campos numéricos y obligatorios).

2. Tabla de Pacientes

Muestra:

* Nombre
* ID
* Riesgo

(El riesgo se calcula automáticamente con base en los signos vitales registrados).

3. Panel de Detalles

Al seleccionar un paciente se muestran sus datos actualizados:

* BPM
* SpO2
* Temperatura

Incluye un panel de color que indica el riesgo:

* Verde: Normal
* Naranja: Alerta
* Rojo: Crítico

4. Simulación de Signos Vitales

Genera valores aleatorios dentro de rangos fisiológicos y actualiza:

* BPM
* SpO2
* Temperatura
* Riesgo

5. Exportación a TXT

Genera automáticamente un archivo en la carpeta exports/ con:

* Datos del paciente
* Fecha y hora de exportación
* Riesgo calculado

Cada archivo tiene el formato:

pacientes_YYYY-MM-DD_HH-MM-SS.txt

6. Gráficos de Signos Vitales

Genera una ventana que muestra un gráfico de barras con:

* BPM
* SpO2
* Temperatura

Integrado mediante matplotlib.

# Lógica Interna del Paciente (POO)

La clase Paciente encapsula:

Nombre
ID
Edad
BPM
SpO2
Temperatura

* Criterios de riesgo:

Crítico: SpO2 < 90, BPM > 140, Temperatura > 39
Alerta: SpO2 < 94, BPM > 110, Temperatura > 38
Normal: valores dentro de rangos seguros

