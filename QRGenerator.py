import qrcode
img=qrcode.make('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
type(img)
img.save("qr.png")