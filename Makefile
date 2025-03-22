# Ejecutar todos los tests con cobertura
test:
	PYTHONPATH=src pytest --cov=src --cov-report=term-missing

# Generar reporte HTML de cobertura
coverage-html:
	PYTHONPATH=src pytest --cov=src --cov-report=html
	open htmlcov/index.html

# Limpiar archivos de reporte de cobertura
clean:
	rm -rf htmlcov .pytest_cache .coverage