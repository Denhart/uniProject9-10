from pywinauto import application
import pywinauto
import time

from pywinauto.findwindows import find_window
from pywinauto.win32functions import SetForegroundWindow

def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
  mustend = time.time() + timeout
  while time.time() < mustend:
    if somepredicate(*args, **kwargs) == False: return True
    time.sleep(period)
  return False


def setSPMFocus(): 
  app = application.Application()
  mainwin = app[u'SPM 1.3.1 Dev']
  time.sleep(0.1)
  SetForegroundWindow(find_window(title='SPM 1.3.1 Dev'))
  mainwin.SetFocus()

def setPyFocus(): 
  app = application.Application()
  mainwin = app[u'Cmder']
  time.sleep(0.1)
  SetForegroundWindow(find_window(title='Cmder'))
  mainwin.SetFocus()


def SatimoSPM(startFreq, endFreq, samples, filename):
  setSPMFocus()
  app = application.Application()
  print("Waiting for program")
  Main = app[u'SPM 1.3.1 Dev'].Wait('active',timeout=120, retry_interval=1)
  print("Program open")
  mainwin = app[u'SPM 1.3.1 Dev']
  mainwin.toolStrip1.Click(coords=(5,5))
  print("Waiting for dialog")
  app[u'Configure Measurement'].Wait('active',timeout=120, retry_interval=1)
  print("Dialog opened") 

  #Configure measurement dialog 
  dlg = app.top_window_()
  dlg.TypeKeys("Filename");
  dlg.TypeKeys("{TAB 4}");
  dlg.TypeKeys(str(startFreq));
  dlg.TypeKeys("{TAB}");
  dlg.TypeKeys(str(samples));
  dlg.TypeKeys("{TAB}");
  dlg.TypeKeys(str(endFreq));
  dlg.TypeKeys("{ENTER}");

  #Measurement started
  print("Now wait until measurement is done") 

  wait_until(mainwin.Cancel.Exists, 60*60, period=10)
  print("Now done")
  time.sleep(1)
  mainwin[u'Static2'].Click()

  print("Waiting for dialog")
  app[u'Save TRX for MiDAS Analysis as'].Wait('active',timeout=120, retry_interval=1)
  print("Dialog opened") 

  dlg = app.top_window_()
  dlg.TypeKeys(filename);
  dlg.TypeKeys("{ENTER}");
  time.sleep(1)
  Main = app[u'Filename - SPM 1.3.1 Dev'].Wait('active',timeout=120, retry_interval=1)
  mainwin.toolStrip1.Click(coords=(5,5))
  setPyFocus()

def calib():
  input("665")
  SatimoSPM(600, 700, 201, "665RefDipole")
  input("740")
  SatimoSPM(700, 800, 201, "740RefDipole")
  input("850")
  SatimoSPM(800, 900, 201, "850RefDipole")
  input("900")
  SatimoSPM(900, 1000, 201, "900RefDipole")
  input("1800")
  SatimoSPM(1600, 1830, 461, "1800RefDipole")
  input("2050")
  SatimoSPM(1830, 2230, 801, "2050RefDipole")
  input("2450")
  SatimoSPM(2280, 2670, 781, "2450RefDipole")

def doMeas(filename):
  input("LB + HB - %s" %filename)
  SatimoSPM(690, 960, 136, filename + "-LB")
  SatimoSPM(1710, 2650 ,471 , filename + "-HB")

