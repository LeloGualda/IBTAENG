import  math

def areacicle(r):
    return math.pi * math.pow(r,2)
def alt(l):
    return math.sqrt((l*l)-((l/2)*(l/2)))
def lad(h,angle):
    return h / math.tan(math.radians(angle))
def raw(b,angle):
    return b * math.tan(math.radians(angle))
area = []
L = 1
H = alt(1)
total = H * L
h = 0

for i in range(0,15):
    if(i == 0):
        area.append(1*areacicle(raw(lad(H,60),30)))
    else:
        area.append(3*areacicle(raw(lad(H-h,60),30)))
    h += raw(lad(H-h,60),30) * 2

sum  = 0
print(3*areacicle((7*math.sqrt(3))/54))
for s,v in enumerate(area):
    print(v)
    sum += v

q = area[1]/(1-area[2]/area[1])

print(q+area[0],sum,total)
