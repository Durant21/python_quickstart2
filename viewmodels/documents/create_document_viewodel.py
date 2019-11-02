from Domain.Documents import Document
from viewmodels.shared.viewmodelbase import ViewModelBase

class CreateDocumentViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.Document = None

    def compute_details(self):
        doc_id = self.data_dict.get('doc_id')
        doc_name = self.data_dict.get('doc_name')

        if not doc_name:
            self.error.append("doc name is a required field.")

        if not self.error:
            doc = Document(
                doc_id=doc_id,
                doc_name=doc_name
            )
            self.Document = doc


