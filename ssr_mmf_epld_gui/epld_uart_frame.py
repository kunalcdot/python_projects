import time
import serial
import sys
import glob


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
RegIntfSel_add = "3A"	# address of the register to control mux between CPU & UART intf. bit '0' is control bit
card_id_reg = "01" # add=01; SSR => "A1" , MMF => "00"
ssr_id = "a1"	#card id in small case and must contain two char.. 
mmf_id = "00"

#---------------------------------------------------------------------------



# ser.close()
#ser.open()
# ser.isOpen()


def string_to_hex(user8bit): # convert the 8-bit user input to hex
    numInt = int(user8bit,16)
    strHex = hex(numInt)
    userHex = strHex[2:].zfill(2)
    # make sure the payload is a two-digit hex
    return userHex	


def put_epld(ser,data):
	#takes reg add in hex format(max=0xff) & returns reg data in hex
	ser.flushOutput()
	ser.flushInput()
	newRegisterValue = string_to_hex(data)
	ser.write(newRegisterValue.decode('hex'))


def get_epld(ser,form):
	reply = ""
	# ser = serial_port
	while ser.inWaiting() > 0:
		reply += ser.read(1)
	
	
	# out = ser.read(1)
	
	# return ('%02x' % ord(reply))	# hex data out
	
	if form == 'b':
		return ((format(ord(reply), 'b')).zfill(8)) # binary string 8bit format
	else:
		return ('%02x' % ord(reply))	# hex data out
	
def epld_uart_we(ser,cmd):
	put_epld(ser,"A5")
	time.sleep(0.01)
	put_epld(ser,"5b")
	time.sleep(0.01)
	put_epld(ser,RegIntfSel_add)	#add
	time.sleep(0.01)
	
	if cmd == "enable" : # write enable
		put_epld(ser,"1")
	elif cmd == "disable" :
		put_epld(ser,"0")
	else :
		return ("wrong argument")
	return ("Success")
	
	
def epld_frame_write(ser,add,data):
	epld_uart_we(ser,"enable")
	put_epld(ser,"A5")
	time.sleep(0.01)
	put_epld(ser,"5B")
	time.sleep(0.01)

	put_epld(ser,str(add))	#add

	time.sleep(0.01)
	put_epld(ser,str(data))
	time.sleep(0.01)
	old_data = get_epld(ser,'h')
	if DebugPrint:
		print("old data: "),
		print(old_data)
	time.sleep(0.01)
	epld_uart_we(ser,"disable")
	
	return old_data
	
def epld_frame_read(ser,add,form):
	time.sleep(0.05)
	put_epld(ser,"A5")
	# time.sleep(0.01)
	
	put_epld(ser,"5a")
	# time.sleep(0.01)

	put_epld(ser,str(add))	#add

	# time.sleep(0.01)
	put_epld(ser,"0")
	
	time.sleep(.01)
	data = get_epld(ser,form)
	if DebugPrint:
		print("Reg add : 0x"+str(add)+"\tRead data: "),
		print(data)
	return data
	
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
				break
			elif card_id == mmf_id:
				print("\nMMF is detected @ "+com)
				detect = 1
				break
		if detect == 0:
			print("\n\t\t------*******------\n\tNo valid device is connected--\nAvailable com ports ==>\t"),
			print com_ports
	
	
# --------------	--------------	--------------	--------------	--------------	--------------	--------------	
	
if __name__ == '__main__':
# Read cmd = a5 5a;		write cmd = a5 5b	
	
	# print(check_com())
	ser = serial.Serial(port='COM3',baudrate=115200,timeout=1)
	epld_frame_write(ser,"1","a1")
	print(epld_frame_read(ser,"1",'b'))
	ser.close()
	epld_detect()
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
