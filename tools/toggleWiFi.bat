@ECHO OFF

explorer ms-settings:network-wifi
ping -n 5 127.0.0.1 > nul

:VBSDynamicBuild
SET TempVBSFile=%tmp%\~tmpSendKeysTemp.vbs
IF EXIST "%TempVBSFile%" DEL /F /Q "%TempVBSFile%"
ECHO Set WshShell = WScript.CreateObject("WScript.Shell") >>"%TempVBSFile%"
ECHO Wscript.Sleep 100                                    >>"%TempVBSFile%"
ECHO WshShell.SendKeys " "                                >>"%TempVBSFile%"
ECHO Wscript.Sleep 100                                    >>"%TempVBSFile%"

CSCRIPT //nologo "%TempVBSFile%"
EXIT