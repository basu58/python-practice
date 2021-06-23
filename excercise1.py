def func():
    while True:
        inp = input("Please enter a number:")
        try:
            x = int(inp)
            print(x)
        except:
            if(inp == "done"):
                print(inp)
                continue
            else:
                func()
func()
