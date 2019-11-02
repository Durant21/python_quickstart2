from viewmodels.documents.create_group_viewodel import CreateGroupViewModel


class UpdateGroupViewModel(CreateGroupViewModel):
    def __init__(self, data_dict, group_id):
        super().__init__(data_dict)
        self.group_id = group_id

    def compute_details(self):
        group_id = self.data_dict.get('group_id')
        if not self.group_id:
            self.errors.append("No group ID specified.")
        if self.group_id != group_id:
            self.errors.append("Group ID mismatch.")

        super().compute_details()

