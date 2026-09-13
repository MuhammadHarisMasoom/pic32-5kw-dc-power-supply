from tkinter import *
import serial
import serial.tools.list_ports as port_list

# Serial port initialization
ser = serial.Serial(None, 115200)

# Initializing main window

window = Tk()
window.title("Power Supply")
window.minsize(width=700, height=500)
window.config(padx=100, pady=50)


# # # ---------------------------- ON ------------------------------------------- #
# # # --------------------------------------------------------------------------- #


def on_button():
   ser.write(b'O') # Selector for ON
   ser.write(b'\x80') # hex byte for turning on the power supply
   # print("on")


on_image= PhotoImage(file='on.png')
ON_button= Button(window, image=on_image,command= on_button, borderwidth=0)
ON_button.grid(row=0, column=1)

# # # ---------------------------- OFF ------------------------------------------- #
# # # --------------------------------------------------------------------------- #

def off_button():
   ser.write(b'X') # Selector for OFF
   ser.write(b'\x00') # hex byte for turning off the power supply
   # print("off")

off_image= PhotoImage(file='off.png')
OFF_button = Button(window, image=off_image,command= off_button, borderwidth=0)
OFF_button.grid(row=0, column=2)

# # # ---------------------------- Factory Reset -------------------------------- #
# # # --------------------------------------------------------------------------- #

def factory_reset_button():
    ser.write(b'Q') # Selector for factory reset
    ser.write(b'\x12') # hex byte for factory resetting power supply
   # print("factory reset done")

factory_reset_image= PhotoImage(file='factory reset.png')
factory_reset_button = Button(window, image=factory_reset_image,command= factory_reset_button, borderwidth=0)
factory_reset_button.grid(row=0, column=3)

# # # ---------------------------- Read Data from Power Supply and Display ------------------------------------------- #

# Label to display the received voltage
received_voltage_label = Label(text="Vout:", font=("Arial", 24))
received_voltage_label.grid(row=1, column=3)

# Label to display the received current
received_current_label = Label(text="Iout:", font=("Arial", 24))
received_current_label.grid(row=2, column=3)

def read_data_from_power_supply():
    try:
        if ser.in_waiting:  # Check if data is available
            selector = ser.read(1)
            read_data_msb = ser.read(1)  # Read 1 byte
            read_data_lsb = ser.read(1)  # Read 1 byte

            read_data_lsb = int.from_bytes(read_data_lsb)  # converting byte to int
            read_data_msb = int.from_bytes(read_data_msb)
            read_data = round((read_data_msb * 256 + read_data_lsb)/256,2)

            print(selector)
            print(read_data_msb)
            print(read_data_lsb)
            print(read_data)

            if selector == b'v':
                received_voltage_label.config(text=f"Vout: {read_data}")
            elif selector == b'i':
                received_current_label.config(text=f"Iout: {read_data}")
            # elif selector == b't':
            #     received_temperature_label.config(text=f"Tempout: {read_data}")
            # elif selector == b'f':
            #     received_fan_label.config(text=f"Fanout: {read_data}")
    except Exception as e:
        print(f"Error reading data: {e}")
    # Schedule the read_data function to run again after 1000ms (1 second)
    window.after(1000, read_data_from_power_supply)

# Start the reading loop
window.after(1000, read_data_from_power_supply)

# # ---------------------------- Voltage Write -------------------------------- #
def write_voltage(event):
   voltage = voltage_write_entry.get()  # Get the value from the Entry widget
   voltage = int(voltage)
   voltage = int.to_bytes(voltage)
   ser.write(b'V')
   ser.write(voltage)



voltage_write_label = Label(text="Vin", font=("Arial", 24))
voltage_write_label.grid(row=1, column=1)
voltage_write_entry = Entry(width=12)
voltage_write_entry.grid(row=1, column=2)
voltage_write_entry.bind("<Return>", write_voltage)

# # ---------------------------- Current Write ------------------------#
def write_current(event):
   current = current_write_entry.get()  # Get the value from the Entry widget
   current = int(current)
   current = int.to_bytes(current)
   ser.write(b'I')
   ser.write(current)


current_write_label = Label(text="Iin", font=("Arial", 24))
current_write_label.grid(row=2, column=1)
current_write_entry = Entry(width=12)
current_write_entry.grid(row=2, column=2)
current_write_entry.bind("<Return>", write_current)

# # # # ---------------------------- Fan Speed Write ------------------------------------------- #
def write_fan(event):
   fan = fan_write_entry.get()  # Get the value from the Entry widget
   fan = int(fan)
   fan = int.to_bytes(fan)
   ser.write(b'F')
   ser.write(fan)

fan_write_label = Label(text="Fan Speed", font=("Arial", 24))
fan_write_label.grid(row=3, column=1)
fan_write_entry = Entry(width=12)
fan_write_entry.grid(row=3, column=2)
fan_write_entry.bind("<Return>", write_fan)

########################################################################
#   Drop down Menu for COM Port selection
########################################################################
p = list(port_list.comports())
t = []

for a in range(len(p)):
    t.append(p[a][0])
    print(t)

variable = StringVar(window)
variable_p = StringVar(window)
variable.set(t[0])

# on change dropdown value
def change_dropdown(*args):
    return variable.get()

w = OptionMenu(window, variable,command = change_dropdown, *t)
w.grid(row = 10, column =2)
port = t[0]

s = serial.Serial(port, timeout=3)

window.mainloop()