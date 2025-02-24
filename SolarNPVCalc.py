import numpy as np

def calculate_npv(consumption_kwh_per_year, utility_rate_per_kwh, system_cost, 
                  interest_rate=0.0, system_lifespan=25, annual_degradation=0.005):
    """
    Calculate the Net Present Value (NPV) of a solar energy investment.

    Parameters:
    - consumption_kwh_per_year: Annual electricity consumption (kWh).
    - utility_rate_per_kwh: Current utility rate ($/kWh).
    - system_cost: Total upfront cost of the solar system ($).
    - interest_rate: Annual loan interest rate (as a decimal).
    - system_lifespan: Expected lifespan of the system (years).
    - annual_degradation: Annual efficiency loss of the solar system (as a decimal).

    Returns:
    - NPV of the solar investment.
    - Payback period in years.
    """
    
    discount_rate = interest_rate if interest_rate > 0 else 0.03  # Default discount rate if no loan
    cash_flows = []
    
    # Calculate yearly savings adjusted for system degradation
    for year in range(1, system_lifespan + 1):
        annual_savings = consumption_kwh_per_year * utility_rate_per_kwh * ((1 - annual_degradation) ** (year - 1))
        discounted_savings = annual_savings / ((1 + discount_rate) ** year)
        cash_flows.append(discounted_savings)

    # Calculate NPV
    npv = -system_cost + sum(cash_flows)

    # Determine payback period
    cumulative_cash_flow = -system_cost
    payback_period = None
    for year, savings in enumerate(cash_flows, start=1):
        cumulative_cash_flow += savings
        if cumulative_cash_flow >= 0:
            payback_period = year
            break

    return npv, payback_period

# Example usage:
if __name__ == "__main__":
    # Example inputs
    consumption = 12000  # kWh per year
    utility_rate = 0.15  # $/kWh
    system_cost = 75000  # $100k system cost
    interest_rate = 0.05  # 5% interest

    npv, payback = calculate_npv(consumption, utility_rate, system_cost, interest_rate)

    print(f"NPV of Solar Investment: ${npv:,.2f}")
    if payback:
        print(f"Estimated Payback Period: {payback} years")
    else:
        print("The investment does not break even within the system's lifespan.")
