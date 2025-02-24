# Solar NPV Calculator Script

# This Python script calculates the Net Present Value (NPV) and payback period for a solar energy investment based on key inputs. 
# The instructions below will help you run the script using **Visual Studio Code (VS Code)** on your desktop.

## 🖥️ **Prerequisites**

# 1. **Install Python:**  
#   - Download and install Python from [python.org](https://www.python.org/). Ensure you check the box **"Add Python to PATH"** during installation.

# 2. **Install Visual Studio Code (VS Code):**  
#   - Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/).

# 3. **Install Python Extension for VS Code:**  
#   - Open VS Code and go to the **Extensions** tab (left sidebar or `Ctrl+Shift+X`).  
#   - Search for **Python** and install the one provided by Microsoft.

# 4. **Install Required Python Packages:**  
#   - Open the **Terminal** in VS Code (`Ctrl+`` or View > Terminal) and run:
#    ```bash
#     pip install numpy
#     ```

#---

## ⚡ **Step-by-Step Instructions**

### 1. **Set Up Your Project**
#- Create a new folder on your computer (e.g., `solar_npv_calculator`).
#- Open VS Code and select **File** > **Open Folder** to open the new folder.
#- In VS Code, click **File** > **New File**, and save it as `solar_npv_calculator.py`.

### 2. **Add the Python Script**
#- Copy and paste the following code into `solar_npv_calculator.py`:

#```python
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
    system_cost = 75000  # $75k system cost
    interest_rate = 0.05  # 5% interest

    npv, payback = calculate_npv(consumption, utility_rate, system_cost, interest_rate)

    print(f"NPV of Solar Investment: ${npv:,.2f}")
    if payback:
        print(f"Estimated Payback Period: {payback} years")
    else:
        print("The investment does not break even within the system's lifespan.")
#```

#---

### 3. **Run the Script**
#- In VS Code, click the **Run** button (top-right corner) or:
#  - Open the terminal and run:
#    ```bash
#    python solar_npv_calculator.py
#    ```
#- You should see output like:
#  ```
#  NPV of Solar Investment: $12,345.67
#  Estimated Payback Period: 9 years
#  ```

#---

### 4. ⚙️ **Customize the Inputs**
#- Update these lines in the script to reflect your own data:
#  ```python
#  consumption = 12000  # Your annual consumption (kWh)
#  utility_rate = 0.15  # Your utility rate ($/kWh)
#  system_cost = 75000  # Your system cost ($)
#  interest_rate = 0.05  # Your loan interest rate (if applicable)
##  ```
#- Save the file and run it again to see the updated results.

# ---

### 💡 **Optional Enhancements:**
#- Add **input()** functions to prompt users for data interactively.
#- Integrate additional financial metrics such as Internal Rate of Return (IRR).
#- Consider adding functionality to factor in local tax credits or escalating utility rates.

#---

### ✅ **Troubleshooting**
#- If python does not work, try:
#  ```bash
#  python3 solar_npv_calculator.py
#  ```
#- Ensure Python and NumPy are correctly installed.
#- Check that VS Code is using the correct Python interpreter (**Ctrl+Shift+P** > *Python: Select Interpreter*).
#- If you encounter a `ModuleNotFoundError` for `numpy`, ensure you have installed it with:
#  ```bash
#  pip install numpy
#  ```
