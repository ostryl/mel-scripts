import maya.cmds as cmds
import math
import sys



if cmds.window(myWindow, exists=True):
cmds.deleteUI(myWindow)
cmds.window(myWindow, title="My Menu", wh=(130,90), sizeable=1, menuBar=True)
cmds.columnLayout("MainLayout", adj=True, parent=myWindow)
cmds.button("apply", label='Execute', c=‘my_command()')
cmds.showWindow(myWindow)