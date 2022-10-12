import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def enviar_email(email: str, senha: str, destino: str, assunto: str, body: str):

    service = Service(ChromeDriverManager().install())
    nav = webdriver.Chrome(service=service)
    nav.maximize_window()
    nav.get(
        "https://login.yahoo.com/?.intl=br&.lang=pt-BR&src=homepage&activity=ybar-signin&pspid=2142170772&done=https%3A%2F%2Fbr.yahoo.com%2F&add=1")
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="login-username"]').send_keys(email)
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="login-signin"]').click()
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="login-passwd"]').send_keys(senha)
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="login-signin"]').click()
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="ybarMailLink"]/span[1]').click()
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="app"]/div[2]/div/div[1]/nav/div/div[1]/a').click()
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="message-to-field"]').send_keys(destino)
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="mail-app-component"]/div/div/div/div[1]/div[3]/div/div/input').send_keys(assunto)
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="editor-container"]/div[1]').send_keys(body)
    time.sleep(5)
    nav.find_element("xpath", '//*[@id="mail-app-component"]/div/div/div/div[2]/div[2]/div/button/span').click()
    time.sleep(5)
