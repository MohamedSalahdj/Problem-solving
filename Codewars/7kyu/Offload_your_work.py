"""
know, is that you are actually offloading your work to other freelancers and and you rarely need to do any work. You're living the life!

To make this process easier you need to write a method called workNeeded to figure out how much time you need to contribute to a project.

Giving the amount of time in minutes needed to complete the project and an array of pair values representing other freelancers' time in [Hours, Minutes] format ie. 
[[2, 33], [3, 44]] calculate how much time you will need to contribute to the project (if at all) and return a string depending on the case.

If we need to contribute time to the project then return "I need to work x hour(s) and y minute(s)"
If we don't have to contribute any time to the project then return "Easy Money!"

"""

def work_needed(project_minutes, free_lancers):
    all_free_lancers_time_minutes = 0
    for i in range(len(free_lancers)):
        all_free_lancers_time_minutes+=(free_lancers[i][0] * 60) + free_lancers[i][-1]
    
    if project_minutes <= all_free_lancers_time_minutes:
        return "Easy Money!" 
    else:
        time = project_minutes - all_free_lancers_time_minutes
        hour = time // 60
        minute = time % 60
        return f"I need to work {hour} hour(s) and {minute} minute(s)"