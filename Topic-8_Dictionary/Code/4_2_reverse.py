roster = {
		'STATS_385': ['Jack', 'Anne', 'John', 'Peter'],
		'PROG_388': ['Tom', 'Mark', 'Jack', 'Jin'],
		'LARGESCALE_487': ['Anne', 'John', 'Jin', 'Jack']
	}
dict_res = dict()
for course in roster.keys():
    names = roster[course]
    for nm in names:
        # if nm is not in dict_res keys, create a new item
        if nm not in dict_res.keys():
            dict_res[nm] = [course]
        # if nm has already been in dict_res keys, append a new course into the value
        else:
            dict_res[nm].append(course)

print(dict_res)