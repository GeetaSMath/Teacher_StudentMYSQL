import logging
import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(filename='employee_service.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

class DataBase:
        @staticmethod
        def mysql_connect_database():
            """
            created class Containes connection part ,loggers, data hiding of configeration
             created function for connection mysql_connect_database containes exception part
            :return: it calls conn
            """
            try:
                logging.info("Trying to establish the database connection")
                conn = mysql.connector.connect(host=os.getenv('host'), user=os.getenv('user'), port=os.getenv('port'), password=os.getenv('pass'),
                                           database=' payroll_servicesdetailes')

                logging.info("Database Connection is Established")
                return conn

            except mysql.connector.Error  as  er:
                logging.error("Connection not Established")
                if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("invalid username or password")
                elif er.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(er)

# call = DataBase.mysqlconnect_database()
# print(call)