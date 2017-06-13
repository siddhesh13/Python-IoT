import dht
import machine, time 

sensor = dht.DHT11(machine.Pin(2))
while 1:
    sensor.measure()
    temperature=sensor.temperature() # eg. 23 (°C)
    humidity=sensor.humidity()
    print("The Temperature is: "+ str(temperature))
    print("The Humidity is: "+ str(humidity))
    time.sleep(5)
