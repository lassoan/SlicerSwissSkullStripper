cmake_minimum_required(VERSION 2.8.9)

project(SwissSkullStripper)

#-----------------------------------------------------------------------------
set(EXTENSION_NAME SwissSkullStripper)
set(EXTENSION_HOMEPAGE "https://github.com/lassoan/SlicerSwissSkullStripper")
set(EXTENSION_CATEGORY "Segmentation")
set(EXTENSION_CONTRIBUTORS "Bill Lorensen (Noware), Stefan Bauer (University of Bern), Thomas Fejes (University of Bern), Mauricio Reyes (University of Bern), Arnaud Gelas (Crisalix), Andras Lasso (PerkLab)")
set(EXTENSION_DESCRIPTION "Atlas-driven skull stripping for MR and CT head studies.")
set(EXTENSION_ICONURL "https://github.com/lassoan/SlicerSwissSkullStripper/raw/master/SwissSkullStripper.png")
set(EXTENSION_SCREENSHOTURLS "https://github.com/lassoan/SlicerSwissSkullStripper/raw/master/Docs/SwissSkullStripperResults1.png https://github.com/lassoan/SlicerSwissSkullStripper/raw/master/Docs/SwissSkullStripperPanel.png")
set(EXTENSION_STATUS "stable")

#-----------------------------------------------------------------------------
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
add_subdirectory(SwissSkullStripper)
add_subdirectory(SwissSkullStripperSampleData)

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_CPACK})
