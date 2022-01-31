import logging
from db_connection import DataBase

logging.basicConfig(filename='../employee_service.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

class DBQueries:
    def __init__(self):
        self.connection = DataBase.mysql_connect_database()
        self.cursor = self.connection.cursor(buffered=True)

    def insert_teacher_data(self, teacher_Id, First_Name, Last_Name, Gender, Mobile_Number, Salary, Start, dept_id):
        """
         created function to insert data into teacher table that conatines attribute
        :param teacher_Id:argument passing to  teacher table
        :param First_Name:argument passing to  teacher table
        :param Last_Name:argument passing to teacher table
        :param Gender:argument passing to teacher table
        :param Mobile_Number:passing to teacher table
        :param Salary:argument paasing to teacher table
        :param Start:argument passing to teacher table
        :return:
        """
        try:
            query_teacher_data_insert = "insert into  teacher_table( teacher_Id, First_Name, Last_Name, Gender," \
                                        " Mobile_Number, Salary, Start, dept_id)" \
                     " values(%d ,'%s', '%s', '%s', '%s',%f, '%s', %d)" \
                     % (teacher_Id, First_Name, Last_Name, Gender, Mobile_Number, Salary, Start, dept_id)
            self.cursor.execute(query_teacher_data_insert)
            self.connection.commit()
            logging.info("Suceefully Get All the Employee services")
            logging.debug("Employee Detailes are")
            return "created teacher table structure"
        except Exception as err:
            logging.error(f"Error: {err}")

    def update_teacher_data(self, First_Name, teacher_Id, ):
        """
        this module containes loggers and exception
        update data from teacher table with reference of primary key that is techer id
        :param name:argument passing teacher id
        :param id:passing argument teacher First_name
        :return:
        """
        try:
            query_teacher_data_update = "update teacher_table set First_Name='%s' where teacher_Id=%d" % (
            First_Name, teacher_Id)
            self.cursor.execute(query_teacher_data_update)
            self.connection.commit()
            logging.info("Suceefully Get All the teacher table")
            logging.debug("teacher Detailes are")
            return "created teacher table structure"
        except Exception as err:
            logging.error(f"Error: {err}")


    def retrive_teacher_data(self):
        """
         created function to retrive data to retive data which is exisited data in teacher table
        :return:
        """
        try:
            query_retrive_teacher_data = 'select * from teacher_table'
            self.cursor.execute(query_retrive_teacher_data)
            self.connection.commit()
            logging.info("Retrive data which inserted")
            logging.debug("existed data")
            res = self.cursor.fetchall()
            for val in res:
                print(val)
        except Exception as err:
            logging.error(f"Error: {err}")

    def delete_teacher_data(self, teacher_Id):
        """
        created delete_data function contain this module loggers and exception
        :param id:passed id reference to delete data
        :return:
        """
        try:
            query_teacher_data_delete = "delete from teacher_table where teacher_Id=%d" % teacher_Id
            self.cursor.execute(query_teacher_data_delete)
            self.connection.commit()
            # techer from teacher with cascade delete
            query ="DELETE FROM teacher_table " \
                   "WHERE teacher_Id=181;"
            get_query = self.connection.selectquery(query)
            print(get_query)
            logging.info("Delete data which inserted")
            logging.debug("Update data")
            return "done operation"
        except Exception as err:
            logging.error(f"Error: {err}")


perform_operation = DBQueries()
perform_operation.insert_teacher_data(200, 'pavan', 'prakru', 'male', '4216549885' ,30000.00, '2021-06-05', 1002)
perform_operation.retrive_teacher_data()
perform_operation.update_teacher_data('Rutvi',111)
perform_operation.delete_teacher_data(141)
