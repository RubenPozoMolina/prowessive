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
export FLASK_APP=app
export FLASK_DEBUG=0
cd prowessive
flask run 
```

## Build and run docker image
```bash
docker build . -t prowessive:development
docker run -d -p 8000:8000 prowessive:development
```
Now you can access to the main page: 
[http://localhost:8000] (http://localhost:8000)

## Testing
To execute tests is mandatory to install chrome and chrome driver:
```bash
sudo ./scripts/install-chrome.sh
sudo ./scripts/install-chromedriver.sh
```
Prepare environment:
```bash
docker-compose up
```

Execute tests:
```bash
pytest -s
```



