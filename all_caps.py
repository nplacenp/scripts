#! Python
#Copies pasted text to clipboard in ALL CAPS

import pyperclip

pyperclip.copy(input('What text would you like converted to CAPS?\n').upper())

print('\n\nPROCESS COMPLETE')