from flask import Flask
from config import get_config
from ext import init_extensions

def create_app(env=None):
    """
    Factory function para crear y configurar la aplicación Flask.

    Args:
        env (str, optional): Nombre del entorno de ejecución 
            ('development', 'testing', 'production'). 
            Si no se pasa, se toma de la variable de entorno FLASK_ENV.

    Returns:
        Flask: Instancia de la aplicación configurada.
    """
    app = Flask(__name__)
    app.config.from_object(get_config(env))

    # Inicializar extensiones
    init_extensions(app)

    # Registrar blueprints aquí
    # from src.blueprints.main import main_bp
    # app.register_blueprint(main_bp)

    return app
