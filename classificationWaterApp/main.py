import tkinter
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import pickle

file_mode = "svc_model.pickle"
svc_model = pickle.load(open(file_mode, "rb"))
    

window = tkinter.Tk()
window.title("Classification Water Quatity use SVM Model")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="Feature Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

ph_label = tkinter.Label(user_info_frame, text="pH value")
ph_label.grid(row=0, column=0)
hardness_label = tkinter.Label(user_info_frame, text="Hardness")
hardness_label.grid(row=0, column=1)

ph_entry = tkinter.Entry(user_info_frame)
hasdness_entry = tkinter.Entry(user_info_frame)
ph_entry.grid(row=1, column=0)
hasdness_entry.grid(row=1, column=1)

solids_label = tkinter.Label(user_info_frame, text="Soild")
soilds_entry = ttk.Entry(user_info_frame)
solids_label.grid(row=0, column=2)
soilds_entry.grid(row=1, column=2)

chloramines_label = tkinter.Label(user_info_frame, text="Chloramines")
chloramines_entry = tkinter.Entry(user_info_frame)
chloramines_label.grid(row=2, column=0)
chloramines_entry.grid(row=3, column=0)

sulfate_label = tkinter.Label(user_info_frame, text="Sulfate")
sulfate_entry = ttk.Entry(user_info_frame)
sulfate_label.grid(row=2, column=1)
sulfate_entry.grid(row=3, column=1)

conductivity_label = tkinter.Label(user_info_frame, text="Conductivity")
conductivity_entry = ttk.Entry(user_info_frame)
conductivity_label.grid(row=2, column=2)
conductivity_entry.grid(row=3, column=2)

organic_carbon_label = tkinter.Label(user_info_frame, text="Organic_carbon")
organic_carbon_entry = ttk.Entry(user_info_frame)
organic_carbon_label.grid(row=4, column=0)
organic_carbon_entry.grid(row=5, column=0)

trihalomethanes_label = tkinter.Label(user_info_frame, text="Trihalomethanes")
trihalomethanes_entry = ttk.Entry(user_info_frame)
trihalomethanes_label.grid(row=4, column=1)
trihalomethanes_entry.grid(row=5, column=1)

turbidity_label = tkinter.Label(user_info_frame, text="Turbidity")
turbidity_entry = ttk.Entry(user_info_frame)
turbidity_label.grid(row=4, column=2)
turbidity_entry.grid(row=5, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=25, pady=10)


courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Kết quả: (độ chính xác của mô hình là 66%)")
registered_label.grid(row=0, column=0)

registered_label = tkinter.Label(courses_frame, text="")
registered_label.grid(row=1, column=0)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



def process_data():
    try:
        X = np.array([ph_entry.get(),hasdness_entry.get(),soilds_entry.get(),chloramines_entry.get(),sulfate_entry.get(),conductivity_entry.get(),organic_carbon_entry.get(),trihalomethanes_entry.get(),turbidity_entry.get()]).astype(float).reshape(1,9)

        scaler_data = [{'average': 7.085076169263963, 'standard': 1.4702280937310304},
                        {'average': 195.976016979664, 'standard': 32.50520182926505},
                        {'average': 21967.641554176098, 'standard': 8756.437565640574},
                        {'average': 7.131168139933786, 'standard': 1.587736261983618},
                        {'average': 334.1899441999459, 'standard': 36.554385336683886},
                        {'average': 425.24040812053494, 'standard': 80.30303423407761},
                        {'average': 14.290476612728673, 'standard': 3.2920013198296187},
                        {'average': 66.21049465625755, 'standard': 15.739744019605242},
                        {'average': 3.9637566690486716, 'standard': 0.7743044233342105}]
        
        for i in range(X.size):
            X[:,i] = (X[:,i] - scaler_data[i]['average'])/scaler_data[i]['standard']
        y_pred = svc_model.predict(X)
        if(y_pred[0] == 0):
            registered_label.configure(text= 'Nước không uống được')
        else:
             registered_label.configure(text= 'Nước uống được')
    except:
        messagebox.showwarning("Warning", "Các đặc trưng chỉ có thể là số và không được nhập trống")


# Button
button = tkinter.Button(frame, text="Enter data", command= process_data,bg='blue',fg='white',font=("Arial", 11,"bold"))
button.config(height=2, width=2)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

 
window.mainloop()
