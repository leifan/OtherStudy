@echo off&title 扫描MAC,IP,计算机名&color a&mode con: cols=60 lines=22
setlocal enabledelayedexpansion
echo.
echo  ============== 制作者：http://www.nb99.net ===============
echo.
echo     扫描内网IP、MAC地址和计算机名，并保存到info.txt文件
echo.
echo  ================== 制作不易，请保留版权 ==================
echo.
:: iqp -> 内网IP的前3位，ip1 -> 起始ip，ip2 -> 结束ip
set ipq=192.168.1
set /a ip1=1
set /a ip2=255
set /a con=0
set /a contotal=%ip2%-%ip1%+1
echo      MAC                IP       计算机名 >info.txt
for /l %%i in (!ip1!,1,!ip2!) do (
        set ip=!ipq!.%%i
        echo 扫描!ip!
        ping !ip! -n 1 -w 1 >nul
        if !errorlevel! equ 0 (
                for /f "tokens=1" %%j in ('nbtstat -a !ip! ^| find /i "UNIQUE" ^| find /i "00"') do set pcname=%%j
                for /f "tokens=4 delims=* " %%j in ('nbtstat -a !ip! ^| find /i "MAC Address"') do set mac=%%j
                echo !mac:~0,-1! !ip! !pcname! >>info.txt
                set /a con=!con!+1
        )
)
echo 共%con%条记录 >>info.txt
echo 共扫描：%contotal%台机器，扫描到：%con%个有效记录&pause >nul