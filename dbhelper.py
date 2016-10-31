import pymysql
import dbconfig


class DBHelper:

    def connect(self, database="sharingan_ali"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def add_user(self, args):
        connection = self.connect()
        try:
            query = "INSERT INTO User(`roleid`,`putao_token_uid`,`putao_name`,`authtype`,`createdate`) "\
                    "values(1,%s,%s,1, now() );"
            with connection.cursor() as cursor:
                cursor.execute(query, ( args['putao_token_uid'], args['putao_name'] ))
                connection.commit()
                # print('#cursor.lastrowid=',cursor.lastrowid)
                return cursor.lastrowid
        finally:
            connection.close()

    def get_user(self, userid):
        connection = self.connect()
        try:
            query = "SELECT putao_name FROM User;"
            if userid is not None:
                query = "SELECT putao_name FROM User where userid = " + userid+";"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()


    def get_childrenPicture(self, patientid):
        connection = self.connect()
        try:
            query = "SELECT picture FROM Patient;"
            if patientid is not None:
                query = "SELECT picture FROM Patient where patientid=" + patientid+";"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def get_children(self, userid):
        connection = self.connect()
        try:
            query = "SELECT * FROM Patient;"
            if userid is not None:
                query = "SELECT Patient.* FROM Patient,Patient_User " \
                        "where Patient.patientid = Patient_User.patientid and Patient_User.userid=" + userid + " order by createdate desc  ;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_children(self, args):
        connection = self.connect()
        try:
            query = "insert  Patient(name,sex,birthday, picture,createdate) values(%s,%s,%s,%s, now() );"
            with connection.cursor() as cursor:
                cursor.execute(query, ( args['name'], args['sex'],args['birthday'],args['picture'] ))
                connection.commit()
                # print('#cursor.lastrowid=',cursor.lastrowid)
                return cursor.lastrowid
        finally:
            connection.close()

    def  add_patientuser(self,args):
        connection = self.connect()
        try:
            query = "insert Patient_User(patientid, userid, createdate)  values(%s,%s, now() );"
            with connection.cursor() as cursor:
                cursor.execute(query, ( args['patientid'], args['userid'] ))
                connection.commit()
        finally:
            connection.close()

    def get_rawmeasure(self, patientid):
        connection = self.connect()
        try:
            query = "SELECT * FROM MeasureRaw;"
            if patientid is not None:
                query = "SELECT * FROM MeasureRaw where patientid = " + patientid + " order by createdate desc limit 100 ;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_rawmeasure(self, args):
        connection = self.connect()
        try:
            query = "insert MeasureRaw( rawdata, patientid, whicheye, createdate) values(%s, %s, %s, now());"
            with connection.cursor() as cursor:
                cursor.execute(query, ( args['rawdata'], args['patientid'],args['whicheye']))
                connection.commit()
        finally:
            connection.close()

    # def get_measure(self):
    #     connection = self.connect()
    #     try:
    #         query = "SELECT * FROM Measure;"
    #         with connection.cursor() as cursor:
    #             cursor.execute(query)
    #         return cursor.fetchall()
    #     finally:
    #         connection.close()

    # def add_measure(self, args):
    #     connection = self.connect()
    #     try:
    #         query = "insert Measure(rawdataid, data, deviceid,createdate) values(%s, %s, %s, now());"
    #         with connection.cursor() as cursor:
    #             cursor.execute(query, (4, args['data'], args['deviceid']))
    #             connection.commit()
    #     finally:
    #         connection.close()

    def add_measurebaseline(self, args):
        connection = self.connect()
        try:
            query = "insert MeasureBaseline( patientid, data, whicheye, createdate) values(%s, %s, %s,now());"
            with connection.cursor() as cursor:
                cursor.execute(query, ( args['patientid'], args['data'],args['whicheye']))
                connection.commit()
        finally:
            connection.close()

    def delete_measurebaseline(self, patientid):
        connection = self.connect()
        try:
            query = "delete FROM MeasureBaseline where patientid = " + patientid +";"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    def get_measurebaseline(self, patientid):
        connection = self.connect()
        try:
            query = "SELECT whicheye,count(*) as num FROM sharingan_ali.MeasureBaseline ;"
            if patientid is not None:
                query = "SELECT whicheye, count(*) as num FROM sharingan_ali.MeasureBaseline where  patientid = " + patientid + " group by whicheye;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def get_measurebaseline_summary(self, patientid):
        connection = self.connect()
        try:
            query = "SELECT whicheye, data  FROM sharingan_ali.MeasureBaseline;"
            if patientid is not None:
                query = "SELECT whicheye, data  as num FROM sharingan_ali.MeasureBaseline where  patientid = " + patientid + " ;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES (%s);"
            print('query=', query)
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
