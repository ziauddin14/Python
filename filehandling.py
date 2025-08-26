# Step 1: File kholo aur likho
file = open("meri_file.txt", "w")   # "w" matlab write
file.write("Hello! Yeh meri pehli file hai.\n")
file.write("Main Python seekh raha hoon.\n")
file.write("File handling bahut interesting hai!\n")        
file.close()
# print("File likh di gayi ✅")

# Step 2: File padho
file = open("meri_file.txt", "r")   # "r" matlab read
content = file.read()
# print("File ka content:\n", content)
file.close()

# Step 3: File ko line by line padho
file = open("meri_file.txt", "r")   # "r" matlab read
for line in file:
    print(line.strip())  # strip() se newline characters hata diye
file.close()

#  "with" se file automatically close ho jayegi
with open("meri_file.txt", "r") as file:  
    data = file.read()

print("Ab file ka pura content hai:")
print(data)

# Step 4: File ko append karo
with open("meri_file.txt", "a") as file:  # "a" matlab append
    file.write("\nYeh naya line hai jo append kiya gaya hai.\n")
print("File ko append kar diya gaya ✅")

