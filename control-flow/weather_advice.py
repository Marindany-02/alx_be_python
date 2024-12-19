# Weather advice .py
#prompt the user
weather = input("what's the weather like today? (sunny/rainy/cold):)
#provide clothing recommendations
if weather == "sunny":
    print("wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
