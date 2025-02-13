class PersonalComputer:  # Renamed class for better clarity
    def __init__(self, memory, disk, model, cpu):
        """Initialize the base attributes of a personal computer."""
        self.memory = memory  # Memory size in MB
        self.disk = disk  # Disk size in MB
        self.model = model  # Model of the PC
        self.cpu = cpu  # CPU type

    def display_info(self):
        """Display general information about the PC."""
        print(f"PC Model: {self.model}, CPU: {self.cpu}, Memory: {self.memory}MB, Disk: {self.disk}MB")


class DesktopPC(PersonalComputer):  # Renamed class for better understanding
    def __init__(self, memory, disk, model, cpu, monitor, keyboard, mouse):
        """Initialize attributes of a desktop PC."""
        super().__init__(memory, disk, model, cpu)
        self.monitor = monitor  # Monitor specifications
        self.keyboard = keyboard  # Keyboard type
        self.mouse = mouse  # Mouse type

    def display_info(self):
        """Print information about the desktop PC."""
        super().display_info()
        print(f"Monitor: {self.monitor}, Keyboard: {self.keyboard}, Mouse: {self.mouse}")


class Laptop(PersonalComputer):  # Renamed class for consistency
    def __init__(self, memory, disk, model, cpu, dimensions, screen_size, battery_life):
        """Initialize attributes of a laptop."""
        super().__init__(memory, disk, model, cpu)
        self.dimensions = dimensions  # Physical size of the laptop
        self.screen_size = screen_size  # Screen size in inches
        self.battery_life = battery_life  # Battery life in hours

    def display_info(self):
        """Print information about the laptop."""
        super().display_info()
        print(f"Dimensions: {self.dimensions}, Screen Size: {self.screen_size} inches, Battery Life: {self.battery_life} hours")


# Example Usage
pc = PersonalComputer(16000, 5000000, 'AMD', 'Ryzen 5 5500')  # Create a personal computer instance
pc.display_info()

# Creating instances of DesktopPC and Laptop
desktop = DesktopPC(16000, 5000000, 'Intel', 'Core i7', '24-inch', 'Mechanical', 'Wireless')
laptop = Laptop(8000, 1000000, 'Dell', 'Core i5', '15x10 inches', 15.6, 8)  # Added battery life attribute

# Displaying their information
desktop.display_info()
laptop.display_info()
