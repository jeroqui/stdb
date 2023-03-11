import os
from dotenv import load_dotenv

load_dotenv()

if os.environ.get("ENV_NAME") == 'Production':
    from .production import *
else:
    from .local import *
