COLOUR_CODE = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "ANTIQUEWHITE1": "#ffefdb",
               "ANTIQUEWHITE2": "#eedfcc", "ANTIQUEWHITE3": "#cdc0b0", "ANTIQUEWHITE4": "#8b8378",
               "AQUAMARINE1": "#7fffd4", "AQUAMARINE2": "#76eec6", "AQUAMARINE4": "	#458b74", "AZUREL":"#f0ffff"}
code = input("Enter a colour:").upper()
while code != "":
    if code in COLOUR_CODE:
        print(code, "is", COLOUR_CODE[code])
    else:
        print("Invalid colour")
    code = input("Enter a colour:").upper()