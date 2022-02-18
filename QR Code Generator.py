import pyqrcode
import png
from pyqrcode import QRCode

dataName = ""
dataPNG = pyqrcode.create(dataName)
dataPNG.png("Personal Details.png", scale = 6)