
import json
import time
from flask import Flask, Response, jsonify, request, render_template, send_from_directory, session, redirect, url_for
from werkzeug.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from functools import wraps
import os
import uuid
import mimetypes
from core.utils.logger import app_logger, command_logger, auth_logger, log_command, log_auth_event
from core.database import init_db, ClientRepository, CommandRepository
from collections import deque



# Error handler for custom exceptions
def handle_error(error):
    response = jsonify({
        "success": False,
        "error": error.message if hasattr(error, 'message') else str(error),
        "status": error.status_code if hasattr(error, 'status_code') else 500
    })
    response.status_code = error.status_code if hasattr(error, 'status_code') else 500
    app_logger.error(f"Error occurred: {error}")
    return response




# Configuração para compatibilidade Windows com MIME types
mimetypes.add_type('application/javascript', '.js')

# Inicialização e configuração do aplicativo Flask
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'teste1234')
app.register_error_handler(Exception, handle_error)



@app.route('/admin/clients')
def get_clients():
    ...