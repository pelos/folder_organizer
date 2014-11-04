# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fo.ui'
#
# Created: Mon Apr 08 21:10:25 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(723, 497)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.folder_to_organize = QtGui.QLabel(Dialog)
        self.folder_to_organize.setObjectName(_fromUtf8("folder_to_organize"))
        self.horizontalLayout.addWidget(self.folder_to_organize)
        self.folder_path = QtGui.QTextEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folder_path.sizePolicy().hasHeightForWidth())
        self.folder_path.setSizePolicy(sizePolicy)
        self.folder_path.setObjectName(_fromUtf8("folder_path"))
        self.horizontalLayout.addWidget(self.folder_path)
        self.Select_Folder_pushButton = QtGui.QPushButton(Dialog)
        self.Select_Folder_pushButton.setObjectName(_fromUtf8("Select_Folder_pushButton"))
        self.horizontalLayout.addWidget(self.Select_Folder_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.amount_of_categories = QtGui.QLabel(Dialog)
        self.amount_of_categories.setObjectName(_fromUtf8("amount_of_categories"))
        self.horizontalLayout_4.addWidget(self.amount_of_categories)
        self.amount_Int = QtGui.QTextEdit(Dialog)
        self.amount_Int.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amount_Int.sizePolicy().hasHeightForWidth())
        self.amount_Int.setSizePolicy(sizePolicy)
        self.amount_Int.setMaximumSize(QtCore.QSize(16777215, 5000))
        self.amount_Int.setDocumentTitle(_fromUtf8(""))
        self.amount_Int.setObjectName(_fromUtf8("amount_Int"))
        self.horizontalLayout_4.addWidget(self.amount_Int)
        self.add_pushButton = QtGui.QPushButton(Dialog)
        self.add_pushButton.setObjectName(_fromUtf8("add_pushButton"))
        self.horizontalLayout_4.addWidget(self.add_pushButton)
        self.minus_pushButton = QtGui.QPushButton(Dialog)
        self.minus_pushButton.setObjectName(_fromUtf8("minus_pushButton"))
        self.horizontalLayout_4.addWidget(self.minus_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.categorie_tableWidget = QtGui.QTableWidget(Dialog)
        self.categorie_tableWidget.setAlternatingRowColors(True)
        self.categorie_tableWidget.setColumnCount(2)
        self.categorie_tableWidget.setObjectName(_fromUtf8("categorie_tableWidget"))
        self.categorie_tableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.categorie_tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.categorie_tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.categorie_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.categorie_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.categorie_tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.categorie_tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.categorie_tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.categorie_tableWidget.setItem(1, 1, item)
        self.categorie_tableWidget.horizontalHeader().setVisible(True)
        self.categorie_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.categorie_tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.categorie_tableWidget.horizontalHeader().setHighlightSections(True)
        self.categorie_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.categorie_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.categorie_tableWidget.verticalHeader().setVisible(False)
        self.categorie_tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.categorie_tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.categorie_tableWidget)
        self.organize_pushButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.organize_pushButton.sizePolicy().hasHeightForWidth())
        self.organize_pushButton.setSizePolicy(sizePolicy)
        self.organize_pushButton.setMinimumSize(QtCore.QSize(0, 5))
        self.organize_pushButton.setObjectName(_fromUtf8("organize_pushButton"))
        self.verticalLayout.addWidget(self.organize_pushButton)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setFormat(_fromUtf8("%p%"))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.folder_to_organize.setText(_translate("Dialog", "Folder to Orginize", None))
        self.folder_path.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">C:\\PC_Files\\scripts\\folder_organizer\\test</span></p></body></html>", None))
        self.Select_Folder_pushButton.setText(_translate("Dialog", "Select Folder", None))
        self.amount_of_categories.setText(_translate("Dialog", "Amount of Categories", None))
        self.amount_Int.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1</span></p></body></html>", None))
        self.add_pushButton.setText(_translate("Dialog", "+", None))
        self.minus_pushButton.setText(_translate("Dialog", "-", None))
        item = self.categorie_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Folder", None))
        item = self.categorie_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "New Row", None))
        item = self.categorie_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Categorie", None))
        item = self.categorie_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Word Tag", None))
        __sortingEnabled = self.categorie_tableWidget.isSortingEnabled()
        self.categorie_tableWidget.setSortingEnabled(False)
        item = self.categorie_tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "Category", None))
        item = self.categorie_tableWidget.item(0, 1)
        item.setText(_translate("Dialog", "tag1 tag2 tag3 etc fish", None))
        item = self.categorie_tableWidget.item(1, 0)
        item.setText(_translate("Dialog", "bla", None))
        item = self.categorie_tableWidget.item(1, 1)
        item.setText(_translate("Dialog", "baby father", None))
        self.categorie_tableWidget.setSortingEnabled(__sortingEnabled)
        self.organize_pushButton.setText(_translate("Dialog", "Organize", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

