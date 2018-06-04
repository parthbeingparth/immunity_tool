$AppLocation = "D:\client\pkgs\ClientF\abc_w.pyw"
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$Home\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\abc_w.lnk")
$Shortcut.TargetPath = $AppLocation
$Shortcut.WorkingDirectory ="D:\client\pkgs\ClientF"
$Shortcut.Save()