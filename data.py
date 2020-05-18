import sys

class b():
    def __init__(self, source):
        self.bits = []
        for i in source:
            self.bits.append(int(i))
        self.value = 0
        self.evaluate()

    def evaluate(self):
        self.length = len(self.bits)

        for i in range(self.length):
            addr = self.length - (i + 1)
            bit = self.bits[addr]
            self.value += ((2 ** i) * bit)

            #print("i: {}\naddr: {}\nbit: {}\nvalue: {}".format(i, addr, bit, self.value))
        print('bits: {}\nvalue: {}\nlength: {}'.format(self.bits, self.value, self.length))
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __len__(self):
        return self.length

    def __getitem__(self, address):
        returnData = ''
        if type(address) is slice:
            if address.start > self.length or address.stop > self.length or address.start < 0 or address.stop < 0:
                raise IndexError('Bit index out of range')
            else:
                if type(address.start) is int:
                    start = address.start
                else:
                    start = 0
                if type(address.stop) is int:
                    stop = address.stop
                else:
                    stop = self.length - 1
                if type(address.step) is int:
                    step = address.step
                else:
                    step = 1

                for i in range(start, stop, step):
                    returnData = returnData + str(self.bits[i])
        else:
            if address >= self.length or address < 0:
                raise IndexError('Bit index out of range')
            else:
                returnData = str(self.bits[address])
        return returnData

    def prepend(self, data):
        loop = len(data)
        for i in range(loop):
            self.bits.insert(0, data.bits[(loop - i) - 1])
        self.evaluate()

    def append(self, data):
        for d in data.bits:
            self.bits.append(int(d))
        self.evaluate()

class B():
    lookup = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    def __init__(self, source):
        self.hex = str(source).lower()
        self.evaluate()
            #print('val: {}\nmod: {}\nvalue: {}'.format(val, mod, self.value))

    def evaluate(self):
        self.value = 0
        self.length = len(self.hex) / 2
        #print('length: {}'.format(self.length))
        if self.length != int(self.length):
            self.length = int(self.length) + 1
            #print('adjusting length: {}'.format(self.length))
            self.hex = '0' + self.hex
        else:
            self.length = int(self.length)

        for i in range(len(self.hex)):
            val = self.lookup.index(self.hex[i])
            mod = len(self.hex) - (i + 1)
            self.value += val * (16 ** mod)
        #print('value: {}\nhex: {}\nlength: {}'.format(self.value, self.hex, self.length))

    def __str__(self):
        return self.hex

    def __repr__(self):
        return self.hex

    def __len__(self):
        return self.length

    def rawlen(self):
        return len(self.hex)

    def __getitem__(self, address):
        returnData = ''
        if type(address) is slice:
            if address.start > self.length or address.stop > self.length or address.start < 0 or address.stop < 0:
                raise IndexError('Byte index out of range')
            else:
                if type(address.start) is int:
                    start = address.start
                else:
                    start = 0
                if type(address.stop) is int:
                    stop = address.stop
                else:
                    stop = self.length - 1
                if type(address.step) is int:
                    step = address.step
                else:
                    step = 1

                for i in range(start, stop, step):
                    returnData = returnData + str(self.hex[2 * i:(2 * i) + 2])
        else:
            if address >= self.length or address < 0:
                raise IndexError('Byte index out of range')
            else:
                returnData = str(self.hex[2 * address:(2 * address) + 2])
        return returnData


        if index >= self.length:
            raise IndexError('Byte index out of range')
        else:
            return B(self.hex[2 * address:(2 * address) + 2])

    def prepend(self, data):
        loop = data.rawlen()
        for i in range(loop):
            self.hex = data.hex[(loop - i) - 1] + self.hex
        self.evaluate()

    def append(self, data):
        for d in data.hex:
            self.hex = self.hex + d
        self.evaluate()

def BToBytes(BIn: B):
    return int.to_bytes(BIn.value, BIn.length, 'big')

def bytesToB(bytesIn: bytes):
    return B(hex(int.from_bytes(bytesIn, 'big'))[2:])

def bToB(bIn: b):
    return(B(hex(bIn.value)[2:]))

def BTob(BIn: B):
    return(b(bin(BIn.value)[2:]))

def intTob(intIn: int):
    return(b(bin(intIn)[2:]))

def bToInt(bIn: b):
    return bIn.value

def intToB(intIn: int):
    return B(hex(intIn)[2:])

def BToInt(BIn: B):
    return BIn.value