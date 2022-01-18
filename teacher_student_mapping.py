import logging
from db_connection import DataBase

logging.basicConfig(filename='employee_service.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

class DBQueriesST:
    def __init__(self):
        self.connection = DataBase.mysql_connect_database()
        self.cursor = self.connection.cursor(buffered=True)

    def insert_teacher_student_mappingdata(self, Student_Id, teacher_Id):
        """

        :param Student_Id:
        :param teacher_Id:
        :return:
        """
        try:
            query_teacher_student_data_insert = "insert into  teacher_student_mapping( Student_Id, teacher_Id)" \
                                        " values(%d ,%d)" \
                                        % (Student_Id, teacher_Id)
            self.cursor.execute(query_teacher_student_data_insert)
            self.connection.commit()
            logging.info("Suceefully Get All the Employee services")
            logging.debug("Students Detailes are")
            return "created student table structure"
        except Exception as err:
            logging.error(f"Error: {err}")

inser_data = DBQueriesST()
inser_data.insert_teacher_student_mappingdata(181, 101)
inser_data.insert_teacher_student_mappingdata(191, 104)




