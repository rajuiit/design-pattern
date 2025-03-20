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

# **Understanding the Adapter Design Pattern in Your Code**

The **Adapter Pattern** is used in this code to integrate two different **legacy security systems** (`LegacySecuritySystem` and `LegacySecuritySystem2`) with a modern **Smart Home Controller** (`SmartHomeController`).

### **Why Use the Adapter Pattern?**

1. The **legacy security systems** (`LegacySecuritySystem` and `LegacySecuritySystem2`) have different function names (`arm_legacy()`, `arm_legacy2()`, etc.).
2. The **SmartHomeController** expects standardized method names (`arm()`, `disarm()`, `trigger_alarm()`).
3. The **Adapter Pattern** allows the SmartHomeController to communicate with any legacy system  **without modifying the legacy code** .

---

## **1. Legacy Security Systems (Old Interfaces)**

These are **two different legacy systems** with their own method names.

### **Legacy Security System 1**

```python
class LegacySecuritySystem:
    def arm_legacy(self):
        print("Legacy Security System Armed 1")

    def disarm_legacy(self):
        print("Legacy Security System Disarmed 1")

    def trigger_alarm_legacy(self):
        print("Legacy Security Alarm Triggered! 1")
```

* Uses `arm_legacy()`, `disarm_legacy()`, and `trigger_alarm_legacy()`.
* These method names are **not compatible** with the `SmartHomeController`.

### **Legacy Security System 2**

```python
class LegacySecuritySystem2:
    def arm_legacy2(self):
        print("Legacy Security System Armed 2")

    def disarm_legacy2(self):
        print("Legacy Security System Disarmed 2")

    def trigger_alarm_legacy2(self):
        print("Legacy Security Alarm Triggered! 2")
```

* Similar to `LegacySecuritySystem`, but with different method names (`arm_legacy2()`, etc.).
* **Again, not directly compatible** with `SmartHomeController`.

---

## **2. Adapter Classes (Bridges Between Old and New)**

These classes **convert** the old method names to the new standard format.

### **Adapter for Legacy Security System 1**

```python
class LegacySecurityAdapter:
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def arm(self):
        self.legacy_system.arm_legacy()

    def disarm(self):
        self.legacy_system.disarm_legacy()

    def trigger_alarm(self):
        self.legacy_system.trigger_alarm_legacy()
```

* Converts `arm_legacy()` → `arm()`
* Converts `disarm_legacy()` → `disarm()`
* Converts `trigger_alarm_legacy()` → `trigger_alarm()`
* Now, the **SmartHomeController** can use this adapter **without knowing** it's using a legacy system.

### **Adapter for Legacy Security System 2**

```python
class LegacySecurityAdapter2:
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def arm(self):
        self.legacy_system.arm_legacy2()

    def disarm(self):
        self.legacy_system.disarm_legacy2()

    def trigger_alarm(self):
        self.legacy_system.trigger_alarm_legacy2()
```

* Does the same job as `LegacySecurityAdapter`, but maps different method names.

---

## **3. Smart Home Controller (Modern Interface)**

The `SmartHomeController` is the **new system** that expects all security systems to have `arm()`, `disarm()`, and `trigger_alarm()` methods.

```python
class SmartHomeController:
    def __init__(self):
        self.security_system = None  # Security system (adapter) will be assigned later

    def integrate_security_system(self, security_system):
        self.security_system = security_system  # Assign an adapter

    def activate_security(self):
        print("Activating Security System...")
        self.security_system.arm()  # Calls the adapter's `arm()`

    def deactivate_security(self):
        print("Deactivating Security System...")
        self.security_system.disarm()  # Calls the adapter's `disarm()`

    def alert_security_breach(self):
        print("Security Breach Detected!")
        self.security_system.trigger_alarm()  # Calls the adapter's `trigger_alarm()`
```

* This class **doesn’t need to know** if it's using an adapter or a real system.
* It works **seamlessly** with any system that implements `arm()`, `disarm()`, and `trigger_alarm()`.

---

## **4. Running the Program (`if __name__ == "__main__":`)**

This is where we **connect everything** and test the integration.

### **Step 1: Create Legacy Security Systems**

```python
legacy_system = LegacySecuritySystem()
adapter1 = LegacySecurityAdapter(legacy_system)

legacy_system2 = LegacySecuritySystem2()
adapter2 = LegacySecurityAdapter2(legacy_system2)
```

* `adapter1` wraps `legacy_system` and translates its methods.
* `adapter2` wraps `legacy_system2` and translates its methods.

### **Step 2: Create Smart Controllers and Integrate Systems**

```python
smart_controller1 = SmartHomeController()
smart_controller1.integrate_security_system(adapter1)
```

* `smart_controller1` now controls `LegacySecuritySystem` **through** `LegacySecurityAdapter`.

```python
smart_controller2 = SmartHomeController()
smart_controller2.integrate_security_system(adapter2)
```

* `smart_controller2` now controls `LegacySecuritySystem2` **through** `LegacySecurityAdapter2`.

### **Step 3: Activate, Trigger Alarm, and Deactivate**

```python
smart_controller1.activate_security()
smart_controller1.alert_security_breach()
smart_controller1.deactivate_security()
```

**Output:**

```
Activating Security System...
Legacy Security System Armed 1
Security Breach Detected!
Legacy Security Alarm Triggered! 1
Deactivating Security System...
Legacy Security System Disarmed 1
```

* The **adapter translates** method calls and communicates with `LegacySecuritySystem`.

```python
smart_controller2.activate_security()
smart_controller2.alert_security_breach()
smart_controller2.deactivate_security()
```

**Output:**

```
Activating Security System...
Legacy Security System Armed 2
Security Breach Detected!
Legacy Security Alarm Triggered! 2
Deactivating Security System...
Legacy Security System Disarmed 2
```

* The second system works  **exactly the same way** , despite its different method names.

---

## **Summary**

### **What Does the Adapter Pattern Do Here?**

✅ **Bridges old systems with new ones**

✅ **Allows `SmartHomeController` to use different security systems with a common interface**

✅ **Eliminates the need to modify legacy code**

### **Key Benefits**

* **Flexibility:** You can add **more legacy systems** without changing `SmartHomeController`.
* **Code Reusability:** The **same controller** can work with  **multiple security systems** .
* **Scalability:** If a **new legacy system** is introduced, you just create a **new adapter** instead of modifying the main system.

---


### **Understanding the Adapter Design Pattern (Refactor the first example: adapter.py) in Your updated code: refactor_code_with_one_adapter.py**

The **Adapter Pattern** is used to make incompatible interfaces work together. In this case, we have **two different legacy security systems** that have different method names, and we want them to work with a **Smart Home Controller** that expects standardized method names.

---

## **Problem in the Original Code**

1. **Two Legacy Security Systems**
   * `LegacySecuritySystem` uses methods:
     * `arm_legacy()`
     * `disarm_legacy()`
     * `trigger_alarm_legacy()`
   * `LegacySecuritySystem2` uses **different** method names:
     * `arm_legacy2()`
     * `disarm_legacy2()`
     * `trigger_alarm_legacy2()`
2. **Two Separate Adapters**
   * `LegacySecurityAdapter` adapts the first system.
   * `LegacySecurityAdapter2` adapts the second system.
   * **Problem** : If we add a **third** legacy security system with new method names, we have to create another adapter.

---

## **Solution: One Flexible Adapter**

Instead of making a new adapter for each system, we create  **one generic adapter** :

### **How Does This New Adapter Work?**

```python
class LegacySecurityAdapter:
    def __init__(self, legacy_system, arm_method, disarm_method, trigger_alarm_method):
        self.legacy_system = legacy_system
        self.arm_method = arm_method
        self.disarm_method = disarm_method
        self.trigger_alarm_method = trigger_alarm_method

    def arm(self):
        getattr(self.legacy_system, self.arm_method)()  # Dynamically call the correct method

    def disarm(self):
        getattr(self.legacy_system, self.disarm_method)()

    def trigger_alarm(self):
        getattr(self.legacy_system, self.trigger_alarm_method)()
```

### **How It Works Step by Step**

* The adapter **stores** the legacy system and the method names passed as arguments.
* When `arm()`, `disarm()`, or `trigger_alarm()` is called, it uses `getattr()` to call the correct method dynamically.

### **Example Usage**

```python
# Creating the first adapter for LegacySecuritySystem
legacy_system1 = LegacySecuritySystem()
adapter1 = LegacySecurityAdapter(legacy_system1, "arm_legacy", "disarm_legacy", "trigger_alarm_legacy")

# Creating the second adapter for LegacySecuritySystem2
legacy_system2 = LegacySecuritySystem2()
adapter2 = LegacySecurityAdapter(legacy_system2, "arm_legacy2", "disarm_legacy2", "trigger_alarm_legacy2")
```

* `adapter1` maps:
  * `arm()` → `arm_legacy()`
  * `disarm()` → `disarm_legacy()`
  * `trigger_alarm()` → `trigger_alarm_legacy()`
* `adapter2` maps:
  * `arm()` → `arm_legacy2()`
  * `disarm()` → `disarm_legacy2()`
  * `trigger_alarm()` → `trigger_alarm_legacy2()`

---

## **Why Is This a Better Solution?**

✅ **One Adapter for All Legacy Systems**

* Instead of writing a new adapter every time, we **reuse** the same one.

✅ **Easier Maintenance**

* If a new legacy security system is added, we just create a new `LegacySecurityAdapter` instance with the correct method names.

✅ **No Code Duplication**

* The logic for adapting different security systems is centralized in  **one place** .

---

## **Final Execution Flow**

1. The **Smart Home Controller** expects a standardized interface with:
   * `arm()`
   * `disarm()`
   * `trigger_alarm()`
2. The **Legacy Security Adapter** converts these calls into the correct legacy method names.
3. This allows any **legacy system to integrate seamlessly** with the smart home.

---

### **Example Output**

```
Activating Security System...
Legacy Security System Armed 1
Security Breach Detected!
Legacy Security Alarm Triggered! 1
Deactivating Security System...
Legacy Security System Disarmed 1

Activating Security System...
Legacy Security System Armed 2
Security Breach Detected!
Legacy Security Alarm Triggered! 2
Deactivating Security System...
Legacy Security System Disarmed 2
```

---

### **Conclusion**

With this design,  **no matter how many different security systems exist** , we can integrate them using a **single adapter** by just passing the correct method names.

## License

This project is licensed under the MIT License.
