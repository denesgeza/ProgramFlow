required_skills = ['python', 'github', 'linux']

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills):
    if skills > set(required_skills):
        interviewees.add(candidate)

print(interviewees)

print(candidates.get('anna'))
# print(candidates.items())
print(candidates['anna'])

print(candidates.get('anna') == candidates['anna'])
# print(candidates['frank']) #--> NOTES gives keyErrror if not in dict
print(candidates.get('frank')) # NOTES does not give an error if key is not present