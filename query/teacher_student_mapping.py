import logging
from db_connection import DataBase

logging.basicConfig(filename='../employee_service.log', filemode='a', level=logging.DEBUG,
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
            # get student name and teacher name who is teaching using teacher student mapping by inner join
            query = "select  Student_Id, teacher_Id FROM teacher_table tb INNER JOIN " \
                    "teacher_student_mapping tm ON tb.teacher_Id = tm.teacher_Id " \
                    "INNER JOIN student_table st ON st.Student_Id = tm.Student_Id;"
            get_query=self.connection.selectquery(query)
            print(get_query)
            logging.info("Suceefully Get All the Employee services")
            logging.debug("Students Detailes are")
            return "created student table structure"
        except Exception as err:
            logging.error(f"Error: {err}")





