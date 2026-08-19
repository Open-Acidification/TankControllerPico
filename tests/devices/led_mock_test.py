from src.devices.library import LED

led = LED()

print(led.is_on)  # False

led.on()
print(led.is_on)  # True

led.off()
print(led.is_on)  # False

led.toggle()
print(led.is_on)  # True
