import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

face_analyze = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'Face Analyze')
multiple_intelligence = ctrl.Antecedent(
    np.arange(3, 13, 1), 'Multiple Intelligence')
coverage_of_majors = ctrl.Consequent(
    np.arange(0, 76, 1), 'Coverage of Majors')

face_analyze['low'] = fuzz.trapmf(face_analyze.universe, [0, 0, 0.08, 0.18])
face_analyze['medium'] = fuzz.trimf(face_analyze.universe, [0.08, 0.18, 0.35])
face_analyze['high'] = fuzz.trapmf(
    face_analyze.universe, [0.18, 0.35, 1.00, 1.00])

multiple_intelligence['low'] = fuzz.trapmf(
    multiple_intelligence.universe, [0, 0, 3, 5])
multiple_intelligence['low medium'] = fuzz.trimf(
    multiple_intelligence.universe, [3, 5, 7])
multiple_intelligence['medium'] = fuzz.trimf(
    multiple_intelligence.universe, [5, 7, 9])
multiple_intelligence['high medium'] = fuzz.trimf(
    multiple_intelligence.universe, [7, 9, 11])
multiple_intelligence['high'] = fuzz.trapmf(
    multiple_intelligence.universe, [9, 11, 12, 12])

coverage_of_majors['low'] = fuzz.trimf(coverage_of_majors.universe, [0, 0, 19])
coverage_of_majors['low medium'] = fuzz.trimf(
    coverage_of_majors.universe, [0, 19, 38])
coverage_of_majors['medium'] = fuzz.trimf(
    coverage_of_majors.universe, [19, 38, 57])
coverage_of_majors['high medium'] = fuzz.trimf(
    coverage_of_majors.universe, [38, 57, 76])
coverage_of_majors['high'] = fuzz.trimf(
    coverage_of_majors.universe, [57, 76, 76])

# face_analyze.view()
# multiple_intelligence.view()
# coverage_of_majors.view()

rule1 = ctrl.Rule(
    face_analyze['low'] & multiple_intelligence['low'], coverage_of_majors['low'])
rule2 = ctrl.Rule(
    face_analyze['low'] & multiple_intelligence['low medium'], coverage_of_majors['low'])
rule3 = ctrl.Rule(
    face_analyze['low'] & multiple_intelligence['medium'], coverage_of_majors['low medium'])
rule4 = ctrl.Rule(
    face_analyze['low'] & multiple_intelligence['high medium'], coverage_of_majors['medium'])
rule5 = ctrl.Rule(
    face_analyze['low'] & multiple_intelligence['high'], coverage_of_majors['medium'])
rule6 = ctrl.Rule(
    face_analyze['medium'] & multiple_intelligence['low'], coverage_of_majors['low medium'])
rule7 = ctrl.Rule(
    face_analyze['medium'] & multiple_intelligence['low medium'], coverage_of_majors['low medium'])
rule8 = ctrl.Rule(
    face_analyze['medium'] & multiple_intelligence['medium'], coverage_of_majors['medium'])
rule9 = ctrl.Rule(
    face_analyze['medium'] & multiple_intelligence['high medium'], coverage_of_majors['high medium'])
rule10 = ctrl.Rule(
    face_analyze['medium'] & multiple_intelligence['high'], coverage_of_majors['high medium'])
rule11 = ctrl.Rule(
    face_analyze['high'] & multiple_intelligence['low'], coverage_of_majors['medium'])
rule12 = ctrl.Rule(
    face_analyze['high'] & multiple_intelligence['low medium'], coverage_of_majors['medium'])
rule13 = ctrl.Rule(
    face_analyze['high'] & multiple_intelligence['medium'], coverage_of_majors['high medium'])
rule14 = ctrl.Rule(
    face_analyze['high'] & multiple_intelligence['high medium'], coverage_of_majors['high'])
rule15 = ctrl.Rule(
    face_analyze['high'] & multiple_intelligence['high'], coverage_of_majors['high'])

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
