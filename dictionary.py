#os dicionarios em python vão guardar chaves ... unicas para que possam ter associadas a valores
#como num dicionairio...

month_convertion = {
        "jan" : "January",
        "fev" : "Febuary",
        "mar" : "March",
        "Apr" : "April",
        "may" : "May",
        "jun" : "June",
        "jul" : "July",
        "ago" : "August",
        "set" : "September",
        "oct" : "October",
        "nov" : "November",
        "Dez" : "Dezember",
}


month = input("Enter the frist's 3 letter's of the month: ")
print("is " + month_convertion[month] + " the month you were looking for?")
validation = input("y/n ?")

if validation == "y" or validation == "yes":
    print("ok, awesome")
elif validation == "n" or validation == "no":
    month = input("try again: ")
    validation = print("is " + month_convertion.get(month))
else:
    print("we cant find the month you are looking for")
