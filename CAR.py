def welcome_user(company_name):
    welcome_messages = {
        'Mercedes': "Welcome to the Mercedes Showroom!",
        'BMW': "Welcome to the BMW Showroom!",
        'Audi': "Welcome to the Audi Showroom!"
    }
    print(welcome_messages.get(company_name, "We do not have that company's cars."))

def choose_model(company_name):
    if company_name == 'Mercedes':
        model = input("Enter the model name for Mercedes (Example: Maybach, GLS, A-Class): ")
    elif company_name == 'BMW':
        model = input("Enter the model name for BMW (Example: X5, M4, 3-Series): ")
    elif company_name == 'Audi':
        model = input("Enter the model name for Audi (Example: Q7, A8, TT): ")
    else:
        print("Sorry, we do not have information for this company.")
        return None
    return model

def variant_and_display(company_name, model_name):
    variant = input(f"Choose the variant for {company_name} {model_name} - Petrol or Diesel: ").lower()

    ex_showroom_prices = {
        'Petrol': 1000000,  
        'Diesel': 1100000, 
    }
    ex_showroom_price = ex_showroom_prices.get(variant.capitalize(), 0)
    CGST = 0.1  
    SGST = 0.1  # 10%
    insurance = 0.05  # 5%
    
    total_tax = ex_showroom_price * (CGST + SGST)
    insurance_fee = ex_showroom_price * insurance
    on_road_price = ex_showroom_price + total_tax + insurance_fee
    
    print(f"\nCar: {company_name} {model_name} - {variant.capitalize()}")
    print(f"Ex-Showroom Price: {ex_showroom_price}")
    print(f"On-Road Price: {on_road_price}")

def main():
    print("Choose a car company from: Mercedes, BMW, Audi")
    company_name = input("Enter the car company name: ")
    
    welcome_user(company_name)
    
    model_name = choose_model(company_name)
    if model_name:
        variant_and_display(company_name, model_name)

if __name__ == "__main__":
    main()
