from peewee import SqliteDatabase, Model, CharField, TextField, DateField

db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Data(BaseModel):
    key = CharField()
    value = CharField()

    @classmethod
    def get_value(cls, key):
        return cls.get(key=key).value

# Create your models here.
class Cliente(BaseModel):
    nome = CharField(max_length=50)
    data_nasc = DateField()
    tel = CharField(max_length=20)
    email = CharField()
    endereco = TextField()
    cpf = CharField(max_length=14)
    rg = CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome

    def get_data(self) -> dict:
        return self.__dict__['__data__']

db.connect()

db.create_tables([Cliente, Data], safe=True)