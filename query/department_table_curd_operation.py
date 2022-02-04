import logging
from db_connection import DataBase

logging.basicConfig(filename='../employee_service.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

class DBQueriesOperation:
    def __init__(self):
        self.connection = DataBase.mysql_connect_database()
        self.cursor = self.connection.cursor(buffered=True)

    def insert_department_data(self, dept_id, DepartmentName, teacher_Id, Student_Id):
        """
         inserting department data dept_id,department name, teacher_id, student_id
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

            query = "select DepartmentName from department inner join teacher_table" \
                    " on department.dept_id = teacher_table.dept_id";
            get_query = self.connection.select_query(query)
            print(get_query)
            logging.info ("sucessfully")
            logging.debug("Department Detailes are")
            return "created Department table structure"
        except Exception as err:
            logging.error(f"Error: {err}")

    def update_department_data(self, DepartmentName, dept_id ):
        """
         updating department data with dept id reference
        :param DepartmentName:
        :param dept_id:
        :return:
        """
        try:
            query_department_data_update = "update Department set DepartmentName='%s' where DepartmentId=%d" % (
                DepartmentName, dept_id)
            self.cursor.execute(query_department_data_update)
            self.connection.commit()
            logging.info("Successfully Get All the teacher table")
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


