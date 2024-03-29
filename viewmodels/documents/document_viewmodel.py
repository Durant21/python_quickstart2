from services import user_service, document_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class DocumentViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = user_service.find_user_by_id(self.user_id)
        self.email = self.request_dict.email.lower().strip()

        self.doc_packages = document_service.get_all_documents()
        # return {'documents': doc_packages}
        # self.name = self.request_dict.name
        # self.email = self.request_dict.email.lower().strip()
        # self.password = self.request_dict.password.strip()
        # self.age = self.request_dict.age.strip()
        self.doc_name = self.request_dict.doc_name.strip()
        self.doc_id = self.request_dict.doc_id.strip()
        t = 1

    # def validate(self):
    #     if not self.name or not self.name.strip():
    #         self.error = 'You must specify a name.'
    #     elif not self.email or not self.email.strip():
    #         self.error = 'You must specify a email.'
    #     elif not self.password:
    #         self.error = 'You must specify a password.'
    #     elif len(self.password.strip()) < 5:
    #         self.error = 'The password must be at least 5 characters.'
    #     elif user_service.find_user_by_email(self.email):
    #         self.error = 'A user with that email address already exists.'
