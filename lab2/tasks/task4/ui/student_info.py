# Form implementation generated from reading ui file './tasks/task4/ui/student_info.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dl_task4_student_info(object):
    def setupUi(self, dl_task4_student_info):
        dl_task4_student_info.setObjectName("dl_task4_student_info")
        dl_task4_student_info.resize(407, 242)
        dl_task4_student_info.setMinimumSize(QtCore.QSize(407, 242))
        self.verticalLayout = QtWidgets.QVBoxLayout(dl_task4_student_info)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_title = QtWidgets.QLabel(parent=dl_task4_student_info)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout.addWidget(self.lbl_title)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_name = QtWidgets.QLabel(parent=dl_task4_student_info)
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=dl_task4_student_info)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=dl_task4_student_info)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=dl_task4_student_info)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lbl_ = QtWidgets.QLabel(parent=dl_task4_student_info)
        self.lbl_.setObjectName("lbl_")
        self.gridLayout.addWidget(self.lbl_, 1, 0, 1, 1)
        self.le_name = QtWidgets.QLineEdit(parent=dl_task4_student_info)
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 0, 1, 1, 1)
        self.le_id = QtWidgets.QLineEdit(parent=dl_task4_student_info)
        self.le_id.setObjectName("le_id")
        self.gridLayout.addWidget(self.le_id, 1, 1, 1, 1)
        self.le_phone = QtWidgets.QLineEdit(parent=dl_task4_student_info)
        self.le_phone.setObjectName("le_phone")
        self.gridLayout.addWidget(self.le_phone, 2, 1, 1, 1)
        self.le_math = QtWidgets.QLineEdit(parent=dl_task4_student_info)
        self.le_math.setObjectName("le_math")
        self.gridLayout.addWidget(self.le_math, 3, 1, 1, 1)
        self.le_lit = QtWidgets.QLineEdit(parent=dl_task4_student_info)
        self.le_lit.setObjectName("le_lit")
        self.gridLayout.addWidget(self.le_lit, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtWidgets.QPushButton(parent=dl_task4_student_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dl_task4_student_info)
        QtCore.QMetaObject.connectSlotsByName(dl_task4_student_info)

    def retranslateUi(self, dl_task4_student_info):
        _translate = QtCore.QCoreApplication.translate
        dl_task4_student_info.setWindowTitle(_translate("dl_task4_student_info", "Student Info"))
        self.lbl_title.setText(_translate("dl_task4_student_info", "Student Info"))
        self.lbl_name.setText(_translate("dl_task4_student_info", "Name"))
        self.label_3.setText(_translate("dl_task4_student_info", "Phone"))
        self.label_4.setText(_translate("dl_task4_student_info", "Math Score"))
        self.label_5.setText(_translate("dl_task4_student_info", "Literature Score"))
        self.lbl_.setText(_translate("dl_task4_student_info", "Student ID"))
        self.btn_add.setText(_translate("dl_task4_student_info", "Add"))