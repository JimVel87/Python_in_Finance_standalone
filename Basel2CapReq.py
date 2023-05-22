import tkinter as TK
from tkinter import ttk

# Dictionary for risk weights by group and credit rating:
# SOV1~6: Claims on sovereigns
# IFI: Claims on the BIS, the IMF, the ECB, the EC and the MDBs
# BSC1~6: Claims on banks and securities companies
# CRP1~5: Claims on corporates
# RET: Claims on retail products
# RES: Claims secured by residential property
# COM: Claims secured by commercial real estate
# OVD1~3: Overdue loans
# OTH: Other assets
# CSH: Cash

risk_weight = {
# Sovereigns:
    'SOV1': 0,   # AAA to AA-
    'SOV2': 0.2, # A+ to A-
    'SOV3': 0.5, # BBB+ to BBB-
    'SOV4': 1,   # BB+ to B-
    'SOV5': 1.5, # Below B-
    'SOV6': 1,   # Unrated
# International financial institutions:
    'IFI': 0,
# Banks and securities companies:
    'BSC1': 0.2, # AAA to AA-
    'BSC2': 0.5, # A+ to A-
    'BSC3': 1,   # BBB+ to BBB-
    'BSC4': 1,   # BB+ to B-
    'BSC5': 1.5, # Below B-
    'BSC6': 1,   # Unrated
# Corporates:
    'CRP1': 0.2, # AAA to AA-
    'CRP2': 0.5, # A+ to A-
    'CRP3': 1,   # BBB+ to BB-
    'CRP4': 1.5, # Below BB-
    'CRP5': 1,   # Unrated
# Retail:
    'RET': 0.75,
# Residential property:
    'RES': 0.35,
# Commercial property:
    'COM': 1,
# Overdue loans (90days+ excl res. mortgages):
    'OVD1': 1.5, # less than 20% of outstanding amount
    'OVD2': 1,   # 20% ~ 49% of outstanding amount
    'OVD3': 1,   # at least 50% of outstanding amount
# Other:
    'OTH': 1,
# Cash:
    'CSH': 0
};

def Basel_2_min_cap_SA(asset_value, asset_type):
    """
    Calculation of the minimum capital requirements for an exposure as prescribed by Basel II, using the Standardised Approach.
    CAR: Capital Adequacy Ratio, RWA: Risk Weighted Assets
    """
    CAR = 0.08;

    # Controls:
    if asset_value < 0:
        raise ValueError("Asset value cannot be negative");

    # Calculations:
    RWA = asset_value * risk_weight[asset_type]; # the risk weight comes from the dictionary
    return RWA * CAR;

def Basel_2_min_cap_IRB(PD, LGD, EAD):
    """
    Calculation of the minimum capital requirements for an exposure as prescribed by Basel II, using the Internal Ratings Based approach.
    PD: Probability of Default, LGD: Loss Given Default, EAD: Exposure At Default
    """
    
    # Controls:
    if PD > 1 or PD < 0:
        raise ValueError("Probability of default must be between 0 and 1");
    if LGD > 1 or LGD < 0:
        raise ValueError("Loss given default must be between 0 and 1");
    if EAD < 0:
        raise ValueError("Exposure at default cannot be negative");

    # Calculation:
    return PD * LGD * EAD;

def is_float(string): # function to check if input is a number (int or float)
    try:
        float(string); # try converting the string to float
        return True; # if successful, return true
    except ValueError:
        return False; # otherwise, return false

# The window
root = TK.Tk(); # creates the root (main) window
root.title("Basel 2 minimum capital requirements");
root.geometry("580x340"); # the window dimensions

# The tabs
root_notebook = ttk.Notebook(root) # creating a notebook to hold the tabs (frames)
tab_SA = ttk.Frame(root_notebook);
tab_IRB = ttk.Frame(root_notebook);
root_notebook.add(tab_SA, text ='Standardised Approach');
root_notebook.add(tab_IRB, text ='Internal Ratings Based');
root_notebook.pack(expand = 1, fill ="both");

#################### tab Standardised Approach ####################

# Constants for widget alignment
COL1 = 20;
COL2 = 130;
COL3 = 250;
COL4 = 350;
ROW1 = 20;
ROW2 = 40;
ROW3 = 60;
ROW4 = 80;
ROW5 = 100;
ROW6 = 120;
ROW7 = 140;
ROW8 = 160;
ROW9 = 180;

# The radio buttons with their labels
asset_type = TK.StringVar(value='SOV1'); # the variable controlled by the radio buttons (string-type object)
# the variable is initialised, otherwise all radio buttons would start as selected
sov_label = TK.Label(tab_SA, text='Sovereigns:');
sov_label.place(x=COL1, y=ROW1);
sov1 = TK.Radiobutton(tab_SA, text='AAA to AA-', variable=asset_type, value='SOV1');
sov1.place(x=COL1, y=ROW2);
sov2 = TK.Radiobutton(tab_SA, text='A+ to A-', variable=asset_type, value='SOV2');
sov2.place(x=COL1, y=ROW3);
sov3 = TK.Radiobutton(tab_SA, text='BBB+ to BBB-', variable=asset_type, value='SOV3');
sov3.place(x=COL1, y=ROW4);
sov4 = TK.Radiobutton(tab_SA, text='BB+ to B-', variable=asset_type, value='SOV4');
sov4.place(x=COL1, y=ROW5);
sov5 = TK.Radiobutton(tab_SA, text='Below B-', variable=asset_type, value='SOV5');
sov5.place(x=COL1, y=ROW6);
sov6 = TK.Radiobutton(tab_SA, text='Unrated', variable=asset_type, value='SOV6');
sov6.place(x=COL1, y=ROW7);
ret = TK.Radiobutton(tab_SA, text='Retail', variable=asset_type, value='RET');
ret.place(x=COL1, y=ROW9);
bsc_label = TK.Label(tab_SA, text='Banks and securities companies:', wraplength=120, justify='left');
bsc_label.place(x=COL2, y=ROW1);
bsc1 = TK.Radiobutton(tab_SA, text='AAA to AA-', variable=asset_type, value='BSC1');
bsc1.place(x=COL2, y=ROW3);
bsc2 = TK.Radiobutton(tab_SA, text='A+ to A-', variable=asset_type, value='BSC2');
bsc2.place(x=COL2, y=ROW4);
bsc3 = TK.Radiobutton(tab_SA, text='BBB+ to BBB-', variable=asset_type, value='BSC3');
bsc3.place(x=COL2, y=ROW5);
bsc4 = TK.Radiobutton(tab_SA, text='BB+ to B-', variable=asset_type, value='BSC4');
bsc4.place(x=COL2, y=ROW6);
bsc5 = TK.Radiobutton(tab_SA, text='Below B-', variable=asset_type, value='BSC5');
bsc5.place(x=COL2, y=ROW7);
bsc6 = TK.Radiobutton(tab_SA, text='Unrated', variable=asset_type, value='BSC6');
bsc6.place(x=COL2, y=ROW8);
crp_label = TK.Label(tab_SA, text='Corporates:');
crp_label.place(x=COL3, y=ROW1);
crp1 = TK.Radiobutton(tab_SA, text='AAA to AA-', variable=asset_type, value='CRP1');
crp1.place(x=COL3, y=ROW2);
crp2 = TK.Radiobutton(tab_SA, text='A+ to A-', variable=asset_type, value='CRP2');
crp2.place(x=COL3, y=ROW3);
crp3 = TK.Radiobutton(tab_SA, text='BBB+ to BB-', variable=asset_type, value='CRP3');
crp3.place(x=COL3, y=ROW4);
crp4 = TK.Radiobutton(tab_SA, text='Below BB-', variable=asset_type, value='CRP4');
crp4.place(x=COL3, y=ROW5);
crp5 = TK.Radiobutton(tab_SA, text='Unrated', variable=asset_type, value='CRP5');
crp5.place(x=COL3, y=ROW6);
csh = TK.Radiobutton(tab_SA, text='Cash', variable=asset_type, value='CSH');
csh.place(x=COL3, y=ROW8);
oth = TK.Radiobutton(tab_SA, text='Other', variable=asset_type, value='OTH');
oth.place(x=COL3, y=ROW9);
ovd_label = TK.Label(tab_SA, text='Overdue loans:');
ovd_label.place(x=COL4, y=ROW1);
ovd1 = TK.Radiobutton(tab_SA, text='less than 20% of outstanding', variable=asset_type, value='OVD1');
ovd1.place(x=COL4, y=ROW2);
ovd2 = TK.Radiobutton(tab_SA, text='20% ~ 49% of outstanding', variable=asset_type, value='OVD2');
ovd2.place(x=COL4, y=ROW3);
ovd3 = TK.Radiobutton(tab_SA, text='at least 50% of outstanding', variable=asset_type, value='OVD3');
ovd3.place(x=COL4, y=ROW4);
res = TK.Radiobutton(tab_SA, text='Residential property', variable=asset_type, value='RES');
res.place(x=COL4, y=ROW6);
com = TK.Radiobutton(tab_SA, text='Commercial property', variable=asset_type, value='COM');
com.place(x=COL4, y=ROW7);
ifi = TK.Radiobutton(tab_SA, text='International Financial Institution', variable=asset_type, value='IFI');
ifi.place(x=COL4, y=ROW9);

# The bottom labels
asset_val = TK.Label(tab_SA, text='Asset value:');
asset_val.place(x=20, y=220);
val_entry = TK.Entry(tab_SA); # creates an entry widget to accept 1-line inputs
val_entry.place(x=100, y=220);
cap_req_SA = TK.Label(tab_SA, text='Capital requirement:');
cap_req_SA.place(x=180, y=280);
req_val_SA = TK.Label(tab_SA, text='0'); # to display the calculated capital requirement
req_val_SA.place(x=300, y=280);

# The calculation function
def calc_req_SA():
    if is_float(val_entry.get()):
        req_val_SA.config(text = Basel_2_min_cap_SA(float(val_entry.get()),asset_type.get()));
    else:
        req_val_SA.config(text = 'Asset value must be a number!');

# The button
calc_button_SA = TK.Button(tab_SA, text='Calculate requirement', command=calc_req_SA); # creates a button that calls the calc function
calc_button_SA.place(x=320, y=220);

#################### tab Internal Ratings Based ####################

# The labels
PD_label = TK.Label(tab_IRB, text='Probability of default:');
PD_label.place(x=20, y=20);
PD_val = TK.Entry(tab_IRB);
PD_val.place(x=150, y=20);
LGD_label = TK.Label(tab_IRB, text='Loss given default:');
LGD_label.place(x=20, y=60);
LGD_val = TK.Entry(tab_IRB);
LGD_val.place(x=150, y=60);
EAD_label = TK.Label(tab_IRB, text='Exposure at default:');
EAD_label.place(x=20, y=100);
EAD_val = TK.Entry(tab_IRB);
EAD_val.place(x=150, y=100);
cap_req_IRB = TK.Label(tab_IRB, text='Capital requirement:');
cap_req_IRB.place(x=100, y=200);
req_val_IRB = TK.Label(tab_IRB, text='0'); # to display the calculated capital requirement
req_val_IRB.place(x=220, y=200);

# The calculation function
def calc_req_IRB():
    if is_float(PD_val.get()) and is_float(LGD_val.get()) and is_float(EAD_val.get()):
        req_val_IRB.config(text = Basel_2_min_cap_IRB(float(PD_val.get()), float(LGD_val.get()), float(EAD_val.get())));
    else:
        req_val_IRB.config(text = 'All inputs must be numbers!');

# The button
calc_button_IRB = TK.Button(tab_IRB, text='Calculate requirement', command=calc_req_IRB); # creates a button that calls the calc function
calc_button_IRB.place(x=100, y=140);

root.update_idletasks();
root.mainloop();