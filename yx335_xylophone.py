with open("yx335_xylophone.svg","w") as f:
    f.write("""<?xml version="1.0" encoding="UTF-8"?>
<svg width="412.5" height="197.75" viewBox="0 0 412.5 197.75" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <style>
        rect, polygon, circle {
            fill: #ffffff;
            stroke: #ff0000;
            stroke-width: 1.5px;
        }
        polyline {
            stroke: #ff0000;
            stroke-width: 1.25px;
        }
    </style>
    <g transform="translate(-220 -419)">""")

    f.write("""\t\t<polygon points="240,443 240,446 602.5,488 602.5,485" />\n""")
    f.write("""\t\t<polygon points="240,495 240,498 602.5,498 602.5,495" />\n""")

    f.write("""\t\t<polygon points="240,567 240,570 602.5,522.5 602.5,519.5" />\n""")
    f.write("""\t\t<polygon points="240,506.5 240,509.5 602.5,509.5 602.5,506.5" />\n""")

    f.write("""\t\t<rect x="240" y="530" width="5" height="20" style="stroke-width: 1.25px;" />\n""")
    f.write("""\t\t<polyline points="245,535 602.5,509.5" />\n""")
    f.write("""\t\t<polyline points="245,545 602.5,519.5" />\n""")

    f.write("""\t\t<rect x="240" y="460.5" width="5" height="20" style="stroke-width: 1.25px;" />\n""")
    f.write("""\t\t<polyline points="245,465.5 572.25,484.75" />\n""")
    f.write("""\t\t<polyline points="572.25,484.75 602.5,488" />\n""")
    f.write("""\t\t<polyline points="245,475.5 572.25,494.75" />\n""")
    f.write("""\t\t<polyline points="572.25,494.75 602.5,495" />\n""")

    f.write("\n")

    for i in range(26):
        f.write("""\t\t<rect x="{}" y="500" width="10" height="{}" />\n""".format(250+(i*13.5),80-(i*2)))
    
    f.write("\n")

    for i in range(25):
        if not ((i%7==3) or (i%7==6)):
            f.write("""\t\t<rect x="{}" y="{}" width="10" height="{}" />\n""".format(256.75+(i*13.5),429+(i*2),79-(i*2)))
    
    f.write("\n")

    f.write("""\t\t<rect x="230" y="433" width="10" style="fill:#ff0000" height="157" />\n""")
    f.write("""\t\t<rect x="602.5" y="480" width="10" style="fill:#ff0000" height="52.5" />\n""")

    f.write("""\t\t<polyline points="230,498.5 240,498.5" />\n""")
    f.write("""\t\t<polyline points="602.5,498.5 612.5,498.5" />\n""")

    f.write("\n")
    
    f.write("""\t\t<rect x="368.75" y="590" width="100" style="fill:#ff0000" height="2.5" />\n""")
    f.write("""\t\t<circle cx="468.75" cy="591.25" r="5" />""")
    f.write("""\t\t<rect x="368.75" y="600" width="100" style="fill:#ff0000" height="2.5" />\n""")
    f.write("""\t\t<circle cx="468.75" cy="601.25" r="5" />""")

    f.write("</g></svg>")