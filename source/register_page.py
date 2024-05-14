from .control import Control
from .form_page import FormPage
from .models import Cliente

class RegisterPage(FormPage):
    title_text = 'CADASTRO DO CLIENTE'
    main_button_text = 'CADASTRAR'
    def on_submit(self, e):
        data = self.get_data()
        error_message = Control.validate_form(data)
        if error_message is not None:
            return e.page.snack_bar.message(error_message, 'error')

        self.main_button.disabled = True

        data['id'] = Cliente.create(**data)

        e.page.data = {'instruction': {'create': data}}

        e.page.snack_bar.message('Cliente criado com sucesso!', 'success')
        return e.page.go('/clients')

    def on_pre_view(self):
        self.main_button.disabled = False
        self.name_field.value = ''
        self.date_field.value = ''
        self.tel_field.value = ''
        self.email_field.value = ''
        self.address_field.value = ''
        self.cpf_field.value = ''
        self.rg_field.value = ''