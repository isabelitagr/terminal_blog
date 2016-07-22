import uuid
import datetime

from database import Database
from models.post import Post


class Blog(object):

    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id


    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date or leave blank for today (in format DDMMYYYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y") #el string que pasan de fecha lo formateo a datetime. string parse time (strptime)
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date
                    )

        post.save_to_mongo()



    def get_posts(self):
        return Post.from_blog(self.id)


    def save_to_mongo(self):
        Database.insert(collection='blogs',  # vamos a poner en esta coleccion
                        data=self.json())


    def json(self):
        return{
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "id": self.id
        }


    @classmethod
    def from_mongo(cls, id):    #se usa por si cambiamos el nombre de la clase no importe
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})  # no nos alcannza con esto porque devolveria solo el json con los datos pero no los posts
                                                        # por eso se instancia un Blog y se lo devuelve.
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])
        # nos devuelve un OBJETO, no info!!!

