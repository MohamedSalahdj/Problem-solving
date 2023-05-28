"""
Consider a list (list = []). You can perform the following commands:

1.insert i e: Insert integer  at position .
2.print: Print the list.
3.remove e: Delete the first occurrence of integer .
4.append e: Insert integer  at the end of the list.
5.sort: Sort the list.
6.pop: Pop the last element from the list.
7.reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

link of problem : https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true


"""
if __name__ == '__main__':
    N = int(input()) 
    l = []
    for i in range(N):
        commands = input().split()
        if commands[0] =='insert':
            l.insert(int(commands[1]), int(commands[-1]))
        elif commands[0] == 'print':
            print(l)
        elif commands[0] == 'remove':
            l.remove(int(commands[1]))
        elif commands[0] == 'append':
            l.append(int(commands[1]))
        elif commands[0] == 'sort':
            l.sort()
        elif commands[0] == 'pop':
            l.pop()
        elif commands[0] == 'reverse':
            l.reverse()
        
        