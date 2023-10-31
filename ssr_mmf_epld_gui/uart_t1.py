import time
import serial
import epld_const

DebugPrint = False
# configure the serial connections (the parameters differs on the device you are connecting to)
# ser = serial.Serial(
	# port='COM3',
	# baudrate=115200,
	# parity=serial.PARITY_NONE,		#serial.PARITY_ODD,
	# stopbits=serial.STOPBITS_ONE,	#serial.STOPBITS_TWO,
	# bytesize=serial.EIGHTBITS,		#serial.SEVENBITS
	# timeout = 1
# )

#	#define
# RegIntfSel_add = "02"	# address of the register to control mux between CPU & UART intf. bit '0' is control bit
brd_rst_reg	= "05"
tp_rst_reg	= "03"
mcp_rst_reg	= "04"

# ----------------------------		#define		----------------------------------
# EPLD smi related control/status	registers address
CmdReg = "c0"
DevAddReg = "c1"
RegAddReg = "c2" # register address of smi slave
WrDataHighReg = "c3"
WrDataLowReg =	"c4"
RdDataHighReg = "c5"
RdDataLowReg =	"c6"
SmiStatusReg = "c8"
# ***********************************************************	




#ser.open()
# ser.isOpen()


def string_to_hex(user8bit): # convert the 8-bit user input to hex
    numInt = int(user8bit,16)
    strHex = hex(numInt)
    userHex = strHex[2:].zfill(2)
    # make sure the payload is a two-digit hex
    return userHex	

# def epld_read(reg_add,form):
	# #takes reg add in hex format(max=0xff) & returns reg data in hex
	# ser.flushOutput()
	# ser.flushInput()
	# newRegisterValue = string_to_hex(reg_add)
	# ser.write(newRegisterValue.decode('hex'))
	# # print('Sendin reg address...'+newRegisterValue)
	# # print('Receiving...')
	# #time.sleep(1)
	# out = ser.read(1)
	# #print len(out)
	# #print out

	# # print("\nhex value printing--------------\n\n")
	# # print('%02x' % ord(out))
	# if form == 'b':
		# return ((format(ord(out), 'b')).zfill(8)) # binary string 8bit format
	# else:
		# return ('%02x' % ord(out))	# hex data out

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
	put_epld(ser,epld_const.RegIntfSel_add)	#add
	time.sleep(0.01)
	
	if cmd == "enable" : # write enable
		put_epld(ser,"1")
	elif cmd == "disable" :
		put_epld(ser,"0")
	else :
		return ("wrong argument")
	return ("Success")
	
	
def epld_frame_write(ser,add,data):
	# time.sleep(0.05)
	epld_uart_we(ser,"enable")
	put_epld(ser,"A5")
	time.sleep(0.01)
	put_epld(ser,"5B")
	time.sleep(0.01)

	put_epld(ser,str(add))	#add

	time.sleep(0.01)
	put_epld(ser,str(data))
	time.sleep(0.02)
	old_data = get_epld(ser,'h')
	if DebugPrint:
		print("old data: "),
		print(old_data)
	time.sleep(0.01)
	epld_uart_we(ser,"disable")
	
	return old_data
	
def epld_frame_read(ser,add,form):
	# time.sleep(0.05)
	put_epld(ser,"A5")
	time.sleep(0.01)
	
	put_epld(ser,"5a")
	time.sleep(0.01)

	put_epld(ser,str(add))	#add

	time.sleep(0.01)
	put_epld(ser,"0")
	
	time.sleep(0.02)	
	data = get_epld(ser,form)
	if DebugPrint:
		print("Reg add : 0x"+str(add)+"\tRead data: "),
		print(data)
	return data
	



#****************************** added for Lion2 smi read********************	
### ---------------start of block -----------------------------------------
### ----------------------------------------------------

def epld_uart_we_fast(ser,cmd):
	put_epld(ser,"A5")
	# time.sleep(0.01)
	put_epld(ser,"5b")
	# time.sleep(0.01)
	# put_epld(ser,epld_const.RegIntfSel_add)	#add
	put_epld(ser,epld_const.RegIntfSel_add)	#add
	time.sleep(0.01)
	
	if cmd == "enable" : # write enable
		put_epld(ser,"1")
	elif cmd == "disable" :
		put_epld(ser,"0")
	else :
		return ("wrong argument")
	return ("Success")
	
	
def epld_frame_write_fast(ser,add,data):
	# time.sleep(0.05)
	epld_uart_we_fast(ser,"enable")
	put_epld(ser,"A5")
	# time.sleep(0.01)
	put_epld(ser,"5B")
	# time.sleep(0.01)

	put_epld(ser,str(add))	#add

	# time.sleep(0.01)
	put_epld(ser,str(data))
	# time.sleep(0.01)
	old_data = 1
	# old_data = get_epld(ser,'h')
	if DebugPrint:
		print("old data: "),
		print(old_data)
	time.sleep(0.01)
	epld_uart_we_fast(ser,"disable")
	
	return old_data



def phyRead(ser,devadd,regadd):	#low level smi rd/wr
	
	epld_frame_write_fast(ser,DevAddReg,str(devadd))
	time.sleep(0.01)
	epld_frame_write_fast(ser,RegAddReg,str(regadd))
	time.sleep(0.01)		
	epld_frame_write_fast(ser,CmdReg,"0e")
	time.sleep(0.01)
	epld_frame_write_fast(ser,CmdReg,"0f")
	time.sleep(0.01)
	epld_frame_write_fast(ser,CmdReg,"00")
	time.sleep(0.01)
	datahigh = (epld_frame_read(ser,RdDataHighReg,'h'))
	time.sleep(0.01)
	datalow = (epld_frame_read(ser,RdDataLowReg,'h'))
	if DebugPrint:
		print(datahigh+datalow)
		# print(datalow)
	return (datahigh + datalow)


def phyWrite(ser,devadd,regadd,data):	#low level smi rd/wr
	
	# pad data to make it 4character length (16 bit)
	data = str(data)
	length = len(data)
	pad_data = []
	for i in range(length,4):
		pad_data.append('0')
	data = ("".join(pad_data)) + data	
	# print data	
	
	# x = raw_input ("---")	
	epld_frame_write_fast(ser,DevAddReg,str(devadd))
	time.sleep(0.01)
	epld_frame_write_fast(ser,RegAddReg,str(regadd))
	time.sleep(0.01)
	epld_frame_write_fast(ser,WrDataHighReg,data[0:2])
	time.sleep(0.01)
	epld_frame_write_fast(ser,WrDataLowReg,data[2:4])
	time.sleep(0.01)
	epld_frame_write_fast(ser,CmdReg,"0c")
	time.sleep(0.01)
	epld_frame_write_fast(ser,CmdReg,"0d")
	time.sleep(0.01)
	epld_frame_write_fast(ser,CmdReg,"00")
	
	time.sleep(0.1)
	return 1
	
	
	# timeout = 2
	# maxtime = time.time()+timeout
	# while time.time() < maxtime:
		# status = epld_frame_read(ser,SmiStatusReg,'b')
		# rdy_bit = status[7-6] # reg_data[7-bit_pos]
		# if rdy_bit == '0':
			# return 1 # success
			# break
		# time.sleep(0.02)
	return 0 #fail
	

#switch rd/wr via SMI... 32bit add & 32bit data-------------------------------
def xcat_read(ser,devadd,sw_regadd):	#sw_regadd --> 32bit
	
# steps:
		# write 16bit add in high add reg --> 0x4
		# write 16bit add in low add reg --> 0x5
		# Read status reg 0x1f --> should be 0x3
		# Read data high & low --> 0x6,0x7
	DebugPrint_local = False
	devadd = str(devadd)
	
	# pad sw_regadd to make it 8character length (32 bit)
	sw_regadd = str(sw_regadd)
	length = len(sw_regadd)
	pad_data = []
	for i in range(length,8):
		pad_data.append('0')
	sw_regadd = ("".join(pad_data)) + sw_regadd	
	# print sw_regadd	
	# print("Xcat status at beginning --->")
	
	status = phyRead(ser,devadd,"1f")
	if status != "0003":
		# return 1 # success
		print("\n\tXcat access error!!!\tDev status =  "+status+"\nExiting...")
		exit(0)
	
	
	# print(phyRead(ser,devadd,"1f"))	
	phyWrite(ser,devadd,"4",sw_regadd[0:4])
	phyWrite(ser,devadd,"5",sw_regadd[4:8])
	timeout = 1
	maxtime = time.time() + timeout
	while time.time() < maxtime:
		status = phyRead(ser,devadd,"1f")
		if status == "0003":
			# return 1 # success
			print("\tRead success")
			break
	if DebugPrint_local:
		print("SMI status --->")
		print(phyRead(ser,devadd,"1f"))
		print("Read data --->")
	dataH = (phyRead(ser,devadd,"06"))
	dataL = (phyRead(ser,devadd,"07"))
	data = dataH + dataL
	return data



def xcat_write(ser,devadd,sw_regadd,data,dev_type):	#sw_regadd --> 32bit ## dev_type ="lion2" / "xcat"
	
# steps:
		# write 16bit add in high add reg --> 0x0
		# write 16bit add in low add reg --> 0x1
		# write 16bit data in high add reg --> 0x2
		# write 16bit data in low add reg --> 0x3
		# Read status reg 0x1f --> should be 0x3
		
	devadd = str(devadd)
	
	# pad sw_regadd to make it 8character length (32 bit)
	sw_regadd = str(sw_regadd)
	length = len(sw_regadd)
	pad_data = []
	for i in range(length,8):
		pad_data.append('0')
	sw_regadd = ("".join(pad_data)) + sw_regadd	
	# print sw_regadd	
		
	phyWrite(ser,devadd,"0",sw_regadd[0:4])
	phyWrite(ser,devadd,"1",sw_regadd[4:8])
	
	# pad data to make it 8character length (32 bit)
	data = str(data)
	length = len(data)
	pad_data = []
	for i in range(length,8):
		pad_data.append('0')
	data = ("".join(pad_data)) + data	
	print ("Data ==> "+data)
	if dev_type == "lion2":
		phyWrite(ser,devadd,"2",data[0:4])
		phyWrite(ser,devadd,"3",data[4:8])
	elif dev_type == "xcat":
		phyWrite(ser,devadd,"8",data[0:4])
		phyWrite(ser,devadd,"9",data[4:8])
	else:
		print("Wrong dev_type\n")
	
	timeout = 1
	maxtime = time.time() + timeout
	while time.time() < maxtime:
		status = phyRead(ser,devadd,"1f")
		if status == "0003":
			# return 1 # success
			print("\n\tWrite success")
			break
	
	
	
	
	
#****************************** added for Lion2 smi read********************	
### ---------------end of block -----------------------------------------







	
def epld_dump(ser):	# epld dump from 0x0 - 0xff as per SSR memory map
	
	start = 0x0  # hex literal, gives us a regular integer
	end = 0xFF
	j = 0
	
	print("\n\tEPLD Dump ==>\n\t====Common Address Space====\n")
	print("0x0:")
	for i in xrange(start, end + 1):
		k = format(i+1, 'X')
		i =  format(i, 'X')	
		
		add = str(i)
		data = (epld_frame_read(ser,add,'h'))
		print(str(data)),
		
		if str(k) == "10":
			print("\n\n\t====MCP Address Space====")
		elif str(k) == "80":
			print("\n\n\t====TP Address Space====")
		
		
		if j ==15:
			print("\n"+str(k)+":\t")
			j = 0
		else:
			j += 1
		
		# print i
		
		
		# time.sleep(0.01)
def brd_rst(ser):
	print("Main board in reset\n")
	epld_frame_write(ser,brd_rst_reg,"00")
	# print(epld_frame_read(ser,brd_rst_reg,'h'))
	time.sleep(1)
	epld_frame_write(ser,brd_rst_reg,"01")
	print("Main board out of reset\n")
	# print(epld_frame_read(ser,brd_rst_reg,'h'))

def tp_rst(ser):
	print("tp in reset\n")
	epld_frame_write(ser,tp_rst_reg,"00")
	print(epld_frame_read(ser,tp_rst_reg,'h'))
	time.sleep(1)
	epld_frame_write(ser,tp_rst_reg,"01")
	print("tp out of reset\n")
	print(epld_frame_read(ser,tp_rst_reg,'h'))

def mcp_rst(ser):
	print("mcp in reset\n")
	epld_frame_write(ser,mcp_rst_reg,"00")
	print(epld_frame_read(ser,mcp_rst_reg,'h'))
	time.sleep(1)
	epld_frame_write(ser,mcp_rst_reg,"01")
	print("mcp out of reset\n")
	print(epld_frame_read(ser,mcp_rst_reg,'h'))
	

	
if __name__ == '__main__':
# Read cmd = a5 5a;		write cmd = a5 5b	
	ser = serial.Serial(port='COM3', baudrate=115200, timeout = 1)
	epld_dump(ser)
	x = raw_input("ctrl+C")
	
	print("Writing 03...\n")
	epld_frame_write("1","03")
	print("1sec..")
	time.sleep(1)
	epld_frame_read("1",'b')
	print("Writing A2...\n")
	epld_frame_write("1","a2")
	time.sleep(1)
	epld_frame_read("1",'h')
	
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
