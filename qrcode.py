import pyqrcode
from pyqrcode import QRCode
import time

print("""
.d88888b.  8888888b.   .d8888b.                888                                                          
d88P" "Y88b 888   Y88b d88P  Y88b               888                                                          
888     888 888    888 888    888               888                                                          
888     888 888   d88P 888         .d88b.   .d88888  .d88b.       .d88b.   .d88b.  88888b.   .d88b.  888d888 
888     888 8888888P"  888        d88""88b d88" 888 d8P  Y8b     d88P"88b d8P  Y8b 888 "88b d8P  Y8b 888P"   
888 Y8b 888 888 T88b   888    888 888  888 888  888 88888888     888  888 88888888 888  888 88888888 888     
Y88b.Y8b88P 888  T88b  Y88b  d88P Y88..88P Y88b 888 Y8b.         Y88b 888 Y8b.     888  888 Y8b.     888     
 "Y888888"  888   T88b  "Y8888P"   "Y88P"   "Y88888  "Y8888       "Y88888  "Y8888  888  888  "Y8888  888     
       Y8b                                                            888                                    
                                                                 Y8b d88P                                    
                                                                  "Y88P"                                     
""")



s = input("Write the site for the qrcode: ")
url = pyqrcode.create(s)
url.svg("QRCode.svg ", scale=10, background="white", module_color="black")
