import os
import pytest
import requests
from waiting import wait
from tests.helpers.config_utils import cfg


def is_server_working():
    return_value = False
    url = cfg['host']
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return_value = True
    except Exception as e:
        print("Error connecting to service:", str(e))
    return return_value


def pytest_configure():
    wait(lambda: is_server_working(), timeout_seconds=cfg['timeout'], waiting_for="Server working")


@pytest.fixture(scope="session", autouse=True)
def environment():
    env = os.getenv('ENVIRONMENT', 'local')
    yield env


@pytest.fixture(scope="session", autouse=True)
def configuration(environment):
    os.environ['DB_HOST'] = cfg['database']['db_host']
    os.environ['DB_PORT'] = str(cfg['database']['db_port'])
    os.environ['DB_NAME'] = cfg['database']['db_name']
    os.environ['DB_USER'] = cfg['database']['db_user']
    os.environ['DB_PASSWORD'] = cfg['database']['db_password']
    yield cfg
