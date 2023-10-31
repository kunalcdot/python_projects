import sys
from PyQt4 import QtGui
from PyQt4.QtCore import *
import time
import Queue
import easygui
# from uart import *
from uart_t1 import *
# from epld_uart_frame import *
import threadgui # gui
import serial
import search_dev
import epld_const

# ---------------------------------------------------------------------
# date = 30-5-18
RegIntfSel_add = "02"
gui_version = "0.4"
# ---------------------------------------------------------------------

cmnd_q = Queue.Queue()
result_q = Queue.Queue()

# pol_id = ["zl_status","act_pas_status","rtm_ps_status","clk2a_mode","clk2b_mode"]
# pol_add = ["0x0","0x5","0x10","0x10","0x10"]

# pol_id = ["zl_status","act_pas_status","rim_ps_status","tp_rst_status"]
# pol_add = ["0x0","0x5","0x90","0x90"]





class MyFirstGuiProgram(QtGui.QDialog,threadgui.Ui_mainwindow):
	def __init__(self, parent=None):
		super(MyFirstGuiProgram,self).__init__(parent)

		self.setupUi(self)
		#self.zl_status.setText("--NA--")
		self.label_gui_ver.setText(gui_version)
		self.get_data_btn.clicked.connect(self.getdata_btn_clicked)
		self.write_btn.clicked.connect(self.write_btn_clicked)
		self.dump_btn.clicked.connect(self.dump_btn_clicked)
		self.exit_btn.clicked.connect(self.exit_btn_clicked)
		self.brd_rst_btn.clicked.connect(self.brd_rst_btn_clicked)
		self.tp_rst_btn.clicked.connect(self.tp_rst_btn_clicked)
		self.mcp_rst_btn.clicked.connect(self.mcp_rst_btn_clicked)
		
		# self.workingthread = workingthread()
		
		self.thread1 = resltqprocessthread()
		self.thread2 = pollingthread()
		self.thread3 = cmdqprocessthread()
		
		# self.connect(self.workingthread, SIGNAL("processdone(QString)"), self.thread1done,Qt.DirectConnection)
		self.connect(self.thread1, SIGNAL("resltqdata(QString,QString)"), self.gui_update,Qt.DirectConnection)
		
		#self.workingthread.start()
		self.thread1.start()
		self.thread2.start()
		self.thread3.start()
		self.connection = "na"
		#self.zl_status.setText("Locked")

	def getdata_btn_clicked(self):
		address = self.add_ip.text()
		id = "user_read"
		id = "xcat_read"
		# print (address)
		data = [address,id]
		cmnd_q.put(data)
	
	
	def write_btn_clicked(self):
		address = self.write_add_ip.text()
		wr_data = self.write_data_ip.text()
		id = "user_write"
		# print (address)
		data = [[address,wr_data],id]
		cmnd_q.put(data)
		
	def dump_btn_clicked(self):
		
		id = "dump"
		data = [0,id]
		cmnd_q.put(data)
		

	def exit_btn_clicked(self):	
		
		self.thread1.stop()
		self.thread2.stop()
		self.thread3.stop()
		self.thread1.quit()
		self.thread2.quit()
		self.thread3.quit()
		sys.exit(0)
	
	def brd_rst_btn_clicked(self):	
		# print("x..")
		id = "brd_rst"
		data = [0,id]
		cmnd_q.put(data)
	def tp_rst_btn_clicked(self):	
		# print("x..")
		id = "tp_rst"
		data = [0,id]
		cmnd_q.put(data)
	def mcp_rst_btn_clicked(self):	
		# print("x..")
		id = "mcp_rst"
		data = [0,id]
		cmnd_q.put(data)
		
		
		
		
		
#---------------- update gui as per incoming data ----------------------
	# use id & reg_data[7-bit_pos] ---------------------

	def gui_update(self,reg_data,id):
			
		if id =="conn_status" :
			
			if self.connection <> reg_data:
				if reg_data == "OK":
					self.label_conn_status.setStyleSheet("color: green")
				else:
					self.label_conn_status.setStyleSheet("color: red")
					
				self.label_conn_status.setText(reg_data)	
			self.connection = reg_data
			
		elif id =="label_epld_ver" :	
			self.label_epld_ver.setText(reg_data)	
		elif id =="label_card_name" :	
			if reg_data == "10100001":	#0xA1
				self.label_card_name.setText("SSR")		
			elif reg_data == "00011111":	#0x1F
				self.label_card_name.setText("MMF")			
			
			# bitvalue = reg_data[7-1] # reg_data[7-bit_pos]
			# if bitvalue == "1" :
				# self.clk2b_mode.setText("Tx mode")
			# elif bitvalue == "0":
				# self.clk2b_mode.setText("Rx mode")
			# else:
				# self.clk2b_mode.setText("--NA--")

		elif id =="user_read" :
						# self.disp_data.setText("0x"+str(reg_data))
			# print("result = 3")
			self.disp_data.setText("0x"+reg_data)
			# self.zl_status.setStyleSheet("QWidget{background-color: red}")
			#QtGui.QMessageBox.information(self, "Error", "Error")
		
		
		elif id =="dummy" :
			pass

		else:	# continuous read..
			pol_id = []
			polling_data = epld_const.pol_array
			size = len(polling_data)
			for i in range(0,size):
				pol_id.append(polling_data[i][0])
			
			i = pol_id.index(id)	
			
			bit_pos = polling_data[i][2]
			bitvalue = reg_data[7-bit_pos] # reg_data[7-bit_pos]
			if bitvalue == "1" :
				cmd = "self."+id+".setText('"+polling_data[i][3]+"')"	
			else:
				cmd = "self."+id+".setText('"+polling_data[i][4]+"')"	
			# print cmd
			exec(str(cmd))
			
		
#*************************************************************************************************************

		
	# def thread1done(self,x):
		# print("thread1 done")
		# self.add_ip.setText("Done")
		# x = int(x)
		# #self.zl_status.setStyleSheet("background-color: red")

		# if (x%2) == 0:
		# #	self.zl_status.setStyleSheet("background-color: green")
			# self.add_ip.setText("Done")
		# else:
			# # self.zl_status.setStyleSheet("background-color: red")
			# self.add_ip.setText("Not Done")
			# print("hi")


# class workingthread(QThread):
    # def __init__(self, parent=None):
        # super(workingthread, self).__init__(parent)

    # def run(self):
        # i = 0
        # while 1:
            # time.sleep(0.7)
           # # print ("from working thread\n")
            # i = i+1
            # if (i%5)==0:
                # x = (i/5)%2
                # #print (x)
                # self.emit(SIGNAL("processdone(QString)"),str(x))

				
				
class pollingthread(QThread):				
	def __init__(self, parent=None):
		super(pollingthread, self).__init__(parent)
		self._isRunning = True
	
	
	def run(self):
		print("\n polling start\n")
		time.sleep(0.5)
		while self._isRunning:
			polling_data = epld_const.pol_array
			size = len(polling_data)
			
			i = 0
			for j in range(0,size):
				# data = [pol_add[i],id]
				data = [polling_data[j][1],polling_data[j][0]]
				cmnd_q.put(data)
				
			time.sleep(2)
			#print ("\ninside polling\n")
			#print(data)				
	def stop(self):
		self._isRunning = False

		
class cmdqprocessthread(QThread):				
	def __init__(self, parent=None):
		super(cmdqprocessthread, self).__init__(parent)
		self._isRunning = True

	def run(self):
		print("\n cmnd q start\n")	
		while self._isRunning:
			while not cmnd_q.empty():
				#print ("cmndq process")
				[add,id] = cmnd_q.get()
				# reg_data ="00000000"
				# if id == "brd_rst":
					# print("tp rst fn")
					# brd_rst(ser)
					# reg_data ="00"
					# id = "dummy"
				# print(xcat_read(ser,"19","4004100"))	
				try:
					if id == "user_read":
						# print("rd fn")
						reg_data = epld_frame_read(ser,str(add),'h')
						# reg_data = epld_frame_read(str(add),'h')
						print("EPLD Read==>\tADD: "+str(add)+"\t  DATA: "+str(reg_data)+"\n")
					elif id == "user_write":
						# print("write fn")
						print(epld_frame_write(ser,str(add[0]),str(add[1]))) #add[0]--> address, add[1]--> data,
						# print(epld_frame_write(str(add[0]),str(add[1]))) #add[0]--> address, add[1]--> data,
						print("EPLD Write-->>\tADD: "+str(add[0])+"\t  DATA: "+str(add[1])+"\n")
						id = "dummy"
					
					elif id == "xcat_read":
						print("rd fn")
						print(xcat_read(ser,"19","4004100")) #add[0]--> address, add[1]--> data,
						# print(epld_frame_write(str(add[0]),str(add[1]))) #add[0]--> address, add[1]--> data,
						# print("XCAT/Lion2 Write-->>\tADD: "+str(add[0])+"\t  DATA: "+str(add[1])+"\n")
						id = "dummy"	
					
					
					elif id == "xcat_write":
						print("xcat wr fn")
						print(xcat_write(ser,"19","4004100")) #add[0]--> address, add[1]--> data,
						# print(epld_frame_write(str(add[0]),str(add[1]))) #add[0]--> address, add[1]--> data,
						# print("XCAT/Lion2 Write-->>\tADD: "+str(add[0])+"\t  DATA: "+str(add[1])+"\n")
						id = "dummy"	
					
					
					elif id == "dump":
						print("dump fn")
						epld_dump(ser)
						id = "dummy"
						
					elif id == "brd_rst":
						# print("brd rst fn")
						brd_rst(ser)
						id = "dummy"
					elif id == "tp_rst":
						# print("brd rst fn")
						tp_rst(ser)
						id = "dummy"
					elif id == "mcp_rst":
						# print("brd rst fn")
						mcp_rst(ser)
						id = "dummy"
										
					else:
						reg_data = epld_frame_read(ser,str(add),'b')
						# reg_data = epld_frame_read(str(add),'b')
						
				
					result_q.put([reg_data,id])				
					result_q.put(["OK","conn_status"])				
				except:
					# QtGui.QMessageBox.information(self,"Error","Error")
					reg_data = "Connecting..."
					id = "conn_status"
					# easygui.exceptionbox(msg="ERROR!!!!Enter valid address\nEnsure EPLD is accessible", title="Error")
					# sys.exit(app.exec_())
					
				#print (reg_data)
				result_q.put([reg_data,id])	

			
	def stop(self):
		self._isRunning = False

class resltqprocessthread(QThread):				
	def __init__(self, parent=None):
		super(resltqprocessthread, self).__init__(parent)
		self._isRunning = True
					
	def run(self):
		# print("xyz & wait")
		
		while self._isRunning:
			while not result_q.empty():
				[reg_data,id] = result_q.get()
				self.emit(SIGNAL("resltqdata(QString,QString)"),str(reg_data),str(id))
	
	def stop(self):
		self._isRunning = False			


if __name__ == '__main__':				
	# ser = serial.Serial(port='COM3',baudrate=115200,timeout=1)
	
	connection_old = "NA"
	while 1:
		[com_no,card_name] = search_dev.epld_detect()
		print com_no
		
		if card_name == "SSR":
			msg = card_name + " is detected @ "+com_no
			epld_const.RegIntfSel_add = "02"
			break
		elif card_name == "MMF":
			msg = card_name + " is detected @ "+com_no
			epld_const.RegIntfSel_add = "3A"
			break
		else:
			msg = "No valid device is detected\nCheck console for more info\n" 
					
			#print("mmf2")
			selected_button = easygui.buttonbox(msg=msg, title="EPLD gui search", choices=('Try Again', 'Quit'))
			
			#print("mmf1")
			
			if selected_button == 'Try Again':
				continue
			else :
				exit(0)
		
	easygui.msgbox(msg=msg, title="EPLD search", ok_button='Next')
	ser = serial.Serial(port=com_no,baudrate=115200,timeout=1)
	app = QtGui.QApplication(sys.argv)
	form = MyFirstGuiProgram()
	form.show()
	sys.exit(app.exec_())





        # Connect "add" button with a custom function (addInputTextToListbox)
		# self.addBtn.clicked.connect(self.addInputTextToListbox)

	# def addInputTextToListbox(self):
		# txt = self.myTextInput.text()
		# self.listWidget.addItem(txt)
