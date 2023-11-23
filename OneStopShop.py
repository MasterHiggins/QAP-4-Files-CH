#Program to calculate insurance costs and receipts for customers
#Written on November 20th, 2023
#Author Chris Higgins

#Imports
import datetime

#Constants
POLICY_NUMBER = "1944"
BASIC_PREMIUM_RATE = 869.00
ADDITIONAL_CAR_DISCOUNT = 0.25
LIABILITY_COVERAGE = 130.00
GLASS_COVERAGE = 86.00
LOANER_COVERAGE = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99
MONTHS_PAID = 8

#functions
def ReceiptLine(Claim, Date, Amount):        #Function to generate line of receipt
    Line = f"  {Claim: >5d}. {Date: <10s}       {Amount: >10s}"
    return Line

def DollarDisplay(Display):
    DisplayDSP = "${:,.2f}".format(Display)
    return(DisplayDSP)

def VehicleCost(Additional):                 #Determining vehicle insurance costs
    Additional -= 1
    Cost = BASIC_PREMIUM_RATE
    Cost += Additional * (ADDITIONAL_CAR_DISCOUNT * BASIC_PREMIUM_RATE)
    return Cost

def MonthlyPayment(TotalPayment, DownPayment):     #Calculating monthly payment
    TotalCost = TotalPayment - DownPayment
    TotalCost = TotalPayment + PROCESSING_FEE
    TotalCost /= MONTHS_PAID
    return TotalCost

def fstr(String):                            #Changing strings to floats
    String = int(String)
    String = float(String)
    return String

#Setup
ClaimDatesDSP = []
AmountsDSP = []
PaymentOptions = ["Full", "Monthly", "Down Payment"]
Provinces = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]

#Mainloop
while True:
    #Inputs
    FirstName = input("What is the customer's first name: ").title()
    LastName = input("What is the customer's last name: ").title()
    Address = input("What is the customer's address: ")
    City = input("What is the customer's city: ").title()
    Province = input("What is the customer's province [ex: MB]: ").upper()
    while Provinces.count(Province) == 0:
        Province = input("Please ensure the province is the correct abbreviation [ex: MB]: ").upper()
    Postal = input("What is the postal code: ").upper()
    Phone = input("What is the customer's phone number: ")
    CarsInsured = int(input("How many cars will be insured: "))
    Glass = ""
    while Glass != "Y" and Glass != "N":
        Glass = input("Glass coverage [Y/N]: ").upper()
    Loan = ""
    while Loan != "Y" and Loan != "N":
        Loan = input("Loaner car coverage [Y/N]: ").upper()
    ExtraLiability = ""
    while ExtraLiability != "Y" and ExtraLiability != "N":
        ExtraLiability = input("Extra liability up to $1,000,000 [Y/N]: ").upper()
    PaymentOption = input("Is customer paying in [Full], [Monthly], or with a [Down payment]: ").title()
    while PaymentOptions.count(PaymentOption) == 0:
        PaymentOption = input("Please ensure the correct option was selected [Full/Monthly/Down Payment]: ").title()
    DownPayment = 0
    if PaymentOption == "Down Payment":
        DownPayment = int(input("What is the down payment: "))
    Date = input("What is the date [YYYY-MM-DD]: ")
    ClaimsAmountPrevious = [0]
    ClaimsDatePrevious = [0]
    while ClaimsAmountPrevious.count("") == 0:
        PreviousClaim = input("Enter a previous claim amount from the customer, press enter when finished: ")
        if PreviousClaim != "":
            PreviousClaim = fstr(PreviousClaim)
            ClaimsAmountPrevious.append(DollarDisplay(PreviousClaim))    #Adding as dollars so it's not done later
        else:
            break
    for claim in range (1, len(ClaimsAmountPrevious)):
        PreviousDate = input(f"Enter the date for claim {ClaimsAmountPrevious[claim]}: ")
        ClaimsDatePrevious.append(PreviousDate)
    
    #Calculations
    InsuranceCosts = VehicleCost(CarsInsured)
    Extras = 0
    if ExtraLiability == "Y":
        Extras += LIABILITY_COVERAGE
    if Glass == "Y":
        Extras += GLASS_COVERAGE
    if Loan == "Y":
        Extras += LOANER_COVERAGE
    TotalPremiumCosts = InsuranceCosts + Extras
    HST = TotalPremiumCosts * HST_RATE
    TotalCost = TotalPremiumCosts + HST
    Payment = MonthlyPayment(TotalCost, DownPayment)
    InvoiceDate = datetime.datetime.strptime(Date, "%Y-%m-%d")
    PaymentDates = []
    for i in range(1, 9):
        PaymentDate = InvoiceDate + datetime.timedelta(days=i * 30)
        PaymentDateResult = PaymentDate.strftime("%Y-%m-%d")
        PaymentDates.append(PaymentDateResult)
    
    #Output
    print()
    print()     #Blank lines to separate output from input in terminal
    print()
    print(f"Customer name: {FirstName} {LastName}")
    print(f"{Address}, {City}, {Province}")
    print(f"Postal code:              {Postal}")
    print(f"Phone number:             {Phone}")
    print(f"-----")
    print(f"Glass coverage?           {Glass}")
    print(f"Loaner Coverage?          {Loan}")
    print(f"Extra Liability Coverage? {ExtraLiability}")
    Extras = DollarDisplay(Extras)
    print(f"Extras:                   {Extras}")
    print(f"-----")
    print(f"Payment option:           {PaymentOption}")
    print(f"Invoice date:             {InvoiceDate}")
    print(f"-----")
    TotalPremiumCostDSP = DollarDisplay(TotalPremiumCosts)
    HSTDSP = DollarDisplay(HST)
    TotalCostDSP = DollarDisplay(TotalCost)
    print(f"Total: {TotalPremiumCostDSP}")
    print(f"HST: {HSTDSP}")
    print(f"Total Cost: {TotalCostDSP}")
    print("---Previous Claims---")
    print(f"Claim #   Claim Date        Amount")
    for i in range (1, len(ClaimsDatePrevious)):
        print(ReceiptLine(i, ClaimsDatePrevious[i], ClaimsAmountPrevious[i]))
    print(ReceiptLine(len(ClaimsDatePrevious), Date, TotalCostDSP))
    print()
    Continue = ""
    while Continue != "Y" and Continue != "N":
        Continue = input("Would you like to enter data for another customer [Y/N]: ").upper()
    if Continue == "N":
        break

print("Thank you for using this program")

#Pain
