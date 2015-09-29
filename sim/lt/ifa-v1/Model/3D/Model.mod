'# MWS Version: Version 2014.5 - Oct 10 2014 - ACIS 23.0.0 -

'# length = mm
'# frequency = GHz
'# time = ns
'# frequency range: fmin = 0 fmax = 3
'# created = '[VERSION]2014.5|23.0.0|20141010[/VERSION]


'@ use template: P9 - PIFA - Mockup

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
'set the units
With Units
    .Geometry "mm"
    .Frequency "GHz"
    .Voltage "V"
    .Resistance "Ohm"
    .Inductance "NanoH"
    .TemperatureUnit  "Celsius"
    .Time "ns"
    .Current "A"
    .Conductance "Siemens"
    .Capacitance "PikoF"
End With
ThermalSolver.AmbientTemperature "0"
'----------------------------------------------------------------------------
Plot.DrawBox True
With Background
     .Type "Normal"
     .Epsilon "1.0"
     .Mue "1.0"
     .XminSpace "0.0"
     .XmaxSpace "0.0"
     .YminSpace "0.0"
     .YmaxSpace "0.0"
     .ZminSpace "0.0"
     .ZmaxSpace "0.0"
End With
With Boundary
     .Xmin "expanded open"
     .Xmax "expanded open"
     .Ymin "expanded open"
     .Ymax "expanded open"
     .Zmin "expanded open"
     .Zmax "expanded open"
     .Xsymmetry "none"
     .Ysymmetry "none"
     .Zsymmetry "none"
End With
' optimize mesh settings for planar structures
With Mesh
     .MergeThinPECLayerFixpoints "True"
     .RatioLimit "20"
     .FPBAAvoidNonRegUnite "True"
     .ConsiderSpaceForLowerMeshLimit "False"
     .MinimumStepNumber "5"
     .AutoMeshNumberOfShapeFaces "300"
End With
With MeshSettings
     .SetMeshType "Hex"
     .Set "RatioLimitGeometry", "20"
End With
With MeshSettings
     .SetMeshType "HexTLM"
     .Set "RatioLimitGeometry", "20"
End With
' change mesh adaption scheme to energy
' 		(planar structures tend to store high energy
'     	 locally at edges rather than globally in volume)
MeshAdaption3D.SetAdaptionStrategy "Energy"
' switch on FD-TET setting for accurate farfields
FDSolver.ExtrudeOpenBC "True"
Solver.PrepareFarfields "False"
PostProcess1D.ActivateOperation "vswr", "true"
PostProcess1D.ActivateOperation "yz-matrices", "true"
'----------------------------------------------------------------------------
'set the frequency range
Solver.FrequencyRange "0", "3"
'----------------------------------------------------------------------------
With MeshSettings
     .SetMeshType "Hex"
     .Set "Version", 1%
End With
With Mesh
     .MeshType "PBA"
End With
'set the solver type
ChangeSolverType("HF Time Domain")

'@ activate local coordinates

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
WCS.ActivateWCS "local"

'@ define material: Copper (annealed)

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Material
     .Reset
     .Name "Copper (annealed)"
     .Folder ""
.FrqType "static" 
.Type "Normal" 
.SetMaterialUnit "Hz", "mm" 
.Epsilon "1" 
.Mue "1.0" 
.Kappa "5.8e+007" 
.TanD "0.0" 
.TanDFreq "0.0" 
.TanDGiven "False" 
.TanDModel "ConstTanD" 
.KappaM "0" 
.TanDM "0.0" 
.TanDMFreq "0.0" 
.TanDMGiven "False" 
.TanDMModel "ConstTanD" 
.DispModelEps "None" 
.DispModelMue "None" 
.DispersiveFittingSchemeEps "1st Order" 
.DispersiveFittingSchemeMue "1st Order" 
.UseGeneralDispersionEps "False" 
.UseGeneralDispersionMue "False" 
.FrqType "all" 
.Type "Lossy metal" 
.SetMaterialUnit "GHz", "mm" 
.Mue "1.0" 
.Kappa "5.8e+007" 
.Rho "8930.0" 
.ThermalType "Normal" 
.ThermalConductivity "401.0" 
.HeatCapacity "0.39" 
.MetabolicRate "0" 
.BloodFlow "0" 
.VoxelConvection "0" 
.MechanicsType "Isotropic" 
.YoungsModulus "120" 
.PoissonsRatio "0.33" 
.ThermalExpansionRate "17" 
.Colour "1", "1", "0" 
.Wireframe "False" 
.Reflection "False" 
.Allowoutline "True" 
.Transparentoutline "False" 
.Transparency "0" 
.Create
End With

'@ new component: component1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Component.New "component1"

'@ define brick: component1:solid1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "solid1" 
     .Component "component1" 
     .Material "Copper (annealed)" 
     .Xrange "0", "PCBW" 
     .Yrange "0", "PCBL" 
     .Zrange "0", "PCBH" 
     .Create
End With

'@ define material: FR-4 (lossy)

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Material
     .Reset
     .Name "FR-4 (lossy)"
     .Folder ""
.FrqType "all" 
.Type "Normal" 
.SetMaterialUnit "GHz", "mm"
.Epsilon "4.3" 
.Mue "1.0" 
.Kappa "0.0" 
.TanD "0.025" 
.TanDFreq "10.0" 
.TanDGiven "True" 
.TanDModel "ConstTanD" 
.KappaM "0.0" 
.TanDM "0.0" 
.TanDMFreq "0.0" 
.TanDMGiven "False" 
.TanDMModel "ConstKappa" 
.DispModelEps "None" 
.DispModelMue "None" 
.DispersiveFittingSchemeEps "General 1st" 
.DispersiveFittingSchemeMue "General 1st" 
.UseGeneralDispersionEps "False" 
.UseGeneralDispersionMue "False" 
.Rho "0.0" 
.ThermalType "Normal" 
.ThermalConductivity "0.3" 
.SetActiveMaterial "all" 
.Colour "0.94", "0.82", "0.76" 
.Wireframe "False" 
.Transparency "0" 
.Create
End With

'@ change material: component1:solid1 to: FR-4 (lossy)

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Solid.ChangeMaterial "component1:solid1", "FR-4 (lossy)"

'@ define brick: component1:Cobber_top

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "Cobber_top" 
     .Component "component1" 
     .Material "Copper (annealed)" 
     .Xrange "0", "PCBW" 
     .Yrange "0", "PCBL" 
     .Zrange "PCBH", "PCBH+Cobber_t" 
     .Create
End With

'@ rename block: component1:solid1 to: component1:FR4

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Solid.Rename "component1:solid1", "FR4"

'@ rename component: component1 to: PCB

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Component.Rename "component1", "PCB"

'@ define brick: PCB:Cobber_btn

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "Cobber_btn" 
     .Component "PCB" 
     .Material "Copper (annealed)" 
     .Xrange "0", "PCBL" 
     .Yrange "0", "PCBW" 
     .Zrange "0", "Cobber_t" 
     .Create
End With

'@ delete shape: PCB:Cobber_btn

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Solid.Delete "PCB:Cobber_btn"

'@ activate global coordinates

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
WCS.ActivateWCS "global"

'@ activate local coordinates

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
WCS.ActivateWCS "local"

'@ define brick: PCB:solid1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "solid1" 
     .Component "PCB" 
     .Material "Copper (annealed)" 
     .Xrange "0", "PCBW" 
     .Yrange "0", "PCBL" 
     .Zrange "0", "Cobber_t" 
     .Create
End With

'@ rename block: PCB:solid1 to: PCB:Cobber_btn

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Solid.Rename "PCB:solid1", "Cobber_btn"

'@ new component: monopole

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Component.New "monopole" 

'@ define brick: monopole:solid1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "solid1" 
     .Component "monopole" 
     .Material "Copper (annealed)" 
     .Xrange "(PCBW/2)-(monoL_1/2)", "(PCBW/2)+monoL_1/2" 
     .Yrange "gph1", "gph2" 
     .Zrange "PCBH+Cobber_t", "PCBH+Cobber_t-0.1" 
     .Create
End With


'@ define brick: monopole:width1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "width1" 
     .Component "monopole" 
     .Material "Copper (annealed)" 
     .Xrange "PCBW/2+monoL_1/2-0.1", "PCBW/2+monoL_1/2" 
     .Yrange "gph1", "gph2" 
     .Zrange "PCBH+Cobber_t", "PCBH+Cobber_t-monoW_2" 
     .Create
End With


'@ define brick: monopole:width2

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "width2" 
     .Component "monopole" 
     .Material "Copper (annealed)" 
     .Xrange "PCBW/2+monoL_1/2", "PCBW/2-monoL_1/2" 
     .Yrange "gph1", "gph2" 
     .Zrange "PCBH+Cobber_t-monoW_2", "PCBH+Cobber_t-monoW_2+0.1" 
     .Create
End With


'@ rename block: monopole:width2 to: monopole:length2

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Solid.Rename "monopole:width2", "length2"


'@ rename block: monopole:solid1 to: monopole:length1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Solid.Rename "monopole:solid1", "length1"


'@ define brick: monopole:width2

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "width2" 
     .Component "monopole" 
     .Material "Copper (annealed)" 
     .Xrange "PCBW/2-monoL_1/2", "PCBW/2-monoL_1/2+0.1" 
     .Yrange "gph1", "gph2" 
     .Zrange "PCBH+Cobber_t-monoW_2+0.1", "PCBH+Cobber_t-monoW_2-monoW_2" 
     .Create
End With


'@ define brick: monopole:length3

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "length3" 
     .Component "monopole" 
     .Material "Copper (annealed)" 
     .Xrange "PCBW/2-monoL_1/2", "PCBW/2-monoL_1/2+monoL_2" 
     .Yrange "gph1", "gph2" 
     .Zrange "PCBH+Cobber_t-2*monoW_2", "PCBH+Cobber_t-2*monoW_2+0.1" 
     .Create
End With


'@ clear picks

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Pick.ClearAllPicks 


'@ pick point

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Pick.PickPointFromCoordinates "13.380401258874", "0.029884953286811", "1.534"


'@ pick mid point

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Pick.PickMidpointFromId "monopole:length1", "11" 


'@ define discrete port: 1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With DiscretePort 
     .Reset 
     .PortNumber "1" 
     .Type "SParameter" 
     .Label "" 
     .Impedance "50.0" 
     .VoltagePortImpedance "0.0" 
     .Voltage "1.0" 
     .Current "1.0" 
     .SetP1 "True", "13.380401258874", "0.029884953286811", "1.534" 
     .SetP2 "True", "13.375", "-1.5", "1.484" 
     .InvertDirection "False" 
     .LocalCoordinates "True" 
     .Monitor "True" 
     .Radius "0.0" 
     .Wire "" 
     .Position "end1" 
     .Create 
End With


'@ define monitor: e-field (f=0.5)

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Monitor 
     .Reset 
     .Name "e-field (f=0.5)" 
     .Dimension "Volume" 
     .Domain "Frequency" 
     .FieldType "Efield" 
     .Frequency "0.5" 
     .UseSubvolume "False" 
     .SetSubvolume  "-49.965409666667",  "104.96540966667",  "-51.965409666667",  "169.96540966667",  "-51.431409666667",  "51.499409666667" 
     .Create 
End With 


'@ define farfield monitor: farfield (f=0.5)

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Monitor 
     .Reset 
     .Name "farfield (f=0.5)" 
     .Domain "Frequency" 
     .FieldType "Farfield" 
     .Frequency "0.5" 
     .UseSubvolume "False" 
     .ExportFarfieldSource "False" 
     .SetSubvolume  "-49.965409666667",  "104.96540966667",  "-51.965409666667",  "169.96540966667",  "-51.431409666667",  "51.499409666667" 
     .Create 
End With 


'@ set mesh properties (Hexahedral)

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Mesh 
     .MeshType "PBA" 
     .SetCreator "High Frequency"
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "Version", 1%
     'MAX CELL - WAVELENGTH REFINEMENT 
     .Set "StepsPerWaveNear", "20" 
     .Set "StepsPerWaveFar", "20" 
     .Set "WavelengthRefinementSameAsNear", "1" 
     'MAX CELL - GEOMETRY REFINEMENT 
     .Set "StepsPerBoxNear", "10" 
     .Set "StepsPerBoxFar", "1" 
     .Set "MaxStepNear", "0" 
     .Set "MaxStepFar", "0" 
     .Set "ModelBoxDescrNear", "maxedge" 
     .Set "ModelBoxDescrFar", "maxedge" 
     .Set "UseMaxStepAbsolute", "0" 
     .Set "GeometryRefinementSameAsNear", "0" 
     'MIN CELL 
     .Set "UseRatioLimitGeometry", "1" 
     .Set "RatioLimitGeometry", "20" 
     .Set "MinStepGeometryX", "0" 
     .Set "MinStepGeometryY", "0" 
     .Set "MinStepGeometryZ", "0" 
     .Set "UseSameMinStepGeometryXYZ", "1" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "FaceRefinementOn", "0" 
     .Set "FaceRefinementPolicy", "2" 
     .Set "FaceRefinementRatio", "2" 
     .Set "FaceRefinementStep", "0" 
     .Set "FaceRefinementNSteps", "2" 
     .Set "EllipseRefinementOn", "0" 
     .Set "EllipseRefinementPolicy", "2" 
     .Set "EllipseRefinementRatio", "2" 
     .Set "EllipseRefinementStep", "0" 
     .Set "EllipseRefinementNSteps", "2" 
     .Set "FaceRefinementBufferLines", "3" 
     .Set "EdgeRefinementOn", "1" 
     .Set "EdgeRefinementPolicy", "1" 
     .Set "EdgeRefinementRatio", "2" 
     .Set "EdgeRefinementStep", "0" 
     .Set "EdgeRefinementBufferLines", "3" 
     .Set "RefineEdgeMaterialGlobal", "0" 
     .Set "RefineAxialEdgeGlobal", "0" 
     .Set "BufferLinesNear", "3" 
     .Set "UseDielectrics", "1" 
     .Set "EquilibrateOn", "0" 
     .Set "Equilibrate", "1.5" 
     .Set "IgnoreThinPanelMaterial", "0" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "SnapToAxialEdges", "1"
     .Set "SnapToPlanes", "1"
     .Set "SnapToSpheres", "1"
     .Set "SnapToEllipses", "1"
     .Set "SnapToCylinders", "1"
     .Set "SnapToCylinderCenters", "1"
     .Set "SnapToEllipseCenters", "1"
End With 
With Discretizer 
     .MeshType "PBA" 
     .PBAType "Fast PBA" 
     .AutomaticPBAType "True" 
     .FPBAAccuracyEnhancement "enable"
     .ConnectivityCheck "False"
     .ConvertGeometryDataAfterMeshing "True" 
     .UsePecEdgeModel "True" 
     .GapDetection "False" 
     .FPBAGapTolerance "1e-3" 
     .SetMaxParallelMesherThreads "Hex", "12"
     .SetParallelMesherMode "Hex", "Maximum"
     .PointAccEnhancement "0" 
     .UseSplitComponents "True" 
     .EnableSubgridding "False" 
     .PBAFillLimit "99" 
     .AlwaysExcludePec "False" 
End With 


'@ define time domain solver parameters

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Mesh.SetCreator "High Frequency" 

With Solver 
     .Method "Hexahedral"
     .CalculationType "TD-S"
     .StimulationPort "All"
     .StimulationMode "All"
     .SteadyStateLimit "-30.0"
     .MeshAdaption "False"
     .AutoNormImpedance "False"
     .NormingImpedance "50"
     .CalculateModesOnly "False"
     .SParaSymmetry "False"
     .StoreTDResultsInCache  "False"
     .FullDeembedding "False"
     .SuperimposePLWExcitation "False"
     .UseSensitivityAnalysis "False"
End With


'@ delete port: port1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Port.Delete "1" 


'@ define brick: monopole:solid1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Brick
     .Reset 
     .Name "solid1" 
     .Component "monopole" 
     .Material "Copper (annealed)" 
     .Xrange "PCBW/2-monoL_1/2", "PCBW/2-monoL_1/2+0.5" 
     .Yrange "gph2", "-0.3" 
     .Zrange "PCBH+Cobber_t", "PCBH+Cobber_t-0.1" 
     .Create
End With


'@ pick mid point

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Pick.PickMidpointFromId "monopole:solid1", "2" 


'@ pick point

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
Pick.PickPointFromCoordinates "13.630635828887", "0.0018751199224931", "1.534"


'@ define discrete port: 1

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With DiscretePort 
     .Reset 
     .PortNumber "1" 
     .Type "SParameter" 
     .Label "" 
     .Impedance "50.0" 
     .VoltagePortImpedance "0.0" 
     .Voltage "1.0" 
     .Current "1.0" 
     .SetP1 "True", "13.625", "-0.3", "1.634" 
     .SetP2 "True", "13.630635828887", "0.0018751199224931", "1.534" 
     .InvertDirection "True" 
     .LocalCoordinates "True" 
     .Monitor "True" 
     .Radius "0.0" 
     .Wire "" 
     .Position "end1" 
     .Create 
End With


'@ set mesh properties (Hexahedral)

'[VERSION]2014.5|23.0.0|20141010[/VERSION]
With Mesh 
     .MeshType "PBA" 
     .SetCreator "High Frequency"
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "Version", 1%
     'MAX CELL - WAVELENGTH REFINEMENT 
     .Set "StepsPerWaveNear", "20" 
     .Set "StepsPerWaveFar", "20" 
     .Set "WavelengthRefinementSameAsNear", "1" 
     'MAX CELL - GEOMETRY REFINEMENT 
     .Set "StepsPerBoxNear", "10" 
     .Set "StepsPerBoxFar", "1" 
     .Set "MaxStepNear", "0" 
     .Set "MaxStepFar", "0" 
     .Set "ModelBoxDescrNear", "maxedge" 
     .Set "ModelBoxDescrFar", "maxedge" 
     .Set "UseMaxStepAbsolute", "0" 
     .Set "GeometryRefinementSameAsNear", "0" 
     'MIN CELL 
     .Set "UseRatioLimitGeometry", "1" 
     .Set "RatioLimitGeometry", "20" 
     .Set "MinStepGeometryX", "0" 
     .Set "MinStepGeometryY", "0" 
     .Set "MinStepGeometryZ", "0" 
     .Set "UseSameMinStepGeometryXYZ", "1" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "FaceRefinementOn", "0" 
     .Set "FaceRefinementPolicy", "2" 
     .Set "FaceRefinementRatio", "2" 
     .Set "FaceRefinementStep", "0" 
     .Set "FaceRefinementNSteps", "2" 
     .Set "EllipseRefinementOn", "0" 
     .Set "EllipseRefinementPolicy", "2" 
     .Set "EllipseRefinementRatio", "2" 
     .Set "EllipseRefinementStep", "0" 
     .Set "EllipseRefinementNSteps", "2" 
     .Set "FaceRefinementBufferLines", "3" 
     .Set "EdgeRefinementOn", "1" 
     .Set "EdgeRefinementPolicy", "1" 
     .Set "EdgeRefinementRatio", "2" 
     .Set "EdgeRefinementStep", "0" 
     .Set "EdgeRefinementBufferLines", "3" 
     .Set "RefineEdgeMaterialGlobal", "0" 
     .Set "RefineAxialEdgeGlobal", "0" 
     .Set "BufferLinesNear", "3" 
     .Set "UseDielectrics", "1" 
     .Set "EquilibrateOn", "0" 
     .Set "Equilibrate", "1.5" 
     .Set "IgnoreThinPanelMaterial", "0" 
End With 
With MeshSettings 
     .SetMeshType "Hex" 
     .Set "SnapToAxialEdges", "1"
     .Set "SnapToPlanes", "1"
     .Set "SnapToSpheres", "1"
     .Set "SnapToEllipses", "1"
     .Set "SnapToCylinders", "1"
     .Set "SnapToCylinderCenters", "1"
     .Set "SnapToEllipseCenters", "1"
End With 
With Discretizer 
     .MeshType "PBA" 
     .PBAType "Fast PBA" 
     .AutomaticPBAType "True" 
     .FPBAAccuracyEnhancement "enable"
     .ConnectivityCheck "False"
     .ConvertGeometryDataAfterMeshing "True" 
     .UsePecEdgeModel "True" 
     .GapDetection "False" 
     .FPBAGapTolerance "1e-3" 
     .SetMaxParallelMesherThreads "Hex", "12"
     .SetParallelMesherMode "Hex", "Maximum"
     .PointAccEnhancement "0" 
     .UseSplitComponents "True" 
     .EnableSubgridding "False" 
     .PBAFillLimit "99" 
     .AlwaysExcludePec "False" 
End With 


