import pyautogui , time
print("Copy paste the code")
l = list()
while True:
    a = input()
    if a.casefold() == "sahith":
        break
    else:
        l.append(a)
print("Open the window and select textbox in 5 seconds")
time.sleep(5)
for i in l:
    pyautogui.typewrite(i)
    pyautogui.press("enter")
    pyautogui.press("home")
print("done")
