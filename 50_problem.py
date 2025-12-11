'''candidate = ["Python", "SQL", "ML", "AI"]
job = ["Python", "Docker", "AI"]
Skills candidate already has
Skills candidate needs to learn
Whether candidate is fully eligible'''
candidate = ["Python", "SQL", "ML", "AI"]
job = ["Python", "Docker", "AI"]
can=set(candidate)
jo=set(job)
already=can.intersection(jo)
print(already)
need=jo-can
print(need)
fully=can.union(jo)
print(fully)