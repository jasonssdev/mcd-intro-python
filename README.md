# MCD - Introduction to Programming in Python

> Master's program - Pontificia Universidad Católica de Chile (Coursera)

[![Tests](https://github.com/jasonssdev/mcd-intro-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/jasonssdev/mcd-intro-python/actions)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Conda Environment](https://img.shields.io/badge/environment-conda-green?logo=anaconda)](environment.yml)

---

## 🏠 Module 1

Welcome to **Week 1** of the course. In this first module, we focus on fundamental programming concepts using Python, including writing functions, unit testing, and professional project structure.

### 🌐 Module Objectives

- Identify key course resources: introductory video, discussion forum, and syllabus.
- Install and configure Python locally.
- Use Coursera to complete simple Python exercises.
- Define and work with `list` and `tuple` structures and their operations/methods.
- Interpret various code solutions using sequential structures.
- Write functions to solve problems involving multiple values.

---

## 📁 Project Structure

```
mcd-intro-python/
├── data/                   # Data files (if applicable)
├── notebooks/             # Jupyter Notebooks
│   └── w1_jss_sumativa1.ipynb
├── src/                   # Source code
│   └── w1_activity.py
├── tests/                 # Unit tests with pytest
│   └── test_w1_activity.py
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