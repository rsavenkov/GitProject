import subprocess

code = subprocess.call("notepad.exe")
# code = subprocess.call(["notepad.exe", "C:/Users/Ruslan/PycharmProjects/GitProject/trunk/rsavenkov/multithreading/my_subprocess.py"])
print('return code:', code)

args = ["ping", "www.yahoo.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
print(data)