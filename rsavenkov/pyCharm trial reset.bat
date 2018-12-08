cd "C:\Users\Ruslan\.PyCharm*\config"
rmdir "eval" /s /q
del "options\options.xml"
reg delete "HKEY_CURRENT_USER\Software\JavaSoft\Prefs\jetbrains\pycharm" /f
