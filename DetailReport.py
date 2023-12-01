# Program to process the data file of an insurance company to produce a detailed report.
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

# Policy Listing - Detailed Report
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF {today}")
print()
print("POLICY CUSTOMER             POLICY     INSURANCE     EXTRA     TOTAL")
print("NUMBER NAME                  DATE       PREMIUM      COSTS    PREMIUM")
print("======================================================================")

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
    policyPremium = 0
    policyExtra = 0
    policyTotal = 0
    policyMonthlyPay = 0
    # Calculations for report
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
    # Print the detail line
    print(f" {policyNumber:<4s}  {customerName:<20s}{FV.FDateS(policyDate):<10s}  {FV.FDollar2(policyPremium):>9s}  {FV.FDollar2(policyExtra):>9s}  {FV.FDollar2(policyTotal):>9s}")

    # Increment the counter and Accumulate the totals
    policyCount += 1
    policyPremiumAcc += policyPremium
    policyExtraAcc += policyExtra
    policyTotalAcc += policyTotal

print("======================================================================")
# Print the summary line 
print(f"Total policies: {policyCount:<3d}                   {FV.FDollar2(policyPremiumAcc):>9s}  {FV.FDollar2(policyExtraAcc):>9s} {FV.FDollar2(policyTotalAcc):>9s}")
print()
print()
print()
print()
print()
# Close the file
policyFile.close()
pd.close()