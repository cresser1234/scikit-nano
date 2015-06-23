# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nanogen_bulk_structures.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BulkStructureGeneratorMainWindow(object):
    def setupUi(self, BulkStructureGeneratorMainWindow):
        BulkStructureGeneratorMainWindow.setObjectName("BulkStructureGeneratorMainWindow")
        BulkStructureGeneratorMainWindow.resize(350, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BulkStructureGeneratorMainWindow.sizePolicy().hasHeightForWidth())
        BulkStructureGeneratorMainWindow.setSizePolicy(sizePolicy)
        BulkStructureGeneratorMainWindow.setMinimumSize(QtCore.QSize(350, 400))
        BulkStructureGeneratorMainWindow.setMaximumSize(QtCore.QSize(800, 1000))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        BulkStructureGeneratorMainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(BulkStructureGeneratorMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.bulk_structure_list_widget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bulk_structure_list_widget.setFont(font)
        self.bulk_structure_list_widget.setObjectName("bulk_structure_list_widget")
        self.verticalLayout_3.addWidget(self.bulk_structure_list_widget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.nx_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.nx_spin_box.setFont(font)
        self.nx_spin_box.setMinimum(1)
        self.nx_spin_box.setMaximum(999)
        self.nx_spin_box.setObjectName("nx_spin_box")
        self.horizontalLayout.addWidget(self.nx_spin_box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.ny_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ny_spin_box.setFont(font)
        self.ny_spin_box.setMinimum(1)
        self.ny_spin_box.setMaximum(999)
        self.ny_spin_box.setObjectName("ny_spin_box")
        self.horizontalLayout_5.addWidget(self.ny_spin_box)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.nz_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.nz_spin_box.setFont(font)
        self.nz_spin_box.setMinimum(1)
        self.nz_spin_box.setMaximum(999)
        self.nz_spin_box.setObjectName("nz_spin_box")
        self.horizontalLayout_4.addWidget(self.nz_spin_box)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        BulkStructureGeneratorMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BulkStructureGeneratorMainWindow)
        QtCore.QMetaObject.connectSlotsByName(BulkStructureGeneratorMainWindow)

    def retranslateUi(self, BulkStructureGeneratorMainWindow):
        _translate = QtCore.QCoreApplication.translate
        BulkStructureGeneratorMainWindow.setWindowTitle(_translate("BulkStructureGeneratorMainWindow", "NanoGen"))
        self.label.setText(_translate("BulkStructureGeneratorMainWindow", "Select Bulk Structure:"))
        self.label_2.setText(_translate("BulkStructureGeneratorMainWindow", "Unit Cells:"))
        self.label_3.setText(_translate("BulkStructureGeneratorMainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">n</span><span style=\" vertical-align:sub;\">x </span>=</p></body></html>"))
        self.label_7.setText(_translate("BulkStructureGeneratorMainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">n</span><span style=\" vertical-align:sub;\">y </span>=</p></body></html>"))
        self.label_6.setText(_translate("BulkStructureGeneratorMainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">n</span><span style=\" vertical-align:sub;\">z </span>=</p></body></html>"))

