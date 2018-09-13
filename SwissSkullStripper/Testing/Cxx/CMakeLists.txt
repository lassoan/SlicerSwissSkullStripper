#-----------------------------------------------------------------------------
set(BASELINE ${CMAKE_CURRENT_SOURCE_DIR}/../../Data/Baseline)
set(INPUT ${CMAKE_CURRENT_SOURCE_DIR}/../../Data/Input)
set(TEMP "${CMAKE_BINARY_DIR}/Testing/Temporary")

set(CLP ${MODULE_NAME})

#-----------------------------------------------------------------------------
add_executable(${CLP}Test ${CLP}Test.cxx)
add_dependencies(${CLP}Test ${CLP})
target_link_libraries(${CLP}Test
  ${CLP}Lib
  ${${MODULE_NAME}_TARGET_LIBRARIES}
  ${SlicerExecutionModel_EXTRA_EXECUTABLE_TARGET_LIBRARIES}
  )
set_target_properties(${CLP}Test PROPERTIES LABELS ${CLP})
set_target_properties(${CLP}Test PROPERTIES FOLDER ${${CLP}_TARGETS_FOLDER})

set(testname ${CLP}Test)
ExternalData_add_test(${CLP}Data NAME ${testname} COMMAND ${SEM_LAUNCH_COMMAND} $<TARGET_FILE:${CLP}Test>
  --compare DATA{${BASELINE}/SwissSkullStripperMaskTest.mha}
  ${TEMP}/SwissSkullStripperMaskTest.mha
  ${CLP}Test
  --atlasMRI DATA{${INPUT}/atlasImage.mha} --atlasMask DATA{${INPUT}/atlasMask.mha}
  DATA{${INPUT}/RegLib_C01_MRMeningioma_1.nrrd}
  ${TEMP}/SwissSkullStripperImage.mha  ${TEMP}/SwissSkullStripperMaskTest.mha
  )
set_property(TEST ${testname} PROPERTY LABELS ${CLP})

#-----------------------------------------------------------------------------
ExternalData_add_target(${CLP}Data)
