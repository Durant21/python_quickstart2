import flask

from infrastructure.view_modifiers import response
import services.document_service as document_service
from viewmodels.account.index_viewmodel import IndexViewModel

from viewmodels.documents.document_viewmodel import DocumentViewModel

blueprint = flask.Blueprint('documents', __name__, template_folder='templates')


@blueprint.route('/documents')
@response(template_file='/documents/index.html')
def index():
    # vm = IndexViewModel()
    vm = DocumentViewModel()
    if not vm.user:
        return flask.redirect('/account/login')

    # doc_packages = document_service.get_all_documents()
    # return {'documents': doc_packages}
    # return flask.render_template('home/index.html', packages=test_packages)
    return vm.to_dict()


@blueprint.route('/documents/create_document')
@response(template_file='/documents/new_document.html')
def get_new_doc_form():
    # vm = LoginViewModel()
    # return vm.to_dict()
    return {}


@blueprint.route('/documents/create_document', methods=['POST'])
@response(template_file='/documents/edit_document.html')
def create_the_doc():
    vm = DocumentViewModel()
    # return vm.to_dict()

    doc = document_service.create_document(vm.doc_name)

    return doc.to_dict()

@blueprint.route('/documents', methods=['POST'])
@response(template_file='/documents/new_document.html')
def new_doc():
    # vm = LoginViewModel()
    # return vm.to_dict()
    return {}


@blueprint.route('/documents/new_document', methods=['POST'])
@response(template_file='/documents/edit_document.html')
def create_doc():
    vm = DocumentViewModel()
    # return vm.to_dict()

    doc = document_service.create_document(vm.doc_name)

    return {}


@blueprint.route('/documents/edit_document', methods=['POST'])
@response(template_file='/documents/edit_document.html')
# def edit_doc():
    # vm = LoginViewModel()
def save_to_edit():
    # return vm.to_dict()
    vm = DocumentViewModel()
    # return vm.to_dict()

    doc = document_service.create_document(vm.doc_name)
    return doc.to_dict()


@blueprint.route('/documents/save_document', methods=['POST'])
@response(template_file='/documents/save_document.html')
def save_doc():
    # vm = LoginViewModel()
    # return vm.to_dict()
    return {}


@blueprint.route('/documents/about_document', methods=['POST'])
@response(template_file='/documents/about_document.html')
def save_to_about():
    vm = DocumentViewModel()
    # return vm.to_dict()

    # TODO  create an edit method for documents

    doc = document_service.get_document_by_name(doc_name='35')
    return doc.to_dict()