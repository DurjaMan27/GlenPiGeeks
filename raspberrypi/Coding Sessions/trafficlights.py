from gpiozero import Button, TrafficLights
from time import sleep

button = Button(21)
lights = TrafficLights(25, 8, 7)

#all lights off
#v = . . . _
# pseudocode v = light on sleep 0.5 light off sleep 0.5 light on sleep 0.5 light off sleep 0.5 light on sleep 0.5 light off sleep 0.5 light on sleep 1 light off sleep 1
#a = . _
#a = light on sleep 0.5 light off sleep 0.5 light on sleep 1 light off sleep 1
lights.on()
sleep(0.5)
lights.off()
sleep(0.5)
  
lights.on()
sleep(0.5)
lights.off()
sleep(0.5)

lights.on()
sleep(0.5)
lights.off()
sleep(0.5)
  
lights.on()
sleep(1)
lights.off()
sleep(2)
# Finish V
# Start A
lights.on()
sleep(0.5)
lights.off()
sleep(0.5)
  
lights.on()
sleep(1)
lights.off()
sleep(2)
#Finish A
#Start R
lights.on()
sleep(0.5)
lights.off()
sleep(0.5)

lights.on()
sleep(1)
lights.off()
sleep(1)

lights.on()
sleep(0.5)
lights.off()
sleep(2)
#Finish R
#Start U
lights.on()
sleep(0.5)
lights.off()
sleep(0.5)
  
lights.on()
sleep(0.5)
lights.off()
sleep(0.5)
  
lights.on()
sleep(1)
lights.off()
sleep(2)
#Finish U
#start N
lights.on()
sleep(1)
lights.off()
sleep(1)
lights.on()
sleep(0.5)
lights.off()
sleep(2)
#Finish N
  

  
