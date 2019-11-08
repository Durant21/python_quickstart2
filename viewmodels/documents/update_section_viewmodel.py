from viewmodels.documents.create_section_viewodel import CreateSectionViewModel


class UpdateSectionViewModel(CreateSectionViewModel):
    def __init__(self, data_dict, sec_id):
        super().__init__(data_dict)
        self.sec_id = sec_id

    def compute_details(self):
        # sec_id = self.data_dict.get('sec_id')
        sec_id = self.sec_id
        if not self.sec_id:
            self.error.append("No section ID specified.")
        if self.sec_id != sec_id:
            self.error.append("Section ID mismatch.")

        super().compute_details()

