from controller.github_controller import GithubRequest

class JobsView():
  def __init__(self):
    self.controller = GithubRequest()

  def set_term(self, term):
    self.term = term

  def response(self):
    return self.controller.search(self.term, "csv")