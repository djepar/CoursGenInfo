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

Find-Package sysinternals -IncludeDependencies