import os
from pathlib import Path

# BASE_DIR: raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
# Carpeta instance/ para datos locales y configuraciones fuera de control de versiones
INSTANCE_DIR = BASE_DIR / "instance"

def _sqlite_uri(filename: str) -> str:
    """Construye la URI de SQLite dentro de la carpeta instance/."""
    return f"sqlite:///{INSTANCE_DIR / filename}"

class BaseConfig:
    # Se corrige el typo: ahora SECRET_KEY
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    JSON_SORT_KEYS = False  # Mantener orden en respuestas JSON
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Si se usa SQLAlchemy

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", _sqlite_uri("dev.sqlite3")
    )

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", _sqlite_uri("prod.sqlite3")  # corregido: solo nombre de archivo
    )

# Hook para cargar configuración según entorno
def get_config(env: str = None):
    """
    Devuelve la clase de configuración según el entorno.
    - env: puede ser 'development', 'testing', 'production'.
    - Si no se pasa, se toma de la variable de entorno FLASK_ENV.
    """
    env = env or os.environ.get("FLASK_ENV", "development").lower()
    mapping = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
    return mapping.get(env, DevelopmentConfig)
