class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.apps = []

    def make_call(self, number):
        print(f"Calling {number}...")

    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"Installing {app_name}...")

    def show_apps(self):
        print(f"Installed apps on {self.model}: {', '.join(self.apps)}")


# Inheriting from Smartphone to create a subclass for a specific brand
class iPhone(Smartphone):
    def __init__(self, model, storage):
        super().__init__("Apple", model, storage)

    def make_call(self, number):
        print(f"iPhone calling {number}... 📱")

    def show_apps(self):
        super().show_apps()
        print("Optimized for iOS.")

# Creating objects
phone = Smartphone("Samsung", "Galaxy S21", "128GB")
phone.make_call("123-456-7890")
phone.install_app("Facebook")
phone.show_apps()

iphone = iPhone("iPhone 13", "256GB")
iphone.make_call("987-654-3210")
iphone.install_app("Instagram")
iphone.show_apps()
