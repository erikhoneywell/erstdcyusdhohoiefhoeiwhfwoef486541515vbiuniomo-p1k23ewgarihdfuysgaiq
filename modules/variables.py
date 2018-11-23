from business_rules.variables import BaseVariables, numeric_rule_variable, string_rule_variable, select_multiple_rule_variable

class ProductVariables(BaseVariables):

    def __init__(self, products):
        self.products = products

    @numeric_rule_variable(label='Total amount of detectors')
    def detectors_total_amount(self):
        return self.returnMatchedKey('detectors','totalAmount')

    @select_multiple_rule_variable (label='List of detectors')
    def detectors_product_list(self):
        return self.returnMatchedKey('detectors','products')
    
    @numeric_rule_variable(label='Total amount of modules')
    def modules_total_amount(self):
        return self.returnMatchedKey('modules','totalAmount')

    @select_multiple_rule_variable (label='List of modules')
    def modules_product_list(self):
        return self.returnMatchedKey('modules','products')
    
    @numeric_rule_variable(label='Total amount of announcers')
    def announcers_total_amount(self):
        return self.returnMatchedKey('announcers','totalAmount')

    @select_multiple_rule_variable (label='List of announcers')
    def announcers_product_list(self):
        return self.returnMatchedKey('announcers','products')
    
    @numeric_rule_variable(label='Total amount of DVC componets')
    def dvc_total_amount(self):
        return self.returnMatchedKey('voceo','totalAmount')

    @select_multiple_rule_variable (label='List of DVC components')
    def dvc_product_list(self):
        return self.returnMatchedKey('voceo','products')
    
    
    @numeric_rule_variable(label='Total amount of CPU componets')
    def cpu_total_amount(self):
        return self.returnMatchedKey('cpu','totalAmount')

    @select_multiple_rule_variable (label='List of CPU components')
    def cpu_product_list(self):
        return self.returnMatchedKey('cpu','products')
    
    #add voceo
    @numeric_rule_variable(label='Total amount of voice components')
    def voice_total_amount(self):
        return self.returnMatchedKey('voceo','totalAmount')

    @select_multiple_rule_variable (label='List of voice components')
    def voice_product_list(self):
        return self.returnMatchedKey('voceo','products')

    #add pcb
    @numeric_rule_variable(label='Total amount of PCB components')
    def pcb_total_amount(self):
        return self.returnMatchedKey('pcb','totalAmount')
    
    @select_multiple_rule_variable (label='List of pcb components')
    def pcb_product_list(self):
        return self.returnMatchedKey('pcb','products')
    
    #add cabinets
    @numeric_rule_variable(label='Total amount of Cabinets components')
    def cabinets_total_amount(self):
        return self.returnMatchedKey('cabinets','totalAmount')
    
    @select_multiple_rule_variable (label='List of Cabinets components')
    def cabinets_product_list(self):
        return self.returnMatchedKey('cabinets','products')

    def returnMatchedKey(self,category,field):
        try: 
            return self.products[category][field] 
        except:
            return [] if field == 'products' else 0