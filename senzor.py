import machine
import time

# Definování pinů
trig = machine.Pin(0, machine.Pin.OUT)
echo = machine.Pin(1, machine.Pin.IN)
led = machine.Pin(2, machine.Pin.OUT)

def measure_distance():
    # Vyslat 10us pulz na Trig pin
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    
    # Čekání na reakci ECHO pinu
    while echo.value() == 0:
        pass
    start = time.ticks_us()
    
    while echo.value() == 1:
        pass
    end = time.ticks_us()
    
    # Výpočet vzdálenosti v centimetrech
    distance = (time.ticks_diff(end, start) * 0.0343) / 2
    return distance

while True:
    dist = measure_distance()
    print('Distance: {} cm'.format(dist))
    
    if dist < 10:  # Když je něco blíž než 10 cm, rozsvítí se LED
        led.on()
    else:
        led.off()
        
    time.sleep(1)
