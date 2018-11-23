from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_SELECT_MULTIPLE, FIELD_NUMERIC
from math import ceil

class ProductActions(BaseActions):

  def __init__(self, response):
    self.response = response

  @rule_action(params={"components": FIELD_SELECT_MULTIPLE})
  def add_components(self, components):
    self.response.add_recommendation(components)
  
  @rule_action(params={"restricted": FIELD_SELECT_MULTIPLE})
  def restict_component(self, restricted):
    self.response.add_restriction(restricted)