from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)
	#def handleDiscovery(self, dev, isNewDev, isNewData):
		#if isNewDev:
			#print "Discovered device", dev.addr
		#elif isNewData:
			#print "Received new data from", dev.addr
#scanner = Scanner().withDelegate(ScanDelegate())
#devices = scanner.scan(2.0)
n=0
scan_time = 3

crash = False

while(True):
    scanner = Scanner().withDelegate(ScanDelegate())
    print 'Scanning for %d seconds.......' % scan_time
    devices = scanner.scan(scan_time)

    for dev in devices:
        #print '%d: Device %s (%s), RSSI=%d dB' % (n, dev.addr, dev.addrType, dev.rssi)
        candidate = []

        for(adtype, desc, value) in dev.getScanData():
            candidate.append(value)

        if candidate[-1][:4] != 'Bike':
            candidate = []
        elif candidate[-1][:4] == 'Bike':
            
            if candidate[-2][-2:] == '0f':
                print '%s CRASH' % candidate[-1][:4] 
                #clear crash state
                candidate = []
