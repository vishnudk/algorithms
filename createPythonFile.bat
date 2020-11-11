@echo off
set /p  fileName=Enter name here : 
echo def function(): >> %fileName%.py
echo 	pass>>%fileName%.py
echo if __name__ == "__main__": >> %fileName%.py
echo    print(function())>>%fileName%.py


