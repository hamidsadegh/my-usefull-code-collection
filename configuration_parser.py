import re

class Configuration_Parser:
  deviceConfig = open('cinfig.txt', 'r')read()
  def parseCostomerName(self):
    customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
    customerNames = re.findall(customerNamePattern, self.deviceConfig)
    return customerNames
