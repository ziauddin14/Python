#****************Exception Handling***********
'''try  block contain the risky code and 
except block containes the code that neeeds to be run when try block code crashes'''
'''
Syntax Error - Before execution- Fix code manually
Runtime Error -(exception)- During execution - use try-except
Logical Error - After execution(wrong result) - debug / test logic
'''
try:
    num = int(input("ENter number: "))
    result = 100 / num
    print("Result : ", result)
except:
    print("something went wrong!")


'''
Most Common Error Types in Python:
"ValueError"
TypeError"
ZeroDivisionError"
NameError"
IndexError
KeyError"
FileNotFoundError"
PermissionError"
ImportError"
ModuleNotFoundError"
AttributeError"
RuntimeError"
MemoryError"
RecursionError"
AssertionError"
IndentationError"
SyntaxError"
OverflowError"
UnicodeError"
'''
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result of division is: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

finally:
    print("Execution of the try-except-finally block is complete.")


try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be a negative number.")
    print(f"Your age is: {age}")
except ValueError as e:
    print(f"Error: {e}")
    
try:
    userName = input("Enter your name: ")
    if len(userName) < 4:
        raise ValueError("User name must contanin 6 letters:")
    else:
        print("Welcome", userName)
except ValueError as e:
    print(e)
    
    
    
def error_menu():
    print("\n🔹 Error Testing Menu 🔹")
    print("1. ValueError")
    print("2. TypeError")
    print("3. ZeroDivisionError")
    print("4. NameError")
    print("5. IndexError")
    print("6. KeyError")
    print("7. FileNotFoundError")
    print("8. PermissionError")
    print("9. ImportError")
    print("10. ModuleNotFoundError")
    print("11. AttributeError")
    print("12. RuntimeError")
    print("13. MemoryError")
    print("14. RecursionError")
    print("15. AssertionError")
    print("16. IndentationError")
    print("17. SyntaxError")
    print("18. OverflowError")
    print("19. UnicodeError")
    print("0. Exit Program")

while True:
    error_menu()
    choice = input("\n Enter your choice: ")

    try:
        if choice == "1":
            num = int("abc")  # ValueError
        elif choice == "2":
            result = "abc" + 5  # TypeError
        elif choice == "3":
            result = 10 / 0  # ZeroDivisionError
        elif choice == "4":
            print(x)  # NameError
        elif choice == "5":
            mylist = [1, 2, 3]
            print(mylist[5])  # IndexError
        elif choice == "6":
            mydict = {"a": 1}
            print(mydict["b"])  # KeyError
        elif choice == "7":
            f = open("abc.txt")  # FileNotFoundError
        elif choice == "8":
            import os
            os.chmod("test.txt", 0o444)  # read-only banane ki koshish
            with open("test.txt", "w") as f:  # likhne ki koshish (PermissionError)
                f.write("hello")
        elif choice == "9":
            import kuchnahi  # ImportError
        elif choice == "10":
            import abcdefg  # ModuleNotFoundError
        elif choice == "11":
            text = "abc"
            text.push("x")  # AttributeError
        elif choice == "12":
            raise RuntimeError("Kuch runtime galti ho gayi")  # RuntimeError
        elif choice == "13":
            a = "a" * (10**10) * (10**10)  # MemoryError (ho sakta hai crash ho)
        elif choice == "14":
            def recurse():
                return recurse()
            recurse()  # RecursionError
        elif choice == "15":
            assert 2 + 2 == 5  # AssertionError
        elif choice == "16":
            # IndentationError ko runtime pe trigger karna mushkil hai
            print("IndentationError tab hota hai jab code ki spacing galat ho.")
        elif choice == "17":
            # SyntaxError bhi runtime pe trigger nahi hota, isliye explain karenge
            print(" SyntaxError tab hota hai jab Python ka grammar galat likha ho (jaise 'if True print(\"hi\")').")
        elif choice == "18":
            import math
            print(math.exp(1000))  # OverflowError (very large number)
        elif choice == "19":
            "abc".encode("utf-8").decode("ascii")  # UnicodeError
        elif choice == "0":
            print("Program se bahar nikal gaye. Bye!")
            break
        else:
            print("Invalid choice! Sahi number dalo.")

    except ValueError:
        print("\n ValueError → Jab galat value ko convert karne ki koshish karo. Example: int('abc')")

    except TypeError:
        print("\n TypeError → Jab galat type ka data sath me use karo. Example: 'abc' + 5")

    except ZeroDivisionError:
        print("\n ZeroDivisionError → Jab number ko 0 se divide karo. Example: 10/0")

    except NameError:
        print("\n NameError → Jab variable define hi nahi hai. Example: print(x)")

    except IndexError:
        print("\n IndexError → Jab list ke bahar index maango. Example: [1,2,3][5]")

    except KeyError:
        print("\n KeyError → Jab dictionary me galat key use karo. Example: {'a':1}['b']")

    except FileNotFoundError:
        print("\n FileNotFoundError → Jab file exist hi nahi karti. Example: open('abc.txt')")

    except PermissionError:
        print("\n PermissionError → Jab file ya resource access karne ka right nahi hai.")

    except ImportError:
        print("\n ImportError → Jab module import karne me problem ho.")

    except ModuleNotFoundError:
        print("\n ModuleNotFoundError → Jab module hi nahi milta. Example: import abcdefg")

    except AttributeError:
        print("\n AttributeError → Jab object me wo method/attribute exist nahi. Example: 'abc'.push()")

    except RuntimeError:
        print("\n RuntimeError → General runtime galti, mostly libraries ke code me aati hai.")

    except MemoryError:
        print("\n MemoryError → Jab memory khatam ho jaye, bohot badi list ya string banate waqt.")

    except RecursionError:
        print("\n RecursionError → Jab function khud ko itni dafa call kare ki limit cross ho jaye.")

    except AssertionError:
        print("\n AssertionError → Jab assert condition galat ho. Example: assert 2+2==5")

    except OverflowError:
        print("\n OverflowError → Jab number bohot bada ho jaye jo Python handle na kar sake.")

    except UnicodeError:
        print("\n UnicodeError → Jab string encoding/decoding me problem ho.")

    except Exception as e:
        print(f"\n Unknown Error: {e}")

    finally:
        print("\n Test complete. Wapis menu par chalte hain...")