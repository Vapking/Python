from collections import deque

def is_match(ch1,ch2):
    match_dict = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    return match_dict[ch1] == ch2

def is_balanced(string):
    stack = deque()
    for ch in string:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if len(stack) == 0:
                return False
            if not is_match(ch,stack.pop()):
                return False
    return len(stack) == 0

def main():
    string = input("Enter A Experssion : ")
    print(is_balanced(string))

if __name__ == '__main__':
    main()
    
