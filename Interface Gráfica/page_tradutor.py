import flet as ft
import time
import sys
import keyboard as kb
sys.path.insert(1, "./functions")

import f_tradutor as td

def main(page):
    
    img_translate = ft.Image(
        src=f"images/translate.svg",
        width=30,
        height=30,
        color= "#DA2693",
    )

    txt_title = ft.Text("Tradutor", 
                        weight=ft.FontWeight.BOLD,
                        size=15)

    title = ft.Container(
        content=ft.Row(
        [img_translate, txt_title ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=5
        ), 
        alignment=ft.alignment.center
    )


    def terminou_de_digitar(e):
        if frase.value.endswith(" "):
            terminou = False
        else:
            terminou = True

        return terminou

    def traduz(e): 
        if frase.value != "":
            time.sleep(1.5)
            if terminou_de_digitar(e) == True:
                traducao = td.Tradutor(td.Tradutor.verifica_idioma(from_lang),td.Tradutor.verifica_idioma(to_lang), frase.value)
                txt_traduzido.value = traducao.traduzir()
                page.update()
        else:
            txt_traduzido.value = ""
            page.update()

    from_lang=ft.Dropdown(
        label="Traduzir de",
        width=350,
        border_color=ft.colors.WHITE,
        options=[
            ft.dropdown.Option("Inglês"),
            ft.dropdown.Option("Português"),
            ft.dropdown.Option("Chinês"),
            ft.dropdown.Option("Espanhol"),
            ft.dropdown.Option("Francês"),
            ft.dropdown.Option("Árabe"),
            ft.dropdown.Option("Russo"),
        ],
        on_change=traduz
        )
    

    to_lang=ft.Dropdown(
        label="Traduzir para",
        width=350,
        border_color=ft.colors.WHITE,
        options=[
            ft.dropdown.Option("Inglês"),
            ft.dropdown.Option("Português"),
            ft.dropdown.Option("Chinês"),
            ft.dropdown.Option("Espanhol"),
            ft.dropdown.Option("Francês"),
            ft.dropdown.Option("Árabe"),
            ft.dropdown.Option("Russo"),
        ],
        on_change=traduz
        )
    

    ltb_from_lang = ft.Container(
        content=from_lang,
        alignment=ft.alignment.center
    )

    ltb_to_lang = ft.Container(
        content=to_lang,
        alignment=ft.alignment.center
    )
   
    frase = ft.TextField(
        label="Digite o Texto",
        border_color=ft.colors.WHITE,
        multiline=True,
        height=80,
        width=350,
        on_change=traduz
        )

    tb_entrada = ft.Container(
        content=frase,
        alignment=ft.alignment.center
    )

    txt_traduzido = ft.Text("",
                            weight=ft.FontWeight.BOLD,
                            size=20)

    container_txt_traduzido = ft.Container(
        content=ft.Row([
            txt_traduzido
        ]),
        height=370,
        bgcolor="#490596",
        alignment=ft.alignment.top_left,
        border_radius=10,
        padding=10
    )

    coluna = ft.Column(
        controls=[
            title,
            ltb_from_lang,
            ltb_to_lang,
            tb_entrada,
            container_txt_traduzido
        ],
        alignment=ft.MainAxisAlignment.START,
        
    )

    main_container = ft.Container(
        content=coluna,
        width=400,
        height=660,
        border_radius=25,
        bgcolor= "#260053",
        padding=12
    )
     
    view = ft.View(
        "/page_tradutor",
        [
            page.main_container
        ]
    )

    return view
