# main.py -- put your code here!
from machine import Pin, ADC
from time import sleep
from machine import mem32
 
peatonal1verde=Pin(23,Pin.OUT)
peatonal2verde=Pin(22,Pin.OUT)
peatonal3verde=Pin(21,Pin.OUT)
vehicular4amarillo=Pin(19,Pin.OUT)
vehicular5verde=Pin(18,Pin.OUT)
vehicular6verde=Pin(5,Pin.OUT)
peatonal1rojo=Pin(13,Pin.OUT)
peatonal2rojo=Pin(12,Pin.OUT)
peatonal3rojo=Pin(14,Pin.OUT)
vehicular4rojo=Pin(27,Pin.OUT)
vehicular5rojo=Pin(26,Pin.OUT)
vehicular6rojo=Pin(25,Pin.OUT)

global b_pare
global b_temperatura
 
b_pare=False
b_temperatura=False
 
lm35_Pin=ADC(Pin(32))
lm35_Pin.atten(ADC.ATTN_11DB)
lm35_Pin.width(ADC.WIDTH_10BIT)
 
 
def off():
    for luz in [peatonal1verde,peatonal2verde,peatonal3verde,vehicular4amarillo,vehicular5verde,vehicular6verde,peatonal1rojo,peatonal2rojo,peatonal3rojo,vehicular4rojo,vehicular5rojo,vehicular6rojo]:
        luz.off()
        luz.value(0)
 
 
def leer_temperatura():
    valor_temperatura=lm35_Pin.read()
    voltaje=(valor_temperatura/1023.0)*3.3
    temperatura_c=voltaje*100
    print("La temperatura es: ",round(temperatura_c,2),"grados Celsius")
    return temperatura_c
 
def interrupcion_temperatura(Pin):
    global b_temperatura
    print("lectura de temperatura")
    b_temperatura=not b_temperatura
 
def interrupcion_pare(Pin):
    global b_pare
    print("Entre a la funcion interrupcion")
    b_pare=True
 
 
pare=Pin(33,Pin.IN,Pin.PULL_UP)
pare.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion_pare)
 
temperatura=Pin(17,Pin.IN,Pin.PULL_UP)
temperatura.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion_temperatura)
 
GPIO_SET=const(0x3FF44004)
 