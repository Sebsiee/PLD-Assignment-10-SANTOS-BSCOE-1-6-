import pyqrcode
import png
from pyqrcode import QRCode

dataName = "Name Sebastian O. Santos, Age: 18"
dataPNG = pyqrcode.create(dataName)
dataPNG.png("Personal Details.png", scale = 6)