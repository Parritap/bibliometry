from selenium import webdriver
from decouple import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import rispy
import re


class ScraperSage:
    def __init__(self, unique_file_path, duplicate_file_path):
        self.download_path = (
            "C:\\Users\\lanth\\Desktop\\Analisis_De_Algortimos_Proyecto"
        )
        self.unique_file_path = unique_file_path
        self.duplicate_file_path = duplicate_file_path
        self.brave_path = (
            "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        )

        chrome_options = Options()
        chrome_options.binary_location = self.brave_path
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disabled-gpu")
        chrome_options.add_argument(
            f"--download-default-directory={self.download_path}"
        )
        chrome_options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": self.download_path,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            },
        )

        self.driver = webdriver.Chrome(options=chrome_options)

    def is_download_complete(self, directory):
        files = os.listdir(directory)
        for f in files:
            if f.endswith(".crdownload"):
                return False
        return True

    def corregir_espacios_ris(self, archivo_entrada, archivo_salida):
        with open(archivo_entrada, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        lineas_corregidas = []
        for linea in lineas:
            linea_corregida = re.sub(r"^([A-Z0-9]{2})\s*-\s*", r"\1  - ", linea.strip())
            lineas_corregidas.append(linea_corregida + "\n")

        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.writelines(lineas_corregidas)

        print(f"Archivo corregido guardado como: {archivo_salida}")

    def process_ris_file(self):
        all_files = [f for f in os.listdir(self.download_path) if f.endswith(".ris")]

        if not all_files:
            print("No se encontraron archivos RIS para procesar.")
            return

        unique_articles = {}
        duplicate_articles = {}

        for file in all_files:
            file_path = os.path.join(self.download_path, file)

            if os.path.getsize(file_path) == 0:
                print(f"El archivo {file} está vacío.")
                continue

            try:
                corrected_file_path = file_path + ".corrected"
                self.corregir_espacios_ris(file_path, corrected_file_path)

                with open(corrected_file_path, "r", encoding="utf-8") as f:
                    entries = rispy.load(f)

                    for entry in entries:
                        identifier = entry.get("DO", None) or entry.get("UR", None)

                        if identifier:
                            if identifier in unique_articles:
                                duplicate_articles[identifier] = entry
                            else:
                                unique_articles[identifier] = entry
                        else:
                            unique_articles[f"noidentifier{len(unique_articles)}"] = (
                                entry
                            )

                os.remove(corrected_file_path)

            except Exception as e:
                print(f"Error al procesar el archivo {file}: {e}")
                continue

        if unique_articles:
            with open(self.unique_file_path, "a", encoding="utf-8") as unique_file:
                rispy.dump(list(unique_articles.values()), unique_file)
            print("Artículos únicos añadidos al archivo.")
        else:
            print("No se encontraron artículos únicos.")

        if duplicate_articles:
            with open(
                self.duplicate_file_path, "a", encoding="utf-8"
            ) as duplicate_file:
                rispy.dump(list(duplicate_articles.values()), duplicate_file)
            print("Artículos repetidos añadidos al archivo.")
        else:
            print("No se encontraron artículos duplicados.")

    def run(self):
        self.driver.get("https://library.uniquindio.edu.co/databases")

        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "div.onload-background")
            )
        )

        fac_ingenieria_access = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//summary[@role='button'][contains(., 'Fac. Ingeniería')]")
            )
        )
        fac_ingenieria_access.click()

        sage_link = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located(
                (
                    By.PARTIAL_LINK_TEXT,
                    "SAGE Revistas Consorcio Colombia - (DESCUBRIDOR)",
                )
            )
        )
        sage_link.click()

        google_button = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.ID, "btn-google"))
        )
        google_button.click()

        email_field = WebDriverWait(self.driver, 70).until(
            EC.element_to_be_clickable((By.ID, "identifierId"))
        )
        email_field.send_keys(config("CORREO_INSTITUCIONAL"))
        email_field.send_keys(Keys.ENTER)

        password_field = WebDriverWait(self.driver, 70).until(
            EC.presence_of_element_located((By.NAME, "Passwd"))
        )
        password_field.send_keys(config("PASSWORD_INSTITUCIONAL"))
        password_field.send_keys(Keys.ENTER)

        sage_box = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                (By.ID, "AllField35ea26a9-ec16-4bde-9652-17b798d5b6750")
            )
        )

        sage_box = self.driver.find_element(
            By.ID, "AllField35ea26a9-ec16-4bde-9652-17b798d5b6750"
        )
        sage_box.send_keys("computational thinking")
        sage_box.send_keys(Keys.ENTER)

        pagina_actual = 1
        numero_pagina = 10
        while pagina_actual <= numero_pagina:
            checkbox = WebDriverWait(self.driver, 70).until(
                EC.presence_of_element_located((By.ID, "action-bar-select-all"))
            )
            if checkbox.is_selected():
                self.driver.execute_script("arguments[0].click();", checkbox)

            self.driver.execute_script("arguments[0].click();", checkbox)

            time.sleep(1)

            download_link = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "a[data-id='srp-export-citations']")
                )
            )

            download_link.click()

            time.sleep(5)

            export_ris_button = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "a.btn.btn-secondary.download__btn")
                )
            )

            ActionChains(self.driver).move_to_element(
                export_ris_button
            ).click().perform()

            while not self.is_download_complete(self.download_path):
                print("Esperando a que la descarga termine...")

            time.sleep(2)

            time.sleep(1)

            close_popup_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button[data-dismiss='modal']")
                )
            )
            ActionChains(self.driver).move_to_element(
                close_popup_button
            ).click().perform()

            time.sleep(5)

            try:
                next_page_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.CSS_SELECTOR,
                            "li.page-item__arrow--next.pagination__item a",
                        )
                    )
                )

                if next_page_button:
                    next_page_button.click()
                    time.sleep(3)
                else:
                    print("No hay siguiente página.")
                    break
                time.sleep(2)
            except Exception as e:
                print("Error al intentar ir a la siguiente página:", e)
                break
            pagina_actual += 1

        self.process_ris_file()
