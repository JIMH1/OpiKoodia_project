//the next few lines set up the ports for the LEDs and the button
//you can change the numbers to match the ports you are using
int ledRed = 12;
int ledYellow = 11;
int ledGreen = 10;
int button = 7;
//the Time variables will be used to calculate the actual reaction time
int startTime = 0;
int endTime = 0;
int reactionTime = 0;

void setup() {
  pinMode (ledRed, OUTPUT);
  pinMode (ledYellow, OUTPUT);
  pinMode (ledGreen, OUTPUT);
  pinMode (button, INPUT);
}

void loop() {
  //turn off all LEDs at the start
  digitalWrite (ledRed, LOW);
  digitalWrite (ledYellow, LOW);
  digitalWrite (ledGreen, LOW);
  //this while statement makes the red LED flash to indicate the game is ready to start
  //the while loop ends when the user pushes the button
  while (digitalRead (button) == 0){
    digitalWrite (ledRed, HIGH);
    delay (50);
    digitalWrite (ledRed, LOW);
    delay (50);
  }
  //the following while statement waits for the button to be released by the user
  while (digitalRead (button) == 1) { } 
  //this delay causes a random wait time between 1.5 and 6 seconds
  delay (random (1500, 6000));
  //turn on all LEDs after the random wait time, this is the signal for the user to push the button again
  digitalWrite (ledRed, HIGH);
  digitalWrite (ledYellow, HIGH);
  digitalWrite (ledGreen, HIGH);
  //millis() records the time when the LEDs are turned on
  //the time is measured in milliseconds since the Arduino was powered on
  startTime = millis ();
  //the following while waits for the button to be pushed
  while (digitalRead (button) == 0) { }
  //the following line records the time the button was pushed
  endTime = millis ();
  //turn off all LEDs
  digitalWrite (ledRed, LOW);
  digitalWrite (ledYellow, LOW);
  digitalWrite (ledGreen, LOW);
  //turn on the LEDs one by one to build suspense
  delay (500);
  digitalWrite (ledRed, HIGH);
  delay (500);
  digitalWrite (ledYellow, HIGH);
  delay (500);
  digitalWrite (ledGreen, HIGH);
  delay (1000);
  //turn off all LEDs, the following if statements will turn on the correct LED
  digitalWrite (ledRed, LOW);
  digitalWrite (ledYellow, LOW);
  digitalWrite (ledGreen, LOW);
  //calculate the reaction time by calculating the difference between the starting time and the ending time
  reactionTime = endTime - startTime;
  //the following if turns on the green LED for a fast reaction time
  //you can make it easier or harder by changing the value in the if statements
  if (reactionTime < 1800){
    digitalWrite (ledGreen, HIGH);
  }
  else{
    //the following if turns on the yellow LED for an average reaction time
    if (reactionTime < 2600){
      digitalWrite (ledYellow, HIGH);
    }
    //the last else turns on the red LED for a slow reaction time
    else{
      digitalWrite (ledRed, HIGH);
    }
  }
  //the following while statements wait for the button to be pressed and released before going back to the start of the program
  while (digitalRead (button) == 0) { }
  while (digitalRead (button) == 1) { }
}
