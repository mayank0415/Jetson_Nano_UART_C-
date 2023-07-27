import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.files import copy
from os.path import join
def find_source_path():
   source_path = ""
   file_path = os.path.expanduser('~') + "/.conan2/conan_pkg_source_path.txt"

   if not os.path.exists(file_path):
      source_path_file = open(file_path, 'w')
      source_path_file.close()

   with open(file_path, "r+") as source_path_file:

      source_path_file.seek(0,0)

      # read by character
      char = source_path_file.read(1)
      if not char:
         source_path = os.getcwd()
         source_path_file.seek(0,0)
         source_path_file.write(source_path)
         print("Source Folder Path File was empty\n")
      else:
         source_path = char + source_path_file.read()
         source_path_file.truncate(0)
         print("Source Folder Path File was not empty\n")

   return source_path


class uart(ConanFile):
    name = "uart"
    version = "1.0.0"

    # Optional metadata
    license = "<Jangoo US>"
    author = "Mayank Garg (mayank@jangoo.us)"
    url = ""
    description = "This is a uart Interface Repository "
    topics = ("<App Logging>", "<Logging>", "<Log>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    
    # Source folder path where source files are present to build the package, generally
    # it should be the same path as the path of this recipe file, conanfile.py
    source_folder = find_source_path()

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["uart"]
