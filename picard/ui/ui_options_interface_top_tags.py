# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InterfaceTopTagsOptionsPage(object):
    def setupUi(self, InterfaceTopTagsOptionsPage):
        InterfaceTopTagsOptionsPage.setObjectName("InterfaceTopTagsOptionsPage")
        InterfaceTopTagsOptionsPage.resize(893, 698)
        self.vboxlayout = QtWidgets.QVBoxLayout(InterfaceTopTagsOptionsPage)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtWidgets.QLabel(InterfaceTopTagsOptionsPage)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.top_tags_list = QtWidgets.QListView(InterfaceTopTagsOptionsPage)
        self.top_tags_list.setDragEnabled(True)
        self.top_tags_list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.top_tags_list.setObjectName("top_tags_list")
        self.vboxlayout.addWidget(self.top_tags_list)

        self.retranslateUi(InterfaceTopTagsOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(InterfaceTopTagsOptionsPage)

    def retranslateUi(self, InterfaceTopTagsOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_("Show the below tags above all other tags in the metadata view"))
