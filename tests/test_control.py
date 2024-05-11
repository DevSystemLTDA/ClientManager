def test_validate_form(control_obj):
    assert control_obj.validate_form({}) == 'Preencha todos os campos!'

    test_data = {
        'nome': 'Teste',
        'data_nasc': '08/07/2004',
        'endereco': 'Teste',
        'email': 'teste',
        'tel': '8888888888',
        'cpf': '1',
        'rg': ''
    }
    assert control_obj.validate_form({}) == 'Preencha todos os campos!'

    test_data['rg'] = '1'
    assert control_obj.validate_form(test_data) == 'Digite seu nome completo!'

    test_data['nome'] = 'Nome Completo'
    assert control_obj.validate_form(test_data) == 'Email inválido!'

    test_data['email'] = 'email@gmail'
    assert control_obj.validate_form(test_data) == 'Email inválido!'

    test_data['email'] = 'email@gmail.com'
    assert control_obj.validate_form(test_data) == 'CPF inválido!'

    test_data['cpf'] = '123.123.123-45'
    assert control_obj.validate_form(test_data) == 'Digite apenas os dígitos do CPF!'

    test_data['cpf'] = '12312312345'
    assert control_obj.validate_form(test_data) == 'RG inválido!'

    test_data['rg'] = '1234123123-4'
    assert control_obj.validate_form(test_data) == 'Digite apenas os dígitos do RG!'

    test_data['rg'] = '12341231234'
    assert control_obj.validate_form(test_data) is None