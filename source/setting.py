# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import sys, ctypes, os, shutil, subprocess, time
from subprocess import Popen, PIPE, CREATE_NEW_CONSOLE


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
		
def emptyf():
	pass
	
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def copy_ow(from_path, to_path): #overwrite folder
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)
		
		
class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(756, 505)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../System/Download/settings-5-xxl.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Dialog.setWindowIcon(icon)
		Dialog.setAutoFillBackground(False)
		Dialog.setSizeGripEnabled(False)
		self.checkBox_9 = QtGui.QCheckBox(Dialog)
		self.checkBox_9.setEnabled(True)
		self.checkBox_9.setGeometry(QtCore.QRect(440, 14, 270, 16))
		self.checkBox_9.setAutoFillBackground(True)
		self.checkBox_9.setCheckable(True)
		self.checkBox_9.setChecked(False)
		self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
		self.pushButton = QtGui.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(620, 471, 79, 23))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2 = QtGui.QPushButton(Dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(371, 471, 84, 23))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.pushButton_3 = QtGui.QPushButton(Dialog)
		self.pushButton_3.setGeometry(QtCore.QRect(490, 471, 101, 23))
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.label_25 = QtGui.QLabel(Dialog)
		self.label_25.setGeometry(QtCore.QRect(20, 470, 271, 16))
		self.label_25.setObjectName(_fromUtf8("label_25"))
		self.label_26 = QtGui.QLabel(Dialog)
		self.label_26.setGeometry(QtCore.QRect(451, 40, 151, 16))
		self.label_26.setObjectName(_fromUtf8("label_26"))
		self.line = QtGui.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(20, 130, 361, 20))
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName(_fromUtf8("line"))
		self.line_2 = QtGui.QFrame(Dialog)
		self.line_2.setGeometry(QtCore.QRect(410, 20, 20, 421))
		self.line_2.setFrameShape(QtGui.QFrame.VLine)
		self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_2.setObjectName(_fromUtf8("line_2"))
		self.layoutWidget = QtGui.QWidget(Dialog)
		self.layoutWidget.setGeometry(QtCore.QRect(20, 24, 291, 91))
		self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
		self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.label = QtGui.QLabel(self.layoutWidget)
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
		self.lineEdit.setText(_fromUtf8(""))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
		self.label_2 = QtGui.QLabel(self.layoutWidget)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
		self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
		self.lineEdit_2.setText(_fromUtf8(""))
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
		self.label_3 = QtGui.QLabel(self.layoutWidget)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
		self.comboBox = QtGui.QComboBox(self.layoutWidget)
		self.comboBox.setObjectName(_fromUtf8("comboBox"))
		self.comboBox.addItem(_fromUtf8(""))
		self.comboBox.addItem(_fromUtf8(""))
		self.comboBox.addItem(_fromUtf8(""))
		self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
		self.layoutWidget1 = QtGui.QWidget(Dialog)
		self.layoutWidget1.setGeometry(QtCore.QRect(20, 150, 391, 231))
		self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
		self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label_4 = QtGui.QLabel(self.layoutWidget1)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.verticalLayout.addWidget(self.label_4)
		self.checkBox = QtGui.QCheckBox(self.layoutWidget1)
		self.checkBox.setObjectName(_fromUtf8("checkBox"))
		self.verticalLayout.addWidget(self.checkBox)
		self.checkBox_2 = QtGui.QCheckBox(self.layoutWidget1)
		self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
		self.verticalLayout.addWidget(self.checkBox_2)
		self.checkBox_3 = QtGui.QCheckBox(self.layoutWidget1)
		self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
		self.verticalLayout.addWidget(self.checkBox_3)
		self.checkBox_4 = QtGui.QCheckBox(self.layoutWidget1)
		self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
		self.verticalLayout.addWidget(self.checkBox_4)
		self.checkBox_5 = QtGui.QCheckBox(self.layoutWidget1)
		self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
		self.verticalLayout.addWidget(self.checkBox_5)
		self.checkBox_6 = QtGui.QCheckBox(self.layoutWidget1)
		self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
		self.verticalLayout.addWidget(self.checkBox_6)
		self.checkBox_7 = QtGui.QCheckBox(self.layoutWidget1)
		self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
		self.verticalLayout.addWidget(self.checkBox_7)
		self.checkBox_8 = QtGui.QCheckBox(self.layoutWidget1)
		self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
		self.verticalLayout.addWidget(self.checkBox_8)
		self.layoutWidget2 = QtGui.QWidget(Dialog)
		self.layoutWidget2.setGeometry(QtCore.QRect(450, 260, 291, 140))
		self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
		self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget2)
		self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
		self.label_7 = QtGui.QLabel(self.layoutWidget2)
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.verticalLayout_4.addWidget(self.label_7)
		self.label_8 = QtGui.QLabel(self.layoutWidget2)
		self.label_8.setObjectName(_fromUtf8("label_8"))
		self.verticalLayout_4.addWidget(self.label_8)
		self.gridLayout_3 = QtGui.QGridLayout()
		self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
		self.label_16 = QtGui.QLabel(self.layoutWidget2)
		self.label_16.setObjectName(_fromUtf8("label_16"))
		self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)
		self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget2)
		self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
		self.gridLayout_3.addWidget(self.lineEdit_7, 0, 1, 1, 1)
		self.label_18 = QtGui.QLabel(self.layoutWidget2)
		self.label_18.setObjectName(_fromUtf8("label_18"))
		self.gridLayout_3.addWidget(self.label_18, 0, 2, 1, 1)
		self.label_19 = QtGui.QLabel(self.layoutWidget2)
		self.label_19.setObjectName(_fromUtf8("label_19"))
		self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)
		self.lineEdit_8 = QtGui.QLineEdit(self.layoutWidget2)
		self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
		self.gridLayout_3.addWidget(self.lineEdit_8, 1, 1, 1, 1)
		self.label_20 = QtGui.QLabel(self.layoutWidget2)
		self.label_20.setObjectName(_fromUtf8("label_20"))
		self.gridLayout_3.addWidget(self.label_20, 1, 2, 1, 1)
		self.label_21 = QtGui.QLabel(self.layoutWidget2)
		self.label_21.setObjectName(_fromUtf8("label_21"))
		self.gridLayout_3.addWidget(self.label_21, 2, 0, 1, 1)
		self.lineEdit_9 = QtGui.QLineEdit(self.layoutWidget2)
		self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
		self.gridLayout_3.addWidget(self.lineEdit_9, 2, 1, 1, 1)
		self.label_22 = QtGui.QLabel(self.layoutWidget2)
		self.label_22.setObjectName(_fromUtf8("label_22"))
		self.gridLayout_3.addWidget(self.label_22, 2, 2, 1, 1)
		self.label_23 = QtGui.QLabel(self.layoutWidget2)
		self.label_23.setObjectName(_fromUtf8("label_23"))
		self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)
		self.lineEdit_10 = QtGui.QLineEdit(self.layoutWidget2)
		self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
		self.gridLayout_3.addWidget(self.lineEdit_10, 3, 1, 1, 1)
		self.label_24 = QtGui.QLabel(self.layoutWidget2)
		self.label_24.setObjectName(_fromUtf8("label_24"))
		self.gridLayout_3.addWidget(self.label_24, 3, 2, 1, 1)
		self.verticalLayout_4.addLayout(self.gridLayout_3)
		self.layoutWidget3 = QtGui.QWidget(Dialog)
		self.layoutWidget3.setGeometry(QtCore.QRect(450, 100, 291, 140))
		self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget3)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.label_5 = QtGui.QLabel(self.layoutWidget3)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.verticalLayout_3.addWidget(self.label_5)
		self.label_6 = QtGui.QLabel(self.layoutWidget3)
		self.label_6.setObjectName(_fromUtf8("label_6"))
		self.verticalLayout_3.addWidget(self.label_6)
		self.gridLayout_2 = QtGui.QGridLayout()
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.label_9 = QtGui.QLabel(self.layoutWidget3)
		self.label_9.setObjectName(_fromUtf8("label_9"))
		self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
		self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget3)
		self.lineEdit_3.setReadOnly(False)
		self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
		self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)
		self.label_13 = QtGui.QLabel(self.layoutWidget3)
		self.label_13.setObjectName(_fromUtf8("label_13"))
		self.gridLayout_2.addWidget(self.label_13, 0, 2, 1, 1)
		self.label_10 = QtGui.QLabel(self.layoutWidget3)
		self.label_10.setObjectName(_fromUtf8("label_10"))
		self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
		self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget3)
		self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
		self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)
		self.label_14 = QtGui.QLabel(self.layoutWidget3)
		self.label_14.setObjectName(_fromUtf8("label_14"))
		self.gridLayout_2.addWidget(self.label_14, 1, 2, 1, 1)
		self.label_11 = QtGui.QLabel(self.layoutWidget3)
		self.label_11.setObjectName(_fromUtf8("label_11"))
		self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
		self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget3)
		self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
		self.gridLayout_2.addWidget(self.lineEdit_5, 2, 1, 1, 1)
		self.label_15 = QtGui.QLabel(self.layoutWidget3)
		self.label_15.setObjectName(_fromUtf8("label_15"))
		self.gridLayout_2.addWidget(self.label_15, 2, 2, 1, 1)
		self.label_12 = QtGui.QLabel(self.layoutWidget3)
		self.label_12.setObjectName(_fromUtf8("label_12"))
		self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
		self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget3)
		self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
		self.gridLayout_2.addWidget(self.lineEdit_6, 3, 1, 1, 1)
		self.label_17 = QtGui.QLabel(self.layoutWidget3)
		self.label_17.setObjectName(_fromUtf8("label_17"))
		self.gridLayout_2.addWidget(self.label_17, 3, 2, 1, 1)
		self.verticalLayout_3.addLayout(self.gridLayout_2)
		self.layoutWidget4 = QtGui.QWidget(Dialog)
		self.layoutWidget4.setGeometry(QtCore.QRect(450, 45, 261, 51))
		self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget4)
		self.horizontalLayout.setSpacing(4)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.lineEdit_11 = QtGui.QLineEdit(self.layoutWidget4)
		self.lineEdit_11.setText(_fromUtf8(""))
		self.lineEdit_11.setReadOnly(False)
		self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
		self.horizontalLayout.addWidget(self.lineEdit_11)
		self.toolButton_2 = QtGui.QToolButton(self.layoutWidget4)
		self.toolButton_2.setCheckable(False)
		self.toolButton_2.setChecked(False)
		self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
		self.horizontalLayout.addWidget(self.toolButton_2)
		self.line_3 = QtGui.QFrame(Dialog)
		self.line_3.setGeometry(QtCore.QRect(10, 450, 711, 20))
		self.line_3.setFrameShape(QtGui.QFrame.HLine)
		self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_3.setObjectName(_fromUtf8("line_3"))
		self.pushButton_4 = QtGui.QPushButton(Dialog)
		self.pushButton_4.setGeometry(QtCore.QRect(450, 421, 111, 21))
		self.pushButton_4.setCheckable(False)
		self.pushButton_4.setChecked(False)
		self.pushButton_4.setAutoRepeat(False)
		self.pushButton_4.setAutoExclusive(False)
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.pushButton_5 = QtGui.QPushButton(Dialog)
		self.pushButton_5.setGeometry(QtCore.QRect(600, 420, 101, 23))
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.label_27 = QtGui.QLabel(Dialog)
		self.label_27.setGeometry(QtCore.QRect(456, 12, 20, 19))
		self.label_27.setText(_fromUtf8(""))
		self.label_27.setPixmap(QtGui.QPixmap(_fromUtf8("../../System/Download/uac-icon-200x200.png")))
		self.label_27.setScaledContents(True)
		self.label_27.setObjectName(_fromUtf8("label_27"))
		self.layoutWidget.raise_()
		self.layoutWidget.raise_()
		self.layoutWidget.raise_()
		self.layoutWidget.raise_()
		self.checkBox_9.raise_()
		self.pushButton.raise_()
		self.pushButton_2.raise_()
		self.pushButton_3.raise_()
		self.label_25.raise_()
		self.label_26.raise_()
		self.layoutWidget.raise_()
		self.line.raise_()
		self.line_2.raise_()
		self.line_3.raise_()
		self.pushButton_4.raise_()
		self.pushButton_5.raise_()
		self.label_27.raise_()
		
		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Setting", None))
		self.checkBox_9.setText(_translate("Dialog", "(Admin!) Enable Afterburner auto-switch", None))
		self.pushButton.setText(_translate("Dialog", "Start mining!", None))
		self.pushButton_2.setText(_translate("Dialog", "Save settings", None))
		self.pushButton_3.setText(_translate("Dialog", "Start Benchmark!", None))
		self.label_25.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:8pt;\">Multi-Algo Switching Manager v0.0.3 by Sev18</span></p></body></html>", None))
		self.label_26.setText(_translate("Dialog", "Select MSIAfterburner.exe:", None))
		self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Workername:</span></p></body></html>", None))
		self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Worker password:</span></p></body></html>", None))
		self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Region:</span></p></body></html>", None))
		self.comboBox.setItemText(0, _translate("Dialog", "Asia", None))
		self.comboBox.setItemText(1, _translate("Dialog", "Europe", None))
		self.comboBox.setItemText(2, _translate("Dialog", "U.S.", None))
		self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Select Algorithm</span>(*Recommended*)</p></body></html>", None))
		self.checkBox.setText(_translate("Dialog", "*Ethash* - Ethreum, Ethereum-classic, Expanse, Musicoin", None))
		self.checkBox_2.setText(_translate("Dialog", "*Equihash* - Zcash, Zclassic", None))
		self.checkBox_3.setText(_translate("Dialog", "Cryptonight - Monero", None))
		self.checkBox_4.setText(_translate("Dialog", "Groestl - Groestlcoin", None))
		self.checkBox_5.setText(_translate("Dialog", "Lyra2RE2 - Vertcoin", None))
		self.checkBox_6.setText(_translate("Dialog", "Myriad-Groestl - Digibyte, Myriadcoin", None))
		self.checkBox_7.setText(_translate("Dialog", "NeoScrypt - Feathercoin, Pheonixcoin", None))
		self.checkBox_8.setText(_translate("Dialog", "Skein - Digibyte, Myriadcoin", None))
		self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Mem-clock dependent algorithm setting</span></p></body></html>", None))
		self.label_8.setText(_translate("Dialog", "(For Ethash, Cryptonight, etc.)", None))
		self.label_16.setText(_translate("Dialog", "Power Limit", None))
		self.label_18.setText(_translate("Dialog", "%", None))
		self.label_19.setText(_translate("Dialog", "Core Clock", None))
		self.label_20.setText(_translate("Dialog", "MHz", None))
		self.label_21.setText(_translate("Dialog", "Mem. Clock", None))
		self.label_22.setText(_translate("Dialog", "MHz", None))
		self.label_23.setText(_translate("Dialog", "Fan Speed", None))
		self.label_24.setText(_translate("Dialog", "%", None))
		self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Core-clock dependent algorithm setting</span></p></body></html>", None))
		self.label_6.setText(_translate("Dialog", "(For Equihash, Groestl, etc.)", None))
		self.label_9.setText(_translate("Dialog", "Power Limit", None))
		self.label_13.setText(_translate("Dialog", "%", None))
		self.label_10.setText(_translate("Dialog", "Core Clock", None))
		self.label_14.setText(_translate("Dialog", "MHz", None))
		self.label_11.setText(_translate("Dialog", "Mem. Clock", None))
		self.label_15.setText(_translate("Dialog", "MHz", None))
		self.label_12.setText(_translate("Dialog", "Fan Speed", None))
		self.label_17.setText(_translate("Dialog", "%", None))
		self.toolButton_2.setText(_translate("Dialog", "...", None))
		self.pushButton_4.setText(_translate("Dialog", "Save OC setting", None))
		self.pushButton_5.setText(_translate("Dialog", "Restore setting", None))


class XDialog(QDialog, Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		#load setting.cfg
		cfgfile = open('setting.cfg', 'r')
		cfgline = cfgfile.readlines()
		cfgdict = {}
		for line in cfgline:
			line = line.strip()
			if '=' in line:
				cfgdict[line.split('=')[0]] = line.split('=')[1]
		self.lineEdit.setText(cfgdict['workername'])
		self.lineEdit_2.setText(cfgdict['password'])
		self.lineEdit_11.setText(cfgdict['ABpath'])
		self.lineEdit_3.setText(cfgdict['zecPowerLimit'])
		self.lineEdit_4.setText(str(float(cfgdict['zecCoreClkBoost'])/1000))
		self.lineEdit_5.setText(str(float(cfgdict['zecMemClkBoost'])/1000))
		self.lineEdit_6.setText(cfgdict['zecFanSpeed'])
		self.lineEdit_7.setText(cfgdict['ethPowerLimit'])
		self.lineEdit_8.setText(str(float(cfgdict['ethCoreClkBoost'])/1000))
		self.lineEdit_9.setText(str(float(cfgdict['ethMemClkBoost'])/1000))
		self.lineEdit_10.setText(cfgdict['ethFanSpeed'])
		self.comboBox.setCurrentIndex(int(cfgdict['region']))
		algolist = cfgdict['selAlgo'].split(',')
		for algo in algolist:
			if algo == 'Ethash':
				self.checkBox.setChecked(True)
			elif algo == 'Equihash':
				self.checkBox_2.setChecked(True)
			elif algo == 'Cryptonight':
				self.checkBox_3.setChecked(True)
			elif algo == 'Groestl':
				self.checkBox_4.setChecked(True)
			elif algo == 'Lyra2RE2':
				self.checkBox_5.setChecked(True)
			elif algo == 'Myriad-Groestl':
				self.checkBox_6.setChecked(True)
			elif algo == 'NeoScrypt':
				self.checkBox_7.setChecked(True)
			elif algo == 'Skein':
				self.checkBox_8.setChecked(True)
		if cfgdict['ABswitch'] == '1':
			self.checkBox_9.setChecked(True)
		else:
			self.lineEdit_11.setDisabled(True)
			self.lineEdit_3.setDisabled(True)
			self.lineEdit_4.setDisabled(True)
			self.lineEdit_5.setDisabled(True)
			self.lineEdit_6.setDisabled(True)
			self.lineEdit_7.setDisabled(True)
			self.lineEdit_8.setDisabled(True)
			self.lineEdit_9.setDisabled(True)
			self.lineEdit_10.setDisabled(True)
			self.toolButton_2.setEnabled(False)
			self.pushButton_4.setEnabled(False)
			self.pushButton_5.setEnabled(False)
		cfgfile.close()
		
		#button connection
		self.pushButton_2.clicked.connect(self.saveSet)
		self.toolButton_2.clicked.connect(self.abPath)
		self.pushButton_4.clicked.connect(self.ocSet)
		self.pushButton_5.clicked.connect(self.restOC)
		self.pushButton_3.clicked.connect(self.runBench)
		self.pushButton.clicked.connect(self.runManager)
		
		#enable ABswitch
		self.checkBox_9.stateChanged.connect(self.enableABswitch)
	
	def saveSet(self):
		cfgfile = open('setting.cfg','w')
		selAlgolist = []
		nonselAlgolist = []
		if self.checkBox.isChecked() == True:
			selAlgolist.append('Ethash')
		else:
			nonselAlgolist.append('Ethash')
		if self.checkBox_2.isChecked() == True:
			selAlgolist.append('Equihash')
		else:
			nonselAlgolist.append('Equihash')
		if self.checkBox_3.isChecked() == True:
			selAlgolist.append('Cryptonight')
		else:
			nonselAlgolist.append('Cryptonight')
		if self.checkBox_4.isChecked() == True:
			selAlgolist.append('Groestl')
		else:
			nonselAlgolist.append('Groestl')
		if self.checkBox_5.isChecked() == True:
			selAlgolist.append('Lyra2RE2')
		else:
			nonselAlgolist.append('Lyra2RE2')
		if self.checkBox_6.isChecked() == True:
			selAlgolist.append('Myriad-Groestl')
		else:
			nonselAlgolist.append('Myriad-Groestl')
		if self.checkBox_7.isChecked() == True:
			selAlgolist.append('NeoScrypt')
		else:
			nonselAlgolist.append('NeoScrypt')
		if self.checkBox_8.isChecked() == True:
			selAlgolist.append('Skein')
		else:
			nonselAlgolist.append('Skein')

		selAlgotxt = ''
		nonselAlgotxt = ''
		for i in selAlgolist:
			selAlgotxt = selAlgotxt + i + ','
		for i in nonselAlgolist:
			nonselAlgotxt = nonselAlgotxt + i + ','
		
		ABswitchtxt = ''
		if self.checkBox_9.isChecked() == True:
			ABswitchtxt = '1'
		else:
			ABswitchtxt = '0'
		
		text = '[Setting]\nworkername='+self.lineEdit.text()+'\npassword='+self.lineEdit_2.text()+'\nregion='+str(self.comboBox.currentIndex())+'\n#region 0-asia 1-europe 2-U.S.\nselAlgo='+selAlgotxt+'\nnonselAlgo='+nonselAlgotxt+'\nABswitch='+ABswitchtxt+'\n#ABswitch 0-off 1-on\nABpath='+self.lineEdit_11.text()+'\n\n[zec]\n[Startup]\nzecFormat=2\nzecPowerLimit='+str(int(self.lineEdit_3.text()))+'\nzecThermalLimit=\nzecCoreClkBoost='+str(int(float(self.lineEdit_4.text())*1000))+'\nzecMemClkBoost='+str(int(float(self.lineEdit_5.text())*1000))+'\nzecFanMode=0\nzecFanSpeed='+str(int(self.lineEdit_6.text()))+'\n\n[eth]\n[Startup]\nethFormat=2\nethPowerLimit='+str(int(self.lineEdit_7.text()))+'\nethThermalLimit=\nethCoreClkBoost='+str(int(float(self.lineEdit_8.text())*1000))+'\nethMemClkBoost='+str(int(float(self.lineEdit_9.text())*1000))+'\nethFanMode=0\nethFanSpeed='+str(int(self.lineEdit_10.text()))
		
		cfgfile.write(text)
		cfgfile.close()
		QMessageBox.information(self, 'Save', 'Setting successfully saved.')
		manbatch = open('start_manager.bat','w')
		manbtext = ':start\n'+str(os.getcwd())+'\manager.exe'+'\ntimeout 1\ngoto start'
		manbatch.write(manbtext)
		manbatch.close()
		
		
	def enableABswitch(self):
		if self.checkBox_9.isChecked():
			if is_admin():
				self.lineEdit_11.setDisabled(False)
				self.lineEdit_3.setDisabled(False)
				self.lineEdit_4.setDisabled(False)
				self.lineEdit_5.setDisabled(False)
				self.lineEdit_6.setDisabled(False)
				self.lineEdit_7.setDisabled(False)
				self.lineEdit_8.setDisabled(False)
				self.lineEdit_9.setDisabled(False)
				self.lineEdit_10.setDisabled(False)
				self.toolButton_2.setEnabled(True)
				self.pushButton_4.setEnabled(True)
				self.pushButton_5.setEnabled(True)
			else:
				QMessageBox.information(self, 'Warning', 'Administrator privilege required. Please re-run as administrator.')
				self.checkBox_9.setChecked(False)
						
		else:
			self.lineEdit_11.setDisabled(True)
			self.lineEdit_3.setDisabled(True)
			self.lineEdit_4.setDisabled(True)
			self.lineEdit_5.setDisabled(True)
			self.lineEdit_6.setDisabled(True)
			self.lineEdit_7.setDisabled(True)
			self.lineEdit_8.setDisabled(True)
			self.lineEdit_9.setDisabled(True)
			self.lineEdit_10.setDisabled(True)
			self.toolButton_2.setEnabled(False)
			self.pushButton_4.setEnabled(False)
			self.pushButton_5.setEnabled(False)
			
	def abPath(self):
		msiab = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Executable files (*.exe)")
		self.lineEdit_11.setText(msiab)

	def ocSet(self):
		if is_admin():
			try:
				msiabpath = self.lineEdit_11.text()
				strmsipath = str(msiabpath)
				abdirpath = strmsipath.replace('MSIAfterburner.exe','')
				profpath = abdirpath+'Profiles'
				copy_ow(str(profpath), 'OCsets\Profiles')
				msicfg = open('OCsets\Profiles\MSIAfterburner.cfg','r')
				msicfgline = msicfg.readlines()
				msicfg.close()
				
				if os.path.exists(profpath):
					shutil.rmtree(profpath)
					os.makedirs(profpath)
				else:
					os.makedirs(profpath)
					
				#off-on-off AB
				os.system('taskkill /F /IM MSIAfterburner.exe /T')
				time.sleep(1)
				subprocess.Popen(str(msiabpath), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

				time.sleep(2)
				os.system('taskkill /IM MSIAfterburner.exe /T')
				time.sleep(1)

				
				msicfg_n = open('OCsets\Profiles\MSIAfterburner.cfg','w')
				for line in msicfgline:
					if 'StartWithWindows' in line:
						msicfg_n.write('StartWithWindows=1\n')
					elif 'RememberSettings' in line:
						msicfg_n.write('RememberSettings=1\n')
					else:
						msicfg_n.write(line)
				msicfg_n.close()
				
				shutil.copy('OCsets\Profiles\MSIAfterburner.cfg', profpath+'\MSIAfterburner.cfg')
				
				
				#texts for profile_z, _e
				zectext = '[Startup]\nFormat=2\nPowerLimit='+str(int(self.lineEdit_3.text()))+'\nThermalLimit=\nCoreClkBoost='+str(int(float(self.lineEdit_4.text())*1000))+'\nMemClkBoost='+str(int(float(self.lineEdit_5.text())*1000))+'\nFanMode=0\nFanSpeed='+str(int(self.lineEdit_6.text()))
				ethtext = '[Startup]\nFormat=2\nPowerLimit='+str(int(self.lineEdit_7.text()))+'\nThermalLimit=\nCoreClkBoost='+str(int(float(self.lineEdit_8.text())*1000))+'\nMemClkBoost='+str(int(float(self.lineEdit_9.text())*1000))+'\nFanMode=0\nFanSpeed='+str(int(self.lineEdit_10.text()))
				

				#save profile data
				proffilelist = []
				for root, dirs, files in os.walk(profpath):
					allfiles = files
				for afile in allfiles:
					if 'MSIAfterburner' not in afile:
						proffilelist.append(afile)
				if os.path.exists('OCsets\\Profile_e'):
					shutil.rmtree('OCsets\\Profile_e\\')
					os.makedirs('OCsets\\Profile_e\\')
				else:
					os.makedirs('OCsets\\Profile_e\\')
				shutil.copy('OCsets\Profiles\MSIAfterburner.cfg', 'OCsets\Profile_e\MSIAfterburner.cfg')
				if os.path.exists('OCsets\\Profile_z'):
					shutil.rmtree('OCsets\\Profile_z\\')
					os.makedirs('OCsets\\Profile_z\\')
				else:
					os.makedirs('OCsets\\Profile_z\\')
				shutil.copy('OCsets\Profiles\MSIAfterburner.cfg', 'OCsets\Profile_z\MSIAfterburner.cfg')
				for proffile in proffilelist:
					
					efile = open('OCsets\\Profile_e\\' + proffile,'w')
					zfile = open('OCsets\\Profile_z\\' + proffile,'w')
					efile.write(ethtext)
					zfile.write(zectext)
					efile.close()
					zfile.close()
				QMessageBox.information(self, 'Save', 'Overclock setting successfully saved.')
				#self.pushButton_4.setEnabled(True)
			except WindowsError as e:
				print e
				QMessageBox.information(self, 'Warning', 'Access denied: Please close "Profile_e", "Profile_z", or "Profiles" directory and try again.') 
				
		
		else:
			QMessageBox.information(self, 'Warning', 'Administrator privilege required. Please re-run as administrator.')
		 
	def restOC(self):
		if is_admin():
			msiabpath = self.lineEdit_11.text()
			strmsipath = str(msiabpath)
			abdirpath = strmsipath.replace('MSIAfterburner.exe','')
			profpath = abdirpath+'Profiles'
			copy_ow('OCsets\Profiles', str(profpath))
		else:
			QMessageBox.information(self, 'Warning', 'Administrator privilege required. Please re-run as administrator.')
		
		
	def runBench(self):
		#save setting
		cfgfile = open('setting.cfg','w')
		selAlgolist = []
		nonselAlgolist = []
		if self.checkBox.isChecked() == True:
			selAlgolist.append('Ethash')
		else:
			nonselAlgolist.append('Ethash')
		if self.checkBox_2.isChecked() == True:
			selAlgolist.append('Equihash')
		else:
			nonselAlgolist.append('Equihash')
		if self.checkBox_3.isChecked() == True:
			selAlgolist.append('Cryptonight')
		else:
			nonselAlgolist.append('Cryptonight')
		if self.checkBox_4.isChecked() == True:
			selAlgolist.append('Groestl')
		else:
			nonselAlgolist.append('Groestl')
		if self.checkBox_5.isChecked() == True:
			selAlgolist.append('Lyra2RE2')
		else:
			nonselAlgolist.append('Lyra2RE2')
		if self.checkBox_6.isChecked() == True:
			selAlgolist.append('Myriad-Groestl')
		else:
			nonselAlgolist.append('Myriad-Groestl')
		if self.checkBox_7.isChecked() == True:
			selAlgolist.append('NeoScrypt')
		else:
			nonselAlgolist.append('NeoScrypt')
		if self.checkBox_8.isChecked() == True:
			selAlgolist.append('Skein')
		else:
			nonselAlgolist.append('Skein')

		selAlgotxt = ''
		nonselAlgotxt = ''
		for i in selAlgolist:
			selAlgotxt = selAlgotxt + i + ','
		for i in nonselAlgolist:
			nonselAlgotxt = nonselAlgotxt + i + ','
		
		ABswitchtxt = ''
		if self.checkBox_9.isChecked() == True:
			ABswitchtxt = '1'
		else:
			ABswitchtxt = '0'
		
		text = '[Setting]\nworkername='+self.lineEdit.text()+'\npassword='+self.lineEdit_2.text()+'\nregion='+str(self.comboBox.currentIndex())+'\n#region 0-asia 1-europe 2-U.S.\nselAlgo='+selAlgotxt+'\nnonselAlgo='+nonselAlgotxt+'\nABswitch='+ABswitchtxt+'\n#ABswitch 0-off 1-on\nABpath='+self.lineEdit_11.text()+'\n\n[zec]\n[Startup]\nzecFormat=2\nzecPowerLimit='+str(int(self.lineEdit_3.text()))+'\nzecThermalLimit=\nzecCoreClkBoost='+str(int(float(self.lineEdit_4.text())*1000))+'\nzecMemClkBoost='+str(int(float(self.lineEdit_5.text())*1000))+'\nzecFanMode=0\nzecFanSpeed='+str(int(self.lineEdit_6.text()))+'\n\n[eth]\n[Startup]\nethFormat=2\nethPowerLimit='+str(int(self.lineEdit_7.text()))+'\nethThermalLimit=\nethCoreClkBoost='+str(int(float(self.lineEdit_8.text())*1000))+'\nethMemClkBoost='+str(int(float(self.lineEdit_9.text())*1000))+'\nethFanMode=0\nethFanSpeed='+str(int(self.lineEdit_10.text()))
		
		cfgfile.write(text)
		cfgfile.close()
		#run benchmark.exe
		subprocess.Popen('benchmark.exe', creationflags=CREATE_NEW_CONSOLE)
	
	def runManager(self):
		#save setting
		cfgfile = open('setting.cfg','w')
		selAlgolist = []
		nonselAlgolist = []
		if self.checkBox.isChecked() == True:
			selAlgolist.append('Ethash')
		else:
			nonselAlgolist.append('Ethash')
		if self.checkBox_2.isChecked() == True:
			selAlgolist.append('Equihash')
		else:
			nonselAlgolist.append('Equihash')
		if self.checkBox_3.isChecked() == True:
			selAlgolist.append('Cryptonight')
		else:
			nonselAlgolist.append('Cryptonight')
		if self.checkBox_4.isChecked() == True:
			selAlgolist.append('Groestl')
		else:
			nonselAlgolist.append('Groestl')
		if self.checkBox_5.isChecked() == True:
			selAlgolist.append('Lyra2RE2')
		else:
			nonselAlgolist.append('Lyra2RE2')
		if self.checkBox_6.isChecked() == True:
			selAlgolist.append('Myriad-Groestl')
		else:
			nonselAlgolist.append('Myriad-Groestl')
		if self.checkBox_7.isChecked() == True:
			selAlgolist.append('NeoScrypt')
		else:
			nonselAlgolist.append('NeoScrypt')
		if self.checkBox_8.isChecked() == True:
			selAlgolist.append('Skein')
		else:
			nonselAlgolist.append('Skein')

		selAlgotxt = ''
		nonselAlgotxt = ''
		for i in selAlgolist:
			selAlgotxt = selAlgotxt + i + ','
		for i in nonselAlgolist:
			nonselAlgotxt = nonselAlgotxt + i + ','
		
		ABswitchtxt = ''
		if self.checkBox_9.isChecked() == True:
			ABswitchtxt = '1'
		else:
			ABswitchtxt = '0'
		
		text = '[Setting]\nworkername='+self.lineEdit.text()+'\npassword='+self.lineEdit_2.text()+'\nregion='+str(self.comboBox.currentIndex())+'\n#region 0-asia 1-europe 2-U.S.\nselAlgo='+selAlgotxt+'\nnonselAlgo='+nonselAlgotxt+'\nABswitch='+ABswitchtxt+'\n#ABswitch 0-off 1-on\nABpath='+self.lineEdit_11.text()+'\n\n[zec]\n[Startup]\nzecFormat=2\nzecPowerLimit='+str(int(self.lineEdit_3.text()))+'\nzecThermalLimit=\nzecCoreClkBoost='+str(int(float(self.lineEdit_4.text())*1000))+'\nzecMemClkBoost='+str(int(float(self.lineEdit_5.text())*1000))+'\nzecFanMode=0\nzecFanSpeed='+str(int(self.lineEdit_6.text()))+'\n\n[eth]\n[Startup]\nethFormat=2\nethPowerLimit='+str(int(self.lineEdit_7.text()))+'\nethThermalLimit=\nethCoreClkBoost='+str(int(float(self.lineEdit_8.text())*1000))+'\nethMemClkBoost='+str(int(float(self.lineEdit_9.text())*1000))+'\nethFanMode=0\nethFanSpeed='+str(int(self.lineEdit_10.text()))
		
		cfgfile.write(text)
		cfgfile.close()
		#run benchmark.exe
		subprocess.Popen('manager.exe', creationflags=CREATE_NEW_CONSOLE)
		
	
app = QApplication(sys.argv)
dlg = XDialog()
dlg.show()
app.exec_()