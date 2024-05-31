import RPi.GPIO as GPIO 
from mfrc522 import SimpleMFRC522 
ledVerde = 35 
ledRojo = 37 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(ledVerde,GPIO.OUT) 
GPIO.output(ledVerde, GPIO.LOW) 
GPIO.setup(ledRojo,GPIO.OUT) 
GPIO.output(ledRojo,GPIO.LOW) 
reader = SimpleMFRC522() 
while True: 
   try: 
       id, text = reader.read() 
       print(id)
       if id==287870326200: 
           print("Estas autorizado") 
           GPIO.output(ledVerde,GPIO.HIGH) 
           GPIO.output(ledRojo,GPIO.LOW)
       else: 
           GPIO.output(ledRojo,GPIO.HIGH) 
           GPIO.output(ledVerde, GPIO.LOW)
   except KeyboardInterrupt: #que pasa cuando escribo ctrlc
       GPIO.cleanup()
       exit() 
