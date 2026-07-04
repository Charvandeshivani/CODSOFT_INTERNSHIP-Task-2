import math
import os
import random
from datetime import datetime

# --- COLOR CONSTANTS FOR ATTRACTIVE CLI ---
CLR_HEADER = "\033[95m"
CLR_BLUE = "\033[94m"
CLR_CYAN = "\033[96m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"
CLR_DIM = "\033[90m"

# --- INTUITIVE MATH QUOTES ---
QUOTES = [
    "Pure mathematics is, in its way, the poetry of logical ideas. - Albert Einstein",
    "Mathematics is the most beautiful and most powerful creation of the human spirit. - Stefan Banach",
    "Wherever there is number, there is beauty. - Proclus",
    "Nature is written in mathematical language. - Galileo Galilei",
]


class CalculatorEngine:
    """Handles arithmetic evaluations, execution validation, and runtime history logging."""

    def __init__(self):
        self.history = []

    def log_history(self, expression, result):
        """Appends computation parameters cleanly into internal stack records."""
        timestamp = datetime.now().strftime("%I:%M:%S %p")
        self.history.append(f"[{timestamp}] {expression} = {CLR_GREEN}{result}{CLR_RESET}")

    def safe_add(self, a, b):
        res = a + b
        self.log_history(f"{a} + {b}", res)
        return res

    def safe_subtract(self, a, b):
        res = a - b
        self.log_history(f"{a} - {b}", res)
        return res

    def safe_multiply(self, a, b):
        res = a * b
        self.log_history(f"{a} × {b}", res)
        return res

    def safe_divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Math Error: Division by Zero is undefined.")
        res = a / b
        self.log_history(f"{a} ÷ {b}", res)
        return res

    def safe_power(self, base, exp):
        res = math.pow(base, exp)
        self.log_history(f"{base} ^ {exp}", res)
        return res

    def safe_sqrt(self, val):
        if val < 0:
            raise ValueError("Math Error: Square root of a negative number requires complex logic.")
        res = math.sqrt(val)
        self.log_history(f"√({val})", res)
        return res

    def safe_percentage(self, total, pct):
        res = (pct / 100) * total
        self.log_history(f"{pct}% of {total}", res)
        return res


# --- USER INTERFACE DESIGN LAYOUTS ---

def display_header():
    """Renders the aesthetic dashboard welcome screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    now = datetime.now().strftime("%A, %B %d, %Y | %I:%M %p")
    quote = random.choice(QUOTES)

    print(f"{CLR_HEADER}========================================================================={CLR_RESET}")
    print(f"{CLR_CYAN}{CLR_BOLD}🧮 INTELLIGENT COMPUTE CORE & CALCULATION ENGINE{CLR_RESET}")
    print(f"{CLR_BLUE}📅 {now}{CLR_RESET}")
    print(f"{CLR_HEADER}========================================================================={CLR_RESET}")
    print(f"{CLR_YELLOW}💡 \"{quote}\"{CLR_RESET}")
    print(f"{CLR_HEADER}-------------------------------------------------------------------------{CLR_RESET}\n")


def display_history_panel(calc):
    """Draws computational logs matrix trace securely."""
    print(f"{CLR_BOLD}📜 RUNTIME MEMORY ARCHIVE (LATEST 5):{CLR_RESET}")
    if not calc.history:
        print(f"   {CLR_DIM}[Memory Stack is Empty]{CLR_RESET}\n")
    else:
        # Show last 5 equations computed to keep layout compact
        for item in calc.history[-5:]:
            print(f"   {item}")
        print()


def get_numeric_input(prompt):
    """Guards against string value format errors during conversions."""
    while True:
        try:
            val = input(prompt).strip()
            if not val:
                print(f"   {CLR_RED}❌ Input field cannot be empty.{CLR_RESET}")
                continue
            return float(val)
        except ValueError:
            print(f"   {CLR_RED}❌ Verification Fault: Please pass a clean numerical digit.{CLR_RESET}")


# --- MAIN EVENT EXECUTION LAYER ---

def main():
    calc = CalculatorEngine()

    while True:
        display_header()
        display_history_panel(calc)

        # Vector Grid of Operations
        print(f"{CLR_BOLD}⚙️  MATHEMATICAL CORE ENGINE OPERATIONS:{CLR_RESET}")
        print(f"   {CLR_CYAN}[1]{CLR_RESET} Addition ➕        {CLR_CYAN}[2]{CLR_RESET} Subtraction ➖     {CLR_CYAN}[3]{CLR_RESET} Multiplication ✖️")
        print(f"   {CLR_CYAN}[4]{CLR_RESET} Division ➗       {CLR_CYAN}[5]{CLR_RESET} Power (x^y) 🔢     {CLR_CYAN}[6]{CLR_RESET} Square Root √")
        print(f"   {CLR_CYAN}[7]{CLR_RESET} Percentage 📊     {CLR_CYAN}[8]{CLR_RESET} Clear Logs 🗑       {CLR_CYAN}[9]{CLR_RESET} Shut Down Engine 🎉")
        print(f"{CLR_HEADER}-------------------------------------------------------------------------{CLR_RESET}")
        
        choice = input(f"{CLR_BOLD}👉 Choice (1-9): {CLR_RESET}").strip()

        try:
            if choice in ["1", "2", "3", "4", "5"]:
                print(f"\n{CLR_BOLD}🔣 PARAMETER MATRIX ARGS:{CLR_RESET}")
                num1 = get_numeric_input("   Enter First Number: ")
                num2 = get_numeric_input("   Enter Second Number: ")
                
                print(f"\n{CLR_BOLD}📊 EVALUATION OUTPUT:{CLR_RESET}")
                if choice == "1":
                    res = calc.safe_add(num1, num2)
                    print(f"   Result: {num1} + {num2} = {CLR_GREEN}{CLR_BOLD}{res}{CLR_RESET}")
                elif choice == "2":
                    res = calc.safe_subtract(num1, num2)
                    print(f"   Result: {num1} - {num2} = {CLR_GREEN}{CLR_BOLD}{res}{CLR_RESET}")
                elif choice == "3":
                    res = calc.safe_multiply(num1, num2)
                    print(f"   Result: {num1} × {num2} = {CLR_GREEN}{CLR_BOLD}{res}{CLR_RESET}")
                elif choice == "4":
                    res = calc.safe_divide(num1, num2)
                    print(f"   Result: {num1} ÷ {num2} = {CLR_GREEN}{CLR_BOLD}{res}{CLR_RESET}")
                elif choice == "5":
                    res = calc.safe_power(num1, num2)
                    print(f"   Result: {num1} ^ {num2} = {CLR_GREEN}{CLR_BOLD}{res}{CLR_RESET}")
                
                input("\nPress Enter to clear register...")

            elif choice == "6":
                print(f"\n{CLR_BOLD}📐 SQUARE ROOT ARG:{CLR_RESET}")
                val = get_numeric_input("   Enter Radicand Number: ")
                res = calc.safe_sqrt(val)
                print(f"\n{CLR_BOLD}📊 EVALUATION OUTPUT:{CLR_RESET}")
                print(f"   Result: √({val}) = {CLR_GREEN}{CLR_BOLD}{res}{CLR_RESET}")
                input("\nPress Enter to clear register...")

            elif choice == "7":
                print(f"\n{CLR_BOLD}📊 PERCENTAGE ALGORITHM:{CLR_RESET}")
                total = get_numeric_input("   Enter Total Amount base: ")
                pct = get_numeric_input("   Enter Target Percentage rate (%): ")
                res = calc.safe_percentage(total, pct)
                print(f"\n{CLR_BOLD}📊 EVALUATION OUTPUT:{CLR_RESET}")
                print(f"   Result: {pct}% of {total} = {CLR_GREEN}{CLR_BOLD}{res}{CLR_RESET}")
                input("\nPress Enter to clear register...")

            elif choice == "8":
                calc.history.clear()
                print(f"\n   {CLR_GREEN}🧹 Computational cache storage cleared down to 0 bytes!{CLR_RESET}")
                input("\nPress Enter...")

            elif choice == "9":
                # --- PROFESSIONAL INTERACTIVE EXIT SCREEN ---
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\n\n{CLR_HEADER}========================================================================={CLR_RESET}")
                print(f"{CLR_CYAN}{CLR_BOLD}🌟 SHUTTING DOWN CORE CALCULATION FRAMEWORK...{CLR_RESET}")
                print(f"{CLR_BLUE}   Runtime states released and system threads terminated gracefully.{CLR_RESET}")
                print(f"   Keep up the math analytics! See you soon! 📊🔬👋🏼")
                print(f"{CLR_HEADER}========================================================================={CLR_RESET}\n\n")
                break
            else:
                print(f"   {CLR_RED}❌ Choice Index Out of Bounds. Select values (1-9).{CLR_RESET}")
                input("\nPress Enter...")

        except (ZeroDivisionError, ValueError) as math_err:
            print(f"\n{CLR_BOLD}📊 EVALUATION OUTPUT:{CLR_RESET}")
            print(f"   {CLR_RED}⚠ Runtime Failure: {math_err}{CLR_RESET}")
            input("\nPress Enter to adjust values...")
        except Exception as e:
            print(f"\n   {CLR_RED}⚠ Fatal Core Exception: {e}{CLR_RESET}")
            input("\nPress Enter...")


if __name__ == "__main__":
    main()