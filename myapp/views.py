from django.shortcuts import render
import json
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt ,name ='dispatch')
class BMIview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        h = data.get("height")
        w = data.get("weight")
        
        #convert height from cm to meter
        height =h/100
        
        #convert BMI
        bmi =w /(height**2)
        
        result ={
            "Height" :data.get('height'),
            "Weight" :w,
            "BMI" :round (bmi ,2)
        }
        
        return JsonResponse(result)
    
    
@method_decorator(csrf_exempt ,name ='dispatch')   
class Ageview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        birth_year = data.get("birth_year")
        current_year = data.get("current_year")
        age  = current_year -birth_year
        
        result ={
            "Birth_year" :birth_year,
            "Current_year" :current_year,
            "Age" : age
        }
        return JsonResponse(result) 
    
@method_decorator(csrf_exempt ,name ='dispatch')
class Percentageview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        obtained_marks= data.get("obtained_mark")
        total_marks = data.get("total_mark")
        percentage = (obtained_marks/total_marks)*100
        
        result = {
            "Obtained_marks" : obtained_marks,
            "Total_mark" : total_marks ,
            "Percantage" :percentage
        }
        return JsonResponse(result)
        
        
@method_decorator(csrf_exempt ,name ='dispatch')         
class Simpleintrestview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        principle = data.get("principle")
        rate = data.get("rate")
        time = data.get("time")
        simpleintrest = (principle*rate*time) /100
        
        result ={
            "Principle" : principle,
            "Rate" : rate,
            "Time" : time,
            "Simpleintrest" :simpleintrest
            
        }
        return JsonResponse(result)
    
            
@method_decorator(csrf_exempt ,name ='dispatch')     
class ElectricityBillView(View):  
    def post (self ,request):
        data =json.loads(request.body)
        
        unit =data.get("unit")
        rate =data.get("rate")
        
        result ={
            "Unit" :unit,
            "Rate" :rate,
            "Amount" :unit*rate
        }   
        return JsonResponse(result)  
   
   
@method_decorator(csrf_exempt ,name ='dispatch')         
class DiscountView(View):
    def post(self , request):
        data =json.loads(request.body)
        
        price =data.get("price")
        discount_percentage =data.get("discount_percentage")
        discount_amount= int((price * discount_percentage) /100)
        final_price =  int(price - discount_amount)
        
        result ={
            "Price" : price ,
            "Discount_percentage" : discount_percentage ,
            "Discount_amount" : discount_amount ,
            "Final_price" : final_price
        } 
        return JsonResponse(result)

@method_decorator(csrf_exempt ,name ='dispatch')
class Profitview(View):
    def post (self ,request) :
        data =json.loads(request.body)
        
        cost_price =data.get("cost_price")
        selling_price =data.get("selling_price")
        profit = selling_price - cost_price
        
        result ={
            "Cost_price" : cost_price ,
            "Selling_price" : selling_price ,
            "Profit" : profit
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt ,name ='dispatch')
class Salaryview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        basic_salary =data.get("basic_salary")
        bonus =data.get("bonus")
        deduction =data.get("deduction")
        net_salary = basic_salary + bonus - deduction
        
        result ={
            "Basic_salary" : basic_salary ,
            "Bonus" : bonus ,
            "Deduction" : deduction ,
            "Net_salary" : net_salary
        }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt ,name ='dispatch')    
class Timeview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        hours =data.get("hours")    
        minutes = hours * 60
        second = hours * 3600
        
        result = {
            "Hours" : hours ,
            "Minutes" : minutes ,
            "Second" : second
        }
        return JsonResponse(result)
    
    
@method_decorator(csrf_exempt ,name ='dispatch')
class Fuelview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        distance =data.get("distance")
        mileage =data.get("mileage")
        fuel_price =data.get("fuel_price")
        fuel_required = int(distance /mileage)
        total_cost = int(fuel_required * fuel_price)
        
        result ={
            "Distance" : distance,
            "Milage" : mileage,
            "Fuel_price" : fuel_price,
            "Fuel_required" :fuel_required,
            "Total_cost" :total_cost
        }
        return JsonResponse(result)
    
    
@method_decorator(csrf_exempt ,name ='dispatch')
class Productview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        cost_price = data.get("cost_price")
        selling_price = data.get("selling_price")
        quantity = data.get("quantity")
        total_cost = cost_price * quantity
        total_sales = selling_price * quantity
        profit =  total_sales - total_cost
        
        result ={
            "Cost_price" : cost_price,
            "Selling_price" : selling_price,
            "Quantity" : quantity,
            "Total_cost" : total_cost,
            "Total_sales" : total_sales,
            "Profit" : profit    
        }
        return JsonResponse(result)
       
@method_decorator(csrf_exempt ,name ='dispatch')
class Worksalaryview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        hours_worked =data.get("hours_worked")
        regular_hours =data.get("regular_hours")
        hourly_rate =data.get("hourly_rate") 
        overtime_rate =data.get("overtime_rate")
        regular_pay = regular_hours * hourly_rate
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * overtime_rate
        total_salary = regular_pay + overtime_pay
        
        result ={
            "Hours_worked" :hours_worked,
            "Regular_hours" : regular_hours,
            "Hourly_rate" : hourly_rate,
            "Overtime_rate" : overtime_rate,
            "Regular_pay" : regular_pay,
            "Overtime_hours" : overtime_hours,
            "Overtime_pay" : overtime_pay,
            "Total_salary" : total_salary
            
            }
        return JsonResponse(result)
    
@method_decorator(csrf_exempt ,name ='dispatch')
class  AgeDetailsview(View):
    def post(self ,request):
        data =json.loads(request.body)
        
        age = data.get("age")
        months = age *12 
        weeks = age *52
        days =age *365
        
        result ={
            "Age" : age,
            "Months"  :months,
            "Weeks" : weeks,
            "Days" :days
        }  
        return JsonResponse(result)