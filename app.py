from flask import Flask

# API Controllers
from controller.api.document_controller import document_controller
from controller.api.qa_controller import qa_controller
from conf_environment.constant import default_files_dir_created

default_files_dir_created()
app = Flask(__name__)

# Register Blueprint
app.register_blueprint(document_controller, url_prefix='/api/v1/document/')
app.register_blueprint(qa_controller, url_prefix='/api/v1/qa/')

app.secret_key = 'flaskragsecurekey'


# default_files_dir_created()
@app.route('/')
def home():  # put application's code here
    return 'Welcome to the Flask RAG-based Application'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
