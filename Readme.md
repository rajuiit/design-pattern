# Design Pattern Coding

This repository contains implementations of various design patterns in Python. Each pattern is implemented in a separate Python script, demonstrating its use case and functionality.

## Design Patterns Implemented

* **Adapter Pattern** (`adapter.py`): Allows incompatible interfaces to work together.
* **Decorator Pattern** (`decorator.py`): Enhances functionality of objects dynamically.
* **Facade Pattern** (`facade.py`): Provides a simplified interface to a complex subsystem.
* **Factory Pattern** (`factory.py`): Creates objects without specifying the exact class.
* **Middleware Pattern** (`middleware.py`): Intercepts requests and responses in a pipeline.
* **Observer Pattern** (`observer.py`): Implements a publish-subscribe mechanism.
* **Prototype Pattern** (`prototype.py`): Creates new objects by copying an existing instance.
* **Proxy Pattern** (`proxy.py`): Controls access to another object.
* **Singleton Pattern** (`singleton.py`): Ensures a class has only one instance.
* **Strategy Pattern** (`strategy.py`): Enables interchangeable algorithms at runtime.

## Getting Started

To use these design patterns in your project:

1. Clone this repository:
   ```sh
   git clone <repository-url>
   cd design-pattern-coding
   ```
2. Run any script to see the design pattern in action:
   ```sh
   python adapter.py
   ```

## **Understanding Singleton Pattern in `SmartHomeConfigManager`**

This code demonstrates the **Singleton design pattern** using a  **Smart Home Configuration Manager** , where multiple smart devices share the same configuration settings.

## **1. Singleton Design Pattern in `SmartHomeConfigManager`**

The **Singleton** pattern ensures that there is only **one instance** of `SmartHomeConfigManager`, which manages all settings for the smart home system.

### **How It Works**

* The class variable `_instance` stores the **single instance** of the class.
* The `__new__()` method ensures that **only one instance** is created.
* If `_instance` is `None`, a new instance is created.
* If `_instance` already exists, the same instance is returned.

#### **Code Breakdown**

```python
class SmartHomeConfigManager:
    _instance = None  # Stores the singleton instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # If instance does not exist, create one
            cls._instance = super(SmartHomeConfigManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.settings = {}  # Initialize settings dictionary
        return cls._instance  # Return the same instance every time

    def set_setting(self, key, value):
        self.settings[key] = value  # Store the setting

    def get_setting(self, key):
        return self.settings.get(key, None)  # Retrieve the setting
```

---

## **2. Smart Devices Using the Singleton**

Each smart device **does not create a new config manager** but instead  **uses the same shared instance** .

### **How It Works**

* Each `SmartDevice` **automatically connects** to the shared `SmartHomeConfigManager`.
* Any setting change in one device  **immediately reflects in all other devices** .

#### **Code Breakdown**

```python
class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.config = SmartHomeConfigManager()  # Each device gets the same instance

    def display_settings(self):
        print(f"[{self.name}] Current Settings: {self.config.settings}")

    def update_setting(self, key, value):
        print(f"[{self.name}] Updating {key} to {value}")
        self.config.set_setting(key, value)  # Updates the shared configuration
```

---

## **3. Running the Code (`if __name__ == "__main__":`)**

### **Step-by-Step Execution**

#### **Step 1: Initialize the Singleton**

```python
config_manager = SmartHomeConfigManager()
config_manager.set_setting("temperature", 22)
config_manager.set_setting("lights", "dim")
```

* The `config_manager` object is created.
* Initial settings **temperature = 22** and **lights = dim** are stored.

#### **Step 2: Create Two Smart Devices**

```python
device1 = SmartDevice("Thermostat")
device2 = SmartDevice("Living Room Lights")
```

* Both `device1` and `device2` get **the same instance** of `SmartHomeConfigManager`.

#### **Step 3: Display Settings**

```python
device1.display_settings()
device2.display_settings()
```

**Output:**

```
[Thermostat] Current Settings: {'temperature': 22, 'lights': 'dim'}
[Living Room Lights] Current Settings: {'temperature': 22, 'lights': 'dim'}
```

* Both devices **see the same settings** since they share the same configuration.

#### **Step 4: Update a Setting from One Device**

```python
device1.update_setting("temperature", 24)
```

**Output:**

```
[Thermostat] Updating temperature to 24
```

* The `temperature` setting is updated to **24** in the shared `SmartHomeConfigManager`.

#### **Step 5: Display Updated Settings**

```python
device1.display_settings()
device2.display_settings()
```

**Output:**

```
[Thermostat] Current Settings: {'temperature': 24, 'lights': 'dim'}
[Living Room Lights] Current Settings: {'temperature': 24, 'lights': 'dim'}
```

* Both devices **see the updated temperature** because they share the  **same configuration instance** .

---

## **Summary**

### **What You Learned**

✅ **Singleton Pattern** → Ensures `SmartHomeConfigManager` has only  **one instance** .

✅ **Shared State** → All smart devices share the  **same settings** .

✅ **Global Access** → Any device can update and read from the  **same configuration manager** .

### **Why Is This Useful?**

* **Prevents conflicting settings** in a smart home system.
* **Saves memory** by not creating multiple configuration objects.
* **Ensures consistency** across multiple devices.

## License

This project is licensed under the MIT License.
