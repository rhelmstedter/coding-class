import qrcode

img = qrcode.make("https://github.com/rhelmstedter/coding-class")
img.save("github_link.png")
