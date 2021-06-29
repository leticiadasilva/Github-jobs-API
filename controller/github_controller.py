from model.github_model import GithubModel

class GithubController():
  def __init__(self):
    self.page = 1
    self.model = GithubModel()

  def search(self, term, return_type):
    return_obj = []

    if return_type == "csv":
      return_obj = self.model.search_as_csv(term, self.page)
    elif return_type == "json":
      return_obj = self.model.search_as_json(term, self.page)
    
    self.page += 1
    return return_obj