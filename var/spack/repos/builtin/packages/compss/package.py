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

from spack import *


class Compss(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://compss.bsc.es"
    url      = "https://compss.bsc.es/repo/sc/stable/COMPSs_3.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.1', sha256='53880443567269faa724d1908a6bc4d82998be3cc93c77386f620c4c8a72e60d')

        # dependencies. 
    depends_on('python@3.6')
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
        install_script('--only-python-3', prefix.compss)
        print("Dirs: " +str(os.listdir(str(prefix))))


    def setup_run_environment(self, env):
        env.set('COMPSS_HOME', self.prefix.compss)
        env.prepend_path('PATH', self.prefix.compss + '/Runtime/scripts/user')
