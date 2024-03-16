class carshowroom:

        def welcome(self,car_comp):
            
                    
            print("welcome to ",car_comp,"family.")
            if(car_comp=="mahindra" ):
                
                print("available models are thar,xuv 300,xuv 700");
            elif(car_comp=="toyota"):
                
                print("available models are innova,fortuner,glanza");
            elif(car_comp=="mercedes"):
                
                print("available models are g-wagon,GLS,E-classcabriolet")
                
            self.car=car_comp
    
        def model(self): 
            
            if(self.car=="mahindra"):
                while True:
                        model_name=input("enter model name:")
                        if(model_name=="1"):
                                model_name="thar"
                        if(model_name=="2"):
                                model_name="xuv 300"
                        if(model_name=="3"):
                                model_name="xuv 700"
                        if(model_name=="thar" or model_name=="xuv 300" or model_name=="xuv 700" ):
                                
                                break
                                
                        else:
                                print("enter only available models:")
            if(self.car=="toyota"):
                while True:
                        model_name=input("enter model name:")
                        if(model_name=="1"):
                                model_name="innova"
                        if(model_name=="2"):
                                model_name="fortuner"
                        if(model_name=="3"):
                                model_name="glanza"
                        if(model_name=="innova" or model_name=="fortuner" or model_name=="glanza" ):
                                
                                break
                                
                        else:
                                print("enter only available models:")
            if(self.car=="mercedes"):
                while True:
                        model_name=input("enter model name:")
                        if(model_name=="1"):
                                model_name="g-wagon"
                        if(model_name=="2"):
                                model_name="GLS"
                        if(model_name=="3"):
                                model_name="E-classcabriolet"
                        if(model_name=="g-wagon" or model_name=="GLS" or model_name=="E-classcabriolet" ):
                                
                                break
                                
                        else:
                                print("enter only available models:")
                                
                
            self.mode=model_name
        def variant(self):
                while True:
                        variant_name=input("enter desired variant in petrol or diesel:")
                        if(variant_name=="petrol" or variant_name=="diesel" ):
                                
                                break
                                
                        else:
                                print("enter only petrol or diesel model:")
        
                self.var=variant_name
        def display(self):
                
            print("you selected:",self.mode,self.var)
            #mahindra cars
            if(self.mode=="thar" and self.var=="petrol"):
                print("ex-showroom price is:1150000")
                onroad=1150000+(0.18*1150000)+(0.15*1150000)+(0.1*1150000)
                print("onroad price is:",onroad)
            if(self.mode=="thar" and self.var=="diesel"):
                print("ex-showroom price is:1100000")
                onroad=1100000+(0.18*1100000)+(0.15*1100000)+(0.1*1100000)
                print("onroad price is:",onroad)
            if(self.mode=="xuv 300" and self.var=="petrol"):
                print("ex-showroom price is:750000")
                onroad=750000+(0.18*750000)+(0.15*750000)+(0.1*750000)
                print("onroad price is:",onroad)
            if(self.mode=="xuv 300" and self.var=="diesel"):
                print("ex-showroom price is:700000")
                onroad=700000+(0.18*700000)+(0.15*700000)+(0.1*700000)
                print("onroad price is:",onroad)
            if(self.mode=="xuv 700" and self.var=="petrol"):
                print("ex-showroom price is:2100000")
                onroad=2100000+(0.18*2100000)+(0.15*2100000)+(0.1*2100000)
                print("onroad price is:",onroad)
            if(self.mode=="xuv 700" and self.var=="diesel"):
                print("ex-showroom price is:2000000")
                onroad=2000000+(0.18*2000000)+(0.15*2000000)+(0.1*2000000)
                print("onroad price is:",onroad)


            #toyota cars
            if(self.mode=="innova" and self.var=="petrol"):
                print("ex-showroom price is:2500000")
                onroad=2500000+(0.18*2500000)+(0.15*2500000)+(0.1*2500000)
                print("onroad price is:",onroad)
            if(self.mode=="innova" and self.var=="diesel"):
                print("ex-showroom price is:2300000")
                onroad=2300000+(0.18*2300000)+(0.15*2300000)+(0.1*2300000)
                print("onroad price is:",onroad)
            if(self.mode=="fortuner" and self.var=="petrol"):
                print("ex-showroom price is:3500000")
                onroad=3500000+(0.18*3500000)+(0.15*3500000)+(0.1*3500000)
                print("onroad price is:",onroad)
            if(self.mode=="fortuner" and self.var=="diesel"):
                print("ex-showroom price is:3300000")
                onroad=3300000+(0.18*3300000)+(0.15*3300000)+(0.1*3300000)
                print("onroad price is:",onroad)
            if(self.mode=="glanza" and self.var=="petrol"):
                print("ex-showroom price is:1050000")
                onroad=1050000+(0.18*1050000)+(0.15*1050000)+(0.1*1050000)
                print("onroad price is:",onroad)
            if(self.mode=="glanza" and self.var=="diesel"):
                print("ex-showroom price is:1000000")
                onroad=1000000+(0.18*1000000)+(0.15*1000000)+(0.1*1000000)
                print("onroad price is:",onroad)

            #mercedes cars
            if(self.mode=="g-wagon" and self.var=="petrol"):
                print("ex-showroom price is:25000000")
                onroad=25000000+(0.18*25000000)+(0.15*25000000)+(0.1*25000000)
                print("onroad price is:",onroad)
            if(self.mode=="g-wagon" and self.var=="diesel"):
                print("ex-showroom price is:23000000")
                onroad=23000000+(0.18*2300000)+(0.15*23000000)+(0.1*23000000)
                print("onroad price is:",onroad)
            if(self.mode=="GLS" and self.var=="petrol"):
                print("ex-showroom price is:35000000")
                onroad=35000000+(0.18*35000000)+(0.15*35000000)+(0.1*35000000)
                print("onroad price is:",onroad)
            if(self.mode=="GLS" and self.var=="diesel"):
                print("ex-showroom price is:33000000")
                onroad=33000000+(0.18*33000000)+(0.15*33000000)+(0.1*33000000)
                print("onroad price is:",onroad)
            if(self.mode=="E-classcabriolet" and self.var=="petrol"):
                print("ex-showroom price is:10500000")
                onroad=10500000+(0.18*10500000)+(0.15*10500000)+(0.1*10500000)
                print("onroad price is:",onroad)
            if(self.mode=="E-classcabriolet" and self.var=="diesel"):
                print("ex-showroom price is:10000000")
                onroad=10000000+(0.18*10000000)+(0.15*10000000)+(0.1*10000000)
                print("onroad price is:",onroad)

while True:
    car_comp=input("enter 1 or mahindra for mahindra,2 or toyota for toyota,3 or mercedes for mercedes:")
    if(car_comp=="1"):
            car_comp="mahindra"
    if(car_comp=="2"):
            car_comp="toyota"
    if(car_comp=="3"):
            car_comp="mercedes"
    if(car_comp=="mahindra" or car_comp=="toyota"  or car_comp=="mercedes" ):
        cust=carshowroom()
        cust.welcome(car_comp)
        cust.model()
        cust.variant()
        cust.display()
        break
    else:
        print("enter correct car company:")