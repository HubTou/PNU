#!/usr/bin/env python
""" about - show system information
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: Hubert Tournier
"""

import getopt
import locale
import logging
import os
import platform
import re
import shutil
import socket
import sys
import sysconfig
import unicodedata

# Version string used by the what(1) and ident(1) commands:
ID = "@(#) $Id: about - show system information v1.0.0 (May 10, 2021) by Hubert Tournier $"

# Optional dependency upon py-cpuinfo
# Use "pip install py-cpuinfo" to install
try:
    import cpuinfo
except ModuleNotFoundError:
    pass

# Default parameters. Can be superseded by command line options
parameters = {
    "Hardware": False,
    "Operating System": False,
    "System": False,
    "Environment": False,
    "Python": False,
}

################################################################################
def display_help():
    """Displays usage and help"""
    print()
    print("usage: about [-d|--debug] [-h|--help|-?] [-v|--version] [-a|--all]")
    print("       [-S|--sys|--system] [-H|--hw|--hardware] [-O|--os|--operating]")
    print("       [-E|--env|--environment] [-P|--py|--python] [--]")
    print("  ----------------------   ---------------------------------------------")
    print("  -a|--all                 Same as -SHOEP")
    print("  -S|--sys|--system        Show information about the system")
    print("  -H|--hw|--hardware       Show information about the hardware")
    print("  -O|--os|--operating      Show information about the Operating System")
    print("  -E|--env|--environment   Show information about the environment")
    print("  -P|--py|--python         Show information about Python")
    print("  -d|--debug               Enable debug mode")
    print("  -h|--help|-?             Print usage and this help message and exit")
    print("  -v|--version             Print version and exit")
    print("  --                       Options processing terminator")
    print()


################################################################################
def process_command_line():
    """Process command line"""
    # pylint: disable=C0103
    global parameters
    # pylint: enable=C0103

    try:
        # option letters followed by : expect an argument
        # same for option strings followed by =
        options, remaining_arguments = getopt.getopt(
            sys.argv[1:],
            "adhvHOSEP?",
            [
                "all",
                "debug",
                "env",
                "environment",
                "everything",
                "hardware",
                "help",
                "hw",
                "life",
                "operating",
                "os",
                "py",
                "python",
                "sys",
                "system",
                "universe",
                "version",
            ],
        )
    except getopt.GetoptError as erreur:
        logging.critical("Syntax error: %s", erreur)
        display_help()
        sys.exit(1)

    for option, _ in options:

        if option in ("-a", "--all"):
            parameters["Hardware"] = True
            parameters["Operating System"] = True
            parameters["System"] = True
            parameters["Environment"] = True
            parameters["Python"] = True

        elif option in ("-H", "--hw", "--hardware"):
            parameters["Hardware"] = True

        elif option in ("-O", "--os", "--operating"):
            parameters["Operating System"] = True

        elif option in ("-S", "--sys", "--system"):
            parameters["System"] = True

        elif option in ("-E", "--env", "--environment"):
            parameters["Environment"] = True

        elif option in ("-P", "--py", "--python"):
            parameters["Python"] = True

        elif option in ("--life", "--universe"):
            print("42!")
            sys.exit(42)

        elif option == "--everything":
            print("Mama mia!")
            sys.exit(88)

        elif option in ("-d", "--debug"):
            logging.disable(logging.NOTSET)

        elif option in ("-h", "--help", "-?"):
            display_help()
            sys.exit(0)

        elif option in ("-v", "--version"):
            print(ID.replace("@(#) $Id: ", "").replace(" $", ""))
            sys.exit(0)

    return remaining_arguments


################################################################################
def printm(first_line, results):
    """Multi-lines print"""
    print(first_line + ":")
    print(">>>>>>>>>>")
    if isinstance(results, list):
        for line in results:
            print(line)
    elif isinstance(results, dict):
        for key, value in results.items():
            print("{}={}".format(key, value))
    else:
        print(results)
    print("<<<<<<<<<<")


################################################################################
# Possible values derived from https://hg.python.org/cpython/file/3.5/Lib/platform.py
def sys_type():
    """Return (approximate) system type"""
    operating_system_type = platform.system()
    if operating_system_type in (
        "FreeBSD",
        "NetBSD",
        "OpenBSD",
        "Linux",
        "Darwin",
        "MacOS X Server",
        "Solaris",
    ):
        return "Unix"
    return operating_system_type


################################################################################
def grep(filename, pattern):
    """Search a string in a file"""
    regexp = re.compile(pattern)
    results = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            result = regexp.match(line)
            if result:
                results.append(line.strip())
    return results


################################################################################
def about_local_system():
    """Show information about the local system"""
    if parameters["System"]:
        print("[System]")
        if sys_type() == "Unix":
            print("os.uname().nodename={}".format(os.uname().nodename))
        hostname = socket.gethostname()
        print("socket.gethostname()={}".format(hostname))
        print("socket.getfqdn()={}".format(socket.getfqdn()))
        print(
            "socket.gethostbyname('{}')={}".format(
                hostname, socket.gethostbyname(hostname)
            )
        )
        print(
            "socket.gethostbyname_ex('{}')={}".format(
                hostname, socket.gethostbyname_ex(hostname)
            )
        )
        print()

        print("[System/Network]")
        print("socket.if_nameindex()={}".format(socket.if_nameindex()))
        print("socket.getdefaulttimeout()={}".format(socket.getdefaulttimeout()))
        print("socket.has_dualstack_ipv6()={}".format(socket.has_dualstack_ipv6()))
        print()


################################################################################
def about_hardware():
    """Show information about the hardware"""
    if parameters["Hardware"]:
        print("[Hardware]")
        if sys_type() == "Unix":
            print("os.uname().machine={}".format(os.uname().machine))
        print("platform.machine()={}".format(platform.machine()))
        print("platform.processor()={}".format(platform.processor()))
        print("os.cpu_count()={}".format(os.cpu_count()))
        print("sys.byteorder={}".format(sys.byteorder))
        if platform.system() == "FreeBSD":
            printm(
                "/var/run/dmesg.boot scan",
                grep("/var/run/dmesg.boot", "^(CPU: |FreeBSD/SMP: |real memory  =)"),
            )
        print()

        print("[Hardware/cpuinfo optional module]")
        try:
            for key, value in cpuinfo.get_cpu_info().items():
                print("{}: {}".format(key, value))
        except NameError:
            print("# For more detailed (and portable) CPU information do:")
            print("# pip install py-cpuinfo ; cpuinfo")
        print()


################################################################################
def about_operating_system():
    """Show information about the operating system"""
    if parameters["Operating System"]:
        print("[Operating system]")
        print("os.name={}".format(os.name))
        print("platform.system()={}".format(platform.system()))
        print("platform.release()={}".format(platform.release()))
        print("sys.platform={}".format(sys.platform))
        print("sysconfig.get_platform()={}".format(sysconfig.get_platform()))
        print("platform.platform()={}".format(platform.platform()))
        print("platform.version()={}".format(platform.version()))
        print("platform.uname()={}".format(platform.uname()))
        if sys_type() == "Unix":
            print("os.uname().sysname={}".format(os.uname().sysname))
            print("os.uname().release={}".format(os.uname().release))
            print("os.uname().version={}".format(os.uname().version))
        elif sys_type() == "Windows":
            print("sys.getwindowsversion()={}".format(sys.getwindowsversion()))
            print("platform.win32_ver()={}".format(platform.win32_ver()))
            print("platform.win32_edition()={}".format(platform.win32_edition()))
            print("platform.win32_is_iot()={}".format(platform.win32_is_iot()))
        print()

        if sys_type() == "Unix":
            print("[Operating system/Configuration]")
            for name in os.confstr_names:
                try:
                    print("os.confstr('{}')={}".format(name, os.confstr(name)))
                except OSError as error:
                    print("os.confstr('{}')={}".format(name, "Error: " + str(error)))
            for name in os.sysconf_names:
                try:
                    print("os.sysconf('{}')={}".format(name, os.sysconf(name)))
                except OSError as error:
                    print("os.sysconf('{}')={}".format(name, "Error: " + str(error)))
            print()

        print("[Operating system/Portability]")
        print("os.curdir={}".format(os.curdir))
        print("os.pardir={}".format(os.pardir))
        print("os.sep={}".format(os.sep))
        print("os.altsep={}".format(os.altsep))
        print("os.extsep={}".format(os.extsep))
        print("os.pathsep={}".format(os.pathsep))
        print("os.defpath={}".format(os.defpath))
        print("os.devnull={}".format(os.devnull))
        print("os.linesep={}".format(os.linesep))


################################################################################
def about_environment():
    """Show information about the environment"""
    if parameters["Environment"]:
        print("[Environment]")
        print("os.getcwd()={}".format(os.getcwd()))
        printm("dict(os.environ)", dict(os.environ))
        print("os.supports_bytes_environ={}".format(os.supports_bytes_environ))
        print("shutil.get_terminal_size()={}".format(shutil.get_terminal_size()))
        print("sys.prefix={}".format(sys.prefix))
        if sys_type() == "Unix":
            print("os.getloadavg()={}".format(os.getloadavg()))
        print()

        print("[Environment/Locale]")
        print("locale.getlocale()={}".format(locale.getlocale()))
        print("locale.getdefaultlocale()={}".format(locale.getdefaultlocale()))
        printm("locale.localeconv()", locale.localeconv())
        print()


################################################################################
def about_python():
    """Show information about the python install"""
    if parameters["Python"]:
        print("[Python]")
        print(
            "sysconfig.get_python_version()={}".format(sysconfig.get_python_version())
        )
        if sys_type() == "Windows":
            print("sys.winver={}".format(sys.winver))
        printm("sys.version:", sys.version)
        print("sys.version_info={}".format(sys.version_info))
        print("sys.hexversion={}".format(sys.hexversion))
        print("sys.implementation={}".format(sys.implementation))
        # print("sys.copyright={}".format(sys.copyright))
        print("platform.python_build()={}".format(platform.python_build()))
        print("platform.python_branch()={}".format(platform.python_branch()))
        print(
            "platform.python_implementation()={}".format(
                platform.python_implementation()
            )
        )
        print("platform.python_revision()={}".format(platform.python_revision()))
        print("platform.python_version()={}".format(platform.python_version()))
        print(
            "platform.python_version_tuple()={}".format(platform.python_version_tuple())
        )
        print()

        print("[Python/Config]")
        print("sys.executable={}".format(sys.executable))
        print("sys.flags={}".format(sys.flags))
        # print("sys.builtin_module_names={}".format(sys.builtin_module_names))
        # print("sys.modules={}".format(sys.modules))
        print("sys.path={}".format(sys.path))
        # print("sys.platlibdir={}".format(sys.platlibdir)) # Python 3.9+
        print("sys.getrecursionlimit()={}".format(sys.getrecursionlimit()))
        print("sys.getswitchinterval()={}".format(sys.getswitchinterval()))
        print("sys.thread_info={}".format(sys.thread_info))
        print("platform.python_compiler()={}".format(platform.python_compiler()))
        if sys_type() == "Unix":
            print("platform.libc_ver()={}".format(platform.libc_ver()))
        print("sys.api_version={}".format(sys.api_version))
        print()

        print("[Python/Math]")
        print("sys.int_info={}".format(sys.int_info))
        print("sys.maxsize={}".format(sys.maxsize))
        print("sys.float_info={}".format(sys.float_info))
        print()

        print("[Python/Unicode]")
        print("sys.getdefaultencoding()={}".format(sys.getdefaultencoding()))
        print("sys.getfilesystemencoding()={}".format(sys.getfilesystemencoding()))
        print("unicodedata.unidata_version={}".format(unicodedata.unidata_version))
        print("sys.maxunicode={}".format(sys.maxunicode))
        print()


################################################################################
logging.basicConfig(
    level=logging.DEBUG, format="%(module)s: %(levelname)s: %(message)s"
)
logging.disable(logging.DEBUG)

process_command_line()

if True not in parameters.values():
    logging.warning("Please select something to show:")
    display_help()
    sys.exit(0)

about_local_system()
about_hardware()
about_operating_system()
about_environment()
about_python()

sys.exit(0)
