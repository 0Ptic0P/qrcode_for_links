import qrcode
while True:
    n = input(str("Please enter the link of video: " ))

    z = input("Please enter the question number: " )

    c = (z)+(".jpg")

    img = qrcode.make(n)

    print(c)

    img.save(c)

    if n != n:
        break

  

 

   

        