import os
from os.path import dirname, join
import sys

from dotenv import load_dotenv

ROOT_DIR = dirname(dirname(__file__))
sys.path.append(str(ROOT_DIR))

dotenv_path = join(ROOT_DIR, ".env")
load_dotenv(dotenv_path)

MICROSOFT_TOKEN_URL = os.environ.get("MICROSOFT_TOKEN_URL")
MICROSOFT_TOKEN_GRANT_TYPE = os.environ.get("MICROSOFT_TOKEN_GRANT_TYPE")
MICROSOFT_TOKEN_SCOPE = os.environ.get("MICROSOFT_TOKEN_SCOPE")
MICROSOFT_CLIENT_ID = os.environ.get("MICROSOFT_CLIENT_ID")
MICROSOFT_CLIENT_SECRET = os.environ.get("MICROSOFT_CLIENT_SECRET")
JOURNEY_SERVICE_BASE_URL = os.environ.get("JOURNEY_SERVICE_BASE_URL")
MILE_TO_METER = 1609
