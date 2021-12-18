import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import skfuzzy.control.visualization as vis

face_analyze = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'Face Analyze')
multiple_intelligence = ctrl.Antecedent(
    np.arange(3, 13, 1), 'Multiple Intelligence')
coverage_of_majors = ctrl.Consequent(
    np.arange(0, 81, 1), 'Coverage of Majors')

face_analyze['Low'] = fuzz.trapmf(face_analyze.universe, [0, 0, 0.08, 0.15])
face_analyze['Medium'] = fuzz.trimf(face_analyze.universe, [0.08, 0.15, 0.30])
face_analyze['High'] = fuzz.trapmf(
    face_analyze.universe, [0.15, 0.30, 1.00, 1.00])

multiple_intelligence['Low'] = fuzz.trapmf(
    multiple_intelligence.universe, [0, 0, 3, 5])
multiple_intelligence['Low Medium'] = fuzz.trimf(
    multiple_intelligence.universe, [3, 5, 7])
multiple_intelligence['Medium'] = fuzz.trimf(
    multiple_intelligence.universe, [5, 7, 9])
multiple_intelligence['High Medium'] = fuzz.trimf(
    multiple_intelligence.universe, [7, 9, 11])
multiple_intelligence['High'] = fuzz.trapmf(
    multiple_intelligence.universe, [9, 11, 12, 12])

coverage_of_majors['Low'] = fuzz.trimf(
    coverage_of_majors.universe, [0, 0, 20])
coverage_of_majors['Low Medium'] = fuzz.trimf(
    coverage_of_majors.universe, [0, 20, 40])
coverage_of_majors['Medium'] = fuzz.trimf(
    coverage_of_majors.universe, [20, 40, 60])
coverage_of_majors['High Medium'] = fuzz.trimf(
    coverage_of_majors.universe, [40, 60, 80])
coverage_of_majors['High'] = fuzz.trimf(
    coverage_of_majors.universe, [60, 80, 80])

rule1 = ctrl.Rule(
    face_analyze['Low'] & multiple_intelligence['Low'], coverage_of_majors['Low'])
rule2 = ctrl.Rule(
    face_analyze['Low'] & multiple_intelligence['Low Medium'], coverage_of_majors['Low'])
rule3 = ctrl.Rule(
    face_analyze['Low'] & multiple_intelligence['Medium'], coverage_of_majors['Low Medium'])
rule4 = ctrl.Rule(
    face_analyze['Low'] & multiple_intelligence['High Medium'], coverage_of_majors['Medium'])
rule5 = ctrl.Rule(
    face_analyze['Low'] & multiple_intelligence['High'], coverage_of_majors['High'])

rule6 = ctrl.Rule(
    face_analyze['Medium'] & multiple_intelligence['Low'], coverage_of_majors['Low'])
rule7 = ctrl.Rule(
    face_analyze['Medium'] & multiple_intelligence['Low Medium'], coverage_of_majors['Low Medium'])
rule8 = ctrl.Rule(
    face_analyze['Medium'] & multiple_intelligence['Medium'], coverage_of_majors['Medium'])
rule9 = ctrl.Rule(
    face_analyze['Medium'] & multiple_intelligence['High Medium'], coverage_of_majors['High Medium'])
rule10 = ctrl.Rule(
    face_analyze['Medium'] & multiple_intelligence['High'], coverage_of_majors['High'])

rule11 = ctrl.Rule(
    face_analyze['High'] & multiple_intelligence['Low'], coverage_of_majors['Low Medium'])
rule12 = ctrl.Rule(
    face_analyze['High'] & multiple_intelligence['Low Medium'], coverage_of_majors['Medium'])
rule13 = ctrl.Rule(
    face_analyze['High'] & multiple_intelligence['Medium'], coverage_of_majors['High Medium'])
rule14 = ctrl.Rule(
    face_analyze['High'] & multiple_intelligence['High Medium'], coverage_of_majors['High'])
rule15 = ctrl.Rule(
    face_analyze['High'] & multiple_intelligence['High'], coverage_of_majors['High'])

# rule1.view()
# rule2.view()
# rule3.view()
# rule4.view()
# rule5.view()
# rule6.view()
# rule7.view()
# rule8.view()
# rule9.view()
# rule10.view()
# rule11.view()
# rule12.view()
# rule13.view()
# rule14.view()
# rule15.view()

estimate_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15])


def fuzzy(face_analyze, multiple_intelligence):
    estimating = ctrl.ControlSystemSimulation(estimate_ctrl)
    estimating.input['Face Analyze'] = face_analyze
    estimating.input['Multiple Intelligence'] = multiple_intelligence
    estimating.compute()
    return estimating.output['Coverage of Majors']


# coverage_of_majors.view(sim=estimating)
plt.show()
