from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

setup(
    name="mead",
    version="0.0.11",
    packages=find_packages(),
    install_requires = [
        "redis",
        "wrapt",
        "redis-orm",
        "aiohttp",
        "aiohttp_session",
        "ujson",
        "cryptography",
    ],
    author = "minamorl",
    author_email = "minamorl@minamorl.com",
    description = "Flexible aiohttp Web Framework",
    tests_require=['tox'],
    cmdclass={'test': Tox},
)
