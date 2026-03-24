while True:
    n = input("enter number : ")

    if (n == "x"):
        print("close game")
        break
    try:
      n = int(n)
      if n >= 10:
        print("success ")
      else:
        print("fail ")
    except ValueError:
      print("enter valid number")
