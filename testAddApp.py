space = "\n"

appName = input("App name: ")
print("You are adding", appName)

appLink = input("App link: ")
print("You are adding", appLink)

print("Type a hex color value")
appColor = input("App color: ")
print("You are adding:", appColor)


def addAll():
    openMain = open("testMain.py", "r+")
    openMain.read()
    openMain.writelines(appName)
    openMain.writelines(space)
    openMain.writelines(appLink)
    openMain.writelines(space)
    openMain.writelines(appColor)
    openMain.read()
    print("Added app")


addAll()
