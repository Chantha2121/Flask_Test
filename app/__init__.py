from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def index():
        return 'Hello'
    
    ## Admin routes
    from app.blueprints.admin import admin_bp
    app.register_blueprint(admin_bp)

    ## Auth routes
    from app.blueprints.auth import auth_db
    app.register_blueprint(auth_db)
    
    return app
    

    