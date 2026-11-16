# GamePerfAnalyzer


### Ambiente virtual

```
python -m venv .venv
```

### Ative o ambiente virtual:

```
.venv\Scripts\activate
```


### Instale as dependências:

```
pip install -r requirements.txt
```

### Execute a API:

```
uvicorn app.main:app --reload --port 8000
```

### Consultar endpoint

```
http://127.0.0.1:8000/api/devices
```

```
http://127.0.0.1:8000/api/devices/current
```
