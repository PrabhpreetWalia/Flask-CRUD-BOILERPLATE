import mysql.connector
import json

class user_model():
    def __init__(self):
        
        try:
            self.con = mysql.connector.connect(host = "localhost", user="root", password="toor", database="flask")
            self.con.autocommit=True
            print("Database connection success")
            self.cur = self.con.cursor(dictionary = True)
        except:
            print("Database connection failed")


    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()

        if len(result) > 0: 
            return json.dumps(result)
        else:
            return "No data found !!"

    def user_add_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, role, phone, password) VALUES('{data['name']}', '{data['email']}', '{data['role']}', '{data['phone']}', '{data['password']}')")
        self.cur.execute("SELECT * FROM users")
        print(self.cur.fetchall())
        return "Added successfully"

    def user_update_model(self, data):
        self.cur.execute(f"""UPDATE users SET name="{data['name']}", email="{data['email']}", role="{data['role']}", phone="{data['phone']}", password="{data['password']}" WHERE id="{data['id']}" """)
        if self.cur.rowcount>0:
            return "Updates Successfully"
        else:
            return "Nothing to Update"

    def user_delete_model(self, id):
        self.cur.execute(f""" DELETE FROM users WHERE id = {id} """)
        if self.cur.rowcount>0:
            return "Deleted Successfully"
        else:
            return "Nothing to delete"