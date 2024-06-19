# This is the step-by-step implementation of a real-world application involving browser and workbook automation.

# ----------------------------------------- STEPS (PHASE 1 - BPM) -------------------------------------------
# Automating the opening of estimates ticket.
# COMPLETE - Step 1) Create a mockup of the real-world workbook.
# COMPLETE - Step 2) Bring BPM automation to the project (Login AND execution)
# COMPLETE - Step 3a) Run the automation from Excel
# COMPLETE - Step 3b) Run the automation WITH parameters
# COMPLETE - Step 4) Optimize VBA to find the correct columns and start from the selected cell
# COMPLETE - Step 5) - VBA Prompt user about valid data.
# COMPLETE - Step 6) Return to Excel after completion, with prompt to accept or cancel sheet recording.
# COMPLETE - Step 7) Record the automation into workbook.
# COMPLETE - Step 7a) open_bpm_ticket function has to read and return the ticket number into main
# COMPLETE - Step 7b) Use a Xlwings' UDF functionality to return ticket number from main to VBA
# COMPLETE - Step 7c) Prompt user to write value into cell and show if cell already has values,
#           appending new ones to existing ones.

# ----------------------------------------- STEPS (PHASE 2 - BPM 2) -------------------------------------------
# Automating the opening of visits ticket.
# COMPLETE - Step 1) Create a new template and define needed variables.
# COMPLETE - Step 2) Obtain Address and City for each possibility
# COMPLETE - Step 3) Create a relation between City and Region
# COMPLETE - Step 3) Refactor the existing code, enabling it to receive different kinds of requests/models.
# COMPLETE - Step 4) Bring the new functionality into existing code
# COMPLETE - Step 5) Move it to production.
# COMPLETE - Step 6) Provide billing dates to facilitate the process' execution.

# ----------------------------------------- STEPS (PHASE 3 - ITSM) -------------------------------------------
# Automating ITSM Tickets with python
# Step 1) Automate ITSM Login
# Step 2) Manipulate history and cookies




# ------------------------------------------------- EXTRAS --------------------------------------------------
# COMPLETE - Extra 1 - Documentation on support.py
# COMPLETE - Extra 2 - Create a UI for new config files
# COMPLETE - Extra 3 - Check if cookies are recent and, if so, simply load them.
# Extra 4 - Implement for several selected clients
# Extra 5 - Error Handling for unexpected conditions (cancellations/timeout >>> always delete time json for safety)
# Extra 6 - Protect sensitive files, even though these don't get uploaded to repo.
# COMPLETE - Extra 7 - If login function runs, use same window instead of opening a new one. (Even use the same tab)
# COMPLETE - Extra 8 - Remove the need for filling in the website on form
# COMPLETE - Extra 9 - Transfer pathing to 'support' script on a 'save cookies function'
# COMPLETE - Extra 10 - Improve VBA code with User Warnings when wrong selections occur
# COMPLETE - Extra 11 - Form now accepts "Enter" key as a valid submit.
# COMPLETE - Extra 12 - Create error handling for clients that are not found in the spreadsheet.
# Extra 7 - Build an option to change login information!

# ------------------------------------------------- IMPORTS -------------------------------------------------

import bpm
import xlwings
from datetime import datetime
# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------------ EXECUTION ------------------------------------------------
# -----------------------------------------------------------------------------------------------------------


# --------------------------------------------- PART 1 - LOGIN ----------------------------------------------

@xlwings.func
def run_bpm(cdie=000000, name="no_name", reason="no_reason", model="no_model",
            start_date=None, end_date=None, billing_date=None):
    driver = bpm.login_user()
    ticket = bpm.open_bpm_ticket(driver)
    bpm.build_bpm_ticket(driver, cdie, name, reason, model, start_date, end_date, billing_date)
    # bpm.close_bpm_ticket(driver)
    # bpm.kill_driver(driver)
    return ticket


# Testing the code
if __name__ == "__main__":
    run_bpm(cdie=413798, model="visit")

