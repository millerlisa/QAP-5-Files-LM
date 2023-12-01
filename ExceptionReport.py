# Program to process the data file of an insurance company to produce an exception report.
# Written by: Lisa Miller
# Written on: 2023-12-01

# Import the required libraries
import FormatValues as FV
import datetime

# Constants 
today = datetime.date.today().strftime("%d-%b-%y")
pd = open("OSICDef.dat", "r")
policyNumber = int(pd.readline())
premium = float(pd.readline())
discount = float(pd.readline())
liability = float(pd.readline())
glass = float(pd.readline())
loaner = float(pd.readline())
HST_RATE = float(pd.readline())
processingFee = float(pd.readline())
pd.close()
print()
# Monthly Payment Listing - Exception Report
print()
print("ONE STOP INSURANCE COMPANY")
print(f"MONTHLY PAYMENT LISTING AS OF {today}")
print()
print("POLICY CUSTOMER            TOTAL                 TOTAL     DOWN     MONTHLY")
print("NUMBER NAME               PREMIUM       HST      COST     PAYMENT   PAYMENT")
print("===========================================================================")

# Initialize the counter and accumulators
policyCount = 0
policyPremiumAcc = 0
policyExtraAcc = 0
policyTotalAcc = 0
HSTAcc = 0
policyCostAcc = 0
policyDownPayAcc = 0
policyMonthlyPayAcc = 0
# Open the file in read mode
policyFile = open("Policies.dat", "r")
# Loop through the file to process each record
for policyRecord in policyFile:
    policyLst = policyRecord.split(",")
    # Assign variables to each item in the list 
    policyNumber = policyLst[0].strip()
    policyDate = policyLst[1].strip()
    policyDate = datetime.datetime.strptime(policyDate, "%Y-%m-%d")
    customerName = policyLst[2].strip() + " " + policyLst[3].strip()
    policyNumOfCars = int(policyLst[9].strip())
    policyLiability = policyLst[10].strip()
    policyGlass = policyLst[11].strip()
    policyLoaner = policyLst[12].strip()
    policyPayType = policyLst[13].strip()
    policyDownPay = float(policyLst[14].strip())
    policyPremium = 0
    policyExtra = 0
    policyTotal = 0
    policyMonthlyPay = 0
    HST = 0
    policyCost = 0
    # Calculations for report
    if policyPayType == "Monthly" or policyPayType == "Down Pay":
        policyCount += 1
        # Calculate the policyPremium
        if policyNumOfCars == "1":
            policyPremium = premium
        else:
            policyPremium = premium + ((premium * (1 - discount)) * ((policyNumOfCars)-1))
        # Calculate the policyExtra
        # Extra Liability
        if policyLiability == "Y":
            policyExtra += (liability * policyNumOfCars)
        # Extra Glass
        if policyGlass == "Y":
            policyExtra += (glass * policyNumOfCars)
        # Extra Loaner
        if policyLoaner == "Y":
            policyExtra += (loaner * policyNumOfCars)
        # Calculate the policyTotal
        policyTotal = policyPremium + policyExtra  
        # Calculate HST
        HST = policyTotal * HST_RATE
        # Calculate the Cost
        policyCost = policyTotal + HST
        # Calculate the Monthly Payment
        if policyPayType == "Monthly" or policyPayType == "Down Pay":
            policyMonthlyPay = (policyCost - policyDownPay + processingFee)/ 12  
        # Print the detail line
        print(f"{policyNumber:<4s} {customerName:<20s}{FV.FDollar2(policyTotal):>9s}    {FV.FDollar2(HST):>7s}  {FV.FDollar2(policyCost):>9s} {FV.FDollar2(policyDownPay):>9s}{FV.FDollar2(policyMonthlyPay):>9s}")

    # Increment the counter and Accumulate the totals
    
    policyPremiumAcc += policyPremium
    policyExtraAcc += policyExtra
    policyTotalAcc += policyTotal
    HSTAcc += HST
    policyCostAcc += policyCost
    policyDownPayAcc += policyDownPay
    policyMonthlyPayAcc += policyMonthlyPay

# Close the file
policyFile.close()
pd.close()
print("===========================================================================")
# Print the summary line 
print(f"Total policies: {policyCount:<3d}     {FV.FDollar2(policyTotalAcc):>10s}  {FV.FDollar2(HSTAcc):>7s} {FV.FDollar2(policyCostAcc):>10s} {FV.FDollar2(policyDownPayAcc):>9s}{FV.FDollar2(policyMonthlyPayAcc):>9s}")
print()
print()
print()
print()
print()
# Close the file
policyFile.close()
pd.close()