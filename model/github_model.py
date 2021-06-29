import requests
import pandas as pd

class GithubModel():
  def __init__(self):
    self.url = 'https://jobs.github.com/positions.json'

  def search_as_json(self, term, page):
    response = self.call(term, page)
    return response.json()

  def search_as_csv(self, term, page):
    response = self.call(term, page)
    return self.transform_to_csv(response.content)

  def call(self, term, page):
    return requests.get(f'{self.url}?page={page}&search={term}')

  def transform_to_csv(self, json):
    f = pd.read_json(json)
    return f.to_csv()