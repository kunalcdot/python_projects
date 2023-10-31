# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threadgui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName(_fromUtf8("mainwindow"))
        mainwindow.resize(683, 695)
        mainwindow.setStyleSheet(_fromUtf8(""))
        self.epldBox = QtGui.QGroupBox(mainwindow)
        self.epldBox.setGeometry(QtCore.QRect(60, 510, 551, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("verdana"))
        font.setPointSize(-1)
        self.epldBox.setFont(font)
        self.epldBox.setStyleSheet(_fromUtf8("QGroupBox{\n"
"/*    background-color: rgb(216, 216, 216);\n"
"    background-color: rgb(228, 250, 255);\n"
"    background-color: rgb(236, 255, 224);*/\n"
"\n"
"    \n"
"border:1px solid gray;color:black;\n"
"background-color:#f2f1f7;\n"
"    border-radius: 10px;\n"
"    margin-top: 1px;\n"
"    \n"
"    font-size: 10px;\n"
"    font-family: verdana;\n"
"    color: #000;  \n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"margin: 1px 1px 1px 5px;\n"
"font-size: 12px;\n"
"    font-family: \"Georgia\";\n"
"\n"
"\n"
"}\n"
"QPushButton{\n"
"\n"
"background-color: #1A70DF;\n"
"     border-radius: 10px;  border: 0;  color: #fff;  \n"
"     \n"
"       padding: 10px 20px; \n"
"    font-size: 15px;\n"
"     font-family: rockwell;margin-top: 1px;\n"
"\n"
"\n"
"/*\n"
"background-color: #1A70DF;\n"
"    \n"
"     border-radius: 1px;  border: 0;  color: #fff;  \n"
"     cursor: pointer;  display: inline-block;    \n"
"     outline: none;  padding: 10px 20px;  text-decoration: none;      \n"
"     box-shadow: inset 0 -2px rgba(0,0,0,0.3);      transition: all .15s linear; \n"
"     -webkit-appearance: none;font-size: 15px;\n"
"     font-family: rockwell;margin-top: 1px;\n"
"     width:108px;\n"
"     font-size: 15px;\n"
"\n"
"*/\n"
"\n"
"\n"
"\n"
"/*\n"
"background-color: rgb(85, 0, 255);\n"
"font: 14pt \"Georgia\";\n"
"color: rgb(255, 253, 192);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"background-color: rgb(255, 255, 127);\n"
"}"))
        self.epldBox.setObjectName(_fromUtf8("epldBox"))
        self.layoutWidget = QtGui.QWidget(self.epldBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 494, 119))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_22 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_2.addWidget(self.label_22, 1, 0, 1, 1)
        self.add_ip = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_ip.setFont(font)
        self.add_ip.setStyleSheet(_fromUtf8(""))
        self.add_ip.setText(_fromUtf8(""))
        self.add_ip.setObjectName(_fromUtf8("add_ip"))
        self.gridLayout_2.addWidget(self.add_ip, 1, 2, 1, 1)
        self.label_20 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 3, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 3, 1, 1, 1)
        self.disp_data = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.disp_data.setFont(font)
        self.disp_data.setStyleSheet(_fromUtf8(""))
        self.disp_data.setObjectName(_fromUtf8("disp_data"))
        self.gridLayout_2.addWidget(self.disp_data, 1, 5, 1, 1)
        self.write_data_ip = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.write_data_ip.setFont(font)
        self.write_data_ip.setStyleSheet(_fromUtf8(""))
        self.write_data_ip.setText(_fromUtf8(""))
        self.write_data_ip.setObjectName(_fromUtf8("write_data_ip"))
        self.gridLayout_2.addWidget(self.write_data_ip, 3, 5, 1, 1)
        self.write_btn = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("rockwell"))
        font.setPointSize(-1)
        self.write_btn.setFont(font)
        self.write_btn.setStyleSheet(_fromUtf8(""))
        self.write_btn.setObjectName(_fromUtf8("write_btn"))
        self.gridLayout_2.addWidget(self.write_btn, 3, 4, 1, 1)
        self.write_add_ip = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.write_add_ip.setFont(font)
        self.write_add_ip.setStyleSheet(_fromUtf8(""))
        self.write_add_ip.setText(_fromUtf8(""))
        self.write_add_ip.setObjectName(_fromUtf8("write_add_ip"))
        self.gridLayout_2.addWidget(self.write_add_ip, 3, 2, 1, 1)
        self.get_data_btn = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("rockwell"))
        font.setPointSize(-1)
        self.get_data_btn.setFont(font)
        self.get_data_btn.setStyleSheet(_fromUtf8(""))
        self.get_data_btn.setObjectName(_fromUtf8("get_data_btn"))
        self.gridLayout_2.addWidget(self.get_data_btn, 1, 4, 1, 1)
        self.label_19 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 5, 1, 1)
        self.epldBox_2 = QtGui.QGroupBox(mainwindow)
        self.epldBox_2.setGeometry(QtCore.QRect(30, 20, 351, 471))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("verdana"))
        font.setPointSize(-1)
        self.epldBox_2.setFont(font)
        self.epldBox_2.setStyleSheet(_fromUtf8("QGroupBox{\n"
"/*    background-color: rgb(216, 216, 216);\n"
"    background-color: rgb(228, 250, 255);\n"
"    background-color: rgb(236, 255, 224);*/\n"
"\n"
"    \n"
"border:1px solid gray;color:black;\n"
"background-color:#f2f1f7;\n"
"    border-radius: 10px;\n"
"    margin-top: 1px;\n"
"    \n"
"    font-size: 10px;\n"
"    font-family: verdana;\n"
"    color: #000;  \n"
"\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"margin: 1px 1px 1px 5px;\n"
"font-size: 12px;\n"
"    font-family: \"Georgia\";\n"
"\n"
"\n"
"}\n"
"QPushButton{\n"
"\n"
"background-color: #1A70DF;\n"
"     border-radius: 10px;  border: 0;  color: #fff;  \n"
"        \n"
"      padding: 10px 20px;     \n"
"    font-size: 15px;\n"
"     font-family: rockwell;margin-top: 1px;\n"
"\n"
"\n"
"/*\n"
"background-color: #1A70DF;\n"
"    \n"
"     border-radius: 1px;  border: 0;  color: #fff;  \n"
"     cursor: pointer;  display: inline-block;    \n"
"     outline: none;  padding: 10px 20px;  text-decoration: none;      \n"
"     box-shadow: inset 0 -2px rgba(0,0,0,0.3);      transition: all .15s linear; \n"
"     -webkit-appearance: none;font-size: 15px;\n"
"     font-family: rockwell;margin-top: 1px;\n"
"     width:108px;\n"
"     font-size: 15px;\n"
"\n"
"*/\n"
"\n"
"\n"
"\n"
"/*\n"
"background-color: rgb(85, 0, 255);\n"
"font: 14pt \"Georgia\";\n"
"color: rgb(255, 253, 192);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"background-color: rgb(255, 255, 127);\n"
"}"))
        self.epldBox_2.setObjectName(_fromUtf8("epldBox_2"))
        self.layoutWidget1 = QtGui.QWidget(self.epldBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 291, 433))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sfp0_modabs = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.sfp0_modabs.setFont(font)
        self.sfp0_modabs.setObjectName(_fromUtf8("sfp0_modabs"))
        self.gridLayout.addWidget(self.sfp0_modabs, 12, 1, 1, 1)
        self.label_31 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout.addWidget(self.label_31, 11, 0, 1, 1)
        self.master_dis_status = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.master_dis_status.setFont(font)
        self.master_dis_status.setObjectName(_fromUtf8("master_dis_status"))
        self.gridLayout.addWidget(self.master_dis_status, 6, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1)
        self.clk2a_mode_3 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.clk2a_mode_3.setFont(font)
        self.clk2a_mode_3.setObjectName(_fromUtf8("clk2a_mode_3"))
        self.gridLayout.addWidget(self.clk2a_mode_3, 8, 1, 1, 1)
        self.zl_status = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.zl_status.setFont(font)
        self.zl_status.setStyleSheet(_fromUtf8(""))
        self.zl_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.zl_status.setObjectName(_fromUtf8("zl_status"))
        self.gridLayout.addWidget(self.zl_status, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.srr_phy_rst_status = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.srr_phy_rst_status.setFont(font)
        self.srr_phy_rst_status.setObjectName(_fromUtf8("srr_phy_rst_status"))
        self.gridLayout.addWidget(self.srr_phy_rst_status, 7, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.act_pas_status = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.act_pas_status.setFont(font)
        self.act_pas_status.setObjectName(_fromUtf8("act_pas_status"))
        self.gridLayout.addWidget(self.act_pas_status, 1, 1, 1, 1)
        self.mcp_rst_status = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.mcp_rst_status.setFont(font)
        self.mcp_rst_status.setObjectName(_fromUtf8("mcp_rst_status"))
        self.gridLayout.addWidget(self.mcp_rst_status, 3, 1, 1, 1)
        self.rim_ps_status = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.rim_ps_status.setFont(font)
        self.rim_ps_status.setObjectName(_fromUtf8("rim_ps_status"))
        self.gridLayout.addWidget(self.rim_ps_status, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.clk2a_mode_2 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.clk2a_mode_2.setFont(font)
        self.clk2a_mode_2.setObjectName(_fromUtf8("clk2a_mode_2"))
        self.gridLayout.addWidget(self.clk2a_mode_2, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.tp_rst_status = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.tp_rst_status.setFont(font)
        self.tp_rst_status.setObjectName(_fromUtf8("tp_rst_status"))
        self.gridLayout.addWidget(self.tp_rst_status, 4, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.label_27 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout.addWidget(self.label_27, 9, 0, 1, 1)
        self.label_35 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout.addWidget(self.label_35, 12, 0, 1, 1)
        self.label_30 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout.addWidget(self.label_30, 10, 0, 1, 1)
        self.coma_mode_status = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.coma_mode_status.setFont(font)
        self.coma_mode_status.setObjectName(_fromUtf8("coma_mode_status"))
        self.gridLayout.addWidget(self.coma_mode_status, 9, 1, 1, 1)
        self.sfp0_txflt = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.sfp0_txflt.setFont(font)
        self.sfp0_txflt.setObjectName(_fromUtf8("sfp0_txflt"))
        self.gridLayout.addWidget(self.sfp0_txflt, 10, 1, 1, 1)
        self.sfp0_rxlos = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.sfp0_rxlos.setFont(font)
        self.sfp0_rxlos.setObjectName(_fromUtf8("sfp0_rxlos"))
        self.gridLayout.addWidget(self.sfp0_rxlos, 11, 1, 1, 1)
        self.label_36 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_36.setFont(font)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout.addWidget(self.label_36, 15, 0, 1, 1)
        self.label_38 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_38.setFont(font)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout.addWidget(self.label_38, 14, 0, 1, 1)
        self.label_37 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_37.setFont(font)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout.addWidget(self.label_37, 13, 0, 1, 1)
        self.sfp1_txflt = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.sfp1_txflt.setFont(font)
        self.sfp1_txflt.setObjectName(_fromUtf8("sfp1_txflt"))
        self.gridLayout.addWidget(self.sfp1_txflt, 13, 1, 1, 1)
        self.sfp1_rxlos = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.sfp1_rxlos.setFont(font)
        self.sfp1_rxlos.setObjectName(_fromUtf8("sfp1_rxlos"))
        self.gridLayout.addWidget(self.sfp1_rxlos, 14, 1, 1, 1)
        self.sfp1_modabs = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.sfp1_modabs.setFont(font)
        self.sfp1_modabs.setObjectName(_fromUtf8("sfp1_modabs"))
        self.gridLayout.addWidget(self.sfp1_modabs, 15, 1, 1, 1)
        self.frame = QtGui.QFrame(mainwindow)
        self.frame.setGeometry(QtCore.QRect(390, 10, 271, 141))
        self.frame.setStyleSheet(_fromUtf8("\n"
"QFrame{\n"
"/*background-color: qlineargradient( x1:0 y1:0, x2:1 y2:1, \n"
"stop:0 \n"
"#a5c2ff,\n"
" stop:1 \n"
"#687184\n"
");*/\n"
"\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"    color: gray;\n"
"    margin: 1px 1px 1px 1px;\n"
"\n"
"font-size: 14px;\n"
"    font-family: \"Cambria\";\n"
"\n"
"\n"
"\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layoutWidget2 = QtGui.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 20, 231, 111))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(5, 2, 5, 1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_16 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)
        self.label_conn_status = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        self.label_conn_status.setFont(font)
        self.label_conn_status.setObjectName(_fromUtf8("label_conn_status"))
        self.gridLayout_3.addWidget(self.label_conn_status, 0, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_card_name = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        self.label_card_name.setFont(font)
        self.label_card_name.setObjectName(_fromUtf8("label_card_name"))
        self.gridLayout_3.addWidget(self.label_card_name, 1, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_3.addWidget(self.label_23, 2, 0, 1, 1)
        self.label_gui_ver = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        self.label_gui_ver.setFont(font)
        self.label_gui_ver.setObjectName(_fromUtf8("label_gui_ver"))
        self.gridLayout_3.addWidget(self.label_gui_ver, 2, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_3.addWidget(self.label_26, 3, 0, 1, 1)
        self.label_epld_ver = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(-1)
        self.label_epld_ver.setFont(font)
        self.label_epld_ver.setObjectName(_fromUtf8("label_epld_ver"))
        self.gridLayout_3.addWidget(self.label_epld_ver, 3, 1, 1, 1)
        self.epldBox_3 = QtGui.QGroupBox(mainwindow)
        self.epldBox_3.setGeometry(QtCore.QRect(390, 160, 271, 281))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("verdana"))
        font.setPointSize(-1)
        self.epldBox_3.setFont(font)
        self.epldBox_3.setStyleSheet(_fromUtf8("QGroupBox{\n"
"/*    background-color: rgb(216, 216, 216);\n"
"    background-color: rgb(228, 250, 255);\n"
"    background-color: rgb(236, 255, 224);*/\n"
"\n"
"    \n"
"border:1px solid gray;color:black;\n"
"background-color:#ffffcc;/*#f2f1f7;*/\n"
"    border-radius: 2px;\n"
"    margin-top: 1px;\n"
"    \n"
"    font-size: 10px;\n"
"    font-family: verdana;\n"
"    color: #000;  \n"
"\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"margin: 1px 1px 1px 5px;\n"
"font-size: 12px;\n"
"    font-family: \"Georgia\";\n"
"\n"
"\n"
"}\n"
"QPushButton{\n"
"\n"
"background-color: #1A708F;\n"
"     border-radius: 10px;  color: #fff;  \n"
"     \n"
"    \n"
" padding: 5px 5px; \n"
"       font-size: 15px;\n"
"     font-family: rockwell;margin-top: 1px;\n"
"\n"
"\n"
"/*\n"
"background-color: #1A70DF;\n"
"    \n"
"     border-radius: 1px;  border: 0;  color: #fff;  \n"
"     cursor: pointer;  display: inline-block;    \n"
"     outline: none;  padding: 10px 20px;  text-decoration: none;      \n"
"     box-shadow: inset 0 -2px rgba(0,0,0,0.3);      transition: all .15s linear; \n"
"     -webkit-appearance: none;font-size: 15px;\n"
"     font-family: rockwell;margin-top: 1px;\n"
"     width:108px;\n"
"     font-size: 15px;\n"
"\n"
"*/\n"
"\n"
"\n"
"\n"
"/*\n"
"background-color: rgb(85, 0, 255);\n"
"font: 14pt \"Georgia\";\n"
"color: rgb(255, 253, 192);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"}\n"
"\n"
"#exit_btn{\n"
"background-color: #af1818;\n"
"}\n"
"\n"
"#mcp_rst_btn{\n"
"background-color: #870eaf;\n"
"}\n"
"\n"
"#tp_rst_btn{\n"
"background-color: #11033a;\n"
"}\n"
"\n"
"#brd_rst_btn{\n"
"background-color: #025b3e;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"background-color: rgb(255, 255, 127);\n"
"}"))
        self.epldBox_3.setObjectName(_fromUtf8("epldBox_3"))
        self.clk2b_mode_5 = QtGui.QLabel(self.epldBox_3)
        self.clk2b_mode_5.setGeometry(QtCore.QRect(194, 279, 137, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.clk2b_mode_5.setFont(font)
        self.clk2b_mode_5.setObjectName(_fromUtf8("clk2b_mode_5"))
        self.layoutWidget_2 = QtGui.QWidget(self.epldBox_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 247, 237))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_4.setHorizontalSpacing(15)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_32 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_32.setFont(font)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_4.addWidget(self.label_32, 2, 0, 1, 1)
        self.brd_rst_btn = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("rockwell"))
        font.setPointSize(-1)
        self.brd_rst_btn.setFont(font)
        self.brd_rst_btn.setStyleSheet(_fromUtf8(""))
        self.brd_rst_btn.setObjectName(_fromUtf8("brd_rst_btn"))
        self.gridLayout_4.addWidget(self.brd_rst_btn, 0, 2, 1, 1)
        self.tp_rst_btn = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("rockwell"))
        font.setPointSize(-1)
        self.tp_rst_btn.setFont(font)
        self.tp_rst_btn.setStyleSheet(_fromUtf8(""))
        self.tp_rst_btn.setObjectName(_fromUtf8("tp_rst_btn"))
        self.gridLayout_4.addWidget(self.tp_rst_btn, 1, 2, 1, 1)
        self.label_34 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_34.setFont(font)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_4.addWidget(self.label_34, 5, 0, 1, 1)
        self.exit_btn = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("rockwell"))
        font.setPointSize(-1)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet(_fromUtf8(""))
        self.exit_btn.setObjectName(_fromUtf8("exit_btn"))
        self.gridLayout_4.addWidget(self.exit_btn, 5, 2, 1, 1)
        self.label_33 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_4.addWidget(self.label_33, 3, 0, 1, 1)
        self.label_29 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_4.addWidget(self.label_29, 1, 0, 1, 1)
        self.label_28 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(-1)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_4.addWidget(self.label_28, 0, 0, 1, 1)
        self.mcp_rst_btn = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("rockwell"))
        font.setPointSize(-1)
        self.mcp_rst_btn.setFont(font)
        self.mcp_rst_btn.setStyleSheet(_fromUtf8(""))
        self.mcp_rst_btn.setObjectName(_fromUtf8("mcp_rst_btn"))
        self.gridLayout_4.addWidget(self.mcp_rst_btn, 2, 2, 1, 1)
        self.dump_btn = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("rockwell"))
        font.setPointSize(-1)
        self.dump_btn.setFont(font)
        self.dump_btn.setStyleSheet(_fromUtf8(""))
        self.dump_btn.setObjectName(_fromUtf8("dump_btn"))
        self.gridLayout_4.addWidget(self.dump_btn, 3, 2, 1, 1)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(_translate("mainwindow", "Dialog", None))
        self.epldBox.setTitle(_translate("mainwindow", "EPLD Register Access", None))
        self.label_22.setText(_translate("mainwindow", "Read", None))
        self.add_ip.setPlaceholderText(_translate("mainwindow", "Range: 0-ff", None))
        self.label_20.setText(_translate("mainwindow", "Write", None))
        self.label_21.setText(_translate("mainwindow", "0 x", None))
        self.disp_data.setText(_translate("mainwindow", "0xFF", None))
        self.disp_data.setPlaceholderText(_translate("mainwindow", "Range: 0-ff", None))
        self.write_data_ip.setPlaceholderText(_translate("mainwindow", "Range: 0-ff", None))
        self.write_btn.setText(_translate("mainwindow", "Write", None))
        self.write_add_ip.setPlaceholderText(_translate("mainwindow", "Range: 0-ff", None))
        self.get_data_btn.setText(_translate("mainwindow", "Get Data", None))
        self.label_19.setText(_translate("mainwindow", "0 x", None))
        self.label.setText(_translate("mainwindow", "    Reg Address", None))
        self.label_10.setText(_translate("mainwindow", "    Data", None))
        self.epldBox_2.setTitle(_translate("mainwindow", "EPLD Status", None))
        self.sfp0_modabs.setText(_translate("mainwindow", "NA", None))
        self.label_31.setText(_translate("mainwindow", "SFP0 RX LOS", None))
        self.master_dis_status.setText(_translate("mainwindow", "NA", None))
        self.label_13.setText(_translate("mainwindow", "SRR PHY RST", None))
        self.label_15.setText(_translate("mainwindow", "RFU", None))
        self.clk2a_mode_3.setText(_translate("mainwindow", "NA", None))
        self.zl_status.setText(_translate("mainwindow", "NA", None))
        self.label_6.setText(_translate("mainwindow", "MCP Reset Status", None))
        self.srr_phy_rst_status.setText(_translate("mainwindow", "NA", None))
        self.label_7.setText(_translate("mainwindow", "RIM Present", None))
        self.act_pas_status.setText(_translate("mainwindow", "NA", None))
        self.mcp_rst_status.setText(_translate("mainwindow", "NA", None))
        self.rim_ps_status.setText(_translate("mainwindow", "NA", None))
        self.label_5.setText(_translate("mainwindow", "Card Status(Act/Pas)", None))
        self.clk2a_mode_2.setText(_translate("mainwindow", "NA", None))
        self.label_4.setText(_translate("mainwindow", "Zarlink Lock Status", None))
        self.label_11.setText(_translate("mainwindow", "Master Disable", None))
        self.label_8.setText(_translate("mainwindow", "TP Reset Status", None))
        self.tp_rst_status.setText(_translate("mainwindow", "NA", None))
        self.label_12.setText(_translate("mainwindow", "SF Reset Status", None))
        self.label_27.setText(_translate("mainwindow", "COMA Mode", None))
        self.label_35.setText(_translate("mainwindow", "SFP0 MOD ABS", None))
        self.label_30.setText(_translate("mainwindow", "SFP0 TX Fault", None))
        self.coma_mode_status.setText(_translate("mainwindow", "NA", None))
        self.sfp0_txflt.setText(_translate("mainwindow", "NA", None))
        self.sfp0_rxlos.setText(_translate("mainwindow", "NA", None))
        self.label_36.setText(_translate("mainwindow", "SFP1 MOD ABS", None))
        self.label_38.setText(_translate("mainwindow", "SFP1 RX LOS", None))
        self.label_37.setText(_translate("mainwindow", "SFP1 TX Fault", None))
        self.sfp1_txflt.setText(_translate("mainwindow", "NA", None))
        self.sfp1_rxlos.setText(_translate("mainwindow", "NA", None))
        self.sfp1_modabs.setText(_translate("mainwindow", "NA", None))
        self.label_16.setText(_translate("mainwindow", "Conn. Status", None))
        self.label_conn_status.setText(_translate("mainwindow", "Disconnected", None))
        self.label_17.setText(_translate("mainwindow", "Card Type", None))
        self.label_card_name.setText(_translate("mainwindow", "NA", None))
        self.label_23.setText(_translate("mainwindow", "GUI Ver", None))
        self.label_gui_ver.setText(_translate("mainwindow", "NA", None))
        self.label_26.setText(_translate("mainwindow", "EPLD ver", None))
        self.label_epld_ver.setText(_translate("mainwindow", "NA", None))
        self.epldBox_3.setTitle(_translate("mainwindow", "Button Panel", None))
        self.clk2b_mode_5.setText(_translate("mainwindow", "NA", None))
        self.label_32.setText(_translate("mainwindow", "MCP only Reset", None))
        self.brd_rst_btn.setText(_translate("mainwindow", "Reset", None))
        self.tp_rst_btn.setText(_translate("mainwindow", "Reset", None))
        self.label_34.setText(_translate("mainwindow", "Close App", None))
        self.exit_btn.setText(_translate("mainwindow", "EXIT", None))
        self.label_33.setText(_translate("mainwindow", "EPLD Dump", None))
        self.label_29.setText(_translate("mainwindow", "TP only Reset", None))
        self.label_28.setText(_translate("mainwindow", "Main board Reset", None))
        self.mcp_rst_btn.setText(_translate("mainwindow", "Reset", None))
        self.dump_btn.setText(_translate("mainwindow", "Dump", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainwindow = QtGui.QDialog()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())

