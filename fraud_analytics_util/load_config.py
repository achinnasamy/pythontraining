import xml.etree.ElementTree as ET
tree = ET.parse('../config/fraud_analytics.xml')
root = tree.getroot()


print root.tag












