from DAL.Sections import DAL_Sections
from BLL.Groups import BLL_Groups
from DAL.Groups import DAL_Groups
from DAL.Doc_Parent import DAL_Doc_Parent
from viewmodels.documents.create_section_viewodel import CreateSectionViewModel
from viewmodels.documents.update_section_viewmodel import UpdateSectionViewModel

class BLL_DocGroupSections:

    @classmethod
    def attach_sections(cls,j_body):
        # verify doc_id, sec_id
        new_group_id = ""

        section_data = {}
        section_data.update(append_doc_id=j_body['append_doc_id'])
        section_data.update(doc_id=j_body['doc_id'])

        append_doc_id = j_body['append_doc_id']
        doc_id = j_body['doc_id']

        # use supplied append_doc_id to retrieve sec_id's as a list
        section_list = DAL_Groups.get_documents_sections(doc_id=append_doc_id,limit=25)

        # for each sec_id in list, insert into Group table
       # BLL_Groups.create_group()
        for s in section_list:
            sec_id = s['sec_id']
            print(sec_id)

            group_data = {"doc_id": doc_id,
                          "sec_id": sec_id}
            r = BLL_Groups.create_group(group_data)
            group_id = r["msg"]

        # With a Doc's sections linked to another Doc, note that relationship in the Doc_Parent table
        doc_data = {"doc_id": doc_id,
                    "parent_id": append_doc_id,
                    "relationship": "direct"}  # direct/copy
        r = DAL_Doc_Parent.create_doc_parent(doc_data)
        return {"status": "201", "msg": r.doc_parent_id}

