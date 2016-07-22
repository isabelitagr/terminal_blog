import uuid
from database import Database
import datetime

class Post(object): #Post hereda de la clase object de python

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None): # le ponemos a id un valor por defecto asi si no le pasamos id por parametro toma valor none
                                                                        # solo se pueden poner paramotros con valor por dfecto al final
                                                                        # a date le paso por defecto el dia de hoy
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id # del moduo uuid usamos el metodo uuid4() que genera  de manera random un id y lo transforma en un string hexadecimal de 32 bits
                                    # si no le paso id creo uno con uuid si le paso un id uso el id que le paso

    def save_to_mongo(self):
        Database.insert(collection='posts',   # vamos a poner en esta coleccion
                        data=self.json())     # esta data

    def json(self): #creates a json representarion of the post --> es un set del tipo key:value
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):  #nos devuelve un OBJETO, no info!!!
        post_data = Database.find_one(collection='posts', query={'id': id}) # no hace falta en los parametros aclarar el nombre pero se hace para legibilidad
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])


    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
