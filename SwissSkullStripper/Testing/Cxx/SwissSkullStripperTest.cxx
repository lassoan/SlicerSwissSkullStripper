#include "itkTestMain.h"

void RegisterTests()
{
  REGISTER_TEST(SwissSkullStripperTest);
}

#undef main
#define main SwissSkullStripperTest

#include "../../SwissSkullStripper.cxx" 
