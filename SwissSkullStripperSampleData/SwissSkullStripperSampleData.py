import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# SwissSkullStripperSampleData
#

class SwissSkullStripperSampleData(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "SwissSkullStripper Sample Data"
    self.parent.categories = ["Sequences"]
    self.parent.dependencies = ["SampleData"]
    self.parent.contributors = ["Andras Lasso (PerkLab)"]
    self.parent.helpText = """This module makes available SwissSkullStripper atlas images in SampleData module"""
    self.parent.acknowledgementText = """
"""

    # don't show this module - additional data will be shown in SampleData module
    parent.hidden = True

    # Add data sets to SampleData module
    iconsPath = os.path.join(os.path.dirname(self.parent.path), 'Resources/Icons')
    import SampleData

    SampleData.SampleDataLogic.registerCustomSampleDataSource(
      category='SwissSkullStripper',
      sampleName='SwissSkullStripperAtlasImage',
      uris='https://github.com/lorensen/SwissSkullStripperExtension/blob/master/SwissSkullStripper/Data/Input/atlasImage.mha?raw=true',
      fileNames='SwissSkullStripperAtlasImage.mha',
      nodeNames='atlasImage',
      loadFileType='VolumeFile',
      thumbnailFileName=os.path.join(iconsPath, 'AtlasImage.png')
      )

    SampleData.SampleDataLogic.registerCustomSampleDataSource(
      category='SwissSkullStripper',
      sampleName='SwissSkullStripperAtlasMask',
      uris='https://github.com/lorensen/SwissSkullStripperExtension/blob/master/SwissSkullStripper/Data/Input/atlasMask.mha?raw=true',
      fileNames='SwissSkullStripperAtlasMask.mha',
      nodeNames='atlasMask',
      loadFileType='VolumeFile',
      loadFileProperties={'labelmap': True},
      thumbnailFileName=os.path.join(iconsPath, 'AtlasMask.png')
      )
