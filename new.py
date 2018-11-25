import xml.etree.ElementTree as ET


ET._namespace_map['http://www.mediawiki.org/xml/export-0.10/'] = ''
ET._namespace_map['http://www.w3.org/2001/XMLSchema-instance'] = 'xsi'
tree = ET.parse('apple.xml')
root = tree.getroot()

count = 1
str1 = " "
str_array = []
length = len(root[1].findall('{http://www.mediawiki.org/xml/export-0.10/}revision'))

for i in root[1].findall('{http://www.mediawiki.org/xml/export-0.10/}revision'):
	if count == length:
		str1 = ET.tostring(i).decode("utf-8")
	else:
		str_array.append(ET.tostring(i).decode("utf-8"))			
	root[1].remove(i)
	count += 1

root[1].append(ET.fromstring(str1))
tree.write('latest.xml')
