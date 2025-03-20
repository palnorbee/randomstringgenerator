import secrets,quantumrandom,string,sv_ttk,ctypes as ct
from string import punctuation
from tkinter import ttk, IntVar, StringVar,Tk
from tktooltip import ToolTip
#TK BASE--------------------------------------------------------------------------------------------------------
root = Tk()
root.title("Random string generator")
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky="NEWS")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)
root.wm_attributes('-toolwindow', 'True')
#VARIABLES--------------------------------------------------------------------------------------------------------
symbols=str(punctuation)
alphabet_upper = string.ascii_uppercase
string_result = StringVar()
string_len = IntVar()
array_len = IntVar()
#LABELS--------------------------------------------------------------------------------------------------------
scale1 = ttk.LabeledScale(mainframe, from_=0, to=25, variable=array_len) #MAX. ARRAY LENGTH IS 1024
scale2 = ttk.LabeledScale(mainframe, from_=0, to=100, variable=string_len)
ttk.Label(mainframe, text="Array length: ").grid(column=1, row=1)
ttk.Label(mainframe, text="String length: ").grid(column=3, row=1)
ttk.Label(mainframe, justify="center", text="Your string: ").grid(column=2, row=1)
#ENTRIES--------------------------------------------------------------------------------------------------------
string_result_entry = ttk.Entry(mainframe, width=15, textvariable=string_result)
#FUNCTIONS--------------------------------------------------------------------------------------------------------
def right_click(content):
    root.clipboard_clear()
    root.clipboard_append(string_result_entry.get())
    tool_tip.destroy()
def enabler():
    button1.grid(column=2, row=3)
    button1.config(state="enabled", text="Generate")
def calculate():
    if scale1.value > 0 < scale2.value:
        string_result_step1=str(quantumrandom.get_data(data_type="hex16", array_length=array_len.get()))
        string_result_step2= (string_result_step1.replace(" ","").strip("[]()").replace(",","")) + alphabet_upper + symbols
        string_result_list=[]
        for i in range(scale2.value):
            string_result_list.append(secrets.choice(string_result_step2))
        string_result.set(value="".join(map(str, string_result_list)))
        button1.config(state="disabled",text="Getting ready")
        button1.after(120000, enabler)
def dark_title_bar(window):
    """
    MORE INFO:
    https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")
#BUTTONS&MISC--------------------------------------------------------------------------------------------------------
button1=ttk.Button(mainframe, command=calculate, text="Generate")
tool_tip = ToolTip(string_result_entry, msg="Right click to copy")
string_result_entry.bind("<Button-3>", right_click)
#GRID--------------------------------------------------------------------------------------------------------
string_result_entry.grid(column=2, row=2, )
scale1.grid(column=1, row=2)
scale2.grid(column=3, row=2)
button1.grid(column=2, row=3)
#PADDING--------------------------------------------------------------------------------------------------------
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
#THEMES--------------------------------------------------------------------------------------------------------
dark_title_bar(root)
sv_ttk.set_theme("dark")
#--------------------------------------------------------------------------------------------------------------
center_window(root)
mainframe.focus()
root.mainloop()


