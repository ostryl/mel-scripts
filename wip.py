import maya.cmds as cmds

#comments look like this
cmds.select(all=True)
cmds.polyCube( w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=[0,1,0], cuv=4, ch=True)

myShader = cmds.shadingNode('anisotropic', aaShader=True)

cmds.select(myCube)
cmds.hyperShade( assign=myShader )
