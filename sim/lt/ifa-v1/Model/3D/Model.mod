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


