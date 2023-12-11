from colorama import Fore, Style, init

init(autoreset=True)

def calc_bmi(kg,m):
    bmi=kg/(m**2) 
    print(f"\nYour Body Mass Index is: {Fore.BLUE}{bmi:.2f}{Style.RESET_ALL}\n")

    if bmi < 18.5:
        print(f"{Fore.YELLOW}🌟Underweight - Have a balanced diet to achieve a healthy weight{Style.RESET_ALL}")
    elif 18.5 <= bmi <= 24.9:
        print(f"{Fore.GREEN}🌈Normal weight - Keep it up!{Style.RESET_ALL}")
    elif 25 <= bmi <= 29.9:
        print(f"{Fore.YELLOW}🏋️Overweight - Start an exercise routine{Style.RESET_ALL}")
    elif 30 <= bmi <= 34.9:
        print(f"{Fore.RED}🍏Obesity class I - Balance diet, exercise, and seek professional guidance for obesity{Style.RESET_ALL}")
    elif 35 <= bmi <= 39.9:
        print(f"{Fore.RED}🥗Obesity class II - Embrace diet, exercise, and professional guidance for obesity class 2 management{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}⚠️Obesity class III - Seek professional guidance promptly for management of obesity through lifestyle changes{Style.RESET_ALL}")

#get input from the user
print("\n" + "-" * 40)
print("\n\t📊 BMI CALCULATOR 📊")
print("\n" + "-" * 40)
kg=float(input("Enter your weight in kilograms: "))
m=float(input("Enter your height in meters: "))
#calculating bmi and classifying into categories using function
bmi=calc_bmi(kg,m)