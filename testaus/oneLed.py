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
#inpin3 = 
#outpin3 = 
#inpin4 = 
#outpin4 = 

GPIO.setmode(GPIO.BOARD)#Ei mitää hajua tästä. Tuskin tarvii monistaa


GPIO.setup(outpin1, GPIO.OUT)
GPIO.setup(outpin2, GPIO.OUT)
#GPIO.setup(outpin3, GPIO.OUT)
#GPIO.setup(outpin4, GPIO.OUT)
#tän voi laittaa PUD_DOWNiksi, mutta se ei oikeen toimi halutulla tavalla. Vaatii vissiin myös, että vaihtaa try blockin sisällä logiikan päinvastaiseks
GPIO.setup(inpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(inpin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(inpin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(inpin4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.output(outpin1, GPIO.LOW)
GPIO.output(outpin2, GPIO.LOW)
#GPIO.output(outpin3, GPIO.LOW)
#GPIO.output(outpin4, GPIO.LOW)

ledState1 = False
ledState2 = False
#ledState3 = False
#ledState4 = False

def turnOnLed(ledPin):
    GPIO.output(ledPin, GPIO.HIGH)
    
def turnOffLed(ledPin):
    GPIO.output(ledPin, GPIO.LOW)
    
def toggleLed(ledPin, ledState):
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
        #readVal3 = GPIO.input(inpin3)
        #readVal4 = GPIO.input(inpin4)
        
        print("readVal1 is:", readVal1, "readVal2 is:", readVal2)#Tässä bugi. Printtaa aina 1 paitsi jos painat, mut heti sen jälkeen taas 1
        #, "readVal3 is:", readVal3, "readVal4 is:", readVal4)
        
        if readVal1 == 0:
            ledState1 = toggleLed(outpin1, ledState1)
            sleep(delay)#ettei paina monesti

        if readVal2 == 0:
            ledState2 = toggleLed(outpin2, ledState2)
            sleep(delay)#ettei paina monesti
        '''
        if readVal3 == 0:
            ledState1 = toggleLed(outpin1, ledState1)
            sleep(delay)#ettei paina monesti

        if readVal4 == 0:
            ledState2 = toggleLed(outpin2, ledState2)
            sleep(delay)#ettei paina monesti
        '''
            
        sleep(delay)
        
except KeyboardInterrupt:#tää käynnistyy painamalla Ctrl + C
    GPIO.cleanup()
    print("GPIO cleaned up")

