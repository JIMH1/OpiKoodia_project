//Tässä kahen ledin ja napin osittainen toteutus
int firstLedPin = 13;    //Eka LEDI on kytketty kolmeentoista
int secondLedPin = 12;   //-|                  |- 12
int thirdLedPin = 11;

int buttonOnePin = 5;    //Napit on vitosessa ja nelosessa
int buttonTwoPin = 4;    //
int buttonThreePin = 3;

int activeLed = 0;       //Kertoo mikä LEDi on päällä (0 = ei mikään, 1 firstLED, 2 secondLED, jne)

float startTime = millis();  //Alkuarvo ajalle

void setup() {//Setupissa määritelty input ja outputit, pitäs laajentaa neljälle napille/ledille
  pinMode(firstLedPin, OUTPUT);    // Define first LED as Output
  pinMode(secondLedPin, OUTPUT);   // Define second LED as Output
  pinMode(thirdLedPin, OUTPUT);   // Define second LED as Output


  pinMode(buttonOnePin, INPUT);    // Define first Button as Input
  pinMode(buttonTwoPin, INPUT);    // Define second Button as Input
  pinMode(buttonThreePin, INPUT);   // Define second LED as Output

  //RNG alustus
  randomSeed(analogRead(0));
}
'''
[17:03]
'''void loop() {
  float startTime;
  float endTime;
  float elapsedTime;

  if (activeLed != 0) {//JOKU ledi on päällä -> tarkistetaan mikä ja sammutetaan se
    if ((activeLed == 1 && digitalRead(buttonOnePin) == HIGH) 
        (activeLed == 2 && digitalRead(buttonTwoPin) == HIGH) 
        (activeLed == 3 && digitalRead(buttonThreePin) == HIGH )) {
      digitalWrite(firstLedPin, LOW);
      digitalWrite(secondLedPin, LOW);
      digitalWrite(thirdLedPin, LOW);

      activeLed = 0;

      endTime = millis();
      elapsedTime = endTime - startTime;
      Serial.println("Your time to deactivate the correct LED is: " + String(elapsedTime) + " ms");
    }
  } else {//Mikään ledi ei ole päällä, sytytetään ledi
    int randomLed = random(3) + 1;
    switch (randomLed) {
      case 1:
        startTime = millis();
        digitalWrite(firstLedPin, HIGH);
        activeLed = 1;

              endTime = millis();
      elapsedTime = endTime - startTime;
      Serial.println("Your time to deactivate the correct LED is: " + String(elapsedTime) + " ms");

        break;

      case 2:
        startTime = millis();
        digitalWrite(secondLedPin, HIGH);
        activeLed = 2;

      endTime = millis();
      elapsedTime = endTime - startTime;
      Serial.println("Your time to deactivate the correct LED is: " + String(elapsedTime) + " ms");

        break;

      case 3:
        startTime = millis();
        digitalWrite(thirdLedPin, HIGH);
        activeLed = 3;

              endTime = millis();
      elapsedTime = endTime - startTime;
      Serial.println("Your time to deactivate the correct LED is: " + String(elapsedTime) + " ms");

        break;
    }
  }
}