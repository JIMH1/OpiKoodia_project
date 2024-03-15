'''
Eka versio ledin ja napin ohjaamiseen. noi placeholderit on paikalla siksi, että näkisin nopeasti, mihin riveihin olis tulossa monistusta.
Kytkentä on aika simppeli, löytyy seuraavan linkin alta:

https://www.youtube.com/watch?v=yL5BNA_Ex6s
9min 52s
'''

#Kiitos Paul McWhorter RaspPi ep 8
from time import sleep
import RPi.GPIO as GPIO


delay = 0.1#Tähän ei kannata koskea, jos laittaa esim 1, ei nappi välttämättä reagoi puskemiseen

#Näitä toki voi muuttaa, mutta en menis mielellään koskemaan. Menee sekavaks nopeasti.
    #Tulevaisuuden kannalta pikemminki "inPinOne, outPinOne, inPinTwo, outPinTwo jne"
inpin = 40
outpin = 38
#PlaceHolder
#PlaceHolder
#PlaceHolder
#PlaceHolder
#PlaceHolder
#PlaceHolder

GPIO.setmode(GPIO.BOARD)#Ei mitää hajua tästä. Tuskin tarvii monistaa


GPIO.setup(outpin, GPIO.OUT)
#tän voi laittaa PUD_DOWNiksi, mutta se ei oikeen toimi halutulla tavalla. Vaatii vissiin myös, että vaihtaa try blockin sisällä logiikan päinvastaiseks
GPIO.setup(inpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#PlaceHolder
#PlaceHolder
#PlaceHolder


GPIO.output(outpin, GPIO.LOW)
#PlaceHolder
#PlaceHolder
#PlaceHolder

ledState = False


def turnOnLed(ledPin):
    GPIO.output(ledPin, GPIO.HIGH)
    
def turnOffLed(ledPin):
    GPIO.output(ledPin, GPIO.LOW)
    
def toggleLed(ledPin):
    global ledState
    ledState = not ledState
    
    if ledState:
        turnOnLed(ledPin)
    else:
        turnOffLed(ledPin)
    
'''
#YLEMPI TRY BLOKKI turnOnLedille ja turnOffLedille
try:
    while True:
        #turnOffLed(outpin)
        readVal = GPIO.input(inpin)
        print(readVal)
        if readVal == 0:
            turnOnLed(outpin)
        else:
            turnOffLed(outpin)
    
        sleep(delay)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO cleaned up")
    
'''
#ALEMPI TRY BLOKK toggleLedille
try:
    while True:
        readVal = GPIO.input(inpin)
        #PlaceHolder
        #PlaceHolder
        #PlaceHolder
        
        print("Value of readVal is", readVal)#Tässä bugi. Printtaa aina 1 paitsi jos painat, mut heti sen jälkeen taas 1
        #PlaceHolder
        #PlaceHolder
        #PlaceHolder
        
        if readVal == 0:
            toggleLed(outpin)
            
            #Tää fixaa välkkymisen, jos nappi on pohjassa
            while GPIO.input(inpin) == 0:
                pass
        #PlaceHolder
        #PlaceHolder
        #PlaceHolder
            
            
        sleep(delay)
        
except KeyboardInterrupt:#tää käynnistyy painamalla Ctrl + C
    GPIO.cleanup()
    print("GPIO cleaned up")
