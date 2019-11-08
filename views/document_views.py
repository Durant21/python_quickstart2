import flask, requests
from flask import request
from DAL.Sections import DAL_Sections
from DAL.Groups import DAL_Groups
from DAL.Documents import DAL_Documents
from BLL.Documents import BLL_Documents
from BLL.Sections import BLL_Sections
from infrastructure.view_modifiers import response
import services.document_service as document_service
from viewmodels.account.index_viewmodel import IndexViewModel
# import viewmodels.documents.create_section_viewodel as CreateSectionViewModel
import services.section_service as section_service
import services.group_service as group_service
from viewmodels.documents.document_viewmodel import DocumentViewModel
from viewmodels.documents.create_section_viewodel import CreateSectionViewModel

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


@blueprint.route('/documents/add_content', methods=['POST'])
@response(template_file='/documents/add_content.html')
# def edit_doc():
    # vm = LoginViewModel()
def add_content():
    doc_id = request.form.get('doc_id')
    doc_name = request.form.get('doc_name')
    # vm = DocumentViewModel()
    # # return vm.to_dict()
    #
    # doc = document_service.create_document(vm.doc_name)
    # return doc.to_dict()
    return {'doc_id': doc_id,'doc_name': doc_name}


@blueprint.route('/documents/save_document', methods=['POST'])
@response(template_file='/documents/save_document.html')
def save_doc():
    # vm = LoginViewModel()
    # return vm.to_dict()

    # collect the doc_id from Form
    doc_id = request.form.get('doc_id')
    section_data = {}
    section_data.update(sec_date_in=request.form.get('sec_date_in'))
    section_data.update(sec_text=request.form.get('sec_text'))

    # vm = DocumentViewModel()
    vm = CreateSectionViewModel(section_data)
    vm.compute_details()

    # doc = document_service.create_document(vm.doc_name)
    Section = DAL_Sections.add_section(vm.Section)

    group_data = {"doc_id": doc_id,
                  "sec_id": Section.sec_id}

    r = group_service.create_group(group_data)
    group_id = r["msg"]

    return {"group_id": group_id}


@blueprint.route('/documents/about_document', methods=['POST'])
@response(template_file='/documents/about_document.html')
def save_to_about():
    data = request.form.get('email')
    vm = DocumentViewModel()
    # return vm.to_dict()
    if not vm.user:
        return flask.redirect('/account/login')

    # TODO  create an edit method for documents

    # doc = document_service.get_document_by_id(doc_id=vm.doc_id)

    mygroups = DAL_Groups.get_documents_sections_to_obj(doc_id=vm.doc_id, limit=25)
    groups_list = []
    #
    groups_list.append(mygroups)

    mygroups1 = {
        'mygroups': {
            'doc_name': 'Company history',
            'page_details': 'Details about company history...',
        },
        'mygroups1': {
            'doc_name': 'Our team',
            'page_details': 'Details about company employees ...',
        },
    }

    aDict = {'user_id': vm.user_id , 'doc_id': vm.doc_id, 'doc_name': vm.doc_name, 'mygroups': mygroups}

    return aDict


@blueprint.route('/documents/update_document', methods=['POST'])
@response(template_file='/documents/about_document.html')
def update_doc():
    doc_id = request.form.get('doc_id')
    doc_name = request.form.get('doc_name')

    doc_data = {"doc_id": doc_id,"doc_name": doc_name}
    r = BLL_Documents.update_document(doc_id=doc_id,doc_data=doc_data)
    # print(r)
    return {}


@blueprint.route('/documents/edit_section', methods=['POST'])
@response(template_file='/documents/edit_section.html')
def edit_section():
    sec_id = request.form.get('sec_id')

    section_dict = BLL_Sections.single_section(sec_id)

    section = section_dict['msg']
    section_data = {"sec_id": section.sec_id, "sec_text":section.sec_text}

    return section_data


@blueprint.route('/documents/save_section', methods=['POST'])
@response(template_file='/documents/save_section.html')
def save_section():
    sec_id = request.form.get('sec_id')
    sec_text = request.form.get('sec_text')
    sec_editor = request.form.get('editor')
    sec_text = request.form.get('aaa')
    sec_date_in = request.form.get('sec_date_in')
    sec_data = {'sec_id': sec_id, 'sec_text': sec_text, 'sec_date_in': sec_date_in}

    msg_dict = BLL_Sections.update_section(sec_id,sec_data)
    # section_data = {"sec_id": section.sec_id, "sec_text":section.sec_text}

    return msg_dict
