
#-----------------------------------------------------------------------------
set(MODULE_NAME SwissSkullStripper)

#-----------------------------------------------------------------------------
#
# SlicerExecutionModel
#
find_package(SlicerExecutionModel REQUIRED)
include(${SlicerExecutionModel_USE_FILE})

#
# ITK
#
set(${PROJECT_NAME}_ITK_COMPONENTS
  ITKIOImageBase
  ITKAnisotropicSmoothing
  ITKBinaryMathematicalMorphology
  ITKCommon
  ITKIOImageBase
  ITKImageFilterBase
  ITKImageFunction
  ITKImageGradient
  ITKImageGrid
  ITKImageIntensity
  ITKLevelSets
  ITKMathematicalMorphology
  ITKOptimizers
  ITKRegistrationCommon
  ITKThresholding
  ITKTransform
  ITKIONRRD
  )
find_package(ITK 4.6 COMPONENTS ${${PROJECT_NAME}_ITK_COMPONENTS} REQUIRED)
set(ITK_NO_IO_FACTORY_REGISTER_MANAGER 1) # See Libs/ITKFactoryRegistration/CMakeLists.txt
include(${ITK_USE_FILE})

set(MODULE_INCLUDE_DIRECTORIES
  )

set(MODULE_SRCS
  SwissSkullStripper.cxx
  )

set(MODULE_TARGET_LIBRARIES
  ${ITK_LIBRARIES} ITKFactoryRegistration
  )

#-----------------------------------------------------------------------------
SEMMacroBuildCLI(
  NAME ${MODULE_NAME}
  TARGET_LIBRARIES ${MODULE_TARGET_LIBRARIES}
  INCLUDE_DIRECTORIES ${MODULE_INCLUDE_DIRECTORIES}
  ADDITIONAL_SRCS ${MODULE_SRCS}
  EXECUTABLE_ONLY
  )
# EXECUTABLE_ONLY is specified to prevent running the module as a DLL.
# Atlas files can only be found relative to an executable file.
# If module would loaded as DLL then we didn't know location of the executable
# and thus the location of atlas files could not be found.

#-----------------------------------------------------------------------------
if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()

# Add default atlas files to binary directory and extension package

set(DEFAULT_ATLAS_FILES
  atlasImage.mha
  atlasMask.mha
  )

foreach(DEFAULT_ATLAS_FILE ${DEFAULT_ATLAS_FILES})
  configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Data/Input/${DEFAULT_ATLAS_FILE}
    ${CMAKE_BINARY_DIR}/${Slicer_CLIMODULES_BIN_DIR}/SwissSkullStripperDefaultAtlas/${DEFAULT_ATLAS_FILE}
    COPYONLY)
  install(
    FILES ${CMAKE_BINARY_DIR}/${Slicer_CLIMODULES_BIN_DIR}/SwissSkullStripperDefaultAtlas/${DEFAULT_ATLAS_FILE}
    DESTINATION ${Slicer_INSTALL_CLIMODULES_BIN_DIR}/SwissSkullStripperDefaultAtlas COMPONENT Runtime)
endforeach()
