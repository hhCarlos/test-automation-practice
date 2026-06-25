## Cómo correr el proyecto de Selenium + Python

Este proyecto usa **Python**, **pytest** y **Selenium** para ejecutar pruebas automatizadas en navegador.

Antes de correr las pruebas, necesitas activar un ambiente virtual de Python.

---

## 1. Entrar a la carpeta del proyecto

Desde la raíz del repositorio:

```bash
cd selenium-automation
```

---

## 2. Crear el ambiente virtual

Este paso solo se hace la primera vez.

```bash
python -m venv .venv
```

Esto crea una carpeta llamada:

```txt
.venv/
```

Ahí se instalarán las dependencias del proyecto sin afectar tu instalación global de Python.

---

## 3. Activar el ambiente virtual

### Mac / Linux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

Cuando el ambiente esté activo, deberías ver algo parecido a esto en tu terminal:

```bash
(.venv) selenium-automation
```

---

## 4. Instalar dependencias

Con el ambiente virtual activo, instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

---

## 5. Correr todas las pruebas

```bash
python -m pytest
```

---

## 6. Correr un archivo específico de pruebas

Por ejemplo, para correr solo las pruebas de Practice:

```bash
python -m pytest tests/practice/test_practice.py
```

Para correr solo las pruebas de Login:

```bash
python -m pytest tests/login/test_login.py
```

---

## 7. Correr las pruebas en modo headless

El modo headless ejecuta las pruebas sin abrir visualmente el navegador.

### Mac / Linux

```bash
HEADLESS=true python -m pytest
```

### Windows PowerShell

```powershell
$env:HEADLESS="true"
python -m pytest
```

### Windows CMD

```cmd
set HEADLESS=true
python -m pytest
```

---

## 8. Desactivar el ambiente virtual

Cuando termines de trabajar:

```bash
deactivate
```

---

## Flujo rápido recomendado

Si ya habías creado el ambiente virtual antes, normalmente solo necesitas:

```bash
cd selenium-automation
source .venv/bin/activate
python -m pytest
```

En Windows PowerShell:

```powershell
cd selenium-automation
.venv\Scripts\Activate.ps1
python -m pytest
```

---

## Problemas comunes

### Error: `ModuleNotFoundError: No module named 'support'`

Asegúrate de estar corriendo los tests desde la carpeta:

```txt
selenium-automation/
```

También revisa que el archivo `pytest.ini` tenga esta configuración:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
pythonpath = .
```

La carpeta `support/` debe estar al mismo nivel que `tests/`:

```txt
selenium-automation/
  tests/
  support/
  pytest.ini
  conftest.py
```

No debe estar dentro de `tests/`.

---

### Error: no encuentra `pytest` o `selenium`

Activa el ambiente virtual e instala dependencias:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

---

### Quiero actualizar el archivo `requirements.txt`

Si instalaste una nueva dependencia, actualiza el archivo así:

```bash
python -m pip freeze > requirements.txt
```

---

## Notas importantes

* `pytest` es quien descubre y ejecuta las pruebas.
* Selenium controla el navegador.
* Los archivos de prueba deben iniciar con `test_`.
* Las funciones de prueba también deben iniciar con `test_`.

Ejemplo válido:

```txt
tests/login/test_login.py
```

```py
def test_should_login_successfully_with_valid_credentials(driver):
    ...
```
