
from viewmodels.documents.create_document_parent_viewmodel import CreateDocumentParentViewModel
from DAL.Doc_Parent import DAL_Doc_Parent
# from DAL.sql_Doc_Parent import Sql_Doc_Parent

class BLL_Doc_Parent:
    # global final_lst
    # final_lst = []

    # @classmethod
    # def get_sections(cls):
    #
    #     my_sections = DAL_Sections.all_sections(limit=25)
    #
    #     return my_sections
    #
    # @classmethod
    # def single_section(cls, sec_id):
    #     section = DAL_Sections.section_by_id(sec_id=sec_id)
    #
    #     # return section
    #
    #     return {"status": "200", "msg": section}
    #
    @classmethod
    def get_doc_parent_by_doc_id(cls, doc_id):
        # doc_parent_relationship = Sql_Doc_Parent.doc_parent_by_doc_id(doc_id=doc_id)
        docs = Sql_Doc_Parent.doc_parent_by_doc_id(doc_id=doc_id)

        aList = [];
        #
        # for d in docs:
        #     aDict = {}
        #     aDict["relationship"] = d["relationship"]
        #     aDict["doc_name"] = d["doc_name"]
        #     aDict["parent_doc_name"] = d["parent_doc_name"]
        #     aDict["doc_id"] = d["doc_id"]
        #
        #     aList.append(aDict)

        final_lst = []
        doc_list = []
        doc_list.append(doc_id)
        final_lst1 = BLL_Doc_Parent.find_parent(doc_list,docs,final_lst)
        final_lst2 = BLL_Doc_Parent.find_child(doc_list,docs,final_lst)

        docs.clear()

        return final_lst1

    @classmethod
    def find_parent(self, doc_list,docs_all,final_lst2,count=0):

        tmp_lst = []

        for d in doc_list:
            for u in docs_all:
                if u['doc_id'] == d:
                    # if u['parent_doc_id'] is not '0':
                    tmp_lst.append(u['parent_id'])

                    final_lst2.append(u)

        if (len(tmp_lst) > 0) and (len(tmp_lst) < 100):
            print("find_parent() length {}".format(len(tmp_lst)))
            self.find_parent(tmp_lst,docs_all,final_lst2,count+1)
        # else:
        print("called find_parent() {} times".format(count))
        return final_lst2

    @classmethod
    def find_child(self, doc_list, docs_all,final_lst, count=0):
        tmp_lst = []
        t = 0

        for d in doc_list:
            for u in docs_all:
                if u['parent_id'] == d:
                    # if u['parent_doc_id'] is not '0':
                    tmp_lst.append(u['doc_id'])

                    final_lst.append(u)

        if (len(tmp_lst) > 0) and (len(tmp_lst) < 100):
            print("find_child() length {}".format(len(tmp_lst)))
            self.find_child(tmp_lst,docs_all,final_lst, count+1)
        # else:


        print("called find_child() {} times".format(count))
        return final_lst

    @classmethod
    def create_doc_parent(cls, j_body):
        # TODO: Validate
        new_data = {}
        new_data.update(doc_id=j_body['doc_id'])
        new_data.update(parent_id=j_body['parent_id'])
        new_data.update(relationship=j_body['relationship'])
        vm = CreateDocumentParentViewModel(new_data)
        vm.compute_details()
        if vm.errors:
            # return "400 " + vm.error_msg
            return {"status": "400", "msg": vm.error_msg}

        try:
            doc_parent = DAL_Doc_Parent.create_doc_parent(vm.DocumentParent)
            # return Response(status=201, json_body=Document.to_dict())
            # return "201 " + Section.sec_id
            # return {"status":"201", "msg":Section.sec_id}
            # create a group
            # group_data = {"doc_id": j_body["doc_id"],
            #               "sec_id": Section.sec_id}
            # r = BLL_Groups.create_group(group_data)
            # group_id = r["msg"]

            print("created doc_parent" + doc_parent.doc_parent_id)
            return {"status": "201", "msg": doc_parent.doc_parent_id}

        except Exception as x:
            # return Response(status=400, body='Could not save car.')
            # return "400 " + "Could not save section."
            return {"status": "400", "msg": "Could not save doc_parent record."}

