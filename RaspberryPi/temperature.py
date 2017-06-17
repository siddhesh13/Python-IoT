import sys
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 23)
    print "Temperature: ",temperature
    print "humidity: ", humidity
    
