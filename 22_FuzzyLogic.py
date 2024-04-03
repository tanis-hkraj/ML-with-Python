import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

quality=ctrl.Antecedent(np.arange(0,11,1),'quality')
service=ctrl.Antecedent(np.arange(0,11,1),'service')
tip=ctrl.Consequent(np.arange(0,26,1),'tip')

quality['poor']=fuzz.trimf(quality.universe,[0,0,3])
quality['average']=fuzz.trimf(quality.universe,[2,5,8])
quality['good']=fuzz.trimf(quality.universe,[5,10,10])
# quality.automf(3)
service['poor']=fuzz.trimf(service.universe,[0,0,3])
service['average']=fuzz.trimf(service.universe,[2,5,8])
service['good']=fuzz.trimf(service.universe,[5,10,10])
# service.automf(3)

# print(quality.view)
tip['low']=fuzz.trimf(tip.universe,[0,0,6])
tip['medium']=fuzz.trimf(tip.universe,[5,10,13])
tip['high']=fuzz.trimf(tip.universe,[13,25,25])

rule1=ctrl.Rule(quality['poor']|service['poor'],tip['low'])
rule2=ctrl.Rule(quality['average']|service['average'],tip['medium'])
rule3=ctrl.Rule(quality['good']|service['good'],tip['high'])

fis=ctrl.ControlSystem([rule1,rule2,rule3])
tip_ctrl=ctrl.ControlSystemSimulation(fis)

tip_ctrl.input['quality']=float(input("Enter the Quality: "))
tip_ctrl.input['service']=float(input("Enter the Service: "))
tip_ctrl.compute()

print("Tip:",tip_ctrl.output['tip'])