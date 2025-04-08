# MCD - Introduction to Programming in Python

> Master's program - Pontificia Universidad Católica de Chile (Coursera)

[![Tests](https://github.com/jasonssdev/mcd-intro-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/jasonssdev/mcd-intro-python/actions)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Conda Environment](https://img.shields.io/badge/environment-conda-green?logo=anaconda)](environment.yml)

---

## 🏠 Week 1

* Identificar los recursos generales del curso: Video de introducción, Foro de presentación y Syllabus con la información general del curso.
* Completar la instalación y configuración de Python en el computador propio.
* Emplear Coursera para resolver ejercicios simples empleando Python.
* Definir la estructura secuencial lista y sus operaciones y métodos que pueden ocuparse en Python.
* Interpretar diferentes soluciones de código que usan tuplas para resolver problemas con múltiples datos.
* Definir la estructura secuencial tupla y sus operaciones y métodos que pueden ocuparse en Python
* Desarrollar soluciones de código a problemas con varios datos, usando tuplas y listas.

## Week 2

* Distinguir qué es una lista de listas y cómo acceder a cada elemento.
* Modelar datos que tienen varias dimensiones, en una representación que utilice listas de listas.
* Demostrar cómo recorrer una lista de listas
* Descubrir mecanismos de resolución de problemas con datos en varias dimensiones, empleando listas de listas.
* Interpretar diferentes soluciones de código que usan listas de listas para resolver problemas.
* Desarrollar un algoritmo para resolver un problema concreto que utiliza datos en varias dimensiones, utilizando listas de listas.
* Proponer estrategias de solución para resolver problemas en Python usando listas de listas.

## Week 3

* Distinguir qué es un stack y una queue, qué aplicaciones reales tienen, y cómo se implementan en Python
* Aplicar el concepto y operaciones de tipos de datos secuenciales para construir soluciones computacionales.
* Desarrollar soluciones de código a problemas de stacks y queues.
* Modelar la resolución de problemas en que los datos tienen un comportamiento tipo LIFO, usando stacks.
* Modelar la resolución de problemas en que los datos tienen un comportamiento tipo FIFO, usando queues.
* Comparar diferentes soluciones de código que usan stacks y queues para resolver problemas.
* Desarrollar soluciones de código a problemas utilizando estructuras de datos secuenciales stacks y queues.

## Week 4

* Aplicar el concepto y operaciones de tipos de datos no secuenciales para construir soluciones computacionales.
* Describir qué es un set y un diccionario en Python, qué aplicaciones reales tienen, y cómo se usan.
* Desarrollar una solución a un problema concreto que requiere guardar datos de forma no secuencial, utilizando sets y/o diccionarios.
* Describir qué es un set en Python, qué aplicaciones reales tiene, y cómo se usa.
* Modelar la resolución de problemas que requieren guardar datos de forma no secuencial, utilizando sets en Python.
* Describir qué es un diccionario en Python, qué aplicaciones reales tiene, y cómo se usa.
* Modelar la resolución de problemas que requieren guardar datos de forma no secuencial, utilizando Diccionarios en Python.
* Comparar diferentes soluciones de código que usan sets y diccionarios para resolver problemas.

---

## 📁 Project Structure

```
mcd-intro-python/
├── data/                   # Data files (if applicable)
├── notebooks/             # Jupyter Notebooks
│   └── w1_jss_sumativa1.ipynb
│   └── ...
├── src/                   # Source code
│   └── w1_activity.py
│   └── ...
├── tests/                 # Unit tests with pytest
│   └── test_w1_activity.py
│   └── ...
├── .github/workflows/     # GitHub Actions workflows
│   └── python-tests.yml
├── .vscode/               # VS Code configuration
│   └── settings.json
├── .env                   # Environment variables
├── environment.yml        # Conda environment file
├── Makefile               # Automation commands
├── pytest.ini             # Pytest configuration
└── README.md
```

---

## 🚀 Quick Start

### 🔄 Clone the repository

```bash
git clone https://github.com/jasonssdev/mcd-intro-python.git
cd mcd-intro-python
```

### 🛠️ Create and activate Conda environment

```bash
conda env create -f environment.yml
conda activate mcd-intro-python
```

---

## 🧪 Run Tests

```bash
make test
```

Or manually:

```bash
PYTHONPATH=src pytest --cov=src --cov-report=term-missing
```

### 📊 View HTML coverage report

```bash
make coverage-html
```
This will open `htmlcov/index.html` in your browser.

### 🛋️ Clean temporary test files

```bash
make clean
```

---

## ✨ GitHub Actions CI

This project runs tests automatically on every `push` and `pull request` to the `main` branch using [GitHub Actions](https://github.com/features/actions).  
You can check the build status in the [Actions tab](https://github.com/jasonssdev/mcd-intro-python/actions).

---

## 🧑‍💻 Author

**Jason**  
[GitHub: @jasonssdev](https://github.com/jasonssdev)  
Panama 🇵🇦

---

## 📄 License

[Apache 2.0 License](LICENSE)