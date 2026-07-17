import xml.etree.ElementTree as ET

def stretch_ascii_height(filename):
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    tree = ET.parse(filename)
    root = tree.getroot()
    
    for text_elem in root.findall('.//{http://www.w3.org/2000/svg}text'):
        if text_elem.get('class') == 'ascii':
            tspans = text_elem.findall('.//{http://www.w3.org/2000/svg}tspan')
            
            # Start y is 30, end y is 650.
            start_y = 30
            end_y = 650
            num_gaps = len(tspans) - 1
            gap = (end_y - start_y) / num_gaps
            
            for i, tspan in enumerate(tspans):
                new_y = start_y + (i * gap)
                tspan.set('y', str(int(new_y)))
                
    tree.write(filename, encoding="utf-8", xml_declaration=True)

stretch_ascii_height("dark_mode.svg")
stretch_ascii_height("light_mode.svg")
print("Stretched ASCII art height successfully!")
