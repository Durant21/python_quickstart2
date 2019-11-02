
from DAL.Groups import DAL_Groups
from viewmodels.documents.create_group_viewodel import CreateGroupViewModel
from viewmodels.documents.update_group_viewmodel import UpdateGroupViewModel

class BLL_Groups:

    @classmethod
    def get_groups(cls):
        my_groups = DAL_Groups.all_groups(limit=25)

        return my_groups

    @classmethod
    def get_docs_groups(cls,doc_id):
        my_groups = DAL_Groups.get_documents_sections(doc_id=doc_id,limit=25)

        return my_groups

    @classmethod
    def single_group(cls,group_id):
        group = DAL_Groups.group_by_id(group_id=group_id)

        return group

    @classmethod
    def create_group(cls,group_data):
        # TODO: Validate
        vm = CreateGroupViewModel(group_data)
        vm.compute_details()
        if vm.errors:
            # return "400 " + vm.error_msg
            return {"status": "400", "msg": vm.error_msg}
        try:
            Group = DAL_Groups.add_group(vm.Group)
            # return Response(status=201, json_body=Document.to_dict())
            # return "201 " + Group.group_id
            return {"status": "201", "msg": Group.group_id}
        except Exception as x:
            # return Response(status=400, body='Could not save car.')
            # return "400 " + "Could not save group."
            return {"status": "400", "msg": "Could not save group."}
    @classmethod
    def update_group(cls,group_id,group_data): # (int,json_body)

        # get the section object by sec_id
        group = DAL_Groups.group_by_id(group_id)

        if not group:
            msg = "404 The group with id '{}' was not found.".format(group_id)
            # return msg
            return {"status": "404", "msg": msg}
        # Validate
        vm = UpdateGroupViewModel(group_data,group_id)
        vm.compute_details()
        if vm.errors:
            # return "400 " + vm.error_msg
            return {"status": "400", "msg": vm.error_msg}
        try:
            DAL_Groups.update_group(vm.Group)
            # return "204 Group updated successfully."
            return {"status": "204", "msg": "Group updated successfully."}
        except:
            # return "400 Could not update group."
            return {"status": "400", "msg": "Could not update group."}