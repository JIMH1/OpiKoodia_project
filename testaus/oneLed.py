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
inpin1 = 40
outpin1 = 38
inpin2 = 37
outpin2 = 35
#PlaceHolder3
#PlaceHolder3
#PlaceHolder4
#PlaceHolder4

GPIO.setmode(GPIO.BOARD)#Ei mitää hajua tästä. Tuskin tarvii monistaa


GPIO.setup(outpin1, GPIO.OUT)
GPIO.setup(outpin2, GPIO.OUT)
#PlaceHolder3
#PlaceHolder4
#tän voi laittaa PUD_DOWNiksi, mutta se ei oikeen toimi halutulla tavalla. Vaatii vissiin myös, että vaihtaa try blockin sisällä logiikan päinvastaiseks
GPIO.setup(inpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(inpin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#PlaceHolder3
#PlaceHolder4


GPIO.output(outpin1, GPIO.LOW)
GPIO.output(outpin2, GPIO.LOW)
#PlaceHolder3
#PlaceHolder4

ledState1 = False
ledState2 = False
#PlaceHolde3
#PlaceHolder4


def turnOnLed(ledPin):
    GPIO.output(ledPin, GPIO.HIGH)
    
def turnOffLed(ledPin):
    GPIO.output(ledPin, GPIO.LOW)
    
def toggleLed(ledPin, ledState):
    #global ledState
    ledState = not ledState
    
    if ledState:
        turnOnLed(ledPin)
    else:
        turnOffLed(ledPin)
    
    return ledState
    
'''
#YLEMPI TRY BLOKKI turnOnLedille ja turnOffLedille
try:
    while True:
        #turnOffLed(outpin1)
        readVal = GPIO.input(inpin1)
        print(readVal)
        if readVal == 0:
            turnOnLed(outpin1)
        else:
            turnOffLed(outpin1)
    
        sleep(delay)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO cleaned up")
    
'''
#ALEMPI TRY BLOKK toggleLedille
try:
    while True:
        readVal1 = GPIO.input(inpin1)
        readVal2 = GPIO.input(inpin2)
        #PlaceHolder
        #PlaceHolder
        
        print("readVal1 is:", readVal1, "readVal2 is:", readVal2)#Tässä bugi. Printtaa aina 1 paitsi jos painat, mut heti sen jälkeen taas 1
        #PlaceHolder
        #PlaceHolder
        #PlaceHolder
        
        if readVal1 == 0:
            ledState1 = toggleLed(outpin1, ledState1)
            sleep(delay)#ettei paina monesti

        if readVal2 == 0:
            ledState2 = toggleLed(outpin2, ledState2)
            sleep(delay)#ettei paina monesti

        #PlaceHolder
        #PlaceHolder
            
            
        sleep(delay)
        
except KeyboardInterrupt:#tää käynnistyy painamalla Ctrl + C
    GPIO.cleanup()
    print("GPIO cleaned up")

