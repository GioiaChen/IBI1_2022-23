# Input all the information about the athlete.
fn = input("First name: ")
ln = input("Last name: ")
loc = input("The location of competition: ")
st = input("Time for swim(min): ")
ct = input("Time for cycle(min): ")
rt = input("Time for run(min): ")

# Define the function to store these information.
class triathlon:
    def __init__(self, x, y, z, a, b, c):
        self.fn = x
        self.ln = y
        self.loc = z
        self.st = a
        self.ct = b
        self.rt = c
        self.tt = str(int(self.st) + int(self.ct) + int(self.rt))

    def store(self):
        return (self.fn,
                self.ln,
                self.loc,
                "SWIM:" + self.st + "min",
                "CYCLE:" + self.ct + "min",
                "RUN:" + self.rt + "min",
                "TOTAL:" + self.tt + "min")


x = triathlon(fn, ln, loc, st, ct, rt)
print(triathlon.store(x))
