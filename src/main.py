void loop() {
  int my_sensor_state = digitalRead(my_sensor);
  
  // print out the state of the sensor
  Serial.println(my_sensor_state);
  delay(1);        // delay in between reads for stability
}