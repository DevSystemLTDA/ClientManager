from source.models import db, Data, Cliente

def test_db_connection():
    assert db.is_closed() is False

def test_table_creation():
    assert db.table_exists('cliente')
    assert db.table_exists('data')

def test_data_model():
    data = Data(key='test_key', value='test_value')
    data.save()
    assert Data.get_value('test_key') == 'test_value'
    data.delete_instance()
    assert Data.get_or_none(key='test_key') is None

def test_cliente_model():
    cliente = Cliente(
        nome='John Doe',
        data_nasc='1990-01-01',
        tel='1234567890',
        email='johndoe@example.com',
        endereco='123 Main St',
        cpf='12345678909',
        rg='1234567890'
    )
    cliente.save()
    assert str(cliente) == 'John Doe'
    assert cliente.get_data() == {
        'id': cliente.id,
        'nome': 'John Doe',
        'data_nasc': '1990-01-01',
        'tel': '1234567890',
        'email': 'johndoe@example.com',
        'endereco': '123 Main St',
        'cpf': '12345678909',
        'rg': '1234567890'
    }
    cliente.delete_instance()
    assert Cliente.get_or_none(id=cliente.id) is None