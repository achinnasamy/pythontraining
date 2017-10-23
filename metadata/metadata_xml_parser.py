
from xml.dom.minidom import parse
import xml.dom.minidom


DOMTree = xml.dom.minidom.parse("metrolinux_metadata_static.xml")


collection = DOMTree.documentElement
if collection.hasAttribute("name"):
   print "Root element : %s" % collection.getAttribute("name")

   operational_metadata = collection.getElementsByTagName("operational_metadata")

   for md in operational_metadata:

       type = md.getElementsByTagName('op_type')[0]
       print "source_system: %s" % type.childNodes[0].data