from django.shortcuts import render
import csv
def index(request):
    with open ('/home/xiran_xu_claire/group-project/final-project/rows.csv') as f:
        f_csv=csv.reader(f)
        context={
                'f_csv':f_csv,
        }
        return  render(request,'squirrels/index.html',context)
   
