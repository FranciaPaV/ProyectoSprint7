# 📊 ProyectoSprint7
## 🎯 Resumen del Proyecto: Aplicación Web para Visualización de Anuncios de Coches

---
### Objetivo:

El proyecto consiste en desarrollar una aplicación web interactiva para visualizar datos de anuncios de venta de coches. La aplicación permite explorar visualmente el conjunto de datos mediante gráficos como histogramas y diagramas de dispersión, facilitando el análisis exploratorio básico a través de una interfaz sencilla e intuitiva.

---
### Tecnologías y herramientas 🐍 
- Python: Lenguaje de programación principal.
- Pandas: Para manipulación y carga de datos CSV.
- Plotly Express: Para crear gráficos interactivos como histogramas y scatter plots.
- Streamlit: Framework para construir la interfaz web y controlar la interacción con el usuario.
- Git & GitHub: Control de versiones y alojamiento del código.
- Render.com: Plataforma para desplegar la aplicación web de manera pública.

---
### Estructura del proyecto 🚀 
* vehicles_us.csv: Archivo CSV con datos de anuncios de coches.
* notebooks/EDA.ipynb: Notebook para el análisis exploratorio de datos con gráficos creados con plotly-express.
* app.py: Archivo principal con la aplicación web creada con Streamlit. Contiene botones/casillas para construir gráficos interactivos basados en el dataset.
* requirements.txt: Archivo que lista las dependencias necesarias (pandas, plotly_express, streamlit).
* README.md: Documentación con instrucciones, descripción del proyecto y pasos para correr la aplicación.

---
### Funcionalidades principales 📌
* Visualización de histogramas sobre la columna "odometer" (kilometraje) de los coches.
* Visualización de diagramas de dispersión para comparar precio y año/modelo de los vehículos.
* Interactividad mediante botones o casillas de verificación para seleccionar qué gráfico mostrar.
* Aplicación desplegada en Render.com para acceso web público.

---
### Proceso y aprendizajes ✅ 
* `Creación y configuración de un entorno virtual en Python para gestionar dependencias.`
* `Uso de VS Code para desarrollo y ejecución local de la aplicación.`
* `Uso básico de Git y GitHub para control de versiones y colaboración.`
* `Desarrollo incremental: desde análisis exploratorio en Jupyter Notebook hasta la implementación final de la app web.`
* `Despliegue en un entorno en la nube (Render) para hacer la aplicación accesible públicamente.`
