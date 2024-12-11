import rhinoscriptsyntax as rs

# Extrude the curve
start_point = rs.CurveStartPoint(curve)
end_point = rs.PointAdd(start_point, (0, 0, height))
extrusion = rs.ExtrudeCurveStraight(curve, start_point, end_point)
    
 # Scale the extrusion
centroid = rs.SurfaceAreaCentroid(extrusion)[0]
scaled_extrusion = rs.ScaleObject(extrusion, centroid, (scale_factor, scale_factor, scale_factor))

# offset the scaled extrusion
offset_extrusion = rs.OffsetSurface(scaled_extrusion, offset_distance, create_solid=True)
    
 # Convert to polysurface
polysurface = rs.coercebrep(offset_extrusion)