import tkinter as TK

def Basel_1_min_capital(asset_value, asset_type):
    """
    Calculation of the minimum capital requirements for an exposure as prescribed by Basel I.
    CAR: Capital Adequacy Ratio, RW: Risk Weight, RWA: Risk Weighted Assets
    """
    CAR = 0.08;
    mortgage_RW = 0.5;
    non_mortgage_RW = 1;
    
    # Controls:
    asset_types = ['mortgage', 'non-mortgage'];
    if asset_type not in asset_types:
        raise ValueError("Invalid asset type. Expected one of: %s" % asset_types);
    if asset_value < 0:
        raise ValueError("Asset value cannot be negative");
        
    # Calculations:
    if asset_type == 'mortgage':
        RWA = asset_value * mortgage_RW;
    else: RWA = asset_value * non_mortgage_RW;
    return RWA * CAR;

# The window
root = TK.Tk(); # creates the root (main) window
root.title("Basel 1 minimum capital requirements");
root.geometry("510x190"); # the window dimensions

# The radio buttons
asset_type = TK.StringVar(value='mortgage'); # the variable controlled by the radio buttons (string-type object)
# the variable is initialised, otherwise both radio buttons would start as selected
rb1 = TK.Radiobutton(root, text="Mortgage", variable=asset_type, value='mortgage');
rb1.place(x=135, y=20);
rb2 = TK.Radiobutton(root, text="Non-mortgage", variable=asset_type, value='non-mortgage');
rb2.place(x=235, y=20);

# The labels
asset_val = TK.Label(root, text='Asset value:');
asset_val.place(x=130, y=60);
val_entry = TK.Entry(root); # creates an entry widget to accept 1-line inputs
val_entry.place(x=220, y=60);
cap_req = TK.Label(root, text='Capital requirement:');
cap_req.place(x=150, y=140);
req_val = TK.Label(root, text='0'); # to display the calculated capital requirement
req_val.place(x=270, y=140);

# The calculation function
def calc_req():
    the_asset_val = val_entry.get(); # retrieve the value from val_entry    
    if the_asset_val.isnumeric():
        req_val.config(text = Basel_1_min_capital(float(the_asset_val),asset_type.get()));
    else:
        req_val.config(text = 'Asset value must be an unsigned number!');

# The button
calc_button = TK.Button(root, text='Calculate requirement', command=calc_req); # creates a button that calls the calc function
calc_button.place(x=175, y=100);

root.update_idletasks();
root.mainloop();