# ExchangesApi
Projeto Django que captura dados de Exchanges, como orderbooks e gera relatórios com eles.


## Instalando Python
Sendo um framework Web Python, Django requer Python. Veja Qual versão do Python eu posso usar com Django? para detalhes. Python inclui um banco de dados leve chamado SQLite então você não precisa configurar um banco de dados agora.

Obtenha a última versão do Python em https://www.python.org/downloads/ ou no gerenciador de pacotes do seu sistema operacional.

Você pode verificar se o Python está instalado digitando **python** no shell, você deve ver algo como:

```
Python 3.x.y
[GCC 4.x] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Instale as ferramentas python:
```
sudo apt-get install python3-dev python3-pip
sudo pip3 install --upgrade pip
sudo pip3 install virtualenv
```

### Configure o wrapper do ambiente virtual. Abra o terminal na pasta raíz do projeto e digite:
```
virtualenv --system-site-packages venv -p /usr/bin/python3
```

### Instale as bibliotecas necessarias:
```
sudo apt-get install libpq-dev python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev
```

### Ative o ambiente virtual:
```
source venv/bin/activate
```

### Instale os requisitos (na pasta raíz do projeto):
```
pip install -r requirements.txt
```

### Realize migrações pendentes (na pasta raíz do projeto):
```
python manage.py migrate
```

### Para rodar o servidor :
```
python manage.py runserver
```
