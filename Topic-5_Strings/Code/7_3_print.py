def sayHello(names):
    for i in range(len(names)):
        # print(f"Hello, {names[i]}")
        words =  "Hello, " + names[i] 
        print(words)
    
names = ['Mark', 'Peter', 'John']
sayHello(names)