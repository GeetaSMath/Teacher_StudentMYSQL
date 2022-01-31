import logging
from db_connection import DataBase

logging.basicConfig(filename='../employee_service.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

class DBQueriesOperation:
    def __init__(self):
        self.connection = DataBase.mysql_connect_database()
        self.cursor = self.connection.cursor(buffered=True)

    def insert_student_data(self, Student_Id, First_Name, Last_Name, Gender, Cource):
        """
        created insert data into student table
        :param Student_Id:passsig student_id
        :param First_Name:passing first name
        :param Last_Name:passing last name
        :param Gender:passing gender
        :param Cource:passing cource
        :return:
        """
        try:
            query_student_data_insert = "insert into  student_table( Student_Id, First_Name, Last_Name, Gender, Cource)" \
                                        " values(%d ,'%s', '%s','%s','%s')" \
                                        % (Student_Id, First_Name, Last_Name, Gender, Cource)
            self.cursor.execute(query_student_data_insert)
            self.connection.commit()
            logging.info("Suceefully Get All the Employee services")
            logging.debug("Students Detailes are")
            return "created student table structure"
        except Exception as err:
            logging.error(f"Error: {err}")

    def retrive_student_data(self):
        """
         created function to retrive data from student_table , this module containes loggers and exception
        :return:
        """
        try:
            query_retrive_student_data = 'select * from student_table'
            self.cursor.execute(query_retrive_student_data)
            self.connection.commit()
            logging.info("Retrive data which inserted")
            logging.debug("existed data")
            res = self.cursor.fetchall()
            return res
            # for val in res:
            #     print(val)
        except Exception as err:
            logging.error(f"Error: {err}")

    def update_student_data(self,  First_Name, Student_Id,):
        """
        created function to update with reference of primary key
        :param Student_Id:
        :param First_Name:
        :return:
        """
        try:
            query_student_data_update = "update student_table set First_Name='%s' " \
                                        "where Student_Id=%d" % (First_Name, Student_Id)
            self.cursor.execute(query_student_data_update)
            self.connection.commit()
            logging.info("Suceefully Get All the student_table")
            logging.debug("student Detailes are")
            return "created student table structure"

        except Exception as err:
            logging.error(f"Error: {err}")

    def delete_student_data(self, Student_Id):
        """
        created delete_data function contain this module loggers and exception
        :param id:passed id reference to delete data
        :return:
        """
        try:
            query_student_data_delete = "delete from Student_table where Student_Id=%d" % Student_Id
            self.cursor.execute(query_student_data_delete)
            self.connection.commit()
            # student from student with cascade delete
            query = "DELETE FROM student_table WHERE Student_Id=161";
            get_query = self.connection.selectquery(query)
            print(get_query)
            logging.info("Delete data which inserted")
            logging.debug("Update data")
            return "done operation"
        except Exception as err:
            logging.error(f"Error: {err}")

# perform_operation_student = DBQueriesOperation()
# perform_operation_student.insert_student_data(163, 'pallavi', 'Math', 'Female', 'Mechanical')
# perform_operation_student.update_student_data('shivam',162)
# perform_operation_student.retrive_student_data()
# perform_operation_student.delete_student_data(102)