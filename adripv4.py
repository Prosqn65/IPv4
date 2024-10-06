
class AddressIPv4:

    def __init__(self, address):
        self.address = address

    def isValid(self):
        octets = self.address.split('.')
        if len(octets)!=4:
            return False
        for octet in octets:
            if not octet.isdigit():
                return False
            if int(octet) < 0 or int(octet) > 255:
                return False
            if octet != "0" and octet[0] == '0':
                return False
        return True
    
    def getAsStr(self):
        return self.address

    def getAsInt(self):
        octets = self.address.split('.')
        return int(octets[0]) << 24 | int(octets[1]) << 16 | int(octets[2]) << 8 | int(octets[3])
    
    def getAsBinaryStr(self):
        octets = self.address.split('.')
        return '.'.join([bin(int(octet))[2:].zfill(8) for octet in octets])
    
    def getOctets(self, n):
        octet = self.address.split('.')
        if n > 4 or n < 1:
            return "Invalid octet"
        return octet[n-1]

    def getClass(self):
        o_class = self.address.split('.')[0]
        if int(o_class) >= 0 and int(o_class) <= 127:
            return "A"
        elif int(o_class) >= 128 and int(o_class) <= 191:
            return "B"
        elif int(o_class) >= 192 and int(o_class) <= 223:
            return "C"
        elif int(o_class) >= 224 and int(o_class) <= 239:
            return "D"
        elif int(o_class) >= 240 and int(o_class) <= 255:
            return "E"
    
    def isPrivate(self):
        octets = self.address.split('.')
        if int(octets[0]) == 10:
            return True
        elif int(octets[0]) == 172 and 16 <= int(octets[1]) <= 31:
            return True
        elif int(octets[0]) == 192 and int(octets[1]) == 168:
            return True
        else:
            return False
    
ip = "172.31.2.178"
print(f"{AddressIPv4(ip).isValid()}\n{AddressIPv4(ip).getAsStr()}\n{AddressIPv4(ip).getAsInt()}\n{AddressIPv4(ip).getAsBinaryStr()}\n{AddressIPv4(ip).getOctets(3)}\n{AddressIPv4(ip).getClass()}\n{AddressIPv4(ip).isPrivate()}")