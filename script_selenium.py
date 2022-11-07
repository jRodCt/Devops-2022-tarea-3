# Importamos bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# en pc debí descargar ejecutable de chromedriver versión 106
#driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver = webdriver.Chrome('./chromedriver', options=chrome_options)

driver.get("http://172.19.0.2:8080/")

# Nueva película 1
# Top Gun: Maverick
agregar = driver.find_element(By.ID, "add-movie")
agregar.click()

title = driver.find_element(By.NAME, "title")
year = driver.find_element(By.NAME, "year")
director = driver.find_element(By.NAME, "director")
rating = driver.find_element(By.NAME, "rating")
review = driver.find_element(By.NAME, "review")


title.send_keys("Top Gun: Maverick")
year.send_keys("2022")
director.send_keys("Joseph Kosinski")
rating.send_keys("7.3/10")
review.send_keys("Maverick, quien lleva 30 años de servicio, es ahora instructor de pilotos militares. " 
                 + "Una última misión, un sacrificio final, obliga a este maestro de los cielos a enfrentar las "
                 + "heridas abiertas del pasado y sus temores más profundos.")

grabar = driver.find_element(By.CLASS_NAME, "btn-primary")
grabar.click()

# Nueva película 2
# El señor de los anillos: la comunidad del anillo 
agregar = driver.find_element(By.ID, "add-movie")
agregar.click()

title = driver.find_element(By.NAME, "title")
year = driver.find_element(By.NAME, "year")
director = driver.find_element(By.NAME, "director")
rating = driver.find_element(By.NAME, "rating")
review = driver.find_element(By.NAME, "review")

title.send_keys("El señor de los anillos: la comunidad del anillo ")
year.send_keys("2001")
director.send_keys("Peter Jackson")
rating.send_keys("8.8/10")
review.send_keys("Frodo Bolsón es un hobbit al que su tío Bilbo hace portador del poderoso Anillo Único, "
                 + "capaz de otorgar un poder ilimitado al que la posea, con la finalidad de destruirlo. "
                 + "Sin embargo, fuerzas malignas muy poderosas quieren arrebatárselo.")

grabar = driver.find_element(By.CLASS_NAME, "btn-primary")
grabar.click()


# Traducción de descripciones de películas Dune y Elvis
# Se utiliza servicio googletrans
# pip install googletrans
import googletrans
from googletrans import Translator

translator = Translator()
translation = translator.translate("Dune", dest='es')
print(translation.text)

# Traducir Dune
dune = driver.find_element(By.XPATH, "/html/body/div/div[1]/h3/a")
dune.click()
review = driver.find_element(By.NAME, "review")
review_dune=review.get_attribute("value")
#print(review_dune)
t_dune = translator.translate(review_dune, dest="es")
review.clear()
review.send_keys(t_dune.text)
grabar = driver.find_element(By.CLASS_NAME, "btn-primary")
grabar.click()

# Traducir Elvis
elvis = driver.find_element(By.XPATH, "/html/body/div/div[2]/h3/a")
elvis.click()
review = driver.find_element(By.NAME, "review")
review_elvis=review.get_attribute("value")
t_elvis = translator.translate(review_elvis, dest="es")
review.clear()
review.send_keys(t_elvis.text)
grabar = driver.find_element(By.CLASS_NAME, "btn-primary")
grabar.click()