@echo off
set /p  fileName=Enter name here : 
echo def function(): >> %fileName%
echo 	pass>>%fileName%
echo if __name__ == "__main__": >> %fileName%
echo    print(function())>>%fileName%


