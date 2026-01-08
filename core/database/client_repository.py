import json
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

from .connection import DatabaseConnection, get_db


class ClientRepository:
    ...