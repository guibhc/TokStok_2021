from selenium import webdriver
import time
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://www.tokstok.com.br'

# Acessa o site
#driver.implicitly_wait(10)
driver.get(url)
time.sleep(5)

# Primeira tarefa
print('Primeira tarefa')
categoria = "Móveis"
driver.find_element_by_xpath("//div[contains(text(), 'Móveis')]").click()
time.sleep(5)

# Escolher um sofa
print('Escolher um sofa')
driver.find_element_by_xpath("//span[contains(text(), 'Sofás')]").click()
time.sleep(5)

# CLica no sexto sofa (pageDown para ter o elemento visivel)
print('CLica no sexto sofa (pageDown para ter o elemento visivel)')
body = driver.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="gallery-layout-container"]/div[6]/section').click()
time.sleep(5)

#Pega o nome do produto
print('Pega o nome do produto')
nome_produto = driver.find_element_by_class_name("vtex-store-components-3-x-productBrand").text

# CLica no botão de compra
print('CLica no botão de compra')
driver.find_element_by_xpath("//span[contains(text(), 'Comprar')]").click() 
time.sleep(5)

# CLica no botão de ir para o carrinho
print('CLica no botão de ir para o carrinho')
driver.find_element_by_xpath("//span[contains(text(), 'Ir para o carrinho')]").click() 
time.sleep(5)

# Verificar o carrinho
print('Verificar o carrinho')
nome_produto_carrinho = driver.find_element_by_xpath("//td[@class='product-name']//a").text.upper()
time.sleep(5)

if nome_produto == nome_produto_carrinho:
    print('Adicionou com sucesso')
else:
    print('Produto do carrinho nao e o mesmo do buscado')

