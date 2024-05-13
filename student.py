from database import Database


class Student(Database):
    def __init__(self):
        super().__init__()

    def search(self):
        self.query("select * from student")
        print(self.get_all())

    def retrieve(self, id):
        self.query("SELECT * FROM student WHERE id =" + id)
        print(self.get_one())

    def create(self, name, gender, email):
        self.query(f"INSERT INTO student (Name, Gender, Email) VALUES ('{name}', '{gender}', '{email}') ")
        self.connection.commit()

    def update(self, id, email):
        self.query(f"UPDATE student SET Email = '{email}' WHERE Id= '{id}' ")
        self.connection.commit()

    def delete(self, id):
        self.query(f"DELETE FROM student WHERE Id = '{id}' ")
        self.connection.commit()


