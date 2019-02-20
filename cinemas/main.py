from app import app
from cinemas.blueprint import cinemas
import view

app.register_blueprint(cinemas, url_prefix='/stereolife')



if __name__ == '__main__':
    app.run()