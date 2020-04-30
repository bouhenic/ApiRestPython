import json

import pymysql


class Bdd:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db


    def Lastselect(self):

        connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )

        with connection.cursor() as cursor:
                sql = "SELECT * FROM `TEMPERATURE` ORDER BY ID DESC LIMIT 1"
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()

                    for row in result:

                        objet = {
                            "id": str(row[0]), "time": str(row[1]), "temp": str(row[2])
                        }
                        objetjson =json.dumps(objet, indent=4)

                        return objetjson

                except:
                    print("Oops! Something wrong")

        connection.commit()
        connection.close()

    def selectById(self, Id):

        connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )

        with connection.cursor() as cursor:
            sql = f"SELECT * FROM `TEMPERATURE` WHERE ID={Id} LIMIT 1"
            try:
                cursor.execute(sql)
                result = cursor.fetchall()

                for row in result:
                    objet = {
                        "id": str(row[0]), "time": str(row[1]), "temp": str(row[2])
                    }
                    objetjson = json.dumps(objet, indent=4)

                    return objetjson

            except:
                print("Oops! Something wrong")

        connection.commit()
        connection.close()

    def insert(self, temp):

        connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )

        with connection.cursor() as cursor:
            sql = f"INSERT INTO temperature(TEMP) VALUES({temp})"
            try:
                cursor.execute(sql)

            except:
                print("Oops! Something wrong")

        connection.commit()
        connection.close()

    def update(self, temp, Id):

        connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )

        with connection.cursor() as cursor:
            sql = f"UPDATE TEMPERATURE SET TEMP = {temp} WHERE id = {Id}"

            try:
                cursor.execute(sql)

            except:
                print("Oops! Something wrong")

        connection.commit()
        connection.close()

    def delete(self, Id):

        connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )

        with connection.cursor() as cursor:
            sql = f"DELETE FROM TEMPERATURE WHERE id={Id}"
            try:
                cursor.execute(sql)

            except:
                print("Oops! Something wrong")

        connection.commit()
        connection.close()
