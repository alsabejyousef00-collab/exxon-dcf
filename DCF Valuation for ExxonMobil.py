# Exxon DCF Model

# Assumptions:

rev_25 = 323_905 # in millions
rev_growth_rates = [-0.02,-0.015, -0.01, 0.015, 0.02]
operating_margin = 0.105 # 10.5%
tax_rate = 0.28
wacc = 0.092 

# Calculate revenues for next 5 years

revenues = [rev_25]
for growth in rev_growth_rates:
    revenues.append(revenues[-1] * (1+growth))

print('Revenues $(millions):')
for i, rev in enumerate(revenues):
        print(f"Year {i}: ${rev:,.0f}")

operating_margins = [0.102, 0.1, 0.098, 0.1, 0.101]

# Calculate operating income 

operating_incomes = []
for i in range(1,len(revenues)): # Start from Year 1 (skip Year 0)
      oi = revenues[i] * operating_margins[i-1]
      operating_incomes.append(oi)

print('\nOperating Income $(millions):')
for i, oi in enumerate(operating_incomes, 1):
    print(f"Year {i}: ${oi:,.0f}")


# Depreciation and Capex as % of revenue

depreciation_pct = 0.08
capex_pct = 0.075
wc_change = 0.005 # Working capital change

# Calculate Free Cash Flow 

fcf = []
for i in range(1,len(revenues)):
    nopat = operating_incomes[i-1]*(1-tax_rate)
    depreciation = revenues[i]* depreciation_pct
    capex = revenues[i] * capex_pct
    wc_change_amnt = revenues[i] * wc_change
    fcf_year = nopat + depreciation - capex - wc_change_amnt
    fcf.append(fcf_year)

print('\nFree Cash Flow $(millions):')
for i, fcf_year in enumerate(fcf,1):
     print(f'Year {i}: ${fcf_year:,.0f}')


# Discount cash flows to present values 

pv_fcf = []
for year, fcf_year in enumerate(fcf, 1):
     pv = fcf_year / ((1+wacc)**year)
     pv_fcf.append(pv)

print('\nPresent Value of FCF $(millions):')
for i, pv in enumerate(pv_fcf, 1):
     print(f"Year{i}: ${pv:,.0f}")

 # Sum of discounted Cast Flows

sum_pv_fcf = sum(pv_fcf)

print(f"\nSum of PV of FCF (Years 1-5): ${sum_pv_fcf:,.0f}")

# Terminal Value 
terminal_growth = 0.005
terminal_fcf = fcf[-1] * (1+terminal_growth)
terminal_value = terminal_fcf/(wacc-terminal_growth)
pv_terminal_value = terminal_value / ((1+wacc) ** len(fcf))

print(f"\nTerminal Value: ${terminal_value:,.0f}")
print(f"PV of Terminal value: ${pv_terminal_value:,.0f}")

# Enterprise Value

enterprise_value = sum_pv_fcf + pv_terminal_value 
print(f"\nEnterprise Value: ${enterprise_value:,.0f}")

# Equity Value and Per-Share Value

net_debt = 43_547 - 10_681 # Debt - Cash (in millions)
shares_outstanding = 4_305 # in millions

equity_value = enterprise_value - net_debt
intrinsic_value_per_share = equity_value / shares_outstanding

print(f"\nNet Debt: ${net_debt:,.0f}M")
print(f"Equity value: ${equity_value:,.0f}")
print(f"Shares Outstanding: {shares_outstanding:,.0f}M")
print(f"Intrinsiv Value Per Share: ${intrinsic_value_per_share:,.2f}")
print(f"\nCurrent Stock Price: $~146")
print(f"Upside/(Downside): {((146/intrinsic_value_per_share - 1) * 100):.1f}%")