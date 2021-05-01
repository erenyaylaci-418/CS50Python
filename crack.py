# buda biter
import sys

dicry = {

"50GApilQSG3E2":"bjbrown",
"502sDZxA/ybHs":"emc",
"50C6B0oz0HWzo":"greg",
"50WUNAFdX/yjA":"jana",
"50n0AAUD.pL8g":"lloyd",
"50CcfIk1QrPr6":"malan",
"50JIIyhDORqMU":"natmelo",
"51v3Nh6ZWGHOQ":"rob",
"61v1CDwwP95bY":"veronica",
"508ny6Rw0aRio":"walker",
"50cI2vYkF0YU2":"zamyla"
}

hash = sys.argv[1]
#if len(sys.argv)  != 2:
    #print("Usage: ./crack hash")
if hash in dicry:
    x = dicry[hash]
    print(x)
else:
    print("Usage: ./crack hash")


