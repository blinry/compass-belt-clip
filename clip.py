import cadquery as cq

motor_diameter = 10 + 0.3 # mm
motor_height = 3 + 0.3
thickness = 1
thickness_bottom = 0.6
cable_thickness = 1.5

belt_hole_distance = 17.5
belt_hole_diameter = 5
belt_hole_height = 4
clip_protrusion = 1

width = max(belt_hole_distance + belt_hole_diameter, motor_diameter + thickness)
height = motor_diameter + thickness

# Construct body with clips. First, we create half of the body.
result = (
    cq.Workplane("front")
    .rect(width/2, height)
    .extrude(motor_height + thickness_bottom + cable_thickness)
    
    .faces(">Z")
    .workplane()
    .moveTo(-width/8)
    .circle(belt_hole_diameter/2)
    .extrude(belt_hole_height)
    
    .faces(">Z")
    .workplane()
    .moveTo(-width/8)
    .circle(belt_hole_diameter/2)
    .extrude(clip_protrusion*0.75, taper=-45)
    
    .faces(">Z")
    .workplane()
    .moveTo(-width/8)
    .circle(belt_hole_diameter*0.61)
    .extrude(clip_protrusion, taper=45)
    
    .faces(">Z")
    .workplane()
    .moveTo(-width/8)
    .rect(2,belt_hole_diameter*1.3)
    .cutThruAll()
    )

# And then mirror it, and add a hole for the motor.
result = (
    result.mirror(result.faces(">X"), union=True)
    .faces(">Z")
    .workplane()
    .moveTo(width/4, 0)
    .hole(motor_diameter, motor_height + belt_hole_height + clip_protrusion + cable_thickness + 0.25)
)

# Ridge between motor cables.
ridge = (
    cq.Workplane("XY")
    .moveTo(width/4,0)
    .rect(1,height)
    .extrude(cable_thickness + thickness_bottom)
)

# Hole at the side.
hole = (
    cq.Workplane("XY")
    .workplane(thickness_bottom)
    .moveTo(width/4,height/2)
    .rect(4,motor_diameter)
    .extrude(cable_thickness*6)
)

result = result.cut(hole)
result = result.union(ridge)

show_object(result)