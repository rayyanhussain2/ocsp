import multiprocessing

value = 272
states  = [
    {"State":"Andhra Pradesh" , "Key Player":0, "Weight":25} ,
    {"State":"Arunachal Pradesh" , "Key Player":0, "Weight":2} ,
    {"State":"Assam" , "Key Player":0, "Weight":14} ,
    {"State":"Bihar" , "Key Player":0, "Weight":40} ,
    {"State":"Chhattisgarh" , "Key Player":0, "Weight":11} ,
    {"State":"Goa" , "Key Player":0, "Weight":2} ,
    {"State":"Gujarat" , "Key Player":0, "Weight":26} ,
    {"State":"Haryana" , "Key Player":0, "Weight":20} ,

    {"State":"Himachal Pradesh" , "Key Player":0, "Weight":4} ,
    {"State":"Jharkhand" , "Key Player":0, "Weight":14} ,
    {"State":"Jharkhand" , "Key Player":0, "Weight":14} ,
    {"State":"Karnataka" , "Key Player":0, "Weight":28} ,
    {"State":"Kerala" , "Key Player":0, "Weight":20} ,
    {"State":"Madhya Pradesh" , "Key Player":0, "Weight":29} ,
    {"State":"Maharastra" , "Key Player":0, "Weight":48} ,
    {"State":"Manipur" , "Key Player":0, "Weight":2} ,
    {"State":"Meghalaya" , "Key Player":0, "Weight":2} ,
    {"State":"Mizoram" , "Key Player":0, "Weight":1} ,
    {"State":"Nagaland" , "Key Player":0, "Weight":1} ,
    {"State":"Odisha" , "Key Player":0, "Weight":21} ,
    {"State":"Punjab" , "Key Player":0, "Weight":13} ,
    {"State":"Rajasthan" , "Key Player":0, "Weight":25} ,
    {"State":"Sikkim" , "Key Player":0, "Weight":1} ,
    {"State":"Tamil Nadu" , "Key Player":0, "Weight":39} ,
    {"State":"Telangana" , "Key Player":0, "Weight":17} ,
    {"State":"Tripura" , "Key Player":0, "Weight":2} ,
    {"State":"Uttarakhand" , "Key Player":0, "Weight":5} ,
    {"State":"UP" , "Key Player":0, "Weight":80} ,
    {"State":"West Bengal" , "Key Player":0, "Weight":42} ,
    {"State":"Andaman and Nicobar Islands" , "Key Player":0, "Weight":1} ,
    {"State":"Chandigarh" , "Key Player":0, "Weight":1} ,
    {"State":"Dadra and Nagar Haveli" , "Key Player":0, "Weight":1} ,
    {"State":"Daman and Diu" , "Key Player":0, "Weight":1} ,
    {"State":"Lakshadweep" , "Key Player":0, "Weight":1} ,
    {"State":"Delhi" , "Key Player":0, "Weight":7} ,
    {"State":"Puducherry" , "Key Player":0, "Weight":1} ,
]

def priority(value, l, states):
    sum = 0
    for i in l:
        sum += i.get("Weight")
        if sum > value:
            for j in states:
                if j["State"] == i["State"]:
                    j["Key Player"] += 1
                    return

def worker(params):
    value, permutation, states = params
    priority(value, permutation, states)

def heapPermutation(a, size, value, states):
    if size == 1:
        worker((value, a, states))
        return

    jobs = []
    for i in range(size):
        new_permutation = a.copy()
        heapPermutation(new_permutation, size - 1, value, states)
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]

if __name__ == '__main__':
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    heapPermutation(states, len(states), value, states)
    print(states)