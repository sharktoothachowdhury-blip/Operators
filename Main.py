Field1=777
Field2=312
Field3=621
Field4=333
Field5=152

Total=(Field1 + Field2 + Field3 + Field4  + Field5)
average=(Total/5)

print(Total," is the Total")
print(average," is the average")

#price per kg is 20 Kawtcha 
PriceperKG=20
Earnings=(Total*PriceperKG)

print("Total Earnings is ",Earnings," Kawtcha")

#FlowDivision and Modules
Bags=(Total//25)
LeftOver=(Total%25)

print("Full Bags Packed are ",Bags)
if(LeftOver>0):
    print("The LeftOvers are",LeftOver," KG")  
else:
    print("There is nothing Leftover")

#Comperisen Operaters

LastYearHarvest=500

print("Better then last Year?",Total>LastYearHarvest)
print("Same as last year?",Total==LastYearHarvest)
print("Atleast as good as last year?",Total>=LastYearHarvest)