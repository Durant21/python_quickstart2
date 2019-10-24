import flask

from infrastructure.view_modifiers import response
import services.document_service as document_service

blueprint = flask.Blueprint('documents', __name__, template_folder='templates')


@blueprint.route('/documents')
@response(template_file='/documents/index.html')
def index():
    doc_packages = document_service.get_all_documents()
    return {'documents': doc_packages}
    # return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/documents/about')
@response(template_file='documents/about.html')
def about():
    return {}
