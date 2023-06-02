import flet as ft
import page_options

def main(page: ft.Page):
    page.title = "Home"

    page.window_center()
    page.window_width = 400

    def go_to_options(e):
        page.route = "/page_options"
        page.update()
        
    btn = ft.ElevatedButton("Options", on_click=go_to_options)
    page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    btn
                ],
            )
        )
        if page.route == "/page_options":
            page.views.append(
                page_options.main(page)
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)