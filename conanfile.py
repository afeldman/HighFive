import os
from conans import ConanFile, tools


class HighfiveConan(ConanFile):
    name = "highfive"
    version = "0.1"
    license = "BSL-1.0"
    author = "anton.feldmann@gmail.com"
    url = "https://github.com/afeldman/HighFive"
    homepage = "https://github.com/BlueBrain/HighFive"
    description = "HighFive - HDF5 header-only C++ Library"
    no_copy_source = True
    topics = ("HighFive", "HDF5", "conan")
    requires = ["hdf5/1.10.6", "xtensor/0.21.5"]

    def package(self):
        self.copy("include/*", dst="include", src="include")

    def package_id(self):
        self.info.header_only()

