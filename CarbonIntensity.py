import requests
import matplotlib.pyplot as plt
import numpy as np

responseIntensity = requests.get('https://api.carbonintensity.org.uk/intensity')
dictIntensity = responseIntensity.json()
for item in dictIntensity['data']:
    intensity = item['intensity']
    print(intensity['forecast'])
    print(intensity['actual'])
    print(intensity['index'])

responseMix = requests.get('https://api.carbonintensity.org.uk/generation')
dictMix = responseMix.json()
data = dictMix['data']
generationalMix = data['generationmix']
fuelList = []
percList = []
print(generationalMix)
print(type(generationalMix))
for item in generationalMix:
    fuelList.append(item['fuel'])
    percList.append(item['perc'])
y = np.array(percList)
mylabels = fuelList
plt.pie(y, labels = mylabels, startangle = 90)
plt.show()


