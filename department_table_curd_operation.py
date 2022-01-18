import logging
from db_connection import DataBase

logging.basicConfig(filename='employee_service.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

class DBQueriesOperation:
    def __init__(self):
        self.connection = DataBase.mysql_connect_database()
        self.cursor = self.connection.cursor(buffered=True)

    def insert_department_data(self, dept_id, DepartmentName, teacher_Id, Student_Id):
        """

        :param DepartmentId:
        :param DepartmentName:
        :param teacher_Id:
        :param Student_Id:
        :return:
        """
        try:
            query_department_data_insert = "insert into  department( dept_id, DepartmentName, teacher_Id, Student_Id)" \
                         " values(%d, '%s', %d, %d)" \
                         % (dept_id, DepartmentName, teacher_Id, Student_Id)
            self.cursor.execute(query_department_data_insert)
            self.connection.commit()
            logging.info("Suceefully")
            logging.debug("Department Detailes are")
            return "created Department table structure"
        except Exception as err:
            logging.error(f"Error: {err}")

    def update_department_data(self, DepartmentName, dept_id ):

        try:
            query_department_data_update = "update Department set DepartmentName='%s' where DepartmentId=%d" % (
            DepartmentName, dept_id)
            self.cursor.execute(query_department_data_update)
            self.connection.commit()
            logging.info("Suceefully Get All the teacher table")
            logging.debug("department Detailes are")
            return "created teacher table structure"
        except Exception as err:
            logging.error(f"Error: {err}")

    def retrive_department_data(self):
        """
         created function to retrive data to retive data which is exisited data in teacher table
        :return:
        """
        try:
            query_retrive_department_data = 'select * from department'
            self.cursor.execute(query_retrive_department_data)
            self.connection.commit()
            logging.info("Retrive data which inserted")
            logging.debug("existed data")
            res = self.cursor.fetchall()
            for val in res:
                print(val)
        except Exception as err:
            logging.error(f"Error: {err}")

    def delete_department_data(self, dept_id):
        """
        created delete_data function contain this module loggers and exception
        :param id:passed id reference to delete data
        :return:
        """
        try:
            query_department_data_delete = "delete from Department where DepartmentId=%d" % dept_id
            self.cursor.execute(query_department_data_delete)
            self.connection.commit()
            logging.info("Delete data which inserted")
            logging.debug("Update data")
            return "done operation"
        except Exception as err:
            logging.error(f"Error: {err}")


perform_department_operation = DBQueriesOperation()
# perform_department_operation.insert_department_data(10102, 'civil', 200, 101)
perform_department_operation.insert_department_data(1002, 'civil', 202, 165)
perform_department_operation.retrive_department_data()
# perform_department_operation.update_department_data()
# perform_department_operation.delete_department_data()
