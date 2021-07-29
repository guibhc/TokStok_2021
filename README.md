# 1. Setup ambiente de desenvolvimento
python -m venv venv

# 2. Instalando bibliotecas necessarias
venv\scripts\activate.bat
pip install selenium

# 3. Download da versão mais recente do ChromeDriver
https://sites.google.com/chromium.org/driver/downloads
A utilizada na data é a versão 92.0.4515.43(https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.43/)

# 3. Rodando a utility
venv\scripts\activate.bat
python scrap.py


# Pokemon
## 1. Instalando bibliotecas necessarias
venv\scripts\activate.bat
pip install requests

## 2. Rodando
venv\scripts\activate.bat
python scrap_pokemon.py