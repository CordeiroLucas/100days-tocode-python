# Control Flow and Logical Operators

print("__________________, \\n",
"ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\\n",       
"                /\  ______________ \\\n",
"               /::\ \ZZZZZZZZZZZZ/\ \\\n",
"              /:/\.\ \        /:/\:\ \\\n",
"             /:/Z/\:\ \      /:/Z/\:\ \\\n",
"            /:/Z/__\:\ \____/:/Z/  \:\ \\\n",
"           /:/Z/____\:\ \___\/Z/    \:\ \\\n",
"           \:\ \ZZZZZ\:\ \ZZ/\ \     \:\ \\\n",
"            \:\ \     \:\ \ \:\ \     \:\ \\\n",
"             \:\ \     \:\ \_\;\_\_____\;\ \\\n",
"              \:\ \     \:\_________________\\\n",
"               \:\ \    /:/ZZZZZZZZZZZZZZZZZ/\\\n",
"                \:\ \  /:/Z/    \:\ \  /:/Z/\\\n",
"                 \:\ \/:/Z/      \:\ \/:/Z/\\\n",
"                  \:\/:/Z/________\;\/:/Z/\\\n",
"                   \::/Z/_______itz__\/Z/\\\n",
"                    \/ZZZZZZZZZZZZZZZZZ/\\\n",
"ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\n")

print("Welcome to Treasure Island.\nYour Mission is to find the Treasure.")

print("You're at a cross road. Where do you want\' to go?\n")
choiceRoad = input("Type \"left\" or \"right\"\n").lower()

if (choiceRoad == "left"):
    print("You\'ve come to a lake. There is an animal island in the middle of the Lake.")
    choiceLake = input("\t\tType \"wait\" to wait for a boat. Type \"sim\" o swim across\n").lower()
    if choiceLake == "wait":
        choiceDoor = input("On wich door? Red, Blue or Yellow?\n").lower()
        if choiceDoor == "yellow":
            print("You Win")
        else:
            print("Game Over")
else:
    print("Game Over!")

