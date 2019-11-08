from Domain.Doc_Parent import DocumentParent

from viewmodels.shared.viewmodelbase import ViewModelBase


class CreateDocumentParentViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.DocumentParent = None

    def compute_details(self):
        doc_parent_id = self.data_dict.get('doc_parent_id')
        doc_id = self.data_dict.get('doc_id')
        parent_id = self.data_dict.get('parent_id')
        relationship = self.data_dict.get('relationship')

        if not doc_id:
            self.errors.append("doc_id is a required field.")

        if not self.errors:
            doc = DocumentParent(
                doc_parent_id=doc_parent_id,
                doc_id=doc_id,
                parent_id=parent_id,
                relationship=relationship,
            )
            self.DocumentParent = doc

