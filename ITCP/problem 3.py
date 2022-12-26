year=int(input("donner l'année"))
def check_the_year(year):
    if ((year % 4 == 0)and(year % 100 != 0 ))or(year % 400 == 0):
        print("leap")
    else :
        print("not leap") 
check_the_year(year)
