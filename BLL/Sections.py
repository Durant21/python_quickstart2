from DAL.Sections import DAL_Sections
from BLL.Groups import BLL_Groups
from viewmodels.documents.create_section_viewodel import CreateSectionViewModel
from viewmodels.documents.update_section_viewmodel import UpdateSectionViewModel

class BLL_Sections:

    @classmethod
    def get_sections(cls):

        my_sections = DAL_Sections.all_sections()

        return my_sections

    @classmethod
    def single_section(cls,sec_id):
        section = DAL_Sections.section_by_id(sec_id=sec_id)

        # return section

        return {"status": "200", "msg": section}

    @classmethod
    def get_sections_by_doc(cls,doc_id):
        section = DAL_Sections.section_by_doc(doc_id=doc_id)

        # return section

        return {"status": "200", "msg": section}


    @classmethod
    def create_section(cls,j_body):
        # TODO: Validate
        section_data = {}
        section_data.update(sec_date_in=j_body['sec_date_in'])
        section_data.update(sec_text=j_body['sec_text'])
        vm = CreateSectionViewModel(section_data)
        vm.compute_details()
        if vm.error:
            # return "400 " + vm.error_msg
            return {"status": "400", "msg": vm.error}

        try:
            Section = DAL_Sections.add_section(vm.Section)
            # return Response(status=201, json_body=Document.to_dict())
            # return "201 " + Section.sec_id
            # return {"status":"201", "msg":Section.sec_id}
            # create a group
            group_data = {"doc_id": j_body["doc_id"],
                          "sec_id": Section.sec_id}
            r = BLL_Groups.create_group(group_data)
            group_id = r["msg"]

            print("created group" + group_id)
            return {"status": "201", "msg": group_id}

        except Exception as x:
            # return Response(status=400, body='Could not save car.')
            # return "400 " + "Could not save section."
            return {"status": "400", "msg": "Could not save section."}

    @classmethod
    def update_section(cls,sec_id,section_data): # (int,json_body)

        # get the section object by sec_id
        section = DAL_Sections.section_by_id(sec_id)

        if not section:
            msg = "404 The section with id '{}' was not found.".format(sec_id)
            # return msg
            return {"status": "404", "msg": msg}

        # Validate
        vm = UpdateSectionViewModel(section_data,sec_id)
        vm.compute_details()
        if vm.error:
            # return "400 " + vm.error_msg
            return {"status": "400", "msg": vm.error}
        try:
            DAL_Sections.update_section(vm.Section)
            # return "204 Section updated successfully."
            return {"status": "204", "msg": "Section updated successfully."}
        except:
            # return "400 Could not update section."
            return {"status": "400", "msg": "Could not update section."}