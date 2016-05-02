import visa
class VNA(object):
##D:\Henrik    
    def __init__(self, interface, savedir):
        self.savedir = savedir
        rm = visa.ResourceManager('@py')
        self.inst = rm.open_resource(interface)

    def save(self, fname):
        self.inst.write(":INITIATE:CONTINUOUS OFF")
        self.inst.write("SWE:POINts 1000")
        self.inst.write(":INITIATE:IMMEDIATE; *WAI")
        self.inst.write("MMEM:STOR:TRAC:CHAN 1, '{0}{1}.s2p'".format(self.savedir ,fname))
        self.inst.write("SWE:POINts 201")
        self.inst.write(":INITIATE:CONTINUOUS ON")

    def setmarkers(self, rx_lb, rx_hb, tx_lb, tx_hb):
        #Set RX marker
        self.inst.write("CALCulate1:PARameter:SELect 'RX'")
        self.inst.write("CALC:MARK1:X {}MHz".format(rx_lb))
        self.inst.write("CALC:MARK2:X {}MHz".format(rx_hb))
        #Set TX marker
        self.inst.write("CALCulate1:PARameter:SELect 'TX'")
        self.inst.write("CALC:MARK1:X {}MHz".format(tx_lb))
        self.inst.write("CALC:MARK2:X {}MHz".format(tx_hb))

    def initSettings(self):
        #Init:
        self.inst.write("*RST; :CONF:TRAC:NAME?")
        self.inst.write("CALC:PAR:DEF:SGR 1,2")
        self.inst.write("FREQ:STAR 600 MHz; STOP 3 GHz")
        self.inst.write("SWE:POINts 201")
        self.inst.write(":DISPLAY:WINDOW1:TRACE1:DELete")
        #RX trace
        self.inst.write(":CALCULATE1:PARAMETER:SDEFINE 'RX','S22'")
        self.inst.write(":DISPLAY:WINDOW1:TRACE1:FEED 'RX'")
        self.inst.write(":DISP:WIND1:TRAC1:Y:PDIV 5")
        self.inst.write("CALC:MARK1 ON; MARK2 ON")
        #TX trace
        self.inst.write(":CALCULATE1:PARAMETER:SDEFINE 'TX','S11'")
        self.inst.write(":DISPLAY:WINDOW1:TRACE2:FEED 'TX'")
        self.inst.write(":DISP:WIND1:TRAC2:Y:PDIV 5")
        self.inst.write("CALC:MARK1 ON; MARK2 ON")
        #ISO trace
        self.inst.write(":CALCULATE1:PARAMETER:SDEFINE 'ISO','S21'")
        self.inst.write(":DISPLAY:WINDOW1:TRACE3:FEED 'ISO'")
        self.inst.write(":DISP:WIND1:TRAC3:Y:PDIV 5")

    def idn(self):
        #Init:
        print(self.inst.query("*IDN?"))
