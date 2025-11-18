import maya.cmds as cmds

#comments look like this
cmds.select( all=True )
cmds.delete( all=True )

mySelections = cmds.ls( sl=True )
myCube =cmds.polyCube
myShader = cmds.shadingNode('blinn', asShader=True )




cmds.polyCube( w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=[0,1,0], cuv=4, ch=True)

myShader = cmds.shadingNode('blinn', asShader=True )
shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shader_name +"SG")
cmds.hyperShade( assign=myShader )
