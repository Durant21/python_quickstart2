import flask, requests
from flask import request

from infrastructure.view_modifiers import response
import services.document_service as document_service
from viewmodels.account.index_viewmodel import IndexViewModel

import services.section_service as section_service
import services.group_service as group_service
# import viewmodels.documents.create_section_viewodel as CreateSectionViewModel
from viewmodels.documents.create_section_viewodel import CreateSectionViewModel

from viewmodels.documents.section_viewmodel import SectionViewModel

blueprint = flask.Blueprint('sections', __name__, template_folder='templates')


@blueprint.route('/sections')
@response(template_file='/sections/index.html')
def index():
    # vm = IndexViewModel()
    vm = SectionViewModel()
    if not vm.user:
        return flask.redirect('/account/login')

    # doc_packages = document_service.get_all_documents()
    # return {'documents': doc_packages}
    # return flask.render_template('home/index.html', packages=test_packages)
    return vm.to_dict()


@blueprint.route('/edit_document', methods=['POST'])
@response(template_file='/documents/edit_document.html')
def create_section():

    # collect the doc_id from Form
    doc_id = request.form.get('doc_id')
    section_data = {}
    section_data.update(sec_date_in=request.form.get('sec_date_in'))
    section_data.update(sec_text=request.form.get('sec_text'))

    # vm = DocumentViewModel()
    vm = CreateSectionViewModel(section_data)

    # doc = document_service.create_document(vm.doc_name)
    Section = section_service.add_section(vm.Section)

    group_data = {"doc_id": doc_id,
                  "sec_id": Section.sec_id}

    r = group_service.create_group(group_data)
    group_id = r["msg"]

    return r.to_dict()


