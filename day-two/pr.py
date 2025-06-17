import gc

a = [1, 2, 3]
b = a
del a
del b

gc.collect()  # Triggers garbage collection manually
