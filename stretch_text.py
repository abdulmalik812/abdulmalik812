import xml.etree.ElementTree as ET

def stretch_stats_height(filename):
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    tree = ET.parse(filename)
    root = tree.getroot()
    
    for text_elem in root.findall('.//{http://www.w3.org/2000/svg}text'):
        if text_elem.get('x') == '500':
            for tspan in text_elem.findall('.//{http://www.w3.org/2000/svg}tspan'):
                y_str = tspan.get('y')
                if y_str:
                    old_y = float(y_str)
                    # Scale factor to stretch from 480 height to ~594 height
                    new_y = 30 + (old_y - 30) * 1.2375
                    tspan.set('y', str(int(new_y)))

    tree.write(filename, encoding="utf-8", xml_declaration=True)

stretch_stats_height("dark_mode.svg")
stretch_stats_height("light_mode.svg")
print("Stretched text height successfully!")
