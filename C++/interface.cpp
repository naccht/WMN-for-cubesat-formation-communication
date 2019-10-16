char incomingByte ; //Variable to store the incoming byte

void setup() {

	//Start the serial communication
	Serial.begin(9600); //Baud rate must be the same as is on xBee module
}

void loop() {
	
  while (Serial.available()>0){
  	//Read the incoming byte
    incomingByte = Serial.read();
    //Start the message when the '<' symbol is received
    if(incomingByte == '<')
    {
     started = true;
   }
   //End the message when the '>' symbol is received
   else if(incomingByte == '>')
   {
     ended = true;
     break; // Done reading - exit from while loop!
   }
 }

}
  
