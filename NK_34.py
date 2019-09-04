def main():
    n = int(input().strip())
    for i in range(n):
        input_str = input().strip()
        if i == n-1:
            try:
                exec(input_str)
                value_content = input_str.split("=")
                exec("print({})".format(value_content[0]).strip())
            except:
                print("NA")
        else:
            exec(input_str)
main()
