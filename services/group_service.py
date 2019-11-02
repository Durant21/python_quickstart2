from viewmodels.documents.create_group_viewodel import CreateGroupViewModel
from DAL.Groups import DAL_Groups

def create_group(group_data):
    # TODO: Validate
    vm = CreateGroupViewModel(group_data)
    vm.compute_details()
    if vm.error:
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