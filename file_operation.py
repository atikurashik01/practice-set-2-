file1 = open("notebook.txt","r")
content = file1.read()
print(content)
file1.close()


file2 = open("notebook.txt","a")
file2.write("\nthis is second line ")
file2.close()