cmake_minimum_required(VERSION 2.8.9)

project(SwissSkullStripper)

#-----------------------------------------------------------------------------
set(EXTENSION_NAME SwissSkullStripper)
set(EXTENSION_HOMEPAGE "http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/SwissSkullStripper")
set(EXTENSION_CATEGORY "Segmentation")
set(EXTENSION_CONTRIBUTORS "Bill Lorensen (Noware), Stefan Bauer (University of Bern), Thomas Fejes (University of Bern), Mauricio Reyes (University of Bern), Arnaud Gelas (Crisalix)")
set(EXTENSION_DESCRIPTION "Atlas-driven skull stripping for MR and CT head studies.")
set(EXTENSION_ICONURL "http://www.slicer.org/slicerWiki/images/c/cd/SwissSkullStripper.png")
set(EXTENSION_SCREENSHOTURLS "http://www.slicer.org/slicerWiki/images/0/01/SwissSkullStripperResults1.png")
set(EXTENSION_STATUS "seeking input from users")

#-----------------------------------------------------------------------------
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
add_subdirectory(SwissSkullStripper)
add_subdirectory(SwissSkullStripperSampleData)

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_CPACK})
