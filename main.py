from Value import Value
from Scale import Scale
from Field import Field


Names = ["Base/Hull/General/Length",
         "Base/Hull/General/Width",

         "Base/Hull/Upper/Height",
         "Base/Hull/Upper/FrontGlacis",
         "Base/Hull/Upper/SideGlacis",
         "Base/Hull/Upper/RearGlacis",
         "Base/Hull/Upper/FrontOffset",
         "Base/Hull/Upper/RearOffset",

         "Base/Hull/Sponsons/Extrusion",
         "Base/Hull/Sponsons/Slant",
         "Base/Hull/Sponsons/FrontGlacis",
         "Base/Hull/Sponsons/RearGlacis",

         "Base/Hull/FrontStrip/Top",
         "Base/Hull/FrontStrip/Bottom",

         "Base/Hull/RearStrip/Top",
         "Base/Hull/RearStrip/Bottom",

         "Base/Hull/Lower/Height",
         "Base/Hull/Lower/FrontGlacis",
         "Base/Hull/Lower/SideGlacis",
         "Base/Hull/Lower/RearGlacis",


         "Base/Turret/Ring/Height",
         "Base/Turret/Ring/Diameter",

         "Base/Turret/Front/Angle",
         "Base/Turret/Front/Length",
         "Base/Turret/Front/Cheek",
         "Base/Turret/Front/Height",

         "Base/Turret/Mid/Length",
         "Base/Turret/Mid/Width",
         "Base/Turret/Mid/Height",
         "Base/Turret/Mid/Angle",

         "Base/Turret/Rear/Angle",
         "Base/Turret/Rear/Length",
         "Base/Turret/Rear/Cheek",
         "Base/Turret/Rear/Height",


         "Mobility/Tracks/Belt/TrackWidth",
         "Mobility/Tracks/Belt/Length",
         "Mobility/Tracks/Belt/Thickness",

         "Mobility/Tracks/Sprocket/Forward",
         "Mobility/Tracks/Sprocket/Height",
         "Mobility/Tracks/Sprocket/Diameter",

         "Mobility/Tracks/Idler/Forward",
         "Mobility/Tracks/Idler/Height",
         "Mobility/Tracks/Idler/Diameter",

         "Mobility/Tracks/RoadWheels/Forward",
         "Mobility/Tracks/RoadWheels/Height",
         "Mobility/Tracks/RoadWheels/Diameter",
         "Mobility/Tracks/RoadWheels/Spacing",

         "Mobility/Tracks/ReturnRollers/Forward",
         "Mobility/Tracks/ReturnRollers/Height",
         "Mobility/Tracks/ReturnRollers/Diameter",
         "Mobility/Tracks/ReturnRollers/Spacing"]


def scale_factor(length_old, length_new):
    factor = length_new / length_old
    return factor


print("SprocketCalc v.1.0")
print("------------------")

length = Value(1, 1)
height = Value(1, 1)
width = Value(1, 1)
print("PIXEL SIZE")
length.px = int(input(" - length: "))
height.px = int(input(" - height: "))
width.px = int(input(" - width: "))
print("------------------")
print("MILLIMETER SIZE")
length.mm = int(input(" - length: "))
height.mm = int(input(" - height: "))
width.mm = int(input(" - width: "))
print("------------------")
length_scale = scale_factor(length.px, length.mm)
height_scale = scale_factor(height.px, height.mm)
width_scale = scale_factor(width.px, width.mm)
scale = Scale(length_scale, height_scale, width_scale)
print(scale.length, scale.height, scale.width)

# Ask user to input length, width and height of vehicle's blueprints (in pixels)
# Ask user to input length, width and height of original vehicle (in mm)
# Based on collected data, scale factors in all axes are calculated
# Ask user about the length of various components of vehicle's blueprints (in pixels)
# Calculate length of those components in mm
# Generate "*.txt" or "*.csv" file containing all relevant data