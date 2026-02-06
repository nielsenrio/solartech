from django import forms
from django.core.exceptions import ValidationError

class ContatoForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        min_length=3,
        required=True,
        widget=forms.TextInput(attrs= {
            'placeholder': 'Digite seu nome',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        widget = forms.TextInput(attrs={
            'placeholder': 'Digite seu email',
            'class': 'form-control'
        })
    )

    mensagem = forms.CharField(
        label='Mensagem',
        min_length=10,
        max_length=300,
        widget=forms.Textarea(attrs={
            'placeholder': 'Digite sua mensagem',
            'class': 'form-control',
            'rows': 4
        })
    )

    def clean_mensagem(self):
        mensagem = self.cleaned_data.get('mensagem', "").strip()
        quantidade_palavras = len(mensagem.split())

        if quantidade_palavras < 5:
            raise ValidationError("A mensagem deve conter pelo menos 5 palavras.")

        return mensagem

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', "").strip()
        tamanho_nome = len(nome.split())

        if tamanho_nome < 2:
            raise ValidationError("Informe o nome e sobrenome ou o nome composto.")

        return nome


# Parte 1 – Entendendo o Form existente (aquecimento)
# 1.Em qual arquivo está definida a classe do formulário?
#   Resp.:'forms.py'.
#
# 2.Qual classe do Django ela estende?
#   Resp.: forms.Form / Meu entendimento é que tratasse de um formulário aonde 'os dados'
#          são apenas coletados para validação por metodo "POST" do HTML.
#
# 3.Onde ocorre a validação dos dados?
#   Resp.: A validação ocorre no back-end.
#
# 4.Em que momento clean_mensagem é executado?
#   Resp.: Quando 'form.is_valid()' é executado.

