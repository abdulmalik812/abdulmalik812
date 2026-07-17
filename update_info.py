import xml.etree.ElementTree as ET

new_stats_xml = """<text x="580" y="30" fill="#c9d1d9">
<tspan x="580" y="30">abdul@malik</tspan> -—————————————————————————————————————————————-—-
<tspan x="580" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> .............................. </tspan><tspan class="value">Human (Developer Edition) 26.0</tspan>
<tspan x="580" y="70" class="cc">. </tspan><tspan class="key">Uptime</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">Passionate Developer</tspan>
<tspan x="580" y="90" class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> ............................ </tspan><tspan class="value">Planet Earth</tspan>
<tspan x="580" y="110" class="cc">. </tspan><tspan class="key">Role</tspan>:<tspan class="cc"> ............................ </tspan><tspan class="value">Full Stack Developer</tspan>
<tspan x="580" y="130" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ............................. </tspan><tspan class="value">VS Code, Figma</tspan>
<tspan x="580" y="150" class="cc">. </tspan>
<tspan x="580" y="170" class="cc">. </tspan><tspan class="key">Frontend</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">React.js, Next.js, Tailwind, Bootstrap</tspan>
<tspan x="580" y="190" class="cc">. </tspan><tspan class="key">Backend</tspan>:<tspan class="cc"> ......................... </tspan><tspan class="value">Python, Django, FastAPI</tspan>
<tspan x="580" y="210" class="cc">. </tspan><tspan class="key">Database</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">PostgreSQL, MySQL, SQLite</tspan>
<tspan x="580" y="230" class="cc">. </tspan><tspan class="key">Tools</tspan>:<tspan class="cc"> ........................... </tspan><tspan class="value">Git, GitHub, Docker</tspan>
<tspan x="580" y="250" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">English, Hindi</tspan>
<tspan x="580" y="270" class="cc">. </tspan>
<tspan x="580" y="290">- Projects</tspan> -————————————————————————————————————————————————————-—-
<tspan x="580" y="310" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> ....................... </tspan><tspan class="value">Coming Soon</tspan>
<tspan x="580" y="330" class="cc">. </tspan>
<tspan x="580" y="350">- Contact</tspan> -—————————————————————————————————————————————————————-—-
<tspan x="580" y="370" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ........................... </tspan><tspan class="value">abdulmalik256786@gmail.com</tspan>
<tspan x="580" y="390" class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">github.com/abdulmalik812</tspan>
<tspan x="580" y="410" class="cc">. </tspan>
<tspan x="580" y="430">- GitHub Stats</tspan> -——————————————————————————————————————————————-—-
<tspan x="580" y="450" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc" id="repo_data_dots"> .... </tspan><tspan class="value" id="repo_data">--</tspan> {<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">--</tspan>}<tspan class="cc" id="repo_stats_gap"> |  </tspan><tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots"> ............ </tspan><tspan class="value" id="star_data">--</tspan>
<tspan x="580" y="470" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc" id="commit_data_dots"> .................... </tspan><tspan class="value" id="commit_data">--</tspan><tspan class="cc" id="commit_stats_gap"> |  </tspan><tspan class="key">Followers</tspan>:<tspan class="cc" id="follower_data_dots"> ........ </tspan><tspan class="value" id="follower_data">--</tspan>
<tspan x="580" y="490" class="cc">. </tspan><tspan class="key">GitHub LOC</tspan>:<tspan class="cc" id="loc_data_dots"> ................... </tspan><tspan class="value" id="loc_data">--</tspan> ( <tspan class="addColor">+</tspan><tspan class="addColor" id="loc_add">--</tspan>, <tspan id="loc_del_dots" /><tspan class="delColor">-</tspan><tspan class="delColor" id="loc_del">--</tspan> )
</text>"""

def update_user_info(filename):
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Increase height to fit the new text lines
    if 'height' in root.attrib:
        root.attrib['height'] = '700px'
    if 'width' in root.attrib:
        root.attrib['width'] = '1350px'
        
    for rect in root.findall('.//{http://www.w3.org/2000/svg}rect'):
        rect.attrib['height'] = '700px'
        rect.attrib['width'] = '1350px'
        
    # Replace the stats <text> block
    for text_elem in root.findall('.//{http://www.w3.org/2000/svg}text'):
        if text_elem.get('x') == '580':
            # We found the stats block, replace it entirely
            new_text_elem = ET.fromstring(new_stats_xml)
            if filename == "light_mode.svg":
                new_text_elem.set('fill', '#24292f')
            root.remove(text_elem)
            root.append(new_text_elem)
            break
            
    tree.write(filename, encoding="utf-8", xml_declaration=True)

update_user_info("dark_mode.svg")
update_user_info("light_mode.svg")
print("User info injected successfully!")
