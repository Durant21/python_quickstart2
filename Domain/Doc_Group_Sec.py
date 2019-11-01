class Doc_Group_Sec:
    def __init__(self):
        self.doc_id = ''
        self.group_id = ''
        self.doc_name = ''
        self.sec_text = ''
        self.sec_id = ''
        self.order = ''

    def add_doc_id(self, id):
        self.doc_id = id

    def add_doc_name(self, name):
        self.doc_name = name

    def add_group_id(self, id):
        self.group_id = id

    def add_sec_text(self,txt):
        self.sec_text = txt

    def add_sec_id(self,id):
        self.sec_id = id

    def add_order(self,order):
        self.order = order

    def to_dict(self):
        return {
            'group_id': self.group_id,
            'doc_id': self.doc_id,
            'doc_name': self.doc_name,
            'sec_text': self.sec_text,
            'sec_id': self.sec_id,
            'order': self.order,
        }
