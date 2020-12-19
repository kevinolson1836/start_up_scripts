
#import pygtk
import gnomekeyring
import sys

gnomekeyring.unlock_sync('login','<password>')
gnomekeyring.unlock_sync('<keyring>','<password>') # Repeat for each keyring you need unlocked automatically

sys.exit(0)
