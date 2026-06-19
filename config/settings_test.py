"""
Settings para tests: usa SQLite en memoria y deshabilita SSL.
Ejecutar con: python manage.py test --settings=config.settings_test
"""
from config.settings import *  # noqa

# Usar SQLite en memoria para tests (más rápido, sin necesitar PostgreSQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Deshabilitar migraciones en tests para mayor velocidad (opcional)
# Si se necesitan las migraciones reales, comentar estas líneas
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

# Descomentar para deshabilitar migraciones en tests:
# MIGRATION_MODULES = DisableMigrations()

# Desactivar logging durante tests
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "handlers": {
        "null": {
            "class": "logging.NullHandler",
        }
    },
    "root": {
        "handlers": ["null"],
        "level": "CRITICAL",
    },
}

# Usar hasher de contraseña más rápido en tests
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# SimpleJWT — reducir tiempos de expiración
from datetime import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
