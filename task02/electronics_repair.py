class Device(object):
    def __init__(self, name, is_broken, repair_price):
        self.__name = name
        self.__is_broken = is_broken
        self.__repair_price = repair_price
    def get_name(self):
        return self.__name
    def get_broken_status(self):
        return self.__is_broken
    def get_repair_price(self):
        return self.__repair_price
    def can_be_repaired(self):
        return True
    
class SuperBrokenDevice(Device):
    def can_be_repaired(self):
        return False

class RepairStudio(object):    
    def __init__(self, max_devices):
        self.__max_devices = max_devices
        self.__current_devices = 0
        self.__device_list = []
    def get_current_devices(self):
        return self.__current_devices
    def get_current_devices_list(self):
        return self.__device_list
    def device_add(self, device):
        if self.__current_devices < self.__max_devices:
            self.__device_list.append(device)
            self.__current_devices += 1
            return "Ok", self.__current_devices, self.__max_devices 
        else:
            return "Studio full"
    def device_repair(self, device):
        if self.__current_devices > 0:
            if device in self.__device_list:
                self.__device_list.remove(device)           
                self.__current_devices -= 1
                return "Ok", self.__current_devices, self.__max_devices
            else:
                return "We don't have the device"
        else:
            return "Studio empty"
    def __iter__(self):
        return (i.get_name() for i in self.__device_list)
        
    
tv_test_receiver = Device("Rhode Schwarz EFA40 Test Receiver", True, 50)
tv_signal_transmitter = Device("Elti DVB-T Transmitter", True, 1000)
chinese_mobile = SuperBrokenDevice("Chinese 1Ph0n3 4", True, 0)
mobile = Device("Genuine iPhone 4S", True, 30)

noname_studio = RepairStudio(2)
print "Before", noname_studio.get_current_devices()
print noname_studio.device_add(tv_signal_transmitter)
print noname_studio.device_add(mobile)

print "After", noname_studio.get_current_devices()
print noname_studio.device_repair(mobile)
for i in noname_studio.get_current_devices_list():
    print i.get_name()

print noname_studio.device_repair(tv_signal_transmitter)