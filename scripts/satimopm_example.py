import satimopm
import serial

basename = "triag_top_vert"
serial_port = "/dev/ttyUSB0"

# Start serial port
ser = serial.Serial(serial_port)
ser.flushInput()
ser.flushOutput()

# Command format:
#   A|B     = slave address 0x07 or 0x06, respectively.
#   x|y|z|t = internal capacitor register (1, 2, 3, 4, respectively)
#   0--f    = capacitor setting (0 ~ 0.3pF, f ~ 2.9pF).

# Only slave address A = 0x7 is used
ser.write(b"Ax0Ay0Az0At0")

# Start sweep
for x in [
        ["0_0", b"Ax0Ay0"],
        ["2_0", b"Ax2Ay0"],
        ["4_0", b"Ax4Ay0"],
        ["6_0", b"Ax6Ay0"],
        ["8_0", b"Ax8Ay0"],
        ["a_0", b"AxaAy0"],
        ["c_0", b"AxcAy0"],
        ["e_0", b"AxeAy0"],
        ["f_1", b"AxfAy1"],
        ["f_3", b"AxfAy3"],
        ["f_5", b"AxfAy5"],
        ["f_7", b"AxfAy7"],
        ["f_9", b"AxfAy9"],
        ["f_b", b"AxfAyb"],
        ["f_d", b"AxfAyd"],
        ["f_f", b"AxfAyf"],
        ]:
    fname,cmd = *x
    fname = basename + "_" + fname
    ser.write(cmd)
    satimopm.measure(fname)

ser.close()
