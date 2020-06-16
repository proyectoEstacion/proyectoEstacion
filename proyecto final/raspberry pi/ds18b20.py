def ds18b20():
tfile = open("/sys/bus/w1/devices/28-031997799e37/w1_slave")
text = tfile.read()
tfile.close()
secondline = text.split("\n")[1]
temperaturedata = secondline.split(" ")[9]
temperature = float(temperaturedata[2:])
temperature = temperature / 1000
return float(temperature)
