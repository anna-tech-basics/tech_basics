

# import tkinter to display gui
# import image to add into main frame

import tkinter as tk
from PIL import Image, ImageTk

# definine class to model and organize code
# reference https://www.geeksforgeeks.org/python-classes-and-objects/?ref=header_search

class GymApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # adding title
        self.title("GymGirls")
        # setting initial sizing to resemble app on your phone
        self.geometry("400x500")

        # Create the first frame within main window self
        # setting background to black
        # grid method to specify position, sticky="nsew" allows frame to fill space
        self.first_frame = tk.Frame(self, bg="black")
        self.first_frame.grid(row=0, column=0, sticky="nsew")
        # calls method to create labels, boxes and button
        self.create_first_frame_widgets()

        # Configure column and row weights # allows frame to expand proportionally
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def create_first_frame_widgets(self):
        # Widgets for the first frame
        # creates username and password label
        # sets font
        # creates entry boxes for username and password
        # grid() method to position widgets
        # padx and pady adds padding
        label_username = tk.Label(self.first_frame, text="Username:", fg="white", font=("Helvetica", 12), bg="black")
        label_username.grid(column=0, row=3, padx=10, pady=10)


        entry_username = tk.Entry(self.first_frame)
        entry_username.grid(column=1, row=3, padx=10, pady=10)

        label_password = tk.Label(self.first_frame, text="Password:", fg="white", font=("Helvetica", 12), bg="black")
        label_password.grid(column=0, row=4, padx=10, pady=10)

        # shows * instead of letters for password
        entry_password = tk.Entry(self.first_frame, show="*")
        entry_password.grid(column=1, row=4, padx=10, pady=10)

        # Creates a button widget to join and a command to execute when clicked

        join_button = tk.Button(self.first_frame, text="Join GymGirls", command=self.on_join_clicked)
        join_button.grid(column=0, row=5, columnspan=2, pady=10)


    # defines what happens when join gymgirls button is clicked
    def on_join_clicked(self):

        # Destroys the first frame
        self.first_frame.destroy()

        # Creates and displays the new frame
        self.create_main_frame()


    # creates main frame
    def create_main_frame(self):
        self.main_frame = tk.Frame(self, bg="#FFE1FF")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configures column and row weights
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # i struggled to put images in here (will work on this for future enhancements)

        #  image1 = Image.open('images/power.png')
        # resized_image = image1.resize((300, 300), Image.ANTIALIAS)
        # pic = ImageTk.PhotoImage(resized_image)

        # adding image
        #   image_label = tk.Label(main_frame, image=pic)
        #  image_label.image = pic
        # image_label.grid(column=0, row=1, columnspan=2, sticky="nsew")

        # Widgets for the main frame
        label_welcome = tk.Label(self.main_frame, text="Welcome to GymGirls!", font=("Helvetica", 16))
        label_welcome.grid(column=0, row=0, columnspan=2, sticky="nsew")


        profile_button = tk.Button(self.main_frame, text="Create Profile", command=self.open_profile_frame)
        profile_button.grid(column=0, row=1, columnspan=2, pady=10, sticky="ew")

    # defines what happens when create profile is clicked
    def open_profile_frame(self):
        # Destroys the main frame
        self.main_frame.destroy()
        # Creates the profile frame
        self.profile_frame = tk.Frame(self, bg="white")
        self.profile_frame.grid(row=0, column=0, sticky="nsew")

        # Configure column and row weights
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Widgets for the profile frame
        label_profile = tk.Label(self.profile_frame, text="Create Your Profile", font=("Helvetica", 16))
        label_profile.grid(column=0, row=0, columnspan=2, sticky="nsew")

        # Add profile input fields (username, password, name, age, etc.)
        label_name = tk.Label(self.profile_frame, text="Name:")
        label_name.grid(column=0, row=1, padx=10, pady=10, sticky="w")

        entry_name = tk.Entry(self.profile_frame)
        entry_name.grid(column=1, row=1, padx=10, pady=10, sticky="ew")

        label_age = tk.Label(self.profile_frame, text="Age:")
        label_age.grid(column=0, row=2, padx=10, pady=10, sticky="w")

        entry_age = tk.Entry(self.profile_frame)
        entry_age.grid(column=1, row=2, padx=10, pady=10, sticky="ew")

        label_membership = tk.Label(self.profile_frame, text="Gym Membership:")
        label_membership.grid(column=0, row=3, padx=10, pady=10, sticky="w")

        # Use a dropdown menu for membership status
        # reference https://www.geeksforgeeks.org/dropdown-menus-tkinter/
        membership_options = ["Yes", "No"]
        var_membership = tk.StringVar(self.profile_frame)
        var_membership.set(membership_options[0])  # Default value
        dropdown_membership = tk.OptionMenu(self.profile_frame, var_membership, *membership_options)
        dropdown_membership.grid(column=1, row=3, padx=10, pady=10, sticky="ew")

        label_gym = tk.Label(self.profile_frame, text="if yes which one:")
        label_gym.grid(column=0, row=4, padx=10, pady=10, sticky="w")

        entry_gym = tk.Entry(self.profile_frame)
        entry_gym.grid(column=1, row=4, padx=10, pady=10, sticky="ew")

        label_goals = tk.Label(self.profile_frame, text="Fitness Goals:")
        label_goals.grid(column=0, row=5, padx=10, pady=10, sticky="w")

        entry_goals = tk.Entry(self.profile_frame)
        entry_goals.grid(column=1, row=5, padx=10, pady=10, sticky="ew")

        label_partner = tk.Label(self.profile_frame, text="Looking for a Gym Partner:")
        label_partner.grid(column=0, row=6, padx=10, pady=10, sticky="w")

        # Use a dropdown menu for partner preference
        partner_options = ["Yes", "No"]
        var_partner = tk.StringVar(self.profile_frame)
        var_partner.set(partner_options[0])
        dropdown_partner = tk.OptionMenu(self.profile_frame, var_partner, *partner_options)
        dropdown_partner.grid(column=1, row=6, padx=10, pady=10, sticky="ew")

        # Adds a button to save the profile
        save_button = tk.Button(self.profile_frame, text="Save Profile", command=self.save_profile)
        save_button.grid(column=0, row=7, columnspan=2, pady=10, sticky="ew")

    # defines what happens when save profile is clicked
    def save_profile(self):
        # destroys profile frame
        self.profile_frame.destroy()
        # creates profile saved frame
        self.saved_profile = tk.Frame(self, bg="white")
        self.saved_profile.grid(row=0, column=0, sticky="nsew")

        # widgets for profile saved frame
        label_saved_profile = tk.Label(self.saved_profile, text="Profile Saved!", font=("Helvetica", 20))
        label_saved_profile.grid(column=2, row=2, columnspan=2, sticky="nsew")

        button_getstarted = tk.Button(self.saved_profile, text="Get started", font=("Helvetica", 22), command=self.get_started)
        button_getstarted.grid(column=4, row=6, columnspan=2, sticky="nsew")

    # defines what happens when get started is clicked
    def get_started(self):
        self.saved_profile.destroy()
        # Recreates the main frame
        self.main_frame = tk.Frame(self, bg="#FFE1FF")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configure column and row weights
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Widgets for the main frame
        label_welcome = tk.Label(self.main_frame, text="Hi GymGirl!", font=("Helvetica", 16))
        label_welcome.grid(column=0, row=0, columnspan=2, sticky="nsew")

        # Adds buttons for different actions
        share_training_button = tk.Button(self.main_frame, text="Share Your Training", command=self.share_training)
        share_training_button.grid(column=0, row=1, columnspan=2, pady=10, sticky="ew")

        connect_button = tk.Button(self.main_frame, text="Connect with Gym Girls at Your Gym", command=self.connect_with_gym_girls)
        connect_button.grid(column=0, row=2, columnspan=2, pady=10, sticky="ew")

        find_gyms_button = tk.Button(self.main_frame, text="Find Gyms with Women-only Options", command=self.find_women_only_gyms)
        find_gyms_button.grid(column=0, row=3, columnspan=2, pady=10, sticky="ew")

        share_experiences_button = tk.Button(self.main_frame, text="Share Experiences", command=self.share_experiences)
        share_experiences_button.grid(column=0, row=4, columnspan=2, pady=10, sticky="ew")

    def share_training(self):
        # room for future enhancement
        pass

    def connect_with_gym_girls(self):
        # room for future enhancement
        pass

    def find_women_only_gyms(self):
        # room for future enhancement
        pass

    def share_experiences(self):
        # room for future enhancement
        pass

app = GymApp()
app.mainloop()
