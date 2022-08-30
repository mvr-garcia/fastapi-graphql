# Fastapi + GraphQl

This is an app that implements a GraphQl api to provide a modern way to query data from a server application.


## Requirements

To make the magic happen, you just need:

- Python 3.10

```bash
mkdir graphql-demo
cd graphql-demo
```

```bash
python -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

To start the server
```bash
uvicorn src.app:app --reload
```

Access the service in [http://localhost:8000/graphql](http://localhost:8000/graphql).

## Authors

Marcos Garcia
e-mail: mvrgarcia05@gmail.com
