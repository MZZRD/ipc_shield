import cadquery as cq
from cadquery import exporters

# Arduino dimensions
# source: https://www.thingiverse.com/thing:4273893
#    and: https://robotdyn.com/pub/media/0G-00005806==MEGA+WiFi-R3-AT2560-ESP8266-32MB-CH340G/DOCS/DIM==0G-00005806==MEGA+WiFi-R3-AT2560-ESP8266-32MB-CH340G.pdf

arduino_base_height = 3.0 #mm

arduino_base_pts = [
    (0.0, 0.0),
    (101.86 - 3.81, 0.0),
    (101.86, 3.81),
    (101.86, 38.10),
    (101.86 - 2.54, 38.10 + 2.54),
    (101.86 - 2.54, 53.61 - 2.54),
    (101.86 - 2 * 2.54, 53.61),
    (0.0, 53.61),
    (0.0, 0.0)
    ]

arduino_hole_pts = [
    (14.11, 2.53),
    (96.66, 2.53),
    (15.36, 50.79),
    (90.33, 50.79)
]

# Arduino base object
shield = (
    cq.Workplane("XY")\
        # Extrude base from arduino_base_pts
        .polyline(arduino_base_pts).wire().extrude(arduino_base_height)\
            # Add a chamfer
            .faces("|Z").chamfer(0.3)
)

# Add holes to Arduino base
shield = shield.faces(">Z").workplane().pushPoints(arduino_hole_pts).hole(3.2)

# Export the shield
exporters.export(shield, '../export/stl/shield_base.stl')
# exporters.export(shield, '../export/step/shield_base.step')

# # Render the solid
# show_object(shield)
