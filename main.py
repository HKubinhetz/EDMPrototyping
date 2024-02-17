# This is the step-by-step implementation of a real-world application involving browser and workbook automation.

# ----------------------------------------- STEPS (PHASE 1 - BPM) -------------------------------------------
# COMPLETE - Step 1) Create a mockup of the real-world workbook.
# COMPLETE - Step 2) Bring BPM automation to the project (Login AND execution)
# COMPLETE - Step 3a) Run the automation from Excel
# COMPLETE - Step 3b) Run the automation WITH parameters
# COMPLETE - Step 4) Optimize VBA to find the correct columns and start from the selected cell
# COMPLETE - Step 5) - VBA Prompt user about valid data.
# Step 6) Create functionality on waiting for process to be approved to return into excel.
#         # True/False for approve or cancel.
# Step 7) Record the automation into workbook.
# COMPLETE - Step 7a) open_bpm_ticket function has to read and return the ticket number into main
# Step 7b) Use an UDF to return ticket number from main to VBA
# Step 7c) Prompt user to write value into cell and show if cell already has values,
#          appending new ones to existing ones.

# ------------------------------------------------- EXTRAS --------------------------------------------------
# COMPLETE - Extra 1 - Documentation on support.py
# COMPLETE - Extra 2 - Create a UI for new config files
# COMPLETE - Extra 3 - Check if cookies are recent and, if so, simply load them.
# Extra 4 - Implement for several selected clients
# Extra 5 - Error Handling for unexpected conditions (cancelations/timeout >>> always delete time json for safety)
# Extra 6 - Protect sensitive files, even though these don't get uploaded to repo.
# Extra 7 - If login function runs, use same window instead of opening a new one. (Even use the same tab)
# COMPLETE - Extra 8 - Remove the need for filling in the website on form
# Extra 8 - Transfer pathing to 'support' script on a 'save cookies function'
# COMPLETE - Extra 9 - Improve VBA code with User Warnings when wrong selections occur

# ------------------------------------------------- IMPORTS -------------------------------------------------

import bpm

# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------------ EXECUTION ------------------------------------------------
# -----------------------------------------------------------------------------------------------------------


# --------------------------------------------- PART 1 - LOGIN ----------------------------------------------

def main(cdie="no_cdie", name="no_name", reason="no_reason"):

    bpm.login_user()
    driver = bpm.load_cookies()
    ticket = bpm.open_bpm_ticket(driver)
    bpm.build_bpm_ticket(driver, cdie, name, reason)
    # bpm.close_bpm_ticket(driver)
    # bpm.kill_driver(driver)
    return ticket


if __name__ == "__main__":
    main()

