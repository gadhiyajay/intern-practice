import weakref

class GFG(list):
    pass

obj = GFG("GeeksForGeeks")

normal_list = obj
print(f'This is a normal object : {normal_list}')

weak_list = weakref.ref(obj)
weak_list_obj = weak_list()
print(f'This is a object created using weak reference : {weak_list_obj}')

proxy_list = weakref.proxy(obj)
print(f'This is a proxy object : {proxy_list}')

for objects in [normal_list, weak_list_obj, proxy_list]:
    print(f'Number of weak references : {weakref.getweakrefcount(objects)}')