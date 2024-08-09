# PPPOE-Password-Finder
Step 1 Physical Preperation
Connect two usb ethernet adapter to your computer.
Connect ethernet cable coming from WAN port of your home router to the first ethernet adapter.
Connect ethernet cable coming from LAN port of your building router or ONT device to the second ethernet adapter.

Step 2 Finding interface and mac
Install wireshark
Open wireshark
Find interface code for the ethernet adapter which connected to home router.
Find interface code for the ethernet adapter which connected to building router.
Find mac address of your home router by listening the interface which connected to home router.
Find mac address of your building router by listening the interface which connected to building router.

Step 3 Run and Find PPPOE Authentication Information
Write the interface and mac informations to the variables in the python code.
Run the python file.
PPPOE Authentication Request will be shown in the console log in 1 minute.
