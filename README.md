# solar
Solar Energy Investment Assessment Models

# Solar NPV Calculator Script

This Python script calculates the Net Present Value (NPV) and payback period for a solar energy investment based on key inputs. The instructions below will help you run the script using **Visual Studio Code (VS Code)** on your desktop.

---

## 🖥️ **Prerequisites**
1. **Install Python:**  
   - Download and install Python from [python.org](https://www.python.org/). Ensure you check the box **"Add Python to PATH"** during installation.

2. **Install Visual Studio Code (VS Code):**  
   - Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/).

3. **Install Python Extension for VS Code:**  
   - Open VS Code and go to the **Extensions** tab (left sidebar or `Ctrl+Shift+X`).  
   - Search for **Python** and install the one provided by Microsoft.

---

## ⚡ **Step-by-Step Instructions**

### 1. **Set Up Your Project**
- Create a new folder on your computer (e.g., `solar_npv_calculator`).
- Open VS Code and select **File** > **Open Folder** to open the new folder.
- In VS Code, click **File** > **New File**, and save it as `solar_npv_calculator.py`.

### 2. **Install Required Python Packages**
- Open the **Terminal** in VS Code (`Ctrl+`` or View > Terminal).
- In the terminal, run:
  ```bash
  pip install numpy
  ```

### 3. **Run the Script**
- In VS Code, click the **Run** button (top-right corner) or:
  - Open the terminal and run:
    ```bash
    python solar_npv_calculator.py
    ```
- You should see output like:
  ```
  NPV of Solar Investment: $12,345.67
  Estimated Payback Period: 9 years
  ```

---

### 4. ⚙️ **Customize the Inputs**
- Update these lines in the script to reflect your own data:
  ```python
  consumption = 12000  # Your annual consumption (kWh)
  utility_rate = 0.15  # Your utility rate ($/kWh)
  system_cost = 75000  # Your system cost ($)
  interest_rate = 0.05  # Your loan interest rate (if applicable)
  ```
- Save the file and run it again to see the updated results.

---

### 💡 **Optional Enhancements:**
- Add **input()** functions to prompt users for data interactively.
- Integrate with **matplotlib** for graphical output.
- Extend calculations to include tax credits or escalating utility rates.

---

### ✅ **Troubleshooting**
- If `python` doesn't work, try:
  ```bash
  python3 solar_npv_calculator.py
  ```
- Ensure Python and NumPy are correctly installed.
- Check that VS Code is using the correct Python interpreter (**Ctrl+Shift+P** > *Python: Select Interpreter*).

---

Now you're all set to run and explore the financial returns of solar energy investments right from your desktop using VS Code! 🌞📈

