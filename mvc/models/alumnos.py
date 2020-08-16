import mysql.connector

class Alumnos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='vxqqg0oa6x33ycb8', 
                password='si5bz9dugvm8j538',
                host='cdm1s48crk8itlnr.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port=3306,
                database='xq2g14cu2ylsahky'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    def select(self):
        try:
            self.connect()
            query = ("SELECT * from alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'id_alumno': row[0],
                    'matricula': row[1],
                    'nombre': row[2],
                    'onelastname': row[3],
                    'twolastname': row[4],
                    'edad': row[5],
                    'borndate': row[6],
                    'sex': row[7],
                    'estado': row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

    def view(self,id_alumno):
        try:
            self.connect()
            query = ("SELECT * from alumnos where id_alumno = %s;")
            values = (id_alumno,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                r = {
                    'id_alumno': row[0],
                    'matricula': row[1],
                    'nombre': row[2],
                    'onelastname': row[3],
                    'twolastname': row[4],
                    'edad': row[5],
                    'borndate': row[6],
                    'sex': row[7],
                    'estado': row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

    def insert(self, matricula, nombre, onelastname, twolastname, edad, borndate, sex, estado):
        try: 
            self.connect()
            query = ("INSERT INTO alumnos (matricula, nombre, onelastname, twolastname, edad, borndate, sex, estado) values(%s, %s, %s, %s, %s, %s, %s, %s );")
            values = (matricula, nombre, onelastname, twolastname, edad, borndate, sex, estado)
            self.cursor.execute(query, values)
            self.cnx.commit() 
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, id_alumno):
        try:
            self.connect()
            query = ("DELETE FROM alumnos WHERE id_alumno = %s;")
            values = (id_alumno,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, id_alumno, matricula, nombre, onelastname, twolastname, edad, borndate, sex, estado):
        try:
            self.connect()
            query = ("UPDATE alumnos SET matricula=%s, nombre=%s, onelastname=%s, twolastname=%s, edad=%s, borndate=%s, sex=%s, estado=%s WHERE id_alumno=%s;")
            values = (matricula, nombre, onelastname, twolastname, edad, borndate, sex, estado, id_alumno)
            self.cursor.execute(query, values)
            self.cnx.commit() 
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Alumnos()
#print(objeto.delete(6))
#objeto.update(9, 1718110387, "Jesus Manuel", "Huerta", "Najera", 20, "2000-06-25", "Masculino", "Hidalgo")

#for row in objeto.select():
#    print(row)
