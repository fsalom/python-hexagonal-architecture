# Ejemplo de proyecto con arquitectura hexagonal

## 🐍 1. Instalar `pyenv`

Si no lo tienes instalado:

```bash
brew update
brew install pyenv
```
Agrega esto a tu `~/.zshrc o ~/.bashrc`:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Después, recarga el terminal:

```bash
source ~/.zshrc
```

## 📦 2. Instalar una Versión de Python

```bash
pyenv install 3.11.9
```

Esto instalará Python en:

```bash
~/.pyenv/versions/3.11.9/bin/python
```

Puedes listar las versiones disponibles con:

```bash
pyenv versions
```

## 🧠 3. Seleccionar una Versión por Proyecto (opcional)

Para usar una versión específica en un proyecto:

```bash
cd /ruta/a/tu/proyecto
pyenv local 3.11.9
```

Esto crea un archivo .python-version que PyCharm también puede detectar.

## 💻 4. Configurar el Intérprete en PyCharm

### Opción 1: Usar Python Instalado con pyenv (global o local)

	1.	Abre tu proyecto en PyCharm
	2.	Ve a Preferences → Project: <tu-proyecto> → Python Interpreter
	3.	Haz clic en el icono de ⚙️ (rueda dentada) → Add...
	4.	Elige System Interpreter
	5.	En ... Browse, selecciona:
	
	~/.pyenv/versions/3.11.9/bin/python
	
	6.	Pulsa OK y espera a que PyCharm indexe el intérprete.

### Opción 2: Crear un Entorno Virtual en PyCharm basado en pyenv

  	1.	Ve a Preferences → Project: <tu-proyecto> → Python Interpreter
	2.	⚙️ → Add... → elige Virtualenv Environment
	3.	En Base interpreter, selecciona:

	~/.pyenv/versions/3.11.9/bin/python

	4.	PyCharm creará un entorno virtual y lo activará para tu proyecto.

