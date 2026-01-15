from django import forms

class loginForm(forms.Form):
    nome_login =forms.CharField(
        label="Nome de login",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control", "placeholder" : "Digite seu nome de login"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control", "placeholder" : "Digite sua senha"
            }
        )
    )

class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control", "placeholder" : "Digite seu nome de usuário"
            }
        )
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control", "placeholder" : "Digite seu e-mail"
            }
        )
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control", "placeholder" : "Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control", "placeholder" : "Digite sua senha novamente"
            }
        )
    )

    def clean_cadastro_nome(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()

            if " " in nome:
                raise forms.ValidationError("O nome de usuário não pode conter espaços.")
            else:
                return nome        
        

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")
    
        if senha_1 != senha_2:
            raise forms.ValidationError("As senhas não coincidem.")
        
        else:
            return senha_2
        