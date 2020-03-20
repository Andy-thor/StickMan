Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
scriptdir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
WinScriptHost.Run Chr(34) & scriptdir + "\run.cmd" & Chr(34), 0
Set WinScriptHost = Nothing
