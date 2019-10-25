from services import user_service, cms_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class PageViewModel(ViewModelBase):
    def __init__(self, full_url: str):
        super().__init__()

        self.page = cms_service.get_page(full_url)

