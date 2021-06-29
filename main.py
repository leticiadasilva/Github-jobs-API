from view.jobs_view import JobsView

print("Type the term to search: ")
jobs = JobsView()
jobs.set_term(input())
print(jobs.response())