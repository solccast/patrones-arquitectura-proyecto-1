from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    config_db(app)

def config_db(app):
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

def reset_db():
    try:
        print("Eliminando BD...")
        db.drop_all()
        print("Creando BD...")
        db.create_all()
        print("Listo...")
    except Exception as e:
        print(f"Error al resetear la base de datos: {e}")
