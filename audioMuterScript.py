import maya.cmds as cmds
import maya.mel as mel
import sys


class audioMuter:
    def __init__(self):
        self.muteVar = False
        self.win1 = 'mainUI'
        if (cmds.window (self.win1, exists = 1)):
            cmds.deleteUI (self.win1)
        cmds.window(self.win1, rtf = 1, w = 200, h = 50, t = 'AudioInput', s = 0)
        cmds.columnLayout (adj = 1)
    
    
        cmds.rowColumnLayout(nc=2)
    
        cmds.textField ('aName', tx = 'Type Audio File Name', w = 200)
        cmds.button (l = 'Load', c = self.loadFileName)  
        
        cmds.showWindow(self.win1)

    def loadFileName(self, *args):
        self.audioName = cmds.textField ('aName', q = 1, tx = 1)
        print(self.audioName)
        cmds.deleteUI(self.win1)
        return (self.audioName)
    
    
    def muteToggle(self):
        if self.muteVar == False:
            cmds.setAttr('{}.mute'.format(self.audioName), 1)
            self.muteVar = True
            print("Audio Muted")
            
        else:
            cmds.setAttr('{}.mute'.format(self.audioName), 0)
            self.muteVar = False
            print("Audio UnMuted")
