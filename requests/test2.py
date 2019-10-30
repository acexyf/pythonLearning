from pymouse import PyMouse


m = PyMouse()

pos = m.position()

# print(pos, pos[0], pos[1])

# m.click(412, 346, 1)


m.move(0, 0)

m.click(412, 346, 1)

print(m.screen_size())