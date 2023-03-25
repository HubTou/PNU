# [Wilderness Survival Guide](https://en.wikipedia.org/wiki/Wilderness_Survival_Guide)
If you want to experience Unix on Windows without waiting for the project progress (not even speaking of completion :-) ) there are several solutions available.

Here's a list of some of them:

### From Microsoft itself:

Years | Name | Windows Version | Comments
--- | --- | --- | ---
1993-1998 | [Microsoft POSIX subsystem](https://en.wikipedia.org/wiki/Microsoft_POSIX_subsystem) | NT | 
1999-2004 | [Windows Services for UNIX](https://en.wikipedia.org/wiki/Windows_Services_for_UNIX) (SFU) | NT | 
2005-2015 | [Subsystem for UNIX-based Applications](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771470(v=ws.11)?redirectedfrom=MSDN) (SUA) | 2003 R2-2008, Vista, 7 |
2016-today | [Windows Subsystem for Linux ](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) (WSL)| 10, 2019 | WSL 2 includes a real Linux kernel running on Hyper-V

### From the open source community:
Years | Name | Windows Version | Comments
--- | --- | --- | ---
1995-2021 | [Cygwin](https://en.wikipedia.org/wiki/Cygwin) | All | Focus on compatibility. Stripped down and being phase out on Windows 32bits versions
1998-2019 | [MinGW](https://en.wikipedia.org/wiki/MinGW) | ? | Focus on simplicity and performance
-2012 | [UWIN](https://en.wikipedia.org/wiki/UWIN) | 95, NT | 
2000-2013 | [UnxUtils](https://en.wikipedia.org/wiki/UnxUtils) | Win32 | Unmaintained
-2017 | [GnuWin32](https://en.wikipedia.org/wiki/GnuWin32) | Win32 | Unmaintained
2014-2020 | [GNU on Windows](https://github.com/bmatzelle/gow/wiki) (GOW) | ? | A lightweight alternative to Cygwin
2014-2019 | [Babun](https://babun.github.io/) | ? | Pre-configured Cygwin with a lot of addons, peculiarly a lovable Windows shell

### From other software vendors:
Years | Name | Windows Version | Comments
--- | --- | --- | ---
1989-2017 | [MKS Toolkit](https://en.wikipedia.org/wiki/MKS_Toolkit) | All |
1996-2010 | [Interix](https://en.wikipedia.org/wiki/Interix) | NT, 2003 R2-2012, Vista, 7, 8| Deprecated

Let's [discuss about it](https://github.com/HubTou/PNU/discussions) if you think I've forgotten other significant ones!

Of course you can also select any real Unix-like system and run it under Windows on [VirtualBox](https://www.virtualbox.org/).

And one day, when the PNU project has made significant progress, you'll be able to enjoy a FreeBSD Subsystem for Windows (FSW).
