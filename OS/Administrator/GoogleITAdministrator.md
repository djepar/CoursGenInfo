## Course Introduction 
Google System Administration and IT Infrastruction 
System admnistration : "The field in It that's responsible for maintaining reliable computer systems in a multi-user environment."

## What is System Administration?
"IT infrastructure encompasses the software, the hardware, network, an services required for an organization to operate in an enterprise IT environment."

## Servers Revisited: 
Server : "Software or machine that provides services to other software or machines". 

## The Cloud
Data Center : "A facility that stores hundreds, if not thousands, of servers."

# Systems Administration Tasks

## Organization Policies
__Questions to keep in mind__ 
- Should users be allowed to install software?
- Should users have complex passwords with certain requirements?
- Should users be allowed to view non-work-related websites, like Facebook?
- If you hand out a company phone to an employee, should you set a device password?

## User and Hardware Provisioning
Hardware and software need to be standarize in some way. 
Stages 
- Procurement (buying)
- Deployment (installing)
- Maintenance (update and fix)
- Retirement (remove and replace)

# Applying Changes

## With Great Power Comes Great Responsibility
Uses admin session the less as possible. 
Record with script or Start-transcript what you do // or do documentation so you remember what you done (in case something went wrong)
- script : `script session.log` and when done `exit` || Ctrl-D
- Start-Transcript : `Start-Transcript -Path C:\Transcript.txt


Rollback : Reverting to a previous state

## Never Test in Production
Production : "the parts of the infrastructure where certain service is executed and served to its users."

Test environment : "A virtual machine running the same configuration as the production environment, but isn't actually serving any users of the service. "

Secondary or stand-by machine : "This machine will be exactly the same as a production machine, but won't receive any traffic actual users until you enable it to do so." 

"For even bigger services, when you have lots of servers providing the service, you may want to have canaries." 

## Assessing Risk
How important is the service, and how critical if the service fails. 

"In general, the more users your services reaches, the more you'll want to ensure that changes aren't disruptive. The more important your service is to your company's operations, the more you'll work to keep the service up." 

## Fixing Things the Right Way
Reproduction case : "Creating a roadmap to retrace the steps that led the user to an unexpected outcome."
Questions when doing a reproduction case: 
"""
- What steps did you take to get to this point?
- What's the unexpected or bad result?
- What's the expected result?
"""

# Intro to IT Infrastructure Service
## Types of IT Infrastructure Services
IaaS : Infrastructure as a Service like Amazon EC2, Linode. Windows Azure and Google Compute Engine. 

NaaS : Networking as a Service

SaaS : Software as a Service

PaaS : Plateform as a Service

DaaS : Directory as a Service

# Network Services
## FTP, SFTP, and TFTP
FTP or File transfer service : no encryption, authentication
SFTP or Secure File transfer: SSH encryption, authentication
TFTP or Trivial FTP : no encryption, no authentication

Other way of booting a computer : PXE Boot (preboot execution)

