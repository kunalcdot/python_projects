import time
import serial
import sys
import glob
from uart_t1 import *

DebugPrint = False
# configure the serial connections (the parameters differs on the device you are connecting to)
# ser = 1
# ser = serial.Serial(
	# port='COM1',
	# baudrate=115200,
	# parity=serial.PARITY_NONE,		#serial.PARITY_ODD,
	# stopbits=serial.STOPBITS_ONE,	#serial.STOPBITS_TWO,
	# bytesize=serial.EIGHTBITS,		#serial.SEVENBITS
	# timeout = 1
# )

#	-------------------------------
#define
# RegIntfSel_add = "3A"	# address of the register to control mux between CPU & UART intf. bit '0' is control bit
card_id_reg = "01" # add=01; SSR => "A1" , MMF => "00"
ssr_id = "a1"	#card id in small case and must contain two char.. 
mmf_id = "1f"

#---------------------------------------------------------------------------



# ser.close()
#ser.open()
# ser.isOpen()

	
def check_com():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    # print ports
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result	

def epld_detect():	# find the com port on which epld is connected and check board id
	detect = 0
	com_ports = check_com()
	# print com_ports
	no_of_coms = len(com_ports)
	if no_of_coms == 0:
		print("---\t\tERROR !!! No com port is available...")
	else:
		#cycle the com ports to find MMF/SSR
		for i in range(0,no_of_coms):
			com = com_ports[i]
			ser = serial.Serial(port=com,baudrate=115200,timeout=1)
			# ser.open()
			# print(ser.isOpen())
			try:
				card_id = str(epld_frame_read(ser,card_id_reg,'h'))
			except:
				# print("wrong")
				continue
				
			if card_id == ssr_id:
				print("\nSSR is detected @ "+com)
				detect = 1
				card_name = "SSR"
				break
			elif card_id == mmf_id:
				print("\nMMF is detected @ "+com)
				detect = 1
				card_name = "MMF"
				break
		if detect == 0:
			print("\n\t\t------*******------\n\tNo valid device is connected--\nAvailable com ports ==>\t"),
			print com_ports
			usr_msg = "No valid device is detected..\nCheck Console for more info!!"
			card_name = "NA"
			return [0,card_name]
		else:
			return [com,card_name]
	
	
# --------------	--------------	--------------	--------------	--------------	--------------	--------------	
	
if __name__ == '__main__':
# Read cmd = a5 5a;		write cmd = a5 5b	
	
	# print(check_com())
	ser = serial.Serial(port='COM3',baudrate=115200,timeout=1)
	epld_frame_write(ser,"1","a1")
	print(epld_frame_read(ser,"1",'b'))
	ser.close()
	print(epld_detect())
	
	
	x = raw_input("ctrl+C")
	print("Writing 03...\n")
	epld_frame_write("1","a5")
	print("1sec..")
	# time.sleep(1)
	print(epld_frame_read("1",'b'))
	print("Writing A2...\n")
	epld_frame_write("1","2a")
	# time.sleep(1)
	print(epld_frame_read("1",'h'))
	
	x = raw_input("ctrl+C")
	
	put_epld("A5")
	time.sleep(0.01)
	print("data A5\n")
	put_epld("5a")
	time.sleep(0.01)

	put_epld("3a")	#add

	time.sleep(0.01)
	put_epld("11")
	print("data 0\n")
	time.sleep(0.01)
	
	print(get_epld())
	
	# print(epld_read("3",'b'))
	# print("hex----")
	# print(epld_read("3", 'h'))
