"""
ext.py
Módulo para integrar y centralizar extensiones de Flask.
- Permite importar todas las extensiones desde un solo lugar.
- Facilita la inicialización en la aplicación principal.
- Se pueden agregar futuras extensiones sin modificar el código base.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Instancias de extensiones (aún no inicializadas)
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

# Hook para inicializar todas las extensiones en la app
def init_extensions(app):
    """
    Inicializa todas las extensiones con la aplicación Flask.
    - app: instancia de Flask
    """
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
