class LegacySecurityAdapter:
    def __init__(self, legacy_system, arm_method, disarm_method, trigger_alarm_method):
        self.legacy_system = legacy_system
        self.arm_method = arm_method
        self.disarm_method = disarm_method
        self.trigger_alarm_method = trigger_alarm_method

    def arm(self):
        getattr(self.legacy_system, self.arm_method)()  # Dynamically call the method

    def disarm(self):
        getattr(self.legacy_system, self.disarm_method)()

    def trigger_alarm(self):
        getattr(self.legacy_system, self.trigger_alarm_method)()

class SmartHomeController:
    def __init__(self):
        self.security_system = None

    def integrate_security_system(self, security_system):
        self.security_system = security_system

    def activate_security(self):
        print("Activating Security System...")
        self.security_system.arm()

    def deactivate_security(self):
        print("Deactivating Security System...")
        self.security_system.disarm()

    def alert_security_breach(self):
        print("Security Breach Detected!")
        self.security_system.trigger_alarm()

# Legacy Security Systems
class LegacySecuritySystem:
    def arm_legacy(self):
        print("Legacy Security System Armed 1")

    def disarm_legacy(self):
        print("Legacy Security System Disarmed 1")

    def trigger_alarm_legacy(self):
        print("Legacy Security Alarm Triggered! 1")

class LegacySecuritySystem2:
    def arm_legacy2(self):
        print("Legacy Security System Armed 2")

    def disarm_legacy2(self):
        print("Legacy Security System Disarmed 2")

    def trigger_alarm_legacy2(self):
        print("Legacy Security Alarm Triggered! 2")

if __name__ == "__main__":
    # Creating one adapter for both legacy systems
    legacy_system1 = LegacySecuritySystem()
    adapter1 = LegacySecurityAdapter(legacy_system1, "arm_legacy", "disarm_legacy", "trigger_alarm_legacy")

    legacy_system2 = LegacySecuritySystem2()
    adapter2 = LegacySecurityAdapter(legacy_system2, "arm_legacy2", "disarm_legacy2", "trigger_alarm_legacy2")

    # Integrating with SmartHomeController
    smart_controller1 = SmartHomeController()
    smart_controller1.integrate_security_system(adapter1)

    smart_controller1.activate_security()
    smart_controller1.alert_security_breach()
    smart_controller1.deactivate_security()

    smart_controller2 = SmartHomeController()
    smart_controller2.integrate_security_system(adapter2)

    smart_controller2.activate_security()
    smart_controller2.alert_security_breach()
    smart_controller2.deactivate_security()
