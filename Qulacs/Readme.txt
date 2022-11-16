///Qulacs///

This evaluation looked at Qulacs as a C++ library, and used the Visual Studio 2019 package. 
It can also be used directly with Python, or compiled with gcc for C++.
The installation steps below correspond to the Visual Studio installation process. 
You can find install instructions for other versions at the Qulacs GitHub page (https://github.com/qulacs/qulacs)

NOTE: I was unable to get Qulacs to fully work, even after following all of the given configuration steps.
These instructions should serve as a guide for how it is supposed to be configured, but will result in an inaccessible source file error in the C++ project when all is said and done.

Installation and Configuration Steps:

0. Make sure you have Python v. 3.7 or Later - If you do not have Python installed, you can install it here: https://www.python.org/downloads/

1. Download Qulacs - Use your favored version of Git to clone the Qulacs repository at https://github.com/qulacs/qulacs. You may install it wherever you wish.

2. Ensure that you have access to CMake - This is a program that is used in the pre-compilation process.
It can be found within the Visual Studio program files ("Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin")
or downloaded from https://cmake.org/download/

3. Add the CMake binary location to your PATH system environment variable - This step will be different depending on your operating system.
Navigate to "CMake\bin" and copy the filepath, then add it to PATH.
The following website contains step-by-step instructions on how to modify PATH on various operating systems: https://www.java.com/en/download/help/path.html

4. Ensure that you have access to Boost - Boost is a library of auxilary functions for C++, and is a dependency of the Qulacs codebase.
You can download Boost from https://www.boost.org/users/download/
You may unzip the file wherever you wish.

5. Add the path to Boost to Qulacs' arguments - In order for Qulacs to use Boost, the path must be configured as a variable for the script that will be used.
Within your Qulacs repository, open CMakeLists.txt.
Directly beneath the line "#Boost", add the command:
"set(Boost_INCLUDE_DIR "Your/Path/Here/boost_1_80_0")"
Be sure to substitute the correct filepath and version number for Boost.

6. Build Qulacs using the command prompt - Run the Command Prompt (or an sequivalent console) as an administrator.
Use the command "cd [your qulacs path]" to set the current directory to the qulacs folder.
Then, run "script\build_msvc_2019.bat" (or a similar command, full details in the Qulacs GitHub ReadMe)
If all is configured correctly, the script will build the static library files in qulacs\visualstudio.

7. Configure C++ project settings - Within Visual Studio, create a new project. In order to use Qulacs in your C++ code, there are some configuration changes that need to be made.

	1. Select "x64" as an active solution platform.
	2. Right Click your project name in Solution Explorer, and select "Properties".
	3. At "VC++ Directories" section, add the full path to ./qulacs/include to "Include Directories"
	4. At "VC++ Directories" section, add the full path to ./qulacs/lib to "Library Directories"
	5. At "C/C++ -> Code Generation" section, change "Runtime library" to "Multi-threaded (/MT)".
	^ NOTE: This step requires that at least one .cpp file be present in your project.
	6. At "Linker -> Input" section, add vqcsim_static.lib;cppsim_static.lib;csim_static.lib; to "Additional Dependencies".

At this point, you are ready to use #include for the Qulacs library, and will have access to all of the code constructs listed in the documentation
(http://docs.qulacs.org/en/latest/api/cpp_library_root.html)
A tutorial for how to get started with Qulacs can be found at http://docs.qulacs.org/en/latest/intro/4.2_cpp_tutorial.html
	
 