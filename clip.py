import cadquery as cq

motor_diameter = 10 + 0.3 # mm
motor_height = 3 + 0.3
thickness = 1
thickness_bottom = 0.6

belt_hole_distance = 17.5
belt_hole_diameter = 5
belt_hole_height = 4
clip_protrusion = 1

width = max(belt_hole_distance + belt_hole_diameter, motor_diameter + thickness)
height = motor_diameter + thickness

result = (
    cq.Workplane("front")
    .rect(width/2, height)
    .extrude(motor_height + thickness_bottom)
    
    .faces(">Z")
    .workplane()
    .moveTo(-width/8)
    .circle(belt_hole_diameter/2)
    .extrude(belt_hole_height)
    
    .faces(">Z")
    .workplane()
    .moveTo(-width/8)
    .circle(belt_hole_diameter/2)
    .extrude(clip_protrusion/2, taper=-45)
        
    # .faces(">Z")
    # .workplane()
    # .moveTo(-width/8)
    # .circle(belt_hole_diameter/2*1.15)
    # .extrude(0.2)
    
    .faces(">Z")
    .workplane()
    .moveTo(-width/8)
    .circle(belt_hole_diameter/2*1.15)
    .extrude(clip_protrusion, taper=45)
    
    .faces(">Z")
    .workplane()
    .moveTo(-width/8)
    .rect(2,belt_hole_diameter*1.2)
    .cutThruAll()
    )

result = (
    result.mirror(result.faces(">X"), union=True)
    .faces(">Z")
    .workplane()
    .moveTo(width/4, 0)
    .hole(motor_diameter, motor_height + belt_hole_height + clip_protrusion)
    .faces(">Y")
    .workplane()
    .moveTo(-width/4,-height*0.45)
    .hole(6, thickness*2)
)


# result = (
#     cq.Workplane("front")
#     .circle((motor_diameter + thickness)/2)
#     .extrude(motor_height + thickness)
#     .faces(">Z")
#     .workplane()
#     .hole(motor_diameter, motor_height)
#     )