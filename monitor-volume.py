#! /usr/bin/python

import evdev
import select
import alsaaudio

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
devices = {dev.fd: dev for dev in devices}

increment=4

done = False
while not done:
	m = alsaaudio.Mixer('Digital',0)
	r, w, x = select.select(devices, [], [])
	for fd in r:
		for event in devices[fd].read():
			event = evdev.util.categorize(event)
			if isinstance(event, evdev.events.RelEvent):
				change = event.event.value*increment				
				if m.getvolume()[0] + change > 100:
					value = 100
				else:
					value = max(0,m.getvolume()[0] + change)
				print("Value: {0}".format(value))				
				m.setvolume(value)

