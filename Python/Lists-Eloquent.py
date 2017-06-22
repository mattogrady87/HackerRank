n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":

        # Create a string with the list cmd given plus the arguments
        # seperated by commas and wrapped in parentheses.
        cmd += "("+ ",".join(args) + ")"

        # Eval lets a python program run python code within itself.
        eval("l."+cmd)

    else:
        print(l) 
