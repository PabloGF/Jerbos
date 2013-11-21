
 #include "pitches.h"

// notes in the melody:

int led = 13;

int melody[] = {
  NOTE_A7,0, NOTE_A7,0,NOTE_A7,0,NOTE_A7,0,NOTE_A7,0,NOTE_A7,0,NOTE_A7,0};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {
   4, 2, 4, 2, 4, 8, 4, 8, 4, 8, 4, 8, 2, 4 };

void setup() {
  
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  
  // iterate over the notes of the melody:

}





void loop () {
  if (Serial.available()) { //Si estÃ¡ disponible
    char c = Serial.read(); //Guardamos la lectura en una variable char
    if (c == 'H') { //Si es una 'H', enciendo el LED
      
        for (int thisNote = 0; thisNote < 14; thisNote++) {

    // to calculate the note duration, take one second 
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000/noteDurations[thisNote];
    tone(8, melody[thisNote],noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(8);
    
  }
      digitalWrite(led, HIGH);tw
    } else if (c == 'L') { //Si es una 'L', apago el LED
      digitalWrite(led, LOW);
    }
  }
}

