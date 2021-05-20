import param
import panel as pn
import os
import time

from lumen.dashboard import Dashboard

root = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
tests = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','lumen','tests'))
exemples =  [
    ('penguins','dashboard.yaml'),
    ('precip','dashboard.yml'),
    ('psud/filters_selections','1_carte.yml')
]
testExample = exemples[2]





class App(param.Parameterized):
    #dashboard = Dashboard(specification=os.path.join(tests, 'sample_dashboard', 'dashboard.yml'))
    #intial_template = dashboard._template
    #doc = intial_template._init_doc()

    dashboard = param.Parameter()
    loading = pn.indicators.LoadingSpinner(value=True)

    def __init__(self, **kwargs):
        super(App, self).__init__(**kwargs)

    @param.depends('dashboard')
    def main(self):
        if not self.dashboard:
            pn.state.add_periodic_callback(self.update, 700, count=1)
            return self.loading
        else:
            return self.dashboard.layout

    def update(self):
        try:
            go = time.perf_counter()
            self.dashboard = Dashboard(specification=os.path.join(root, 'examples', testExample[0], testExample[1]))
            print(f"Time to create the dashboard {self.dashboard.name} :  {go}")
        except(Exception) as e:
            self.dashboard = pn.pane.HTML(object=f"<p>Erreur dans la préparation du dashboard : {e}</p>")
            print(e)



app = App()

pn.Row(app.main)


