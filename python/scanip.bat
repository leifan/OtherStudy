@echo off&title ɨ��MAC,IP,�������&color a&mode con: cols=60 lines=22
setlocal enabledelayedexpansion
echo.
echo  ============== �����ߣ�http://www.nb99.net ===============
echo.
echo     ɨ������IP��MAC��ַ�ͼ�������������浽info.txt�ļ�
echo.
echo  ================== �������ף��뱣����Ȩ ==================
echo.
:: iqp -> ����IP��ǰ3λ��ip1 -> ��ʼip��ip2 -> ����ip
set ipq=192.168.1
set /a ip1=1
set /a ip2=255
set /a con=0
set /a contotal=%ip2%-%ip1%+1
echo      MAC                IP       ������� >info.txt
for /l %%i in (!ip1!,1,!ip2!) do (
        set ip=!ipq!.%%i
        echo ɨ��!ip!
        ping !ip! -n 1 -w 1 >nul
        if !errorlevel! equ 0 (
                for /f "tokens=1" %%j in ('nbtstat -a !ip! ^| find /i "UNIQUE" ^| find /i "00"') do set pcname=%%j
                for /f "tokens=4 delims=* " %%j in ('nbtstat -a !ip! ^| find /i "MAC Address"') do set mac=%%j
                echo !mac:~0,-1! !ip! !pcname! >>info.txt
                set /a con=!con!+1
        )
)
echo ��%con%����¼ >>info.txt
echo ��ɨ�裺%contotal%̨������ɨ�赽��%con%����Ч��¼&pause >nul