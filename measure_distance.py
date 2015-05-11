
    # get the points
    fidNode1=slicer.mrmlScene.GetNodesByName('targets-REG').GetItemAsObject(0)
    fidNode2=slicer.mrmlScene.GetNodesByName('needle Tip').GetItemAsObject(0)

    target_position=[0.0,0.0,0.0]
    needleTip_position=[0.0,0.0,0.0]

    fidNode1.GetNthFiducialPosition(1,target_position)
    fidNode2.GetNthFiducialPosition(0,needleTip_position)

    target_position=[target_position[0],target_position[1],target_position[2],1]
    needleTip_position=[needleTip_position[0],needleTip_position[1],needleTip_position[2],1]

    # change fiducial points from RAS to IJK
    RAStoIJK=vtk.vtkMatrix4x4()

    # get the yellow background volume ID
    lm=slicer.app.layoutManager()
    yellowWidget = lm.sliceWidget('Yellow')
    compositNodeYellow=yellowWidget.mrmlSliceCompositeNode()
    backgroundVolumeNode=slicer.mrmlScene.GetNodeByID(compositNodeYellow.GetBackgroundVolumeID())

    # get the RAS to IJK matrix
    backgroundVolumeNode.GetRASToIJKMatrix(RAStoIJK)

    # get the IJK points
    target_position_IJK=RAStoIJK.MultiplyPoint(target_position)
    needleTip_position_IJK=RAStoIJK.MultiplyPoint(needleTip_position)

    # calculate 2D distance
    distance_x=abs(target_position_IJK[0]-needleTip_position_IJK[0])
    distance_y=abs(target_position_IJK[1]-needleTip_position_IJK[1])
    distance_z=abs(target_position_IJK[2]-needleTip_position_IJK[2])

    print ('needleTip_position_IJK[0] = '+str(needleTip_position_IJK[0]))
    print ('needleTip_position_IJK[1] = '+str(needleTip_position_IJK[1]))
    print ('needleTip_position_IJK[2] = '+str(needleTip_position_IJK[2]))

    print ('target_position_IJK[0] = '+str(target_position_IJK[0]))
    print ('target_position_IJK[1] = '+str(target_position_IJK[1]))
    print ('target_position_IJK[2] = '+str(target_position_IJK[2]))

    print ('distance_x = '+str(distance_x))

    print ('distance_y = '+str(distance_y))

    print ('distance_z = '+str(distance_z))