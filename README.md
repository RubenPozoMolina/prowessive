# prowessive
RAD for pwa

## Prepare virtual environment

```bash 
python3 -m venv venv
source venv/bin/activate
pip install --editable ".[dev]"
```

## Execute from command line for development purposes:
```bash
export FLASK_APP=prowessive
export FLASK_DEBUG=0
cd prowessive
flask run 
```

## Build and run docker image
```bash
docker build . -t prowessive:development
docker run -p 8080:8080 prowessive:development
```

