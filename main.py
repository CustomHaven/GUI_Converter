from tkinter import Tk, Label, Button, Entry

def miles_to_km():
  if input.get().isnumeric():
    kilometers = float(input.get()) * 1.609
    result.config(text=f"{kilometers:.2f}")
  else:
    print("input is not a type int.")

# Window
window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=100, height=100)
window.config(padx=20, pady=20, background="white")

# Labels
equal = Label(text="is equal to", background="white")
miles = Label(text="Miles", background="white")
km = Label(text="Km", background="white")
result = Label(text="0", background="white")


# Button
button = Button(text="Calculate", command=miles_to_km)

# Entry
input = Entry(width=7)
# input.insert(END, string="0")


# Grids
input.grid(column=1, row=0)
miles.grid(column=2, row=0)
equal.grid(column=0, row=1)
result.grid(column=1, row=1)
km.grid(column=2, row=1)
button.grid(column=1, row=2)

window.mainloop()