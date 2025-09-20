@echo off
set INPUT=docs\diagrams
set OUT=docs\diagrams\build
if not exist "%OUT%" mkdir "%OUT%"
for %%f in (%INPUT%\*.dot) do (
  echo Render %%f
  dot -Tpng "%%f" -o "%OUT%\%%~nf.png"
)
echo Hecho. Salida en %OUT%
pause