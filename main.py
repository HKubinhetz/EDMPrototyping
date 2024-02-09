# This is the step-by-step implementation of a real-world application involving browser and workbook automation.

# ----------------------------------------- STEPS (PHASE 1 - BPM) -------------------------------------------
# COMPLETE - Step 1) Create a mockup of the real-world workbook.
# COMPLETE - Step 2) Bring BPM automation to the project (Login AND execution)
# Step 3a) Run the automation from Excel
# Step 3b) Run the automation WITH parameters
# Step 4) Record the automation into workbook
# Step 5) Tests and error handling
# Step 6) Production


# ------------------------------------------------- EXTRAS --------------------------------------------------
# Extra 1 - Documentation on support.py
# Extra 2 - Create a Tkinter UI for new config files
# Extra 3 - Check if cookies are recent and, if so simply load them.

# ------------------------------------------------- IMPORTS -------------------------------------------------

import bpm

# -----------------------------------------------------------------------------------------------------------
# ------------------------------------------------ EXECUTION ------------------------------------------------
# -----------------------------------------------------------------------------------------------------------


# --------------------------------------------- PART 1 - LOGIN ----------------------------------------------

bpm.login_user()
driver = bpm.load_cookies()
bpm.open_bpm_ticket(driver)
bpm.build_bpm_ticket(driver)