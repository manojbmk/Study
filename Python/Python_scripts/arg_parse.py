import argparse

if __name__ == '__main__':
    #Initialize the parser
    parser = argparse.ArgumentParser(
        description="My Math script"
    )
    #Add the parameters positional/optional
    parser.add_argument("num1",help="Number 1",type=float)
    parser.add_argument("num2",help="Number 2",type=float)
    parser.add_argument('--operation',help="provide operator",default='+')

    #parse the arguments
    args = parser.parse_args()
    #print(args)

    if args.operation == "+":
        print(args.num1 + args.num2)
    elif args.operation == "-":
        print(args.num1 - args.num2)
    elif args.operation == "**":
        print(args.num1 ** args.num2)
    else:
        print("Please enter a valid operation")