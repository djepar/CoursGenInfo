# Question 1
- Creating a registry of laptop so it's easier to track laptops and who have them. So putting a label for the laptop and creating a list, with the name of the person, the serial number of the laptop and the id of the user.
- Also, maybe start to buy more similar laptop for easier maintenance. Even thought, we need to keep in mind, the different needs (cpu strenght, needs for a gpu, ram, etc). 
  - Keep a laptop or two in backup so people don't have to wait and loose time 
- Put all the computer into LDAP so
  - we can implement strict password requirement
  - give HR a way to retrieve password for employees. 
  - Create different restrictions based on the needs of each employees title.
- Keep the cloud for the rest, and give the password and everything from the LDAP session credential, so if there is a problem, the IT or HR rep can just look for the password and such from the LDAP for the cloud. 

# Question 2
- Put the software into the cloud, for a better and more consistent link. Create commercial email, create a slack account to communicate, etc.
- Give less power relative to the directory where every file are : writing-reading priviledge if the person need to write, otherwise reading if the person only need to read. No delete permission except for a few person. 
- Putting in place a scaling plan, so we can plan the growth, also using service or infrastructure as service could eliminate the need for other IT support. 
  - Also, putting an automatic-help-desk service to help with easy It-related question.
- Create an image of an all-install software, so we don't have to install everything on every computers. 

# Question 3
- either change the open-source ticketing system or remove it completely, would be easier. 
- Install a messaging system with an app-has-a-service
- Testing the website to see where is the problem, and install an alert system with a diagnostic tool for aftwerward.
- If the backup can be put on a single disk, using a cloud shouldn't be expensive, which would be easier.
- Disable the directory for the persons that are leaving. 