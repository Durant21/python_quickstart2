from viewmodels.documents.create_document_viewodel import CreateDocumentViewModel


class UpdateDocumentViewModel(CreateDocumentViewModel):
    def __init__(self, data_dict, doc_id):
        super().__init__(data_dict)
        self.doc_id = doc_id

    def compute_details(self):
        doc_id = self.data_dict.get('doc_id')
        if not self.doc_id:
            self.errors.append("No doc ID specified.")
        if self.doc_id != doc_id:
            self.errors.append("Document ID mismatch.")

        super().compute_details()

