##Estudiar los precios de los resultados##

import pandas as pd
import re
ScrapingLiverpool = pd.read_csv("/home/luis/Documentos/UNAM/CuartoSemestre/Sociedad de la Información/WebScraping/liverpoolXBOXOne.csv")
ScrapingSears = pd.read_csv("/home/luis/Documentos/UNAM/CuartoSemestre/Sociedad de la Información/WebScraping/scrappingSears.csv")


ConsolasLiverpool = ScrapingLiverpool[ScrapingLiverpool['ProductName'].str.contains('CONSOLA',flags=re.IGNORECASE)]

ConsolasSears = ScrapingSears[ScrapingSears['Nombre del producto'].str.contains('CONSOLA',flags=re.IGNORECASE)]

print("Liverpool:","\n",ConsolasLiverpool,"\n\n","Sears:","\n",ConsolasSears,"\n\n")

##Buscar el valor mas pequeño y comparar##

minLiverpool = ConsolasLiverpool['Price'].min()
minSears = ConsolasSears['Precios'].min()

if minLiverpool < minSears:
    print ("En Liverpool esta mas barato el XBOX One, esta en: ",minLiverpool)
elif minSears < minLiverpool: 
    print("En Sears esta mas barato el XBOX One, esta en: ",minSears)
else:
    print("El Xbox One cuesta lo mismo en Sears y Liverpool.")
