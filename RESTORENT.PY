import os
from PIL import Image

print("\t\t\t\t\t\t-----------------------------------------")
print("\t\t\t\t\t\t\t--Welcome to my Restaurant--")
print("\t\t\t\t\t\t-----------------------------------------")

Restaurant_Menu = {
    "Pizza": 350,
    "Pasta": 650,
    "Burger": 120,
    "Coffee": 75,
    "Tea": 20,
    "Bhajiya": 300,
    "Potato Sev": 250,
    "Manchurian Noodles": 280,
    "Veg Rice": 250,
    "Veg Sorma": 70,
    "Red Pantis": 230,
    "Veg Biriyani": 180,
    "Chana Dhokla": 210,
    "Chart": 80,
    "Vada pav": 35,
    "Jalebi": 465,
    "Mix Pulav": 450,
    "Malai Paneer": 400,
    "Dahi Bhalla": 120,
    "Mix Puri Sabji": 200
}

print(" 1. Pizza: Rs.350\n 2. Pasta: Rs.650\n 3. Burger: Rs.120\n 4. Coffee: Rs.75\n 5. Tea Rs.20\n 6. Bhajiya: Rs.300\n 7. Potato Sev: Rs.250\n 8. Manchurian Noodles: Rs.280\n 9. Veg Rice: Rs.250\n 10. Veg Sorma: Rs.70\n 11. Red Pantis: Rs.230\n 12. Veg Biriyani: Rs.180\n 13. Chana Dhokla: Rs.210\n 14. Chart: Rs.80\n 15. Vada pav: Rs.35\n 16. Jalebi: Rs.465\n 17. Mix Pulav: Rs.450\n 18. Malai Paneer: Rs.400\n 19. Dahi Bhalla: Rs.120\n 20. Mix Puri Sabji: Rs.200")

Total_Order_Amount = 0
Order_Item = input("\n\tEnter the Food-Name You want to Order : ")
if Order_Item in Restaurant_Menu:
    Total_Order_Amount += Restaurant_Menu[Order_Item]
    print(f"\tYour item {Order_Item} has been added to your orders.")
else:
    print("Order something else, as we cannot serve that yet.")

Ask_Another_Item = input("Do you want to add another Item? (Yes/No) : ")
if Ask_Another_Item.lower() == "yes":
    Again_Asking_Order_Item = input("Enter the name of the second Item : ")
    if Again_Asking_Order_Item in Restaurant_Menu:
        Total_Order_Amount += Restaurant_Menu[Again_Asking_Order_Item]
        print(f"Item {Again_Asking_Order_Item} has been added to your Order.")

print(f"\nThe total Amount to pay for the items is {Total_Order_Amount}.")

qr_code_path = "C:/Users/kishan gupta/Downloads/GooglePay_QR.png"

if os.path.exists(qr_code_path):
    img = Image.open(qr_code_path)
    img.show()
else:
    print("QR code image not found at the specified path.")