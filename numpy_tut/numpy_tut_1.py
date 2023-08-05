import numpy as np

math = [1, 2, 3, 4]

math1 = [[1, 2, 3, 4], [5, 6, 7, 8]]

math2 = np.random.randint(0, 5, 10)

math4 = math2[math2> 3]

math3 = np.array(math1)

print(np.array(math))
print(np.array(math1))
print(np.arange(start=0, stop=10))
print(np.zeros((5, 5)))
print(np.ones((5, 5)))
print(np.linspace(start=0, stop=10, num=10))
print(np.eye(4))
print(np.random.rand(5, 5))
print(np.random.randn(5, 5))
print(np.random.randint(0, 5, 10))
print(math2.reshape(2, 5))
print(math2.max())
print(math2.argmax())
print(math2.shape)
print(math2.dtype)

print(math2[0])
print(math2[1: 5])
print(math2[:5])
print(math2[5:])
print(math3[:1, 1:])
print(math4)