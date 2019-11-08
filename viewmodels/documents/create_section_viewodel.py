from Domain.Sections import Section

from viewmodels.shared.viewmodelbase import ViewModelBase


class CreateSectionViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.Section = None
        self.sec_id = None
        self.sec_text = None
        self.sec_date_in = None

    def compute_details(self):
        # sec_id = self.data_dict.get('sec_id')
        adict = self.data_dict
        sec_text = adict.get('sec_text')
        # sec_text = self.data_dict.get('sec_text')
        sec_date_in = adict.get('sec_date_in')
        sec_id = self.sec_id
        # sec_text = self.sec_text
        # sec_date_in = self.sec_date_in
        # doc_id = self.data_dict.get('doc_id')

        if not sec_text:
            self.error.append("Section Text is required content.")

        if not self.error:
            section = Section(
                sec_id=sec_id,
                sec_text=sec_text,
                sec_date_in=sec_date_in
            )
            self.Section = section


