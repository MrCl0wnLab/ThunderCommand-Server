# Conexão e schema do banco
from datetime import datetime
import os
import sqlite3
from contextlib import contextmanager
from typing import List, Dict, Any, Union, Tuple, Optional


DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'thunder_command_database.db')

class DatabaseConnection:
    ...

@contextmanager
def get_db():
    ...


def init_db():
    ...