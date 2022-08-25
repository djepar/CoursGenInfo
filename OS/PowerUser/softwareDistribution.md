# Software Distribution
From Operating Systems and You, the google-coursera IT certification. 
## Windows : Software Packages
### Executable file(.exe)
 Contain instructions for a computer to execute when they're run. 
Executable isnt something unique to Windows, but the special implementation of Windows is the portable executable or PE format. 


#### PE format (Portable Executable)
The filename extension of PE are :
- acm, .ax, .cpl, .dll, .drv, .efi, .exe, .mui, .ocx, .scr, .sys, .tsp

"The PE FORMAT is a datastructure that encapsulates the information necessary for the Windows OS loader to manage the wrapped executable code. This includes dynamic library references for linking, API export and import tables, resource management data and thread-local storage (TLS) data." (https://en.wikipedia.org/wiki/Portable_Executable, 19 of August 2022)
### Microsoft Install package(.msi)
Used to guide a program called the Windows Installer in the installation, maintenance, and removal of programs on the Windows operating system. 
### Windows Store 
A platform to download and install universal Windows platform apps. 
Can work on desktop PCs or Windows tablet. 
The format is APPX
For more information :  https://docs.microsoft.com/en-ca/windows/win32/appxpkg/make-appx-package--makeappx-exe-?redirectedfrom=MSDN
### How to install program from the terminal

#### .exe
For exe : only write the path and the name of the files : 
`PS C:\Users\jpara\Documents\Etudes\CoursGenInfo\hello.exe`


## Linux : Software Packages
Difference between distribution. 
### Debian
Packaged as a .deb file for Debian
To install a .deb : dpkg 
`sudo dpkg -i atom-amd64.deb`
To remove
`sudo dpkg -r atom`
To find the list of program
`dpkg -l`

## Mobile App Packages
Install through App stores : a central, managed marketplace for app developers to publish and sell mobile apps. 
Or with sideloading, but it's more dangerous. 
For Google Play Custom App Publishing API : https://developers.google.com/android/work/play/custom-app-api/get-started

## Windows : Archives
The core or source software files that are compressed into one file. 
To compress on PS
```
Compress-Archive -Path C:\Users\jpara\Documents\Etudes\CoursGenInfo\Directory ~Desktop\CompressedDir
```
For more info : https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/compress-archive?view=powershell-7.2&viewFallbackFrom=powershell-5.0

to unzip :
```
Expand-Archive -LiteralPath <PathToZipFile> -DestinationPath <PathToDestination>
Expand-Archive .\Compressed.zip Decompressed
```
## Linux : Archives
To extract a file using 7zip, use the command 7z and the flag e for extract and then the file you want to extract.
It's a to compressed.
```
7z a dir1
7z e dir1
```

### Tar 
See : http://www.linfo.org/tar.html

## Windows : Package Dependencies
Dependency :Counting on other pieces of software to make an application work, since one bit of code depends on another, in order to work. 
A library :  a way to package a bunch of useful code tha tsomeone else wrote.
TO install sysinternals and the chocolatey 
```
Register-PackageSource -Name chocolatey -ProviderName chocolatey -Location https://chocolatey.org/api/v2
```
Find-Package sysinternals -IncludeDependencies

## Linux : Package Dependencies and Package Manager
Package managers : come with the works to make package installation and removal easier, including installing package dependencies. 
dpkg is a package manager for Debian-based Linux systems.

Apt and dpkg : both command-line package management interfaces

Differences (from https://www.makeuseof.com/apt-vs-dpkg/ )
 - APT or apt-get uses dpkg to install Package 
 - APT can Download packages while dpkg only let you install local file. 
 - Dpkg don't install dependencies. APt will.

Installation with apt : `sudo apt install <program>`
Uninstall with apt : `sudo apt remove <remove>`
Update with apt : `sudo apt upgrade` or `sudo apt update`

PPA : A Personal Package Archive, a software repository for uploading source packages to be built and published as an Advanced Packaging Tool (APT) repository by Launchpag

In Linux repository sources are listed in : /etc/apt/sources.list
#Package Managers
## Windows : Package Manager
Package manager : Makes sure that the process of software installation, removal, update, and dependency management is as easy and automatic as possible. 
### Chocolatey : Third-party package manager
Example : `choco install notepadplusplus.install`

Can also use NuGet, another package manager

## Windows : Underneath the hood
To look what do an installer program do, we can use the Process Monitoring of the Microsoft CIS internals toolkits. 
Orca.exe : a database table editor for creating and editing Windows Installer packages and merge modules. The tool provides a graphical interface for validation, highlighting the particular entries where validation errors or warnings occur. 

Windows Software Development Kit(SDK) : includes redistributable components, documentation, installer, database validation tool, database table editor, database schema, development tools, VBScript tools, sample product and code samples. 

Process Monitor : An advanced monitoring tool for Windows that shows real-time file system, Registry and process/thread activity. 

## Linux : Underneath the Hood 
Normally : from an app you have the code, the README files and a setup_script

# Device Software Management
Driver : Used to help our hardware devices interact with our Operating System
## Windows : Device Manager
In Windowws, Microsoft groups all of the devices and drivers on the computer in a single Microsoft management console :  the Device Manager
Access it in run : devmgmt.msc
Or Windows+x > Devices Manager

## Linux : Devices and Drivers
In Linux, even hardware are considere a file. 
When a new device is connected, a device file is created in the /dev directory. 

Character devices or character special files : 
- like keyboard, or mouse transmit data character by character.
- Raw devices, meaning that the programs don't read and write aligned block
Block devices or block special files: 
- like USB drives, hard drives, and CDROMS, transfer blocks of data; a data block.
-  Buffered access to hardware devices and provide some abstraction from their specifics
SD devices : mass storage devices
/dev/sd[a-Z] 
To see the list of the device : https://web.archive.org/web/20160424173724/https://www.kernel.org/doc/Documentation/devices.txt

udev : "(userspace / dev) is a device manager for the Linux kernel, as the successor of devfsd and hotplug, udev primarily manages devices nodes in the /dev directory" (https://en.wikipedia.org/wiki/Udev, 20 august 2022)

# Windows : Operating System Updates
Windows IT Pro Blog : https://techcommunity.microsoft.com/t5/windows-it-pro-blog/bg-p/Windows10Blog

# Linux : Operating System Updates
With : `apt- upgrade`
But it doesnt upgrade the kernel. To know the version of the kernel : `uname -r`
For the full upgrade : `sudo apt full-upgrade`
Linux kernel is a monolithic kernel

# Filesystems

## Review of Filesystems 
Filesystem : Used to keep track of files and file storage on disk. 

In Windows : NTFS
In Linux : ext4
Fat32 works with Windows, Linux and MacOS

## Disk Anatomy
"A store device can be split into partition. "
"A partition is the piece of a disk tha tyou can manage. "
"To add a filesystem to a disk, first you need to create a partition."

It's possible to add different filesystems on different partitions of the same disk. 

"When you format a filesystem on a partition, it becomes a volume."

Partition table : tells the OS how the disk is partitioned. 
Two mains partition table schemes : Master Boot Record (MBR) and GUID Partition Table(GPT)

MBR : Max 2TB of volume size, mostly on Microsoft, only 4 Partitions 
GPT : becoming the new standard : 2TB or greater, one type of partition and unlimited nbr of partitions. 

Windows : Disk Partitioning and Formatting a Filesystem
Using the GUI : Disk Management

PS : `Diskpart` 
Then list disk
To wipe a disk : clena



