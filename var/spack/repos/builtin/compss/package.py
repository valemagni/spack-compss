# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install compss
#
# You can edit this file again by typing:
#
#     spack edit compss
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Compss(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://compss.bsc.es"
    url = "https://compss.bsc.es/repo/sc/stable/COMPSs_3.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers=['lezzidan']

    version("3.2", sha256="f32825d7f26bde13cd3699f0aea14da18632b30cf08f113a06ae050033efc837")
    #version("3.2", sha256="30d7f8e1e845fbb562057ff1b2d50a14d709208ab7ad4e1e39b74f163937672a")
    #version("3.1", sha256="53880443567269faa724d1908a6bc4d82998be3cc93c77386f620c4c8a72e60d")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    depends_on('python@3.9')
    depends_on('py-setuptools', type='build')
    depends_on('openjdk')
    depends_on('boost')
    depends_on('libxml2')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')

    def install(self, spec, prefix):
        import os
        print("Prefix: " + str(prefix))
        install_script = Executable('./install')
        install_script('-T', prefix.compss)
        print("Dirs: " +str(os.listdir(str(prefix))))


    def setup_run_environment(self, env):
        env.set('COMPSS_HOME', self.prefix.compss)
        env.prepend_path('PATH', self.prefix.compss + '/Runtime/scripts/user')
