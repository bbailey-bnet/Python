import sys
#possible values for sys.platform include:
#linux
#win32
#cygwyn
#darwin
#os2
#os2emx
#riscos
#atheos
#freebsd7
#freebsd8


my_system = sys.platform

if my_system == 'Win32':
    print("Windows specific build initializing...")
elif my_system == 'darwin':
    print("OS X specific build initializing...")
