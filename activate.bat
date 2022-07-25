@echo off
title Windows10Activator

:: get if arguments were passed
If "%~1"=="" goto error11
if "%~2"=="" goto error12

set arg1 = %~1
set arg2 = %~2

if arg1 == Home set key = TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 && goto getServer
if arg1 == HomeN set key = 3KHY7-WNT83-DGQKR-F7HPR-844BM && goto getServer
if arg1 == HomeSingleLang set key = 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH && goto getServer
if arg1 == HomeCountrySpec set key = PVMJN-6DFY6–9CCP6–7BKTT-D3WVR && goto getServer
if arg1 == Proffesional set key = W269N-WFGWX-YVC9B-4J6C9-T83GX && goto getServer
if arg1 == ProffesionalN set key = MH37W-N47XK-V7XM9-C7227-GCQG9 && goto getServer
if arg1 == Education set key = NW6C2-QMPVW-D7KKK-3GKT6-VCFB2 && goto getServer
if arg1 == EducationN set key = 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ && goto getServer
if arg1 == Enterprise set key = NPPR9-FWDCX-D2C8J-H872K-2YT43 && goto getServer
if arg1 == EnterpriseN set key = DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 && goto getServer
goto error20

:getServer
if arg2 == xspace set server = kms.xpsace.in && goto finish
if arg2 == msguides set server = kms8.msguides.com && goto finish
goto error30

:finish
echo  ACTIVATING WINDOWS
echo --------------------
echo Installing product key..
slmgr /ipk %key%
echo Product key installed!
timeout /t 1 >nul
echo Setting KMS machine..
slmgr /skms %server%
echo KMS machine set!
timeout /t 1 >nul
echo Activating Windows..
slmgr /ato
echo Done!
echo --------------------
echo.
echo Windows activation complete!
echo If failed, please check settings and try again.
echo.
echo PRESS ANY KEY TO EXIT
pause >nul
exit

:error11
echo ------ ERROR 11 -------
echo Invalid argument or no argument at position 1.
echo Press any key to exit.
echo -----------------------
pause >nul
exit

:error12
echo ------ ERROR 12 -------
echo Invalid argument or no argument at position 2.
echo Press any key to exit.
echo -----------------------
pause >nul
exit

:error20
echo ------ ERROR 20 -------
echo Argument 1 invalid, the provided OS name is not available.
echo Please check your settings and try again, if this error persists
echo contact developers for more information.
echo Press any key to exit.
echo -----------------------
pause >nul
exit

:error30
echo ------ ERROR 11 -------
echo Argument 2 invalid, the provided kms machine name is not valid.
echo Please check your settings and try again, if this error persists
echo contact developers for more information
echo Press any key to exit.
echo -----------------------
pause >nul
exit