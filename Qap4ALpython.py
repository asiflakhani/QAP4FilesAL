# Description: The insurance program to calculate the insurance policies for their customer.
# Author: Asif Lakhani  
# Date(s): 15 March 2024 - 
 
 
# Define required libraries.
import FormatValues as FV
import ImpFunctions as ImF
import datetime
import sys
import time

global noCars, extraLiability, glassCoverage, optLoanerCar, downPayment, extraLiabilityMsg, glassCoverageMsg, optLoanerCarMsg, payMsg, payMethod


# Define program constants.
TODAY = datetime.datetime.now()

# Open the defaults file and read the values into variables
DV = open('defvalues.dat', 'r')
POLICY_NUM = int(DV.readline())
BASIC_PREMIUM = float(DV.readline())
ADD_CAR_DISCOUNT = float(DV.readline())
EXTRA_LIABILITY_COST = float(DV.readline())
GLASS_COVERAGE_COST = float(DV.readline())
LOANER_CAR_COST = float(DV.readline())
HST_RATE = float(DV.readline())
PROCESS_MONTH_FEES = float(DV.readline())
DV.close()
 



 
# Define program functions.
def carPremium(totalCars):
    firstCarPremium = BASIC_PREMIUM

    if totalCars > 1:
        addCarPremium = (BASIC_PREMIUM * ADD_CAR_DISCOUNT) * (totalCars - 1)
    else:
        addCarPremium = 0

    totalPremium = firstCarPremium + addCarPremium

    return firstCarPremium, addCarPremium, totalPremium





def coverage():
    global noCars, extraLiability, glassCoverage, optLoanerCar, downPayment, payMsg
    while True:
        try:
            noCars = int(input("Enter the number of cars insured                          : "))
        except:
            print("\033[0;31mData Entry Error - No of cars is not in a valid format, please try again.\033[0m")
            print()
        else:
            if noCars == "":
                print("\033[0;31mData Entry Error - No of cars cannot be blank, please try again.\033[0m")
                print()
            else:
                break


    
    while True:
        global extraLiabilityMsg, glassCoverageMsg, optLoanerCarMsg, payMethod
        extraLiability = input("Do you want extra liability for upto $1,000,000? (Y/N)    : ").upper()
        if extraLiability != "Y" and extraLiability != "N":
            print("\033[0;31mData Entry Error - Input must be Y or N, please try again.\033[0m")
            print()
        else:
            if extraLiability == "Y":
                extraLiability = EXTRA_LIABILITY_COST
                extraLiabilityMsg = "Covered"
            elif extraLiability == "N":
                extraLiability = 0
                extraLiabilityMsg = "Not Covered"
            break

    
    while True:
        glassCoverage = input("Do you want glass coverage? (Y/N)                         : ").upper()
        if glassCoverage != "Y" and glassCoverage != "N":
            print("\033[0;31mData Entry Error - Input must be Y or N, please try again.\033[0m")
            print()
        else:
            if glassCoverage == "Y":
                glassCoverage = GLASS_COVERAGE_COST
                glassCoverageMsg = "Covered"
            elif glassCoverage == "N":
                glassCoverage = 0
                glassCoverageMsg = "Not Covered"
            break

    
    while True:
        optLoanerCar = input("Do you want optional coverage for loaner car? (Y/N)       : ").upper()
        if optLoanerCar != "Y" and optLoanerCar != "N":
            print("\033[0;31mData Entry Error - Input must be Y or N, please try again.\033[0m")
            print()
        else:
            if optLoanerCar == "Y":
                optLoanerCar = LOANER_CAR_COST
                optLoanerCarMsg = "Covered"
            elif optLoanerCar == "N":
                optLoanerCar = 0
                optLoanerCarMsg = "Not Covered"
            break

    
    print()
    print("\033[3;35mFull Payment (FP), Monthly Payment (MP), Down Payment (DP)\033[0m")
    
    
    payMethodList = ["FP", "MP", "DP"]
    while True:
        payMethod = input("Enter the payment method. (FP / MP / DP)                  : ").upper()
        if payMethod == "":
            print("\033[0;31mData Entry Error - Payment method cannot be blank, please try again.\033[0m")
            print()
        elif payMethod not in payMethodList:
            print("\033[0;31mData Entry Error - Invalid payment method, please try again.\033[0m")
            print()
        elif payMethod == "DP":
            payMsg = "Monthly"
            while True:
                try:
                    downPayment = float(input("Enter the down payment amount                             : "))
                    break
                except ValueError:
                    print("\033[0;31mData Entry Error - Down payment is not in a valid format, please try again.\033[0m")
                    print()
            break  # Exit the main loop after obtaining the down payment
        elif payMethod == "FP":
            downPayment = 0
            payMsg = "Full"
            break  # Exit the main loop after obtaining the down payment
        elif payMethod == "MP":
            downPayment = 0
            payMsg = "Monthly"
            break  # Exit the main loop after obtaining the down payment
        else:
            break  




def claims():
    claimNo = ["00001", "00002", "00003"]
    claimDate = ["2023-01-10", "2023-05-20", "2023-10-08"]
    claimAmount = [100.00, 50.00, 250.00]
    while True:
            
        # Add a new claim to a list.
        while True:
            newClaimNo = input("Enter a new claim number (99999)                        : ")
            if newClaimNo == "":
                print("\033[0;31mData Entry Error - Claim number is not in a valid format, please try again.\033[0m")
                print()
            elif not newClaimNo.isdigit():
                print("\033[0;31mData Entry Error - Claim number must be digits only, please try again.\033[0m")
                print()
            elif len(newClaimNo) != 5: 
                print("\033[0;31mData Entry Error - Claim number must be 5 digits only, please try again.\033[0m")
                print()
            else:
                break
                
        claimNo.append(newClaimNo)


        while True:
            try:
                newClaimDate = input("Enter a claim date (YYYY-MM-DD)                         : ")
                newClaimDate = datetime.datetime.strptime(newClaimDate, "%Y-%m-%d")
            except:
                print("\033[0;31mData Entry Error - Claim date is not in a valid format, please try again.\033[0m")
                print()
            else:
                if newClaimDate == "":
                    print("\033[0;31mData Entry Error - Claim date cannot be empty, please try again.\033[0m")
                    print()
                else:
                    break
                    

        newClaimDate = FV.FDateS(newClaimDate)
        claimDate.append(newClaimDate)


        while True:
            try:
                newClaimAmount = input("Enter a claim amount                                    : ")
                newClaimAmount = float(newClaimAmount)
            except:
                print("\033[0;31mData Entry Error - Claim amount is not in a valid format, please try again.\033[0m")
                print()
            else:
                break
            
        claimAmount.append(newClaimAmount)

        print()
        while True:
            claimContinue = input("\033[0;32mWould you like to process another insurance claim? (Y/N): \033[0m").upper()
            print()
            if claimContinue != "Y" and claimContinue != "N":
                print("\033[0;31mData Entry Error - Input must be Y or N, please try again.\033[0m")
                print()
            else:
                break
        
        if claimContinue == "N":
            break

    return claimNo, claimDate, claimAmount







 
 
# Main program starts here.
while True:
    print()
    print()
    print("                           \033[1;34mOne Stop Insurance Company\033[0m")
    print()
    
     

    # Program Inputs
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")
    print("                             \033[0;36mPersonal Information\033[0m")
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")
    print()

    cusFirstName = ImF.fName("First Name")
    cusLastName = ImF.lName("Last Name")
    cusFullName = cusFirstName + " " + cusLastName
    
    cusAddress = ImF.strAddress("Address")
    cusCity = ImF.city("City")
    cusProvince = ImF.provList("Province")
    cusPostalCode = ImF.postalCode("X9X9X9")
    cusAddress2 = cusCity + ", " + cusProvince + ", " + cusPostalCode

    cusPhone = ImF.cellNumber("9999999999")
    print()
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")   
    print("                             \033[0;36mCoverage Information\033[0m")
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")
    print()
    coverageInput = coverage()
   
    print()
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")
    print("                             \033[0;36mClaim's Information\033[0m")
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")
    print()

    claimLst = claims()
    claimNo = claimLst[0]
    claimDate = claimLst[1]
    claimAmount = claimLst[2]

    
    print("\033[0;33mClaim data successfully saved...\033[0m", end='\r')
    time.sleep(.6)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
    time.sleep(.6)  # To create the blinking effect
    print("\033[0;33mPrinting Receipt\033[0m", end='\r')
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
    time.sleep(.3)  # To create the blinking effect


    # Program Calculations

    premium = carPremium(noCars)
    firstCar = premium[0]
    addCar = premium[1]
    totalPre = premium[2]
    

    totalExtraCost = extraLiability + glassCoverage + optLoanerCar
    totalInsPremium = totalPre + totalExtraCost
    HST = totalInsPremium * HST_RATE
    totalCost = totalInsPremium + HST
    
    # If the user choose to pay in installments with or without the down payment
    
    monPaymentFP = totalCost
    monPaymentMP = (totalCost + PROCESS_MONTH_FEES) / 8
    monPaymentDP = (totalCost + PROCESS_MONTH_FEES - downPayment) / 8

    invDate = TODAY
    firstPayDate = invDate.replace(day=1, month=invDate.month + 1)


    if payMethod == "FP":
        totalCost = totalCost
        monPay = monPaymentFP
    elif payMethod == "MP":
        totalCost = totalCost + PROCESS_MONTH_FEES
        monPay = monPaymentMP
    else:
        totalCost = totalCost + PROCESS_MONTH_FEES - downPayment
        monPay = monPaymentDP



    # Program Output
    print("\033[0;35m==================================================================================\033[0m")
    print()
    print("                           \033[1;34mOne Stop Insurance Company\033[0m")
    print()
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")
    print("                           \033[0;36m******Client Receipt******\033[0m")
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")
    print()

    print(f"Name   : {cusFullName:<30s}              Invoice Date     : {FV.FDateS(invDate):>10s}")
    print(f"Address: {cusAddress:<30s}              Insurance Policy # {POLICY_NUM:>10d}")
    print(f"         {cusAddress2:<30s}              Number of cars   : {noCars:>10d}")
    print(f"Phone  # {cusPhone:<30s}")
    print()
    print()
    print("\033[1;32mCOVERAGE OPTION                                      PAYMENT OPTION\033[0m")
    print("\033[1;32m----------------------------                         -----------------------------\033[0m")
    print(f"Extra Liability: {extraLiabilityMsg:<12s}                        Payment type     : {payMsg:>10s}")
    print(f"Glass Coverage : {glassCoverageMsg:<12s}                        Down Payment     : {FV.FDollar2(downPayment):>10s}")
    
    if payMethod == "FP":
        print(f"Loaner Car     : {optLoanerCarMsg:<12s}                        Total Payment    : {FV.FDollar2(monPay):>10s}")
    elif payMethod == "MP" or payMethod == "DP":
        print(f"Loaner Car     : {optLoanerCarMsg:<12s}                        Monthly Payment  : {FV.FDollar2(monPay):>10s}")

    # print(f"Loaner Car     : {optLoanerCarMsg:<12s}                        Monthly Payment     : {FV.FDollar2(monPay):>7s}")
    print("\033[1;32m----------------------------                         -----------------------------\033[0m")
    print()
    
    print()
    print(f"First Car Premium.................................................... : {FV.FDollar2(firstCar):>10s}")
    print(f"Additional Car Premium............................................... : {FV.FDollar2(addCar):>10s}")
    print(f"\033[1mTotal Premium........................................................ : {FV.FDollar2(totalPre):>10s}\033[0m")

    print()
    print(f"Liability Cost....................................................... : {FV.FDollar2(extraLiability):>10s}")
    print(f"Glass Cost........................................................... : {FV.FDollar2(glassCoverage):>10s}")
    print(f"Loaner Cost.......................................................... : {FV.FDollar2(optLoanerCar):>10s}")
    print(f"\033[1mTotal Extra Cost..................................................... : {FV.FDollar2(totalExtraCost):>10s}\033[0m")
    
    print()
    print(f"\033[1mTotal Insurance Premium.............................................. : {FV.FDollar2(totalInsPremium):>10s}\033[0m")
    print()
    print(f"HST Amount........................................................... : {FV.FDollar2(HST):>10s}")
    
    if payMethod == "MP":
        print(f"Monthly Payment Processing Fees...................................... : {FV.FDollar2(PROCESS_MONTH_FEES):>10s}")
    elif payMethod == "DP":
        print(f"Monthly Payment Processing Fees...................................... : {FV.FDollar2(PROCESS_MONTH_FEES):>10s}")
        print(f"Down Payment......................................................... : {FV.FDollar2(downPayment):>10s}")
    
    print()
    print(f"\033[1mTotal Cost........................................................... : {FV.FDollar2(totalCost):>10s}\033[0m")

    print()
    print(f"Your first monthly installment date is............................... : {FV.FDateS(firstPayDate):>10s}")


    print()
    print()
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")
    print("                          \033[0;36mPrevious Insurance Claims\033[0m")
    print("\033[0;36m----------------------------------------------------------------------------------\033[0m")

    print()
    print("                Claim No          Claim Date         Claim Amount")
    print("            ---------------------------------------------------------")
    
    Index = 0
    for claim in claimNo:
        print(f"                 {str(claimNo[Index]):<5}            {claimDate[Index]:<10}         {FV.FDollar2(claimAmount[Index]):>10}")
        Index += 1

    print("            ---------------------------------------------------------")
    print()
    print("\033[0;35m==================================================================================\033[0m")
    print()
     
    
    f = open("InsuranceQuotes.dat", "a")
 
    # All values written to file must be a string.  If you have a numeric
    # value, use the str() function to convert.
    f.write("{}, ".format(cusFullName))
    f.write("{}, ".format(cusAddress))
    f.write("{}, ".format(cusAddress2))
    f.write("{}, ".format(str(cusPhone)))
    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(FV.FDateS(invDate)))
    f.write("{}, ".format(str(noCars)))
    f.write("{}, ".format(FV.FDollar2(downPayment)))
    f.write("{}, ".format(FV.FDollar2(monPay)))
    f.write("{}, ".format(FV.FDollar2(totalInsPremium)))
    f.write("{}, ".format(FV.FDollar2(HST)))
    f.write("{}, ".format(FV.FDollar2(totalCost)))
    f.write("{}\n ".format(FV.FDateS(firstPayDate)))
    
    f.close()

    
    print(f"\033[0;33mCongratulations {cusFullName}! Your policy data has been successfully saved.\033[0m")
    print()
    time.sleep(.3)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns

    POLICY_NUM += 1

 
 
    while True:
        program_continue = input("Would you like to process another insurance quotation? (Y/N): ").upper()
        if program_continue != "Y" and program_continue != "N":
            print("\033[0;31mData Entry Error - Must enter either Y or N, please try again.\033[0m")
            print()
        else:
            break
    if program_continue == "N":
        break
       
   
# Housekeeping.

DV = open('defvalues.dat', 'w')
DV.write("{}\n".format(str(POLICY_NUM)))
DV.write("{}\n".format(str(BASIC_PREMIUM)))
DV.write("{}\n".format(str(ADD_CAR_DISCOUNT)))
DV.write("{}\n".format(str(EXTRA_LIABILITY_COST)))
DV.write("{}\n".format(str(GLASS_COVERAGE_COST)))
DV.write("{}\n".format(str(LOANER_CAR_COST)))
DV.write("{}\n".format(str(HST_RATE)))
DV.write("{}\n".format(str(PROCESS_MONTH_FEES)))
DV.close()
 
print()
print("\033[1;34m----------------------------------------------------------------------------------\033[0m")
print("            \033[1;34mThank you for using the One Stop Insurance Company program!\033[0m")
print("\033[1;34m----------------------------------------------------------------------------------\033[0m")
print()