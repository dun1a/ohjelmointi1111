
def gallontoliters(gallonmäärä):
    litra = gallonmäärä*3.785
    return litra

while True:
    gallonmäärä = int(input('Anna gallonmäärä litroiksi: '))
    if gallonmäärä <=-1:
        break
    litra = gallontoliters(gallonmäärä)
    print(litra)
