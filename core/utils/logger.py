import logging
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler
import os

# O logger vai coletar informaççoes e enviar para sqlite

def log_command(command: str, client_id: str):
    ...

def log_auth_event(event: str, token: str):
    ...

def log_client(event: str, client: str):
    ...

def setup_logger(name: str, log_table: str, level=logging.INFO) -> logging.Logger:
    ...