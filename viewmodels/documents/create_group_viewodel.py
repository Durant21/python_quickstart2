from Domain.Groups import Group

from viewmodels.shared.viewmodelbase import ViewModelBase


class CreateGroupViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.Group = None

    def compute_details(self):
        group_id = self.data_dict.get('group_id')
        doc_id = self.data_dict.get('doc_id')
        sec_id = self.data_dict.get('sec_id')

        if not sec_id:
            self.error.append("sec_id is required.")

        if not doc_id:
            self.error.append("doc_id is required.")

        if not self.error:
            group = Group(
                group_id=group_id,
                doc_id=doc_id,
                sec_id=sec_id
            )
            self.Group = group


