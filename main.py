# This is the step-by-step implementation of a real-world application involving browser and workbook automation.

# ----------------------------------------- STEPS (PHASE 1 - BPM) -------------------------------------------
# COMPLETE - Step 1) Create a mockup of the real-world workbook.
# COMPLETE - Step 2) Bring BPM automation to the project (Login AND execution)
# COMPLETE - Step 3a) Run the automation from Excel
# COMPLETE - Step 3b) Run the automation WITH parameters
# Step 4) Record the automation into workbook
# COMPLETE - Step 5) Optimize VBA to find the correct columns and start from the selected cell
# Step 6) - VBA Prompt user about data.
# Step 7) Production


# ------------------------------------------------- EXTRAS --------------------------------------------------
# Extra 1 - Documentation on support.py
# COMPLETE - Extra 2 - Create a UI for new config files
# COMPLETE - Extra 3 - Check if cookies are recent and, if so, simply load them.
# Extra 4 - Implement for several selected clients
# Extra 5 - Error Handling for unexpected conditions (cancellations/timeout >>> always delete time json for safety)

# ------------------------------------------------- IMPORTS -------------------------------------------------

import bpm

# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------------ EXECUTION ------------------------------------------------
# -----------------------------------------------------------------------------------------------------------


# --------------------------------------------- PART 1 - LOGIN ----------------------------------------------

def main(cdie="no_cdie", name="no_name", reason="no_reason"):

    bpm.login_user()
    driver = bpm.load_cookies()
    bpm.open_bpm_ticket(driver)
    bpm.build_bpm_ticket(driver, cdie, name, reason)


if __name__ == "__main__":
    main()

