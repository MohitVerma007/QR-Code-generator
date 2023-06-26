import qrcode as qr

img = qr.make("https://www.youtube.com/watch?v=5XK_YC2nS6s")
img.save("myqr.png")