' ExportEfficiency

Sub Main ()
	Dim Studio As Object

	Begin Dialog UserDialog 360,161,"Export Efficiency Sweep" ' %GRID:10,7,1,1
		Text 0,0,180,14,"Parameter",.LParameter
		Text 0,21,180,14,"From",.LFrom
		Text 0,42,180,14,"To",.LTo
		Text 0,63,180,14,"Step",.LStep
		Text 0,84,180,14,"Output dir",.LOutputdir
		Text 0,105,180,14,"AC (e.g. AC1, AC2, ...)",.LAc
		TextBox 180,0,180,21,.EParameter
		TextBox 180,21,180,21,.EFrom
		TextBox 180,42,180,21,.ETo
		TextBox 180,63,180,21,.EStep
		TextBox 180,84,180,21,.EOutputDir
		TextBox 180,105,180,21,.EAc
		OKButton 180,140,90,21
		CancelButton 270,140,90,21
	End Dialog
	Dim dlg As UserDialog
	Dialog dlg

	' Do parameter sweep. Save txt file for each iteration
	Dim ThisVal As Double
	For ThisVal = CDbl(dlg.EFrom) To CDbl(dlg.ETo)+0.01 STEP CDbl(dlg.EStep)
		StoreParameter(dlg.EParameter, ThisVal)
		DS.UpdateResults
		SelectTreeItem "1D Results\Efficiencies\System Tot. Efficiency [" + dlg.EAc + "]"
		ExportPlotData dlg.EOutputDir + "\" + CStr(ThisVal) + ".txt"
	Next
End Sub

