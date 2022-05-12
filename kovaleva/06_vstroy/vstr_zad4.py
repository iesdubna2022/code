import json

class DB:
    def __init__(self, File):
        """Конструктор"""
        self.File = File
    
    def list(self):
        """
        Получение списка доступных ключей
        """
        return self.conn.keys()
    
    def set(self, db_name, key):
        """
        Установление ключа значения
        """
        self.conn[key] = db_name

    def get(self, key):
        """
        Получение значения по ключу
        """
        return self.conn[key]

    def __enter__(self):
        """
        Открываем подключение с базой данных.
        """
        with open(self.File) as files:
            self.conn = json.load(files)
        
        return self

    def __exit__(self):
        """
        Закрываем подключение.
        """
        with open(self.File, "w") as files:
            json.dump(self.conn, files)
        
with DB("db.json") as db:
    print(db.list())
    db.set("Reed", "Alice")
    print(db.get("Reed"))
