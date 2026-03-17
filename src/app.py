import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment
from flet.controls.border_radius import horizontal

def main(page: flet.Page):
    # configurações
    page.title = "Primeira api"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700
    # funções
    def salvar_nome():
        text.value = f'Olá {input_nome.value}  {input_sobrenome.value}'
        page.update()

    def salvar_numero(e):  # O argumento deve ser declarado aqui
        try:
            numero = int(int_numero.value)
            tipo = "par" if numero % 2 == 0 else "ímpar"
            text.value = f'O número {numero} é {tipo}'
        except ValueError:
            text.value = "Por favor, digite um número válido"
        page.update()

    def verificar_maioridade(e):
        try:
            # Converte o texto para número inteiro
            idade = int(int_idade.value)

            if idade >= 18:
                text.value = f"Você tem {idade} anos e é Maior de Idade! "
                page.update()

            else:
                text.value = f"Você tem {idade} anos e é Menor de Idade! "
                page.update()

        except ValueError:
            text.value = "Erro: Digite uma idade válida (números)."
            page.update()

        page.update()

    # componentes
    text = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    int_numero = TextField(label="Numero")
    int_idade = TextField(label="Sua Idade")


    btn_idade = OutlinedButton("Verificar Maioridade", on_click=verificar_maioridade)
    btn_salvar= OutlinedButton("Salvar_nome", on_click=salvar_nome)
    btn_salvar1 = OutlinedButton("Salvar_número", on_click=salvar_numero)

    #construção de tala

    page.add(
        Column([
            input_nome,
            input_sobrenome,
            int_numero,
            int_idade,
            btn_salvar,
            btn_salvar1,
            btn_idade,
            text
        ],
        width=400,
        horizontal_alignment = CrossAxisAlignment.CENTER

        )

    )

flet.app(main)

