'''
Created on 6 mai 2015

@author:  Cyril Jacquet
'''
from gui import plugins as gui_plugins
from PyQt5.Qt import pyqtSlot
from PyQt5.QtCore import Qt


class SynopsisDockPlugin(gui_plugins.GuiWriteSubWindowDockPlugin):
    '''
    SynopsisDockPlugin
    Be careful, this plugin is the basis for the NotesDockPlugin in plugin/notesdock
    '''
    is_builtin_plugin = True
    ignore = False
    def __init__(self):
        '''
        Constructor
        '''

        super(SynopsisDockPlugin, self).__init__()
    
    def gui_class(self):
        return GuiSynopsisDock
    
class CoreSynopsisDock():
    '''
    CoreSynopsisDock
    '''

    dock_name = "synopsis-dock" 
    note_type_name = "synopsis"
    
    def __init__(self):
        '''
        Constructor
        '''

        super(CoreSynopsisDock, self).__init__()
        self._synopsis_rich_text = None
        self._sheet_id = None
        self.tree_sheet = None        

    @property
    def sheet_id(self):
        return self._sheet_id
    
    @sheet_id.setter
    def sheet_id(self, sheet_id):
        if self._sheet_id == sheet_id:
            return
        self._sheet_id = sheet_id
        if self.sheet_id is not None:
            self.tree_sheet = core_cfg.core.tree_sheet_manager.get_tree_sheet_from_sheet_id(self.sheet_id)
            _ = self.synopsis_rich_text
            
            
        
    @property   
    def synopsis_rich_text(self):
        self._synopsis_rich_text = ""
            # if self._sheet_id is not None:
            #     other_contents_dict = self.tree_sheet.get_other_contents()
            #     try :
            #         self._synopsis_rich_text = other_contents_dict[self.note_type_name]
            #     except KeyError:
            #         self._synopsis_rich_text = ""
            
        return self._synopsis_rich_text
        
    @synopsis_rich_text.setter
    def synopsis_rich_text(self,  text):
        if self.sheet_id is not None:
            self.tree_sheet = core_cfg.core.tree_sheet_manager.get_tree_sheet_from_sheet_id(self.sheet_id)
            self.tree_sheet.set_other_content(self.note_type_name,  text) 
            self._synopsis_rich_text = text
    

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject, QSettings
from gui import cfg as gui_cfg
from gui.paper_manager import NotePaper
from plugins.synopsisdock import synopsis_dock_ui

class GuiSynopsisDock(QObject):
    '''
    GuiSynopsisDock
    '''
    dock_name = "synopsis-dock" 
    dock_displayed_name = _("Synopsis")
    note_type_name = "synopsis"

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(GuiSynopsisDock, self).__init__(parent)
        self.widget = None
        self._project_id = None
        self._sheet_id = None
        self._note_id = None

        gui_cfg.data.noteHub().contentChanged.connect(self.get_update)

    @property
    def project_id(self):
        """

        :return:
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        :param id:
        """
        self._project_id = project_id

    @property
    def paper_id(self):
        """
        Only used for compatibility with API, return sheet_id
        :return:
        """
        return self.sheet_id

    @paper_id.setter
    def paper_id(self, paper_id):
        """
        Only used for compatibility with API, call sheet_id
        :param id:
        """
        self.sheet_id = paper_id

    @property
    def sheet_id(self):
        return self._sheet_id
    
    @sheet_id.setter
    def sheet_id(self, sheet_id):
        if self._sheet_id == sheet_id:
            pass
        self._sheet_id = sheet_id
        if self.sheet_id is not None:
            pass

    def get_widget(self):
        
        if self.widget is None:
            self.widget = QWidget()
            self.ui = synopsis_dock_ui.Ui_SynopsisDock()
            self.ui.setupUi(self.widget)
            gui_cfg.signal_hub.apply_settings_widely_sent.connect(self.apply_settings)
            self.apply_settings()
            self.ui.writingZone.has_minimap = False
            self.ui.writingZone.has_scrollbar = False
            self.ui.writingZone.is_resizable = False
            self.ui.has_side_tool_bar = False        

            if self.sheet_id is not None:
                self.get_update()
                # connect :
                self.ui.writingZone.text_edit.textChanged.connect(self.apply_text_change, type=Qt.UniqueConnection)
                
            self.widget.gui_part = self
        return self.widget
 
    def get_update(self):
        if self.sheet_id is not None:
            # determine the synopsis (note) of this sheet
            self._note_id = gui_cfg.data.noteHub().getSynopsisFromSheetCode(self._project_id, self._sheet_id)
            # apply changes :
            self.ui.writingZone.text_edit.blockSignals(True)
            text = NotePaper(self._project_id, self._note_id).content
            self.ui.writingZone.set_rich_text(text)
            self.ui.writingZone.text_edit.blockSignals(False)
        
    @pyqtSlot()
    def apply_text_change(self):
        self.ui.writingZone.text_edit.textChanged.disconnect(self.apply_text_change)
        NotePaper(self._project_id, self._note_id).content = self.ui.writingZone.text_edit.toHtml()
        self.ui.writingZone.text_edit.textChanged.connect(self.apply_text_change, type=Qt.UniqueConnection)

    @pyqtSlot()
    def apply_settings(self):
        settings = QSettings()
