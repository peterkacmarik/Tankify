import flet as ft



def page_logo():
    return ft.Container(
        padding=ft.padding.only(left=20, right=20, top=0, bottom=0),
        alignment=ft.alignment.center,
        # border=ft.border.all(0),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    src="/logo/fuel_logo_transparent_1024_crop_128.png",
                    # src="https://play-lh.googleusercontent.com/I1u3j-M8szNVPKlCshG7Ra2k4tis-aNlOF5oFUyGVhxSUjFnMUy3Y_LDtIYKoFRrWwc",
                    width=128,
                    height=128,
                )
            ]
        )
    )
        # padding=ft.padding.only(left=20, right=20, top=0, bottom=0),
        # alignment=ft.alignment.center,
        # border=ft.border.all(0),
        # content=ft.Image(
        #     src=f"/logo/logo_drivvo.png",
        #     width=130,
        #     height=130,
        # ),
    # )