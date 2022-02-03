from query.student_table_curd_operation import DBQueriesOperation
from query.teacher_curd_table_operation import DBQueries
from query.department_table_curd_operation import DBQueriesOperation
from query.teacher_student_mapping import DBQueriesST

class controllinfo():
    def get_student_details(self):
        """
         created function get infromation
        :return:
        """
        perform_operation_student = DBQueriesOperation()
        perform_operation_student.insert_student_data(200, 'sangeeta', 'Math', 'Female', 'cse')
        output=perform_operation_student.retrive_student_data()
        for out in output:
            print(out)
        perform_operation_student.delete_student_data(),
        perform_operation_student.update_student_data()

    def get_teacher_details(self):
        """
         get teacher details from teacher
        :return:
        """
        perform_operation = DBQueries()
        perform_operation.insert_teacher_data()
        output = perform_operation.retrive_teacher_data()
        for out in output:
            print(out)
        perform_operation.update_teacher_data(),
        perform_operation.delete_teacher_data()

    def get_department_details(self):
        """
         get department details
        :return:
        """
        perform_department_operation = DBQueriesOperation()
        perform_department_operation.insert_department_data()
        output=perform_department_operation.retrive_department_data()
        for out in output:
            print(out)
        perform_department_operation.delete_student_data(),
        perform_department_operation.update_department_data()

    def get_stu_teacher_mapping(self):
        """
         get student teachet details
        :return:
        """
        inser_data = DBQueriesST()
        inser_data.insert_teacher_student_mappingdata(181, 101)

    if __name__ == "__main__":
        while True:
            choice= int(input("enter your choice"))
            my_dict = {
                1:get_student_details,
                2:get_teacher_details,
                3:get_department_details,
                4:get_stu_teacher_mapping
            }
            my_dict.get(choice)()





