
# from DocTrace_v3.DocTrace_v3.Domain.Documents import Document
from DAL.Documents import DAL_Documents
from viewmodels.documents.create_document_viewodel import CreateDocumentViewModel
from viewmodels.documents.update_document_viewmodel import UpdateDocumentViewModel


class BLL_Documents:

    @classmethod
    def get_documents(cls):

        my_documents = DAL_Documents.all_documents()

        return my_documents

    @classmethod
    def single_document(cls,doc_id):
        doc = DAL_Documents.doc_by_id(doc_id=doc_id)

        return doc


    @classmethod
    def single_document_by_name(cls,doc_name):
        doc = DAL_Documents.doc_by_name(doc_name=doc_name)

        return doc

    @classmethod
    def create_document(cls,doc_data):

        # # test if Document already exists
        # doc = BLL_Documents.single_document_by_name(doc_name)
        # if not doc:
        #     print('could not find {}'.format(doc_name))


        # TODO: Validate
        vm = CreateDocumentViewModel(doc_data)
        vm.compute_details()
        if vm.error:
            # return "400 " + vm.error_msg
            return {"status": "400", "msg": vm.error}

        try:
            Document = DAL_Documents.add_document(vm.Document)
            # return Response(status=201, json_body=Document.to_dict())
            # return "201 " + Document.doc_id
            return {"status": "201", "msg": Document.doc_id}

        except Exception as x:
            # return Response(status=400, body='Could not save car.')
            # return "400 " + "Could not save document."
            return {"status": "400", "msg": "Could not save document."}

    @classmethod
    def update_document(cls,doc_id,doc_data): # (int,json_body)

        # get the document object by doc_id
        doc = DAL_Documents.doc_by_id(doc_id)

        if not doc:
            msg = "404 The document with id '{}' was not found.".format(doc_id)
            return msg

        # Validate
        vm = UpdateDocumentViewModel(doc_data,doc_id)
        vm.compute_details()
        if vm.error:
            return "400 " + vm.error
        try:
            DAL_Documents.update_document(vm.Document)
            return "204 Document updated successfully."
        except:
            return "400 Could not update document."
