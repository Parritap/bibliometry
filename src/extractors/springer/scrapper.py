from playwright.sync_api import sync_playwright
import os
import sys


# For springer
def download_files(link, download_path):
    pagina = 0

    os.makedirs(download_path, exist_ok=True)  # Crear la carpeta si no existe

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(link)

        page.wait_for_timeout(5000)  # Esperar a que la página cargue

        while True:
            try:
                page.wait_for_selector("ol.u-list-reset", timeout=120000)
            except:
                print("Error: No se encontró la lista de resultados.")
                break

            for contador in range(1, 21):
                print(f"Procesando el artículo {pagina * 20 + contador}...")

                link = page.query_selector(f"a[data-track-context='{contador}']")
                if not link:
                    print(
                        f"Advertencia: No se encontró el enlace para el contador {contador}"
                    )
                    continue

                link.click()
                page.wait_for_selector(
                    "div.c-bibliographic-information__column p.c-bibliographic-information__download-citation",
                    timeout=60000,
                )

                download_button = page.query_selector(
                    "div.c-bibliographic-information__column p.c-bibliographic-information__download-citation a"
                )
                if not download_button:
                    print("Advertencia: No se encontró el botón de descarga.")
                    page.go_back()
                    page.wait_for_load_state("load")
                    continue

                with page.expect_download() as download_info:
                    download_button.click()
                    download = download_info.value
                    filename = os.path.join(download_path, download.suggested_filename)
                    download.save_as(filename)

                page.go_back()
                page.wait_for_load_state("load")

            pagina += 1

            next_page = page.query_selector("a.eds-c-pagination__link[rel='next']")
            if not next_page:
                print("No hay más páginas disponibles.")
                break

            page.wait_for_timeout(2000)  # Pequeña pausa antes de hacer click
            next_page.click()
            page.wait_for_load_state("load")

        browser.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <link> <ruta_descarga>")
        sys.exit(1)

    link = sys.argv[1]
    download_path = sys.argv[2]

    download_files(link, download_path)
