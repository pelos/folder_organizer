import os
import sys
from PyQt4 import QtCore, QtGui
from fo import Ui_Dialog
import shutil


class fo_controls(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        #pyuic4 -x C:\PC_Files\scripts\folder_organizer.fo.ui > C:\PC_Files\scripts\folder_organizer.fo.py
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        self.Select_Folder_pushButton.clicked.connect(self.check)

        self.add_pushButton.clicked.connect(self.addrows)
        self.add_pushButton.clicked.connect(self.add)

        self.minus_pushButton.clicked.connect(self.minrows)
        self.minus_pushButton.clicked.connect(self.minus)
        self.organize_pushButton.clicked.connect(self.organize)


        self.amount_Int.textChanged.connect(self.textor)

    def check(self):
        dir = QtGui.QFileDialog.getExistingDirectory(caption="Select the folder you wish to organize")
        self.folder_path.setText(dir)

    def add(self):
        #print self.amount_Int.toPlainText()
        ot = self.amount_Int.toPlainText()
        int_ot = int(ot)
        int_ot += 1
        int_ot = str(int_ot)
        int_ot = QtCore.QString(int_ot)
        self.amount_Int.setText(int_ot)

    def minus(self):
        #print self.amount_Int.toPlainText()

        if int(self.amount_Int.toPlainText()) == 1:
            pass
        else:
            ot = self.amount_Int.toPlainText()
            int_ot = int(ot)
            int_ot = int_ot - 1
            int_ot = str(int_ot)
            int_ot = QtCore.QString(int_ot)
            self.amount_Int.setText(int_ot)


    def addrows(self):
        amount_lines = int(self.amount_Int.toPlainText())
        if amount_lines >= 1:
            self.categorie_tableWidget.insertRow(0)
        else:
            pass

    def minrows(self):
        amount_lines = int(self.amount_Int.toPlainText())
        if amount_lines > 1:
            self.categorie_tableWidget.removeRow(0)
        else:
            pass

    def textor(self):
        textor = self.amount_Int.toPlainText()








    def file_list_dir(self):
        self.path_folder = str(self.folder_path.toPlainText())
        list_file_name = os.listdir(self.path_folder)
        list_file_with_path = []
        for i in list_file_name:
            file_local = os.path.join(self.path_folder, i)
            list_file_with_path.append(file_local)

        # print list_file_name
        # print list_file_with_path
        return list_file_name, list_file_with_path

    def organize(self):
        """
        we bring the information from the UI, and we use it to create the folder structure.
        and then we move the file to their proper location.
        """
        self.file_name = self.file_list_dir()[0]
        self.file_with_path = self.file_list_dir()[1]
        print self.file_name
        print self.file_with_path


        self.category_list = []
        self.tag_list = []

        if os.path.exists(self.path_folder):
            row_count = self.categorie_tableWidget.rowCount()
            for i in range(row_count):
                category = str(self.categorie_tableWidget.item(i, 0).text())
                self.category_list.append(category)
                # we check if the folder all ready exist, if it does, keep going with the code
                if os.path.exists(self.path_folder + "/" + category):
                    pass
                else:
                    os.mkdir(self.path_folder + "/" + category)
                tags = str(self.categorie_tableWidget.item(i, 1).text())
                self.tag_list.append(tags)
                print category + "-> " + tags
        else:
            print "select a valid folder"


        print self.category_list
        print self.tag_list
        #self.finder_if_file_in_tag()
        print "************************"
        self.find_row_of_category()




    def finder_if_file_in_tag(self):
        for index, archivo in enumerate(self.file_with_path):
            print archivo
            if os.path.isfile(archivo):
                print archivo + " this is a file"
                print self.file_name[index]
            elif os.path.isdir(archivo):
                print archivo + " this is a folder"

            if archivo in self.tag_list:
                print index



    def find_row_of_category(self):
        progress_count = 0
        self.progressBar.setRange(0,len(self.file_with_path))
        self.progressBar.reset()
        for index,archivo in enumerate(self.file_with_path):
            archivo_pure_name = archivo.split(".")[0]
            archivo_pure_name = archivo_pure_name.split("\\")[-1]
            print archivo_pure_name
            for indexx, tagg in enumerate(self.tag_list):
                    if archivo_pure_name in tagg:
                        print indexx
                        destination_path = self.path_folder +"\\" +self.categorie_tableWidget.item(indexx,0).text()
                        print destination_path
                        print "hello"
                        print archivo
                        shutil.move(archivo,str(destination_path))
            progress_count = progress_count + 1
            print progress_count
            self.progressBar.setValue(progress_count)
app = QtGui.QApplication(sys.argv)
form = fo_controls()
form.show()
app.exec_()