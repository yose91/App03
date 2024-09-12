import flet as ft


def main(page: ft.Page):
    page.title="Calculadora"
    page.bgcolor="blue"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    lbl1=ft.text("Calculadora",
                style=ft.TextStyle(size=48,height="bold"))
    img1=ft.Image(src="ouija.png",width=200,height=200)
    btnSumar=ft.ElevatedButton("Sumar",
                            color="red",
                            width=50,
                            height=50
                            )
    
    btnBorrar=ft.ElevatedButton("Borrar",
                                color="pink",
                                width=100,
                                height=50
                                )
    def calcular_suma(txt_num1, txt_num2, txt_resultado):
        try:
            num1 = float(txt_num1.value.strip())
            num2 = float(txt_num2.value.strip())
            resultado = num1 + num2
            txt_resultado.value = f"Resultado: {resultado}"
        except ValueError:
            txt_resultado.value = "Error: Ingresa valores correctos"
    
    page.add(
        ft.Column(
            [
                lbl1,
                img1,
                ft.Row(
                    [btnSumar,btnBorrar]
                )
            ]
        )
    )

ft.app(main)
