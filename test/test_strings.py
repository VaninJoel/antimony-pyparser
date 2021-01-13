
# Original source: <antimony-root>/src/test/test-data/initialValue.txt
initialValue = '''x=3
'''

# Original source: <antimony-root>/src/test/test-data/parameter.txt
parameter = '''a=3
'''

# Original source: <antimony-root>/src/test/test-data/parameter_inf.txt
parameter_inf = '''a=inf
'''

# Original source: <antimony-root>/src/test/test-data/parameter_nan.txt
parameter_nan = '''a=NaN
'''

# Original source: <antimony-root>/src/test/test-data/compartment.txt
compartment = '''x in y
'''

# Original source: <antimony-root>/src/test/test-data/rxn_right.txt
rxn_right = '''-> S1;
'''

# Original source: <antimony-root>/src/test/test-data/initialAssignment.txt
initialAssignment = '''x = 4/6
'''

# Original source: <antimony-root>/src/test/test-data/assignmentRule.txt
assignmentRule = '''x := 4.8
'''

# Original source: <antimony-root>/src/test/test-data/negparen.txt
negparen = '''a=-(x+2)
'''

# Original source: <antimony-root>/src/test/test-data/non_ascii.txt
non_ascii = '''â€"
a=3
'''

# Original source: <antimony-root>/src/test/test-data/rateRule.txt
rateRule = '''x' = 4.4
'''

# Original source: <antimony-root>/src/test/test-data/mean.txt
mean = '''a.mean = 25'''

# Original source: <antimony-root>/src/test/test-data/initialConcentration.txt
initialConcentration = '''species x=3
'''

# Original source: <antimony-root>/src/test/test-data/mode.txt
mode = '''a.mode = 25
'''

# Original source: <antimony-root>/src/test/test-data/parameter_neginf.txt
parameter_neginf = '''a=-infinity
'''

# Original source: <antimony-root>/src/test/test-data/reaction.txt
reaction = '''J0: a->; k1
'''

# Original source: <antimony-root>/src/test/test-data/median.txt
median = '''a.median = 25
'''

# Original source: <antimony-root>/src/test/test-data/SBO_param.txt
SBO_param = '''a.sboTerm = 25
'''

# Original source: <antimony-root>/src/test/test-data/species.txt
species = '''species x in y
'''

# Original source: <antimony-root>/src/test/test-data/event.txt
event = '''at(time>3): x=3
'''

# Original source: <antimony-root>/src/test/test-data/kurtosis.txt
kurtosis = '''a.kurtosis = 25
'''

# Original source: <antimony-root>/src/test/test-data/skewness.txt
skewness = '''a.skewness = 25
'''

# Original source: <antimony-root>/src/test/test-data/variance.txt
variance = '''a.variance = 25
'''

# Original source: <antimony-root>/src/test/test-data/reactionIn.txt
reactionIn = '''J0 in C: ->a; k1
'''

# Original source: <antimony-root>/src/test/test-data/names.txt
names = '''x is "This Name!"
'''

# Original source: <antimony-root>/src/test/test-data/range.txt
range = '''a.range = {-25, 25}'''

# Original source: <antimony-root>/src/test/test-data/sampleSize.txt
sampleSize = '''a.sampleSize = 25
'''

# Original source: <antimony-root>/src/test/test-data/simple_flux.txt
simple_flux = '''J0: s1->;
J0 > 0
'''

# Original source: <antimony-root>/src/test/test-data/simple_flux2.txt
simple_flux2 = '''J0: s1->;
0 < J0
'''

# Original source: <antimony-root>/src/test/test-data/initialAmount.txt
initialAmount = '''species x in C=3/C
'''

# Original source: <antimony-root>/src/test/test-data/simple_flux_neg.txt
simple_flux_neg = '''J0: s1->;
-3 < J0
'''

# Original source: <antimony-root>/src/test/test-data/standardError.txt
standardError = '''a.standardError = 25
'''

# Original source: <antimony-root>/src/test/test-data/SBO_param2.txt
SBO_param2 = '''a = 3
a.sboTerm = 25
'''

# Original source: <antimony-root>/src/test/test-data/units.txt
units = '''unit mL = .001*liters
'''

# Original source: <antimony-root>/src/test/test-data/SBO_species.txt
SBO_species = '''species a.sboTerm = 25
'''

# Original source: <antimony-root>/src/test/test-data/interactionActivation.txt
interactionActivation = '''J0: S1->;
Ji: S2 -o J0;
'''

# Original source: <antimony-root>/src/test/test-data/interactionGeneric.txt
interactionGeneric = '''J0: S1->;
Ji: S2 -( J0;
'''

# Original source: <antimony-root>/src/test/test-data/interactionInhibition.txt
interactionInhibition = '''J0: S1->;
Ji: S2 -| J0;
'''

# Original source: <antimony-root>/src/test/test-data/standardDeviation.txt
standardDeviation = '''a.standardDeviation = 25
'''

# Original source: <antimony-root>/src/test/test-data/substance_only_species.txt
substance_only_species = '''substanceOnly species S1
'''

# Original source: <antimony-root>/src/test/test-data/simple_objective.txt
simple_objective = '''J0: s1->;

maximize J0
'''

# Original source: <antimony-root>/src/test/test-data/simple_objective2.txt
simple_objective2 = '''J0: s1->;

minimize J0
'''

# Original source: <antimony-root>/src/test/test-data/two_sided_flux.txt
two_sided_flux = '''J0: s1->;
-10 < J0 < 10
'''

# Original source: <antimony-root>/src/test/test-data/eventT0.txt
eventT0 = '''at(time>3), t0=false: x=3
'''

# Original source: <antimony-root>/src/test/test-data/distribution.txt
distribution = '''a.distribution = normal(3,x)'''

# Original source: <antimony-root>/src/test/test-data/encodes.txt
encodes = '''a=3
a encodes "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/hasPart.txt
hasPart = '''a=3
a hasPart "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/SBO_compartment.txt
SBO_compartment = '''compartment a.sboTerm = 25
'''

# Original source: <antimony-root>/src/test/test-data/credibleInterval.txt
credibleInterval = '''a.credibleInterval = {0, x}
'''

# Original source: <antimony-root>/src/test/test-data/eventPriority.txt
eventPriority = '''at(time>3), priority=2: x=3
'''

# Original source: <antimony-root>/src/test/test-data/hasTaxon.txt
hasTaxon = '''a=3
a hasTaxon "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/identity.txt
identity = '''a=3
a identity "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/interquartileRange.txt
interquartileRange = '''a.interquartileRange = {x, y}'''

# Original source: <antimony-root>/src/test/test-data/isPartOf.txt
isPartOf = '''a=3
a isPartOf "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/occursIn.txt
occursIn = '''a=3
a occursIn "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/rxn_right_mod.txt
rxn_right_mod = '''module foo()
  -> S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/SBO_reaction.txt
SBO_reaction = '''J0: A->; 
J0.sboTerm = 888
'''

# Original source: <antimony-root>/src/test/test-data/coefficientOfVariation.txt
coefficientOfVariation = '''a.coefficientOfVariation = 25
'''

# Original source: <antimony-root>/src/test/test-data/hasVersion.txt
hasVersion = '''a=3
a hasVersion "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/SBO_localvar.txt
SBO_localvar = '''model foo()
  sboTerm = 5
end'''

# Original source: <antimony-root>/src/test/test-data/confidenceInterval.txt
confidenceInterval = '''a.confidenceInterval = {0, 25}
'''

# Original source: <antimony-root>/src/test/test-data/hasProperty.txt
hasProperty = '''a=3
a hasProperty "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/isEncodedBy.txt
isEncodedBy = '''a=3
a isEncodedBy "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/isHomologTo.txt
isHomologTo = '''a=3
a isHomologTo "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/isVersionOf.txt
isVersionOf = '''a=3
a isVersionOf "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/simple_flux_and_objective.txt
simple_flux_and_objective = '''J0: s1->;

J0<3
maximize J0
'''

# Original source: <antimony-root>/src/test/test-data/simple_flux_and_objective2.txt
simple_flux_and_objective2 = '''J0: s1->;

J0>3
minimize J0
'''

# Original source: <antimony-root>/src/test/test-data/isPropertyOf.txt
isPropertyOf = '''a=3
a isPropertyOf "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/compound_units4.txt
compound_units4 = '''unit persecondsq = 1 / seconds^2
'''

# Original source: <antimony-root>/src/test/test-data/isDescribedBy.txt
isDescribedBy = '''a=3
a isDescribedBy "BQB_thing"
'''

# Original source: <antimony-root>/src/test/test-data/eventPersistent.txt
eventPersistent = '''at(time>3), persistent=false: x=3
'''

# Original source: <antimony-root>/src/test/test-data/formula_objective.txt
formula_objective = '''J0: s1->;

maximize 3 J0 + 2 J0
'''

# Original source: <antimony-root>/src/test/test-data/simple_objective4.txt
simple_objective4 = '''OBJ = J0
maximize OBJ
J0: s1->;
'''

# Original source: <antimony-root>/src/test/test-data/simple_objective5.txt
simple_objective5 = '''maximize OBJ
OBJ = J0
J0: s1->;
'''

# Original source: <antimony-root>/src/test/test-data/eventFromTrigger.txt
eventFromTrigger = '''at(time>3), fromTrigger=false: x=3
'''

# Original source: <antimony-root>/src/test/test-data/SBO_event.txt
SBO_event = '''E0: at(time>3): b=4
E0.sboTerm=901
'''

# Original source: <antimony-root>/src/test/test-data/SBO_module.txt
SBO_module = '''model foo()
end

foo.sboTerm = 8
'''

# Original source: <antimony-root>/src/test/test-data/simple_objective3.txt
simple_objective3 = '''J0: s1->;

OBJ = J0
maximize OBJ
'''

# Original source: <antimony-root>/src/test/test-data/function_name.txt
function_name = '''function foo()
 3;
end
foo is "foo!"'''

# Original source: <antimony-root>/src/test/test-data/compound_units1.txt
compound_units1 = '''unit voltage = 1000 grams * 1 meters^2
'''

# Original source: <antimony-root>/src/test/test-data/module_name.txt
module_name = '''module foo()
 a=3;
end
foo is "foo!"
'''

# Original source: <antimony-root>/src/test/test-data/SBO_submodel.txt
SBO_submodel = '''model foo()
end

A:foo()
A.sboTerm=8
'''

# Original source: <antimony-root>/src/test/test-data/SBO_function.txt
SBO_function = '''function foo()
  3;
end

foo.sboTerm = 8'''

# Original source: <antimony-root>/src/test/test-data/hierarchy.txt
hierarchy = '''model foo()
  x=3;
end

model bar()
  A: foo()
end
'''

# Original source: <antimony-root>/src/test/test-data/compound_units2.txt
compound_units2 = '''unit voltage = 1000 grams * meters^2 / seconds^3 / ampere
'''

# Original source: <antimony-root>/src/test/test-data/port.txt
port = '''model foo(x)
  x=3;
end

model bar()
  A: foo(X)
end
'''

# Original source: <antimony-root>/src/test/test-data/defaultSubCompartment.txt
defaultSubCompartment = '''model foo()
 species x;
end

model bar()
 A: foo();
end
'''

# Original source: <antimony-root>/src/test/test-data/simple_flux3.txt
simple_flux3 = '''J0: s1->;
J1: s2->;

J0 < 1000
J0 > 0
J1 <= 1000
J1 >= 0
'''

# Original source: <antimony-root>/src/test/test-data/simple_flux3_reverse.txt
simple_flux3_reverse = '''J0: s1->;
J1: s2->;

1000 > J0
0 < J0
1000 >= J1
0 <= J1
'''

# Original source: <antimony-root>/src/test/test-data/compound_units3.txt
compound_units3 = '''unit voltage = 1000 grams * 1 meters^2 / 1 seconds^3 / 1 ampere
'''

# Original source: <antimony-root>/src/test/test-data/externalParameter2.txt
externalParameter2 = '''a.externalParameter = x; a.externalParameter is "http://my.url/"
'''

# Original source: <antimony-root>/src/test/test-data/externalParameter3.txt
externalParameter3 = '''a.externalParameter = -x; a.externalParameter is "http://my.url/"
'''

# Original source: <antimony-root>/src/test/test-data/SBO_module_rt.txt
SBO_module_rt = '''// Created by libAntimony v2.12.0
model *foo()
end

foo.sboTerm = 8'''

# Original source: <antimony-root>/src/test/test-data/deletion.txt
deletion = '''model foo()
  x=3;
end

model bar()
  A: foo()
  delete A.x
end
'''

# Original source: <antimony-root>/src/test/test-data/externalParameter1.txt
externalParameter1 = '''a.externalParameter = {-20, -15}; a.externalParameter is "http://my.url/"
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionOnly.txt
replaceReactionOnly = '''model foo()
  J0: x->;
end

model bar()
  A: foo()
  A.J0 is J1
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionOnly2.txt
replaceReactionOnly2 = '''model foo()
  J0: ->x;
end

model bar()
  A: foo()
  A.J0 is J1
end
'''

# Original source: <antimony-root>/src/test/test-data/units_rt.txt
units_rt = '''//Created by libAntimony v2.5
// Unit definitions:
unit mL = 1e-3 litre;
'''

# Original source: <antimony-root>/src/test/test-data/function_name_rt.txt
function_name_rt = '''// Created by libAntimony v2.12.0
function foo()
  3;
end

foo is "foo!"'''

# Original source: <antimony-root>/src/test/test-data/deleteAssignmentRuleOfAnother.txt
deleteAssignmentRuleOfAnother = '''model foo()
  P1 := X;
end

model bar1()
  A: foo();
  delete A.X;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteRateRuleOfAnother.txt
deleteRateRuleOfAnother = '''model foo()
  P1' = X;
end

model bar1()
  A: foo();
  delete A.X;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionWithKineticLaw.txt
replaceReactionWithKineticLaw = '''model foo()
  J0: S1->;x;
end

model bar()
  A: foo()
  A.J0 is J1
end
'''

# Original source: <antimony-root>/src/test/test-data/SBO_function_rt.txt
SBO_function_rt = '''// Created by libAntimony v2.12.0
function foo()
  3;
end

foo.sboTerm = 8'''

# Original source: <antimony-root>/src/test/test-data/deleteAssignmentRuleIndirect.txt
deleteAssignmentRuleIndirect = '''model foo()
  P1 := 3;
end

model bar1()
  A: foo();
  delete A.P1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteInitialAssignmentOfAnother.txt
deleteInitialAssignmentOfAnother = '''model foo()
  P1 = 3*X;
end

model bar1()
  A: foo();
  delete A.X;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteRateRuleIndirect.txt
deleteRateRuleIndirect = '''model foo()
  P1' = 3;
end

model bar1()
  A: foo();
  delete A.P1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteInitialAssignmentIndirect.txt
deleteInitialAssignmentIndirect = '''model foo()
  P1 = 2/3;
end

model bar1()
  A: foo();
  delete A.P1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpeciesInDefaultCompartment.txt
deleteSpeciesInDefaultCompartment = '''model foo()
  species S1
end

model bar1()
  A: foo();
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpeciesPortDefaultCompartment.txt
deleteSpeciesPortDefaultCompartment = '''model foo(S1)
  species S1
end

model bar1()
  A: foo();
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceInitialAssignment.txt
replaceInitialAssignment = '''model foo()
  x = 4/8
end

model bar()
  A: foo()
  A.x is y
  y = 2/2
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceParameter.txt
replaceParameter = '''model foo()
  x = 4.8
end

model bar()
  A: foo()
  A.x is y
  y = 2.2
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceAssignmentRule.txt
replaceAssignmentRule = '''model foo()
  x := 4.8
end

model bar()
  A: foo()
  A.x is y
  y := 2.2
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceRateRule.txt
replaceRateRule = '''model foo()
  x' = 4.8
end

model bar()
  A: foo()
  A.x is y
  y' = 2.2
end
'''

# Original source: <antimony-root>/src/test/test-data/compound_units4_rt.txt
compound_units4_rt = '''//Created by libAntimony v2.5
// Unit definitions:
unit persecondsq = 1 / second^2;
'''

# Original source: <antimony-root>/src/test/test-data/deleteAssignmentRuleDirect.txt
deleteAssignmentRuleDirect = '''model foo()
  P1 := 3;
end

model bar1()
  A: foo();
  A.P1 is x;
  x :=;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteInitialAssignmentDirect.txt
deleteInitialAssignmentDirect = '''model foo()
  P1 = 3^2;
end

model bar1()
  A: foo();
  A.P1 is x;
  x =;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteKineticLaw.txt
deleteKineticLaw = '''model foo()
  J1: S1 -> ; K1;
end

model bar1()
  A: foo();
  delete A.K1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteRateRuleDirect.txt
deleteRateRuleDirect = '''model foo()
  P1' = 3;
end

model bar1()
  A: foo();
  x is A.P1;
  x' =;
end
'''

# Original source: <antimony-root>/src/test/test-data/formula_objective2.txt
formula_objective2 = '''J0: s1->;

maximize 3 J0 + 2 J0 - 4*J0 - (8*J0 - -2.2*J0 - ( - ( - (- (-0.1 J0)))))
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpecies.txt
deleteSpecies = '''model foo()
  species S1 in C1
end

model bar1()
  A: foo();
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionWithCompartments1.txt
replaceReactionWithCompartments1 = '''model foo()
  x in C2;
  J0: x->;
end

model bar()
  A: foo()
  A.J0 is J1
end
'''

# Original source: <antimony-root>/src/test/test-data/compound_units1_rt.txt
compound_units1_rt = '''//Created by libAntimony v2.5
// Unit definitions:
unit voltage = 1e3 gram * metre^2;
'''

# Original source: <antimony-root>/src/test/test-data/deleteProduct.txt
deleteProduct = '''model foo()
  J1: S1 -> S2; K1;
end

model bar1()
  A: foo();
  delete A.S2;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteReactant.txt
deleteReactant = '''model foo()
  J1: S1 -> S2; K1;
end

model bar1()
  A: foo();
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpeciesPort.txt
deleteSpeciesPort = '''model foo(S1)
  species S1 in C1
end

model bar1()
  A: foo();
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/submodelInteraction.txt
submodelInteraction = '''model foo()
  species S2;
  J0: x->;
  S2 -o J0;
end

model bar()
  A: foo()
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment3.txt
deleteEventAssignment3 = '''model foo()
  E1: at (Y1 > 3): Z1=0;
end

model bar()
  A: foo();
  delete A.Z1;
end
'''

# Original source: <antimony-root>/src/test/test-data/defaultSubSubCompartment.txt
defaultSubSubCompartment = '''model foo()
 species x;
end

model bar()
 A: foo();
end

model baz()
 A: bar();
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionWithKineticLawRxnRef.txt
replaceReactionWithKineticLawRxnRef = '''model foo()
  J0: S1->;J1;
  J1: ->S1;
end

model bar()
  A: foo()
  A.J0 is Jtop
end
'''

# Original source: <antimony-root>/src/test/test-data/three_level_constraints.txt
three_level_constraints = '''const x, y
0 < x < 1
8 > x > 3
-5 < x <= 3
100 > x >= 4
2 != x != 5
constraint: y==x==7
'''

# Original source: <antimony-root>/src/test/test-data/replaceCompartment.txt
replaceCompartment = '''model foo()
  compartment x = 4.8
end

model bar()
  A: foo()
  A.x is y
  y = 2.2
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceSpeciesDefaultCompartment.txt
replaceSpeciesDefaultCompartment = '''model foo()
  species S1
end

model bar1()
  A: foo();
  species S2;
  A.S1 is S2;
end
'''

# Original source: <antimony-root>/src/test/test-data/assignmentRule_rt.txt
assignmentRule_rt = '''//Created by libAntimony v2.5
// Assignment Rules:
x := 4.8;

//Other declarations:
var x;
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpeciesInDefaultCompartment2.txt
deleteSpeciesInDefaultCompartment2 = '''model foo()
  species S1
end

model bar1()
  species S2;
  A: foo();
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment5.txt
deleteEventAssignment5 = '''model foo()
  E1: at (Y1 > 3): Z1=z, Q1=q;
end

model bar()
  A: foo();
  delete A.z;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment.txt
deleteEventAssignment = '''model foo()
  E1: at (Y1 > 3): Z1=0, Q1=0;
end

model bar()
  A: foo();
  delete A.Z1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment4.txt
deleteEventAssignment4 = '''model foo()
  E1: at (Y1 > 3): Z1=0, Q1=0;
end

model bar()
  A: foo();
  delete A.Q1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteTrigger.txt
deleteTrigger = '''model foo()
  E1: at (Y1 > 3): Z1=0, Q1=0;
end

model bar()
  A: foo();
  delete A.Y1;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionWithCompartments2.txt
replaceReactionWithCompartments2 = '''model foo()
  J0 in C1;
  x in C2;
  J0: x->;
end

model bar()
  A: foo()
  A.J0 is J1
end
'''

# Original source: <antimony-root>/src/test/test-data/subport.txt
subport = '''model foo(x0)
  x0=3;
end

model bar(x1)
  A: foo(x1)
end

model baz(x2)
  A: bar(x2)
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceSpecies.txt
replaceSpecies = '''model foo()
  species S1 in C1
end

model bar1()
  A: foo();
  species S2;
  A.S1 is S2;
end
'''

# Original source: <antimony-root>/src/test/test-data/initialValue_rt.txt
initialValue_rt = '''//Created by libAntimony v2.5
// Variable initializations:
x = 3;

//Other declarations:
const x;
'''

# Original source: <antimony-root>/src/test/test-data/parameter_rt.txt
parameter_rt = '''//Created by libAntimony v2.5
// Variable initializations:
a = 3;

//Other declarations:
const a;
'''

# Original source: <antimony-root>/src/test/test-data/replaceInteraction.txt
replaceInteraction = '''model foo()
  species S2;
  J0: x->;
  S2 -o J0;
end

model bar()
  A: foo()
  A.J0 is J1
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteModifierKineticLaw.txt
deleteModifierKineticLaw = '''model foo()
  species S2;
  J1: S1 -> ; S2*K1;
end

model bar1()
  A: foo();
  delete A.S2;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteReaction.txt
deleteReaction = '''model foo()
  species S1 in C1
  J1: S1 ->; K1;
end

model bar1()
  A: foo();
  delete A.J1;
end
'''

# Original source: <antimony-root>/src/test/test-data/initialAssignment_rt.txt
initialAssignment_rt = '''//Created by libAntimony v2.5
// Variable initializations:
x = 4/6;

//Other declarations:
const x;
'''

# Original source: <antimony-root>/src/test/test-data/parameter_inf_rt.txt
parameter_inf_rt = '''//Created by libAntimony v2.5
// Variable initializations:
a = inf;

//Other declarations:
const a;
'''

# Original source: <antimony-root>/src/test/test-data/parameter_neginf_rt.txt
parameter_neginf_rt = '''//Created by libAntimony v2.5
// Variable initializations:
a = -inf;

//Other declarations:
const a;
'''

# Original source: <antimony-root>/src/test/test-data/parameter_nan_rt.txt
parameter_nan_rt = '''//Created by libAntimony v2.7.0
// Variable initializations:
a = NaN;

//Other declarations:
const a;
'''

# Original source: <antimony-root>/src/test/test-data/simple_flux_eq_neq.txt
simple_flux_eq_neq = '''J0: s1->;
J1: s2->;

constraint: J0 == 5
constraint: J0 != 3
constraint: 5 == J1
constraint: 3 != J0
'''

# Original source: <antimony-root>/src/test/test-data/SBO_submodel_shadowed.txt
SBO_submodel_shadowed = '''model foo()
  sboTerm=1
end
 
A: foo()
A.sboTerm is b
A.sboTerm = 3
A.SBOTERM = 27
foo.sboTerm = 83
'''

# Original source: <antimony-root>/src/test/test-data/subport2.txt
subport2 = '''model foo(x0)
  x0=3;
end

model bar()
  A: foo()
end

model baz()
  A: bar()
  A.A.x0 is x1;
end
'''

# Original source: <antimony-root>/src/test/test-data/compound_units2_rt.txt
compound_units2_rt = '''//Created by libAntimony v2.5
// Unit definitions:
unit voltage = 1e3 gram * metre^2 / (second^3 * ampere);
'''

# Original source: <antimony-root>/src/test/test-data/compound_units3_rt.txt
compound_units3_rt = '''//Created by libAntimony v2.5
// Unit definitions:
unit voltage = 1e3 gram * metre^2 / (second^3 * ampere);
'''

# Original source: <antimony-root>/src/test/test-data/initialConcentration_rt.txt
initialConcentration_rt = '''//Created by libAntimony v2.5
// Compartments and Species:
species x;

// Species initializations:
x = 3;
'''

# Original source: <antimony-root>/src/test/test-data/defaultOrNotCompartment.txt
defaultOrNotCompartment = '''model foo()
 species x;
end

model bar()
 species y in C;
end

model baz()
 A: bar();
 B: foo();
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteModifier.txt
deleteModifier = '''model foo()
  species S2;
  J1: S1 -> ; ;
  S2 -o J1;
end

model bar1()
  A: foo();
  delete A.S2;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteDelay.txt
deleteDelay = '''model foo()
  E1: at DELAY1 after (Y1 > 3): Z1=0, Q1=0;
end

model bar()
  A: foo();
  delete A.DELAY1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deletePriority.txt
deletePriority = '''model foo()
  E1: at (Y1 > 3), priority=PRIORITY1: Z1=0;
end

model bar()
  A: foo();
  delete A.PRIORITY1;
end
'''

# Original source: <antimony-root>/src/test/test-data/negparen_rt.txt
negparen_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = -(x + 2);
x = ;

// Other declarations:
const a, x;'''

# Original source: <antimony-root>/src/test/test-data/global_units.txt
global_units = '''length = meters;
area = meters^2;
volume = meters^3;
substance = moles;
extent = dimensionless;
time_unit = seconds*60
'''

# Original source: <antimony-root>/src/test/test-data/rateRule_rt.txt
rateRule_rt = '''//Created by libAntimony v2.5
// Rate Rules:
x' = 4.4;

// Variable initializations:
x = ;

//Other declarations:
var x;
'''

# Original source: <antimony-root>/src/test/test-data/substance_only_species_rt.txt
substance_only_species_rt = '''// Created by libAntimony v2.10.0
// Compartments and Species:
substanceOnly species S1;

// Species initializations:
S1 = ;
'''

# Original source: <antimony-root>/src/test/test-data/numeric_constraints.txt
numeric_constraints = '''const x, y
x < 1
x > 3
x <= 3
x >= 4
x != 5
constraint: x==7

1 < y
2 > y
0 <= y
3 >= y
1.5 != y
constraint: 1.7 == y
'''

# Original source: <antimony-root>/src/test/test-data/event_rt.txt
event_rt = '''//Created by libAntimony v2.5
// Events:
_E0: at time>3: x = 3;

// Variable initializations:
x = ;

//Other declarations:
var x;
'''

# Original source: <antimony-root>/src/test/test-data/SBO_param_rt.txt
SBO_param_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// SBO terms:
a.sboTerm = 25'''

# Original source: <antimony-root>/src/test/test-data/SBO_param2_rt.txt
SBO_param2_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// SBO terms:
a.sboTerm = 25'''

# Original source: <antimony-root>/src/test/test-data/hasPart_rt.txt
hasPart_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a part "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/names_rt.txt
names_rt = '''//Created by libAntimony v2.5
// Variable initializations:
x = ;

//Other declarations:
const x;

//Display Names:
x is "This Name!";
'''

# Original source: <antimony-root>/src/test/test-data/hasTaxon_rt.txt
hasTaxon_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a taxon "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/numeric_constraints_neg.txt
numeric_constraints_neg = '''const x, y
x < -1
x > -3
x <= -3
x >= -4
x != -5
constraint: x==-7

-1 < y
-2 > y
-0 <= y
-3 >= y
-1.5 != y
constraint: -1.7 == y
'''

# Original source: <antimony-root>/src/test/test-data/hasVersion_rt.txt
hasVersion_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a version "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/isEncodedBy_rt.txt
isEncodedBy_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a encoder "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/isHomologTo_rt.txt
isHomologTo_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a homolog "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/SBO_species_rt.txt
SBO_species_rt = '''// Created by libAntimony v2.12.0
// Compartments and Species:
species a;

// Species initializations:
a = ;

// SBO terms:
a.sboTerm = 25'''

# Original source: <antimony-root>/src/test/test-data/eventDelay.txt
eventDelay = '''//Created by libAntimony v2.5
// Events:
_E0: at 2 after time>3: x = 3;

// Variable initializations:
x = ;

//Other declarations:
var x;
'''

# Original source: <antimony-root>/src/test/test-data/eventDelay_rt.txt
eventDelay_rt = '''//Created by libAntimony v2.5
// Events:
_E0: at 2 after time>3: x = 3;

// Variable initializations:
x = ;

//Other declarations:
var x;
'''

# Original source: <antimony-root>/src/test/test-data/hasProperty_rt.txt
hasProperty_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a property "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/identity_rt.txt
identity_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a identity "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/isPartOf_rt.txt
isPartOf_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a parthood "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/isVersionOf_rt.txt
isVersionOf_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a hypernym "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/occursIn_rt.txt
occursIn_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a container "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/rxn_right_rt.txt
rxn_right_rt = '''// Created by libAntimony v2.10.0
// Compartments and Species:
species S1;

// Reactions:
_J0:  -> S1; ;

// Species initializations:
S1 = ;'''

# Original source: <antimony-root>/src/test/test-data/SBO_localvar_rt.txt
SBO_localvar_rt = '''// Created by libAntimony v2.12.0
model *foo()

  // Variable initializations:
  sboTerm = 5;

  // Other declarations:
  const sboTerm;
end'''

# Original source: <antimony-root>/src/test/test-data/encodes_rt.txt
encodes_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a encodement "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/eventT0_rt.txt
eventT0_rt = '''//Created by libAntimony v2.5
// Events:
_E0: at time>3, t0=false: x = 3;

// Variable initializations:
x = ;

//Other declarations:
var x;
'''

# Original source: <antimony-root>/src/test/test-data/mean_rt.txt
mean_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.mean = 25'''

# Original source: <antimony-root>/src/test/test-data/mode_rt.txt
mode_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.mode = 25'''

# Original source: <antimony-root>/src/test/test-data/fluxes_and_objectives.txt
fluxes_and_objectives = '''J0: s1->;
J1: s2->;
J2: s3->;
J3: ->s1;

-10<J0<-3
-5>J1>-100
-100<=J2<=-10
-100>=J3>=-2.2

Obj = J0 - J1 - 2 * J2 - 3.3*J3
minimize Obj
'''

# Original source: <antimony-root>/src/test/test-data/isDescribedBy_rt.txt
isDescribedBy_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a description "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/model1.txt
model1 = '''model foo(p1, p2)
  --p1--p2--
end

model bar()
  sub1: foo(x, y);
  sub2: foo(z, q);
  sub1--sub2
  //p1--sub--stop2
  //sub.J0 = 13;
end
'''

# Original source: <antimony-root>/src/test/test-data/median_rt.txt
median_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.median = 25'''

# Original source: <antimony-root>/src/test/test-data/subsubport.txt
subsubport = '''model foo(x0)
  x0=3;
end

model bar()
  A1: foo()
end

model baz()
  A2: bar()
end

model biff()
  A3: baz()
  A3.A2.A1.x0 is x1;
end
'''

# Original source: <antimony-root>/src/test/test-data/eventPriority_rt.txt
eventPriority_rt = '''//Created by libAntimony v2.5
// Events:
_E0: at time>3, priority = 2: x = 3;

// Variable initializations:
x = ;

//Other declarations:
var x;
'''

# Original source: <antimony-root>/src/test/test-data/isPropertyOf_rt.txt
isPropertyOf_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = 3;

// Other declarations:
const a;

// CV terms:
a propertyBearer "BQB_thing"'''

# Original source: <antimony-root>/src/test/test-data/module_name_rt.txt
module_name_rt = '''// Created by libAntimony v2.12.0
model *foo()

  // Variable initializations:
  a = 3;

  // Other declarations:
  const a;
end

foo is "foo!"'''

# Original source: <antimony-root>/src/test/test-data/skewness_rt.txt
skewness_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.skewness = 25'''

# Original source: <antimony-root>/src/test/test-data/variance_rt.txt
variance_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.variance = 25'''

# Original source: <antimony-root>/src/test/test-data/kurtosis_rt.txt
kurtosis_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.kurtosis = 25
'''

# Original source: <antimony-root>/src/test/test-data/sampleSize_rt.txt
sampleSize_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.sampleSize = 25'''

# Original source: <antimony-root>/src/test/test-data/SBO_submodel_rt.txt
SBO_submodel_rt = '''// Created by libAntimony v2.12.0
model foo()
end


// Sub-modules, and any changes to those submodules:
A: foo();

// SBO terms:
A.sboTerm = 8

'''

# Original source: <antimony-root>/src/test/test-data/eventPersistent_rt.txt
eventPersistent_rt = '''//Created by libAntimony v2.5
// Events:
_E0: at time>3, persistent=false: x = 3;

// Variable initializations:
x = ;

//Other declarations:
var x;
'''

# Original source: <antimony-root>/src/test/test-data/range_rt.txt
range_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.range = {-25, 25}'''

# Original source: <antimony-root>/src/test/test-data/eventFromTrigger_rt.txt
eventFromTrigger_rt = '''//Created by libAntimony v2.5
// Events:
_E0: at time>3, fromTrigger=false: x = 3;

// Variable initializations:
x = ;

//Other declarations:
var x;
'''

# Original source: <antimony-root>/src/test/test-data/standardError_rt.txt
standardError_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.standardError = 25'''

# Original source: <antimony-root>/src/test/test-data/standardDeviation_rt.txt
standardDeviation_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.standardDeviation = 25'''

# Original source: <antimony-root>/src/test/test-data/coefficientOfVariation_rt.txt
coefficientOfVariation_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.coefficientOfVariation = 25'''

# Original source: <antimony-root>/src/test/test-data/confidenceInterval_rt.txt
confidenceInterval_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.confidenceInterval = {0, 25}'''

# Original source: <antimony-root>/src/test/test-data/credibleInterval_rt.txt
credibleInterval_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;
x = ;

// Other declarations:
const a, x;

// Uncertainty parameters:
a.credibleInterval = {0, x}'''

# Original source: <antimony-root>/src/test/test-data/distribution_rt.txt
distribution_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;
x = ;

// Other declarations:
const a, x;

// Uncertainty parameters:
a.distribution = normal(3, x)'''

# Original source: <antimony-root>/src/test/test-data/SBO_event_rt.txt
SBO_event_rt = '''// Created by libAntimony v2.12.0
// Events:
E0: at time > 3: b = 4;

// Variable initializations:
b = ;

// Other declarations:
var b;

// SBO terms:
E0.sboTerm = 901'''

# Original source: <antimony-root>/src/test/test-data/SBO_reaction_rt.txt
SBO_reaction_rt = '''// Created by libAntimony v2.12.0
// Compartments and Species:
species A;

// Reactions:
J0: A -> ; ;

// Species initializations:
A = ;

// SBO terms:
J0.sboTerm = 888'''

# Original source: <antimony-root>/src/test/test-data/rxn_right_mod_rt.txt
rxn_right_mod_rt = '''// Created by libAntimony v2.10.0
model *foo()

  // Compartments and Species:
  species S1;

  // Reactions:
  _J0:  -> S1; ;

  // Species initializations:
  S1 = ;
end'''

# Original source: <antimony-root>/src/test/test-data/interquartileRange_rt.txt
interquartileRange_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;
x = ;
y = ;

// Other declarations:
const a, x, y;

// Uncertainty parameters:
a.interquartileRange = {x, y}'''

# Original source: <antimony-root>/src/test/test-data/SBO_compartment_rt.txt
SBO_compartment_rt = '''// Created by libAntimony v2.12.0
// Compartments and Species:
compartment a;

// Compartment initializations:
a = ;

// Other declarations:
const a;

// SBO terms:
a.sboTerm = 25'''

# Original source: <antimony-root>/src/test/test-data/interactionActivation_rt.txt
interactionActivation_rt = '''//Created by libAntimony v2.5
// Compartments and Species:
species S1, S2;

// Reactions:
J0: S1 -> ; ;

// Interactions:
Ji: S2 -o J0; ;

// Species initializations:
S1 = ;
S2 = ;
'''

# Original source: <antimony-root>/src/test/test-data/interactionGeneric_rt.txt
interactionGeneric_rt = '''//Created by libAntimony v2.5
// Compartments and Species:
species S1, S2;

// Reactions:
J0: S1 -> ; ;

// Interactions:
Ji: S2 -( J0; ;

// Species initializations:
S1 = ;
S2 = ;
'''

# Original source: <antimony-root>/src/test/test-data/interactionInhibition_rt.txt
interactionInhibition_rt = '''//Created by libAntimony v2.5
// Compartments and Species:
species S1, S2;

// Reactions:
J0: S1 -> ; ;

// Interactions:
Ji: S2 -| J0; ;

// Species initializations:
S1 = ;
S2 = ;
'''

# Original source: <antimony-root>/src/test/test-data/compartment_rt.txt
compartment_rt = '''//Created by libAntimony v2.5
// Compartments and Species:
compartment y;

// Compartment initializations:
y = ;

// Variable initializations:
x = ;

//Other declarations:
const y, x;
'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment2.txt
deleteEventAssignment2 = '''model foo()
  E1: at DELAY1 after (Y1 > 3), priority=PRIORITY1: Z1=0, Q1=0;
  e2: at delay2 after (y2 > 3), priority=priority2: z2=0, q2=0;
end

model bar()
  A: foo();
  delete A.Z1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteDelay2.txt
deleteDelay2 = '''model foo()
  E1: at DELAY1 after (Y1 > 3), priority=PRIORITY1: Z1=0, Q1=0;
  e2: at delay2 after (y2 > 3), priority=priority2: z2=0, q2=0;
end

model bar()
  A: foo();
  delete A.DELAY1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deletePriority2.txt
deletePriority2 = '''model foo()
  E1: at DELAY1 after (Y1 > 3), priority=PRIORITY1: Z1=0, Q1=0;
  e2: at delay2 after (y2 > 3), priority=priority2: z2=0, q2=0;
end

model bar()
  A: foo();
  delete A.PRIORITY1;
end
'''

# Original source: <antimony-root>/src/test/test-data/global_units_rt.txt
global_units_rt = '''//Created by libAntimony v2.5.2
// Unit definitions:
unit length = metre;
unit area = metre^2;
unit volume = metre^3;
unit substance = mole;
unit extent = dimensionless;
unit time_unit = 6e1 second;
'''

# Original source: <antimony-root>/src/test/test-data/species_rt.txt
species_rt = '''//Created by libAntimony v2.5
// Compartments and Species:
compartment y;
species x in y;

// Species initializations:
x = ;

// Compartment initializations:
y = ;

//Other declarations:
const y;
'''

# Original source: <antimony-root>/src/test/test-data/externalParameter2_rt.txt
externalParameter2_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;
x = ;

// Other declarations:
const a, x;

// Uncertainty parameters:
a.externalParameter = x
a.externalParameter is "http://my.url/"'''

# Original source: <antimony-root>/src/test/test-data/externalParameter1_rt.txt
externalParameter1_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;

// Other declarations:
const a;

// Uncertainty parameters:
a.externalParameter = {-20, -15}
a.externalParameter is "http://my.url/"
'''

# Original source: <antimony-root>/src/test/test-data/externalParameter3_rt.txt
externalParameter3_rt = '''// Created by libAntimony v2.12.0
// Variable initializations:
a = ;
x = ;

// Other declarations:
const a, x;

// Uncertainty parameters:
a.externalParameter = -x
a.externalParameter is "http://my.url/"'''

# Original source: <antimony-root>/src/test/test-data/initialAmount_rt.txt
initialAmount_rt = '''//Created by libAntimony v2.5
// Compartments and Species:
compartment C;
species x in C;

// Species initializations:
x = 3/ C;

// Compartment initializations:
C = ;

//Other declarations:
const C;
'''

# Original source: <antimony-root>/src/test/test-data/reaction_rt.txt
reaction_rt = '''//Created by libAntimony v2.5
// Compartments and Species:
species a;

// Reactions:
J0: a -> ; k1;

// Species initializations:
a = ;

// Variable initializations:
k1 = ;

//Other declarations:
const k1;
'''

# Original source: <antimony-root>/src/test/test-data/two_sided_flux_complete.txt
two_sided_flux_complete = '''J0: s1->;
J1: s2->;
J2: s3->;
J3: ->s1;
J4: ->s2;
J5: ->s3;
J6: s1->s2;
J7: s2->s3;

-10 < J0 < 10
0 <= J1 <= 25
-30 < J2 <= -10
-40 <= J3 < 100

50 > J4 > 0
20 >= J5 >= -55
100 > J6 >= 77
120 >= J7 > 110
'''

# Original source: <antimony-root>/src/test/test-data/hierarchy_rt.txt
hierarchy_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  x = 3;

  //Other declarations:
  const x;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
end
'''

# Original source: <antimony-root>/src/test/test-data/port_rt.txt
port_rt = '''//Created by libAntimony v2.5
model foo(x)

  // Variable initializations:
  x = 3;

  //Other declarations:
  const x;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo(X);
end
'''

# Original source: <antimony-root>/src/test/test-data/defaultSubCompartment_rt.txt
defaultSubCompartment_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species x;

  // Species initializations:
  x = ;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
end
'''

# Original source: <antimony-root>/src/test/test-data/formula_objective_rt.txt
formula_objective_rt = '''//Created by libAntimony v2.7.0
// Compartments and Species:
species s1;

// Reactions:
J0: s1 -> ; ;

// The objective function (for FBC analysis):
_objective0: maximize 3*J0 + 2*J0;

// Species initializations:
s1 = ;
'''

# Original source: <antimony-root>/src/test/test-data/replaceSpeciesDefaultCompartment_rt.txt
replaceSpeciesDefaultCompartment_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S1;

  // Species initializations:
  S1 = ;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.S1 is S2;
end
'''

# Original source: <antimony-root>/src/test/test-data/formula_objective2_rt.txt
formula_objective2_rt = '''//Created by libAntimony v2.7.0
// Compartments and Species:
species s1;

// Reactions:
J0: s1 -> ; ;

// The objective function (for FBC analysis):
_objective0: maximize 3*J0 + 2*J0 + -4*J0 + -8*J0 + -2.2*J0 + 0.1*J0;

// Species initializations:
s1 = ;
'''

# Original source: <antimony-root>/src/test/test-data/deleteAssignmentRuleDirect_rt.txt
deleteAssignmentRuleDirect_rt = '''//Created by libAntimony v2.5
model foo()

  // Assignment Rules:
  P1 := 3;

  //Other declarations:
  var P1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.P1 is x;

  // Assignment Rules:
  x := ;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceAssignmentRule_rt.txt
replaceAssignmentRule_rt = '''//Created by libAntimony v2.5
model foo()

  // Assignment Rules:
  x := 4.8;

  //Other declarations:
  var x;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.x is y;

  // Assignment Rules:
  y := 2.2;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteAssignmentRuleIndirect_rt.txt
deleteAssignmentRuleIndirect_rt = '''//Created by libAntimony v2.5
model foo()

  // Assignment Rules:
  P1 := 3;

  //Other declarations:
  var P1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.P1;
end
'''

# Original source: <antimony-root>/src/test/test-data/model2.txt
model2 = '''import "/home/lpsmith/antimony/testmodels/model1.txt"
import "/home/lpsmith/antimony/testmodels/SBMLModels/oscli.xml"

model foo2()
  q: foo();
  a + b -> c; sin(24);
  e + d -> f; xor(24, 25);
  r: oscli();
  r.X1 = 5;
  //model quib;
end

A:foo2();
B:bar();
'''

# Original source: <antimony-root>/src/test/test-data/deletion_rt.txt
deletion_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  x = 3;

  //Other declarations:
  const x;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.x;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceParameter_rt.txt
replaceParameter_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  x = 4.8;

  //Other declarations:
  const x;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.x is y;

  // Variable initializations:
  y = 2.2;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteInitialAssignmentDirect_rt.txt
deleteInitialAssignmentDirect_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  P1 = 3^2;

  //Other declarations:
  const P1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.P1 is x;

  // Variable initializations:
  x = ;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteInitialAssignmentIndirect_rt.txt
deleteInitialAssignmentIndirect_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  P1 = 2 / 3;

  //Other declarations:
  const P1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.P1;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceInitialAssignment_rt.txt
replaceInitialAssignment_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  x = 4 / 8;

  //Other declarations:
  const x;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.x is y;

  // Variable initializations:
  y = 2 / 2;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpeciesInDefaultCompartment_rt.txt
deleteSpeciesInDefaultCompartment_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S1;

  // Species initializations:
  S1 = ;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/reactionIn_rt.txt
reactionIn_rt = '''//Created by libAntimony v2.5
// Compartments and Species:
compartment C;
species a in C;

// Reactions:
J0 in C:  -> a; k1;

// Species initializations:
a = ;

// Compartment initializations:
C = ;

// Variable initializations:
k1 = ;

//Other declarations:
const C, k1;
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpeciesPortDefaultCompartment_rt.txt
deleteSpeciesPortDefaultCompartment_rt = '''//Created by libAntimony v2.5
model foo(S1)

  // Compartments and Species:
  species S1;

  // Species initializations:
  S1 = ;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionOnly2_rt.txt
replaceReactionOnly2_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species x;

  // Reactions:
  J0:  -> x; ;

  // Species initializations:
  x = ;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.x is A__x;
  A.J0 is J1;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionOnly_rt.txt
replaceReactionOnly_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species x;

  // Reactions:
  J0: x -> ; ;

  // Species initializations:
  x = ;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.x is A__x;
  A.J0 is J1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteInitialAssignmentOfAnother_rt.txt
deleteInitialAssignmentOfAnother_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  P1 = 3 * X;
  X = ;

  //Other declarations:
  const P1, X;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.X;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteRateRuleDirect_rt.txt
deleteRateRuleDirect_rt = '''//Created by libAntimony v2.5
model foo()

  // Rate Rules:
  P1' = 3;

  // Variable initializations:
  P1 = ;

  //Other declarations:
  var P1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.P1 is x;

  // Rate Rules:
  x' = ;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceRateRule_rt.txt
replaceRateRule_rt = '''//Created by libAntimony v2.5
model foo()

  // Rate Rules:
  x' = 4.8;

  // Variable initializations:
  x = ;

  //Other declarations:
  var x;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.x is y;

  // Rate Rules:
  y' = 2.2;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteRateRuleIndirect_rt.txt
deleteRateRuleIndirect_rt = '''//Created by libAntimony v2.5
model foo()

  // Rate Rules:
  P1' = 3;

  // Variable initializations:
  P1 = ;

  //Other declarations:
  var P1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.P1;
end
'''

# Original source: <antimony-root>/src/test/test-data/numeric_distributions_rev.txt
numeric_distributions_rev = '''//Created by libAntimony v2.10.0
// Variable initializations:
a = normal(1, 2);
b = normal(1, 2, 3, 4);
c = uniform(1, 2);
d = exponential(1);
e = exponential(1, 2, 3);
f = gamma(1, 2);
g = gamma(1, 2, 3, 4);
h = poisson(1);
i = poisson(1, 2, 3);

// Other declarations:
const a, b, c, d, e, f, g, h, i;
'''

# Original source: <antimony-root>/src/test/test-data/defaultSubSubCompartment_rt.txt
defaultSubSubCompartment_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species x;

  // Species initializations:
  x = ;
end

model bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
end

model *baz()

  // Sub-modules, and any changes to those submodules:
  A: bar();
end
'''

# Original source: <antimony-root>/src/test/test-data/submodelInteraction_rt.txt
submodelInteraction_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S2, x;

  // Reactions:
  J0: x -> ; ;

  // Interactions:
  _J0: S2 -o J0; ;

  // Species initializations:
  S2 = ;
  x = ;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
end
'''

# Original source: <antimony-root>/src/test/test-data/subport_rt.txt
subport_rt = '''//Created by libAntimony v2.5
model foo(x0)

  // Variable initializations:
  x0 = 3;

  //Other declarations:
  const x0;
end

model bar(x1)

  // Sub-modules, and any changes to those submodules:
  A: foo(x1);
end

model *baz(x2)

  // Sub-modules, and any changes to those submodules:
  A: bar(x2);
end
'''

# Original source: <antimony-root>/src/test/test-data/SBO_submodel_shadowed_rt.txt
SBO_submodel_shadowed_rt = '''// Created by libAntimony v2.12.0
model foo()

  // Variable initializations:
  sboTerm = 1;

  // Other declarations:
  const sboTerm;
end

foo.sboTerm = 83


// Sub-modules, and any changes to those submodules:
A: foo();
A.sboTerm is b;

// Variable initializations:
b = 3;

// SBO terms:
A.SBOTerm = 27

'''

# Original source: <antimony-root>/src/test/test-data/subport2_rt.txt
subport2_rt = '''//Created by libAntimony v2.5
model foo(x0)

  // Variable initializations:
  x0 = 3;

  //Other declarations:
  const x0;
end

model bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
end

model *baz()

  // Sub-modules, and any changes to those submodules:
  A: bar();
  A.A.x0 is x1;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionWithKineticLawRxnRef_rt.txt
replaceReactionWithKineticLawRxnRef_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S1;

  // Reactions:
  J0: S1 -> ; J1;
  J1:  -> S1; ;

  // Species initializations:
  S1 = ;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.S1 is A__S1;
  A.J1 is A__J1;
  A.J0 is Jtop;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceCompartment_rt.txt
replaceCompartment_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  compartment x;

  // Compartment initializations:
  x = 4.8;

  //Other declarations:
  const x;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.x is y;

  // Compartment initializations:
  y = 2.2;
end
'''

# Original source: <antimony-root>/src/test/test-data/fixname_test.txt
fixname_test = '''// Created by libAntimony v2.10.0
model foo(ext_)

  // Compartments and Species:
  compartment ext_;

  // Rate Rules:
  ext_' = 6;

  // Compartment initializations:
  ext_ = 5 + 2;

  // Other declarations:
  var ext_;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo(e1);
end

bar is "bar"'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment3_rt.txt
deleteEventAssignment3_rt = '''//Created by libAntimony v2.5
model foo()

  // Events:
  E1: at Y1 > 3: Z1 = 0;

  // Variable initializations:
  Y1 = ;
  Z1 = ;

  //Other declarations:
  var Z1;
  const Y1;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.E1, A.Z1;
end
'''

# Original source: <antimony-root>/src/test/test-data/numeric_distributions.txt
numeric_distributions = '''//Created by libAntimony v2.10.0
// Variable initializations:
a = normal(1, 2);
b = truncatedNormal(1, 2, 3, 4);
c = uniform(1, 2);
d = exponential(1);
e = truncatedExponential(1, 2, 3);
f = gamma(1, 2);
g = truncatedGamma(1, 2, 3, 4);
h = poisson(1);
i = truncatedPoisson(1, 2, 3);

// Other declarations:
const a, b, c, d, e, f, g, h, i;
'''

# Original source: <antimony-root>/src/test/test-data/deleteRateRuleOfAnother_rt.txt
deleteRateRuleOfAnother_rt = '''//Created by libAntimony v2.5
model foo()

  // Rate Rules:
  P1' = X;

  // Variable initializations:
  P1 = ;
  X = ;

  //Other declarations:
  var P1;
  const X;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  // Rate Rules:
  A.P1' = ;

  //Deleted elements from submodels:
  delete A.X;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment4_rt.txt
deleteEventAssignment4_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  Y1 = ;
  Q1 = ;
  Z1 = ;

  // Events:
  E1: at Y1 > 3: Z1 = 0, Q1 = 0;

  //Other declarations:
  var Q1, Z1;
  const Y1;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.Q1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment_rt.txt
deleteEventAssignment_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  Y1 = ;
  Q1 = ;
  Z1 = ;

  // Events:
  E1: at Y1 > 3: Z1 = 0, Q1 = 0;

  //Other declarations:
  var Q1, Z1;
  const Y1;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.Z1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteAssignmentRuleOfAnother_rt.txt
deleteAssignmentRuleOfAnother_rt = '''//Created by libAntimony v2.5
model foo()

  // Assignment Rules:
  P1 := X;

  // Variable initializations:
  X = ;

  //Other declarations:
  var P1;
  const X;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  // Assignment Rules:
  A.P1 := ;

  //Deleted elements from submodels:
  delete A.X;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceSpecies_rt.txt
replaceSpecies_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  compartment C1;
  species S1 in C1;

  // Species initializations:
  S1 = ;

  // Compartment initializations:
  C1 = ;

  //Other declarations:
  const C1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.C1 is A__C1;
  A.S1 is S2;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpeciesInDefaultCompartment2_rt.txt
deleteSpeciesInDefaultCompartment2_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S1;

  // Species initializations:
  S1 = ;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  // Compartments and Species:
  species S2;

  // Species initializations:
  S2 = ;

  //Deleted elements from submodels:
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment5_rt.txt
deleteEventAssignment5_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  Y1 = ;
  Q1 = ;
  q = ;
  Z1 = ;
  z = ;

  // Events:
  E1: at Y1 > 3: Z1 = z, Q1 = q;

  //Other declarations:
  var Q1, Z1;
  const Y1, q, z;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.z;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteModifier_rt.txt
deleteModifier_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S2, S1;

  // Reactions:
  J1: S1 -> ; ;

  // Interactions:
  _J0: S2 -o J1; ;

  // Species initializations:
  S2 = ;
  S1 = ;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.S2, A._J0;
end
'''

# Original source: <antimony-root>/src/test/test-data/fluxes_and_objectives_rt.txt
fluxes_and_objectives_rt = '''//Created by libAntimony v2.7.0
// Compartments and Species:
species s1, s2, s3;

// Reactions:
J0: s1 -> ; ;
J1: s2 -> ; ;
J2: s3 -> ; ;
J3:  -> s1; ;

// The objective function (for FBC analysis):
Obj: minimize J0 + -1*J1 + -2*J2 + -3.3*J3;

// Constraints:
-10 < J0 < -3
-5 > J1 > -100
-100 <= J2 <= -10
-100 >= J3 >= -2.2

// Species initializations:
s1 = ;
s2 = ;
s3 = ;
'''

# Original source: <antimony-root>/src/test/test-data/deletePriority_rt.txt
deletePriority_rt = '''//Created by libAntimony v2.5
model foo()

  // Events:
  E1: at Y1 > 3, priority = PRIORITY1: Z1 = 0;

  // Variable initializations:
  Y1 = ;
  PRIORITY1 = ;
  Z1 = ;

  //Other declarations:
  var Z1;
  const Y1, PRIORITY1;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.PRIORITY1;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionWithKineticLaw_rt.txt
replaceReactionWithKineticLaw_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S1;

  // Reactions:
  J0: S1 -> ; x;

  // Species initializations:
  S1 = ;

  // Variable initializations:
  x = ;

  //Other declarations:
  const x;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.S1 is A__S1;
  A.x is A__x;
  A.J0 is J1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpecies_rt.txt
deleteSpecies_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  compartment C1;
  species S1 in C1;

  // Species initializations:
  S1 = ;

  // Compartment initializations:
  C1 = ;

  //Other declarations:
  const C1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteSpeciesPort_rt.txt
deleteSpeciesPort_rt = '''//Created by libAntimony v2.5
model foo(S1)

  // Compartments and Species:
  compartment C1;
  species S1 in C1;

  // Species initializations:
  S1 = ;

  // Compartment initializations:
  C1 = ;

  //Other declarations:
  const C1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteDelay_rt.txt
deleteDelay_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  Y1 = ;
  DELAY1 = ;
  Q1 = ;
  Z1 = ;

  // Events:
  E1: at DELAY1 after Y1 > 3: Z1 = 0, Q1 = 0;

  //Other declarations:
  var Q1, Z1;
  const Y1, DELAY1;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.DELAY1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteKineticLaw_rt.txt
deleteKineticLaw_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S1;

  // Reactions:
  J1: S1 -> ; K1;

  // Species initializations:
  S1 = ;

  // Variable initializations:
  K1 = ;

  //Other declarations:
  const K1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.K1;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceInteraction_rt.txt
replaceInteraction_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S2, x;

  // Reactions:
  J0: x -> ; ;

  // Interactions:
  _J0: S2 -o J0; ;

  // Species initializations:
  S2 = ;
  x = ;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.S2 is A__S2;
  A.x is A__x;
  A.J0 is J1;

  // Interactions:
  _J0: A__S2 -o J1; ;
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionWithCompartments1_rt.txt
replaceReactionWithCompartments1_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  compartment C2;
  species x in C2;

  // Reactions:
  J0: x -> ; ;

  // Species initializations:
  x = ;

  // Compartment initializations:
  C2 = ;

  //Other declarations:
  const C2;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.C2 is A__C2;
  A.x is A__x;
  A.J0 is J1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteProduct_rt.txt
deleteProduct_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S1, S2;

  // Reactions:
  J1: S1 -> S2; K1;

  // Species initializations:
  S1 = ;
  S2 = ;

  // Variable initializations:
  K1 = ;

  //Other declarations:
  const K1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.S2;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteReactant_rt.txt
deleteReactant_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S1, S2;

  // Reactions:
  J1: S1 -> S2; K1;

  // Species initializations:
  S1 = ;
  S2 = ;

  // Variable initializations:
  K1 = ;

  //Other declarations:
  const K1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.S1;
end
'''

# Original source: <antimony-root>/src/test/test-data/numeric_distributions_extended.txt
numeric_distributions_extended = '''//Created by libAntimony v2.10.0
// Variable initializations:
a = bernoulli(1);
b = binomial(1, 2);
c = cauchy(1, 2);
d = chisquare(1);
e = laplace(1, 2);
f = lognormal(1, 2);
g = rayleigh(1);
h = binomial(1, 2, 3, 4);
i = cauchy(1, 2, 3, 4);
j = chisquare(1, 2, 3);
k = laplace(1, 2, 3, 4);
l = lognormal(1, 2, 3, 4);
m = rayleigh(1, 2, 3);

// Other declarations:
const a, b, c, d, e, f, g, h, i, j, k, l, m;
'''

# Original source: <antimony-root>/src/test/test-data/deleteModifierKineticLaw_rt.txt
deleteModifierKineticLaw_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  species S2, S1;

  // Reactions:
  J1: S1 -> ; S2 * K1;

  // Species initializations:
  S2 = ;
  S1 = ;

  // Variable initializations:
  K1 = ;

  //Other declarations:
  const K1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.S2;
end
'''

# Original source: <antimony-root>/src/test/test-data/subsubport_rt.txt
subsubport_rt = '''//Created by libAntimony v2.5
model foo(x0)

  // Variable initializations:
  x0 = 3;

  //Other declarations:
  const x0;
end

model bar()

  // Sub-modules, and any changes to those submodules:
  A1: foo();
end

model baz()

  // Sub-modules, and any changes to those submodules:
  A2: bar();
end

model *biff()

  // Sub-modules, and any changes to those submodules:
  A3: baz();
  A3.A2.A1.x0 is x1;
end
'''

# Original source: <antimony-root>/src/test/test-data/defaultOrNotCompartment_rt.txt
defaultOrNotCompartment_rt = '''//Created by libAntimony v2.5
model bar()

  // Compartments and Species:
  compartment C;
  species y in C;

  // Species initializations:
  y = ;

  // Compartment initializations:
  C = ;

  //Other declarations:
  const C;
end

model foo()

  // Compartments and Species:
  species x;

  // Species initializations:
  x = ;
end

model *baz()

  // Sub-modules, and any changes to those submodules:
  A: bar();
  B: foo();
end
'''

# Original source: <antimony-root>/src/test/test-data/replaceReactionWithCompartments2_rt.txt
replaceReactionWithCompartments2_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  compartment C1, C2;
  species x in C2;

  // Reactions:
  J0 in C1: x -> ; ;

  // Species initializations:
  x = ;

  // Compartment initializations:
  C1 = ;
  C2 = ;

  //Other declarations:
  const C1, C2;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.C1 is A__C1;
  A.C2 is A__C2;
  A.x is A__x;
  A.J0 is J1;
end
'''

# Original source: <antimony-root>/src/test/test-data/test45.txt
test45 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Rate Rules:
  t1' = time/t1 + 3;

  // Variable initializations:
  t1 = 1;

  // Other declarations:
  var t1;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), timeconv = timeconv;
  sub1.t1 * paramconv is t1;

  // Variable initializations:
  timeconv = 60;
  paramconv = 0.01;

  // Other declarations:
  const timeconv, paramconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/deleteReaction_rt.txt
deleteReaction_rt = '''//Created by libAntimony v2.5
model foo()

  // Compartments and Species:
  compartment C1;
  species S1 in C1;

  // Reactions:
  J1: S1 -> ; K1;

  // Species initializations:
  S1 = ;

  // Compartment initializations:
  C1 = ;

  // Variable initializations:
  K1 = ;

  //Other declarations:
  const C1, K1;
end

model *bar1()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.J1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteTrigger_rt.txt
deleteTrigger_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  // Have to put E1 first here because otherwise the order of variables
  //  gets changed in the roundtripped version.
  E1 = ;
  Y1 = ;
  Q1 = ;
  Z1 = ;

  // Events:
  E1: at Y1 > 3: Z1 = 0, Q1 = 0;

  //Other declarations:
  var Q1, Z1;
  const Y1;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.E1, A.Y1;
end
'''

# Original source: <antimony-root>/src/test/test-data/test24.txt
test24 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Reactions:
  J0:  -> s1; 10;

  // Species initializations:
  s1 = 1/C;

  // Compartment initializations:
  C = 1;

  // Other declarations:
  const C;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), extentconv = extentconv;

  // Variable initializations:
  extentconv = 1000;

  // Other declarations:
  const extentconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/test39.txt
test39 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Reactions:
  J0:  -> s1; J0_p1*s1;

  // Species initializations:
  s1 = 0.001/C;

  // Compartment initializations:
  C = 1;

  // Variable initializations:
  p1 = 100;
  J0_p1 = 10;

  // Other declarations:
  const C, p1;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1();
  sub1.p1 is p1;
  sub1.J0_p1 is p1;

  // Variable initializations:
  p1 = 100;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/test54.txt
test54 = '''// Created by libAntimony v2.12.0

// Warnings from automatic translation:
//    Unable to process deletion from submodel B in model baz.  Deletions of Deletion elements have not been added as a concept in Antimony.

model foo()

  // Variable initializations:
  x = 3;

  // Other declarations:
  const x;
end

foo is "foo"

model bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  // Deleted elements from submodels:
  delete A.x;
end

bar is "bar"

model *baz()

  // Sub-modules, and any changes to those submodules:
  B: bar();
end
'''

# Original source: <antimony-root>/src/test/test-data/test27.txt
test27 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Assignment Rules:
  t1 := time + 3;

  // Other declarations:
  var t1;
end

model moddef2()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), timeconv = timeconv;

  // Variable initializations:
  timeconv = 60;

  // Other declarations:
  const timeconv;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef2(), timeconv = timeconv;

  // Variable initializations:
  timeconv = 60;

  // Other declarations:
  const timeconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/test46.txt
test46 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Assignment Rules:
  p80 := J0 + 6;

  // Reactions:
  J0:  -> s1; 10;

  // Species initializations:
  s1 = 1/C;

  // Compartment initializations:
  C = 1;

  // Other declarations:
  var p80;
  const C;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), timeconv = timeconv;

  // Variable initializations:
  timeconv = 60;

  // Other declarations:
  const timeconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/deleteEventAssignment2_rt.txt
deleteEventAssignment2_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  Y1 = ;
  DELAY1 = ;
  PRIORITY1 = ;
  Q1 = ;
  Z1 = ;
  y2 = ;
  delay2 = ;
  priority2 = ;
  q2 = ;
  z2 = ;

  // Events:
  E1: at DELAY1 after Y1 > 3, priority = PRIORITY1: Z1 = 0, Q1 = 0;
  e2: at delay2 after y2 > 3, priority = priority2: z2 = 0, q2 = 0;

  //Other declarations:
  var Q1, Z1, q2, z2;
  const Y1, DELAY1, PRIORITY1, y2, delay2, priority2;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.Z1;
end
'''

# Original source: <antimony-root>/src/test/test-data/deleteDelay2_rt.txt
deleteDelay2_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  Y1 = ;
  DELAY1 = ;
  PRIORITY1 = ;
  Q1 = ;
  Z1 = ;
  y2 = ;
  delay2 = ;
  priority2 = ;
  q2 = ;
  z2 = ;

  // Events:
  E1: at DELAY1 after Y1 > 3, priority = PRIORITY1: Z1 = 0, Q1 = 0;
  e2: at delay2 after y2 > 3, priority = priority2: z2 = 0, q2 = 0;

  //Other declarations:
  var Q1, Z1, q2, z2;
  const Y1, DELAY1, PRIORITY1, y2, delay2, priority2;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.DELAY1;
end
'''

# Original source: <antimony-root>/src/test/test-data/test44.txt
test44 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Assignment Rules:
  p80 := J0 + 6;

  // Reactions:
  J0:  -> s1; 10;

  // Species initializations:
  s1 = 1/C;

  // Compartment initializations:
  C = 1;

  // Other declarations:
  var p80;
  const C;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), extentconv = extentconv;

  // Variable initializations:
  extentconv = 1000;

  // Other declarations:
  const extentconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/deletePriority2_rt.txt
deletePriority2_rt = '''//Created by libAntimony v2.5
model foo()

  // Variable initializations:
  Y1 = ;
  DELAY1 = ;
  PRIORITY1 = ;
  Q1 = ;
  Z1 = ;
  y2 = ;
  delay2 = ;
  priority2 = ;
  q2 = ;
  z2 = ;

  // Events:
  E1: at DELAY1 after Y1 > 3, priority = PRIORITY1: Z1 = 0, Q1 = 0;
  e2: at delay2 after y2 > 3, priority = priority2: z2 = 0, q2 = 0;

  //Other declarations:
  var Q1, Z1, q2, z2;
  const Y1, DELAY1, PRIORITY1, y2, delay2, priority2;
end

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();

  //Deleted elements from submodels:
  delete A.PRIORITY1;
end
'''

# Original source: <antimony-root>/src/test/test-data/test58.txt
test58 = '''// Created by libAntimony v2.12.0

// Warnings from automatic translation:
//    Cannot replace stoichiometries in Antimony:  all replacedElements and replacedBy children of z in reaction J2 will be ignored.

model foo()

  // Compartments and Species:
  species x;

  // Reactions:
  J0: x + x -> ; ;

  // Species initializations:
  x = ;
end

foo is "foo"

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.J0 is J1;

  // Compartments and Species:
  species y, z;

  // Reactions:
  J2:  -> z; ;

  // Species initializations:
  y = ;
  z = ;
end
'''

# Original source: <antimony-root>/src/test/test-data/test59.txt
test59 = '''// Created by libAntimony v2.12.0

// Warnings from automatic translation:
//    Cannot replace stoichiometries in Antimony:  all replacedElements and replacedBy children of z in reaction J2 will be ignored.

model foo()

  // Compartments and Species:
  species x;

  // Reactions:
  J0: x -> ; ;

  // Species initializations:
  x = ;
end

foo is "foo"

model *bar()

  // Sub-modules, and any changes to those submodules:
  A: foo();
  A.J0 is J1;

  // Compartments and Species:
  species y, z;

  // Reactions:
  J2:  -> z + z; ;

  // Species initializations:
  y = ;
  z = ;
end
'''

# Original source: <antimony-root>/src/test/test-data/test48.txt
test48 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Assignment Rules:
  p80 := J0 + 6;

  // Reactions:
  J0:  -> s1; ;

  // Species initializations:
  s1 = 1/C;

  // Compartment initializations:
  C = 1;

  // Other declarations:
  var p80;
  const C;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), timeconv = timeconv, extentconv = extentconv;

  // Variable initializations:
  timeconv = 60;
  extentconv = 1000;

  // Other declarations:
  const timeconv, extentconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/test47.txt
test47 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Assignment Rules:
  p80 := J0 + 6;

  // Reactions:
  J0:  -> s1; 10;

  // Species initializations:
  s1 = 1/C;

  // Compartment initializations:
  C = 1;

  // Other declarations:
  var p80;
  const C;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), timeconv = timeconv, extentconv = extentconv;

  // Variable initializations:
  timeconv = 60;
  extentconv = 1000;

  // Other declarations:
  const timeconv, extentconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/test25.txt
test25 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Reactions:
  J0:  -> s1; s1*time/delay(s1, 2e4);

  // Species initializations:
  s1 = 1/C;

  // Compartment initializations:
  C = 1;

  // Other declarations:
  const C;
end

model moddef2()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1();
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef2(), extentconv = extentconv;

  // Variable initializations:
  extentconv = 1000;

  // Other declarations:
  const extentconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/exchangetest.txt
exchangetest = '''// Created by libAntimony v2.12.0
model *testmod()

  // Compartments and Species:
  species A__S1;

  // Assignment Rules:
  Q := X/cf - 3;

  // Rate Rules:
  X' = (0.2/timeconv)*cf;

  // Reactions:
  A___J0: A__S1 -> ; (A__k1*A__S1/timeconv)*extentconv;

  // Events:
  A___E0: at (X/cf) > 3, priority = Q: A__y = 4;
  A___E1: at (X/cf) > 3, priority = R: A__y = 5;

  // Species initializations:
  A__S1 = ;

  // Variable initializations:
  X = ;
  cf = 100;
  A__y = ;
  R = 20;
  timeconv = 60;
  extentconv = 10;
  U1 = ;
  U2 = ;
  A__k1 = ;

  // Other declarations:
  var X, Q, A__y, U1, U2;
  const cf, R, timeconv, extentconv, A__k1;
end
'''

# Original source: <antimony-root>/src/test/test-data/comp.txt
comp = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  species s1 in C;

  // Assignment Rules:
  t3 := delay(t1,3);

  // Rate Rules:
  t1' = time/ t1+3;

  // Reactions:
  J0:  -> s1; (t3*time)/(s1*delay(t5,0.2));

  // Events:
  _E0: at 1/time after time>3: t5 = time;

  // Species initializations:
  s1 = 0.001/ C;

  // Compartment initializations:
  C = 1;

  // Variable initializations:
  t1 = 1;
  t5 = 1;
  t2 = time+3;
  t4 = 1;

  //Other declarations:
  var t5, t1, t2, t3, t4;
  const C;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), timeconv = timeconv;
  sub1.C is C;
  sub1.s1 is s1;
  sub1.t1 is t1;
  sub1.t2 is t2;
  sub1.t3 is t3;
  sub1.t4 is t4;
  sub1.t5 is t5;

  // Variable initializations:
  timeconv = 60;

  //Other declarations:
  const timeconv;
end
'''

# Original source: <antimony-root>/src/test/test-data/test22.txt
test22 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Assignment Rules:
  t3 := delay(t1, 3);

  // Rate Rules:
  t1' = time/t1 + 3;

  // Reactions:
  J0:  -> s1; t3*time/(s1*delay(t5, 2e-1));

  // Events:
  _E0: at 1/time after time > 3: t5 = time;

  // Constraints:
  constraint _con0: time < (t4*t5)

  // Species initializations:
  s1 = 0.001/C;

  // Compartment initializations:
  C = 1;

  // Variable initializations:
  t5 = 1;
  t4 = 1;
  t1 = 1;
  t2 = time + 3;

  // Other declarations:
  var t5, t4, t1, t2, t3;
  const C;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), timeconv = timeconv;
  sub1.C is C;
  sub1.s1 is s1;
  sub1.t1 is t1;
  sub1.t2 is t2;
  sub1.t3 is t3;
  sub1.t4 is t4;
  sub1.t5 is t5;

  // Variable initializations:
  timeconv = 60;

  // Other declarations:
  const timeconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/test23.txt
test23 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Assignment Rules:
  t3 := delay(t1, 3);

  // Rate Rules:
  t1' = time*t1 + 3;

  // Reactions:
  J0:  -> s1; s1*t3*time/delay(t5, 2e4);

  // Events:
  _E0: at 1/time after time > 3: t5 = time;

  // Constraints:
  constraint _con0: time < (t4*t5)

  // Species initializations:
  s1 = 1/C;

  // Compartment initializations:
  C = 1;

  // Variable initializations:
  t5 = 1;
  t4 = 1;
  t1 = 1;
  t2 = time + 3;

  // Other declarations:
  var t5, t4, t1, t2, t3;
  const C;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), timeconv = timeconv, extentconv = extentconv;
  sub1.t1 is t1;
  sub1.t2 is t2;
  sub1.t3 is t3;
  sub1.t4 is t4;
  sub1.t5 is t5;

  // Variable initializations:
  timeconv = 60;
  extentconv = 1000;

  // Other declarations:
  const timeconv, extentconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/test28.txt
test28 = '''// Created by libAntimony v2.12.0
model moddef1()

  // Compartments and Species:
  compartment C;
  substanceOnly species s1 in C;

  // Reactions:
  J0:  -> s1; s1*time/delay(s1, 2e4);

  // Species initializations:
  s1 = 1/C;

  // Compartment initializations:
  C = 1;

  // Other declarations:
  const C;
end

model moddef2()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef1(), timeconv = timeconv, extentconv = extentconv;

  // Variable initializations:
  timeconv = 60;
  extentconv = 10;

  // Other declarations:
  const timeconv, extentconv;
end

model moddef3()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef2(), timeconv = timeconv, extentconv = extentconv;

  // Variable initializations:
  timeconv = 60;
  extentconv = 10;

  // Other declarations:
  const timeconv, extentconv;
end

model *doc0()

  // Sub-modules, and any changes to those submodules:
  sub1: moddef3(), timeconv = timeconv, extentconv = extentconv;

  // Variable initializations:
  timeconv = 60;
  extentconv = 10;

  // Other declarations:
  const timeconv, extentconv;
end

doc0 is "doc0"
'''

# Original source: <antimony-root>/src/test/test-data/test61.txt
test61 = '''// Created by libAntimony v2.12.0

// Warnings from automatic translation:
//    Cannot replace stoichiometries in Antimony:  all replacedElements and replacedBy children of S1 in reaction R1 will be ignored.

model enzyme()

  // Compartments and Species:
  compartment c;
  substanceOnly species S1 in c;

  // Reactions:
  R1: S1 => ; S1/R1_k;

  // Species initializations:
  S1 = 1/c;
  S1 has mole_per_litre;

  // Compartment initializations:
  c = 1;
  c has litre;

  // Variable initializations:
  R1_k = 0.1;
  R1_k has second;

  // Other declarations:
  const c;

  // Unit definitions:
  unit extent = mole;
  unit time_unit = second;
  unit mole_per_litre = mole / litre;
end

enzyme is "enzyme"

model *aggregate()

  // Sub-modules, and any changes to those submodules:
  submod1: enzyme();

  // Compartments and Species:
  compartment c;
  substanceOnly species S in c, S1 in c;

  // Reactions:
  R1: S1 => S; S/R1_k;

  // Species initializations:
  S = 1/c;
  S has mole_per_litre;
  S1 = 1/c;
  S1 has mole_per_litre;

  // Compartment initializations:
  c = 1;
  c has litre;

  // Variable initializations:
  R1_k = 0.1;
  R1_k has second;

  // Other declarations:
  const c;

  // Unit definitions:
  unit extent = mole;
  unit time_unit = second;
  unit mole_per_litre = mole / litre;
end

aggregate is "aggregate"
'''

# Original source: <antimony-root>/src/test/test-data/replace_rules_and_constraints.txt
replace_rules_and_constraints = '''// Created by libAntimony v2.12.0

// Warnings from automatic translation:
//    Unable to create port rule__iBioSim7 in model CompModel because RateRule elements only exist as part of other Antimony elements, and do not function as their own separate entities which may be flagged as a port.
//    Unable to create port constraint__constraint0 in model CompModel because Constraint elements do not have IDs in SBML, and therefore cannot be made into ports in Antimony.
//    Unable to create port R1__C1 in model CompTest3_antimony_roundtrip because the object the port referenced is in a submodel, and these objects cannot be declared ports in Antimony.
//    Unable to create port R3__C1 in model CompTest3_antimony_roundtrip because the object the port referenced is in a submodel, and these objects cannot be declared ports in Antimony.
//    Unable to create port R1_kf0__C1 in model CompTest3_antimony_roundtrip because the object the port referenced is in a submodel, and these objects cannot be declared ports in Antimony.
//    Unable to create port S2__C1 in model CompTest3_antimony_roundtrip because the object the port referenced is in a submodel, and these objects cannot be declared ports in Antimony.

model CompModel(Cell, R1, R3, event0, R1_kf0, perSecond, S2, event1)

  // Compartments and Species:
  compartment Cell;
  species S1 in Cell, S2 in Cell;

  // Assignment Rules:
  V1 := S1 + S2;

  // Rate Rules:
  V2' = S1*S2;

  // Reactions:
  R1: S1 => S2; R1_kf0*S1;
  R3: S2 => S1; R3_kf0*S2;

  // Events:
  event0: at 10 after time >= 100, t0=false, persistent=false, fromTrigger=false: S1 = 10;
  event1: at 100 after true, t0=false, persistent=false, fromTrigger=false: S2 = 100;

  // Constraints:
  constraint _con0: 1 == 1

  // Species initializations:
  S1 = 0;
  S2 = 0;

  // Compartment initializations:
  Cell = 1;

  // Variable initializations:
  R3_kf0 = 1;
  R1_kf0 = 1;
  V2 = 0;
  x = ;
  R1_kf = 0.1;
  R3_kf = 0.1;
  R1_kr = 1;
  R3_kr = 1;
  kd = 0.0075;
  kmdiff_f = 1;
  kmdiff_r = 0.01;
  kecd = 0.005;
  kecdiff = 1;
  np = 10;
  ko = 0.05;

  // Other declarations:
  var V1, V2;
  const Cell, R3_kf0, R1_kf0, x, R1_kf, R3_kf, R1_kr, R3_kr, kd, kmdiff_f;
  const kmdiff_r, kecd, kecdiff, np, ko;

  // Unit definitions:
  unit perSecond = 1 / second;

  // Display Names:
  kd is "Degradation rate";
  kmdiff_f is "Forward membrane diffusion rate";
  kmdiff_r is "Reverse membrane diffusion rate";
  kecd is "Extracellular degradation rate";
  kecdiff is "Extracellular diffusion rate";
  np is "Stoichiometry of production";
  ko is "Open complex production rate";
end

CompModel is "CompModel"

model *CompTest3_antimony_roundtrip(Cell)

  // Sub-modules, and any changes to those submodules:
  C1: CompModel();
  C1.Cell is Cell;

  // Compartments and Species:
  species $S1 in Cell, S2 in Cell;

  // Rate Rules:
  C1.V2' = ;
  S1' = 1;

  // Constraints:
  constraint _con0: 2 == 2

  // Species initializations:
  S1 = 0;
  S2 = 0;

  // Variable initializations:
  topKf = 3;
  kr_f = 0.5;
  kr_r = 1;
  ka_f = 0.0033;
  ka_r = 1;
  kc_f = 0.05;
  kc_r = 1;
  ko_f = 0.033;
  ko_r = 1;
  kao_f = 1;
  kao_r = 1;
  kmdiff_f = 1;
  kmdiff_r = 0.01;
  kd = 0.0075;
  kecd = 0.005;
  nc = 2;
  nr = 30;
  ko = 0.05;
  kb = 0.0001;
  ng = 2;
  np = 10;
  ka = 0.25;
  kecdiff = 1;

  // Deleted elements from submodels:
  delete C1.perSecond, C1.event0, C1.event1;

  // Other declarations:
  const topKf, kr_f, kr_r, ka_f, ka_r, kc_f, kc_r, ko_f, ko_r, kao_f, kao_r;
  const kmdiff_f, kmdiff_r, kd, kecd, nc, nr, ko, kb, ng, np, ka, kecdiff;

  // Display Names:
  kr_f is "Forward repression binding rate";
  kr_r is "Reverse repression binding rate";
  ka_f is "Forward activation binding rate";
  ka_r is "Reverse activation binding rate";
  kc_f is "Forward complex formation rate";
  kc_r is "Reverse complex formation rate";
  ko_f is "Forward RNAP binding rate";
  ko_r is "Reverse RNAP binding rate";
  kao_f is "Forward activated RNAP binding rate";
  kao_r is "Reverse activated RNAP binding rate";
  kmdiff_f is "Forward membrane diffusion rate";
  kmdiff_r is "Reverse membrane diffusion rate";
  kd is "Degradation rate";
  kecd is "Extracellular degradation rate";
  nc is "Stoichiometry of binding";
  nr is "Initial RNAP count";
  ko is "Open complex production rate";
  kb is "Basal production rate";
  ng is "Initial promoter count";
  np is "Stoichiometry of production";
  ka is "Activated production rate";
  kecdiff is "Extracellular diffusion rate";
end

CompTest3_antimony_roundtrip is "CompTest"
'''

# Original source: <antimony-root>/src/test/test-data/CompTest.txt
CompTest = '''// Created by libAntimony v2.12.0

// Warnings from automatic translation:
//    Unable to create port constraint__constraint0 in model CompModel because Constraint elements do not have IDs in SBML, and therefore cannot be made into ports in Antimony.
//    Unable to create port functionDefinition__f in model CompModel because function defintions are global in Antimony, not local.
//    Unable to process deletion from submodel C1 in model CompTest.  Function definitions are global in Antimony, not local, and therefore cannot be deleted from submodels.
//    Unable to process deletion from submodel C1 in model CompTest, because Constraints do not have IDs in SBML.
//    Unable to create port reaction__R1__C1 in model CompTest because the object the port referenced is in a submodel, and these objects cannot be declared ports in Antimony.
//    Unable to create port reaction__R3__C1 in model CompTest because the object the port referenced is in a submodel, and these objects cannot be declared ports in Antimony.

function f(x)
  2*x;
end

function neighborQuantityLeft(a)
  0;
end

neighborQuantityLeft is "neighborQuantityLeft"

function neighborQuantityRight(a)
  0;
end

neighborQuantityRight is "neighborQuantityRight"

function neighborQuantityAbove(a)
  0;
end

neighborQuantityAbove is "neighborQuantityAbove"

function neighborQuantityBelow(a)
  0;
end

neighborQuantityBelow is "neighborQuantityBelow"

function getCompartmentLocationX(a)
  0;
end

getCompartmentLocationX is "getCompartmentLocationX"

function getCompartmentLocationY(a)
  0;
end

getCompartmentLocationY is "getCompartmentLocationY"


model CompModel(Cell, R1, R3, event0, event1, R3_kf0, R1_kf0, perSecond, S1, S2)

  // Compartments and Species:
  compartment Cell;
  species S1 in Cell, S2 in Cell;

  // Assignment Rules:
  V1 := S1 + S2;

  // Rate Rules:
  V2' = S1*S2;

  // Reactions:
  R1 in Cell: S1 => S2; R1_kf0*S1;
  R3 in Cell: S2 => S1; R3_kf0*S2;

  // Events:
  event0: at 10 after time >= 100, t0=false, persistent=false, fromTrigger=false: S1 = 10;
  event1: at 100 after true, t0=false, persistent=false, fromTrigger=false: S2 = 100;

  // Constraints:
  V1 != V2

  // Species initializations:
  S1 = 0;
  S2 = 0;

  // Compartment initializations:
  Cell = 1;

  // Variable initializations:
  V2 = 0;
  R1_kf = 0.1;
  R3_kf = 0.1;
  x = ;
  kr_f = 0.5;
  kr_r = 1;
  ka_f = 0.0033;
  ka_r = 1;
  kc_f = 0.05;
  kc_r = 1;
  ko_f = 0.033;
  ko_r = 1;
  kao_f = 1;
  kao_r = 1;
  kmdiff_f = 1;
  kmdiff_r = 0.01;
  kd = 0.0075;
  kecd = 0.005;
  nc = 2;
  nr = 30;
  ko = 0.05;
  kb = 0.0001;
  ng = 2;
  np = 10;
  ka = 0.25;
  kecdiff = 1;
  kf = 2;
  R1_kr = 1;
  R3_kr = 1;
  R1_kf0 = 1;
  R3_kf0 = 1;

  // Other declarations:
  var V1, V2;
  const second, Cell, R1_kf, R3_kf, x, kr_f, kr_r, ka_f, ka_r, kc_f, kc_r;
  const ko_f, ko_r, kao_f, kao_r, kmdiff_f, kmdiff_r, kd, kecd, nc, nr, ko;
  const kb, ng, np, ka, kecdiff, kf, R1_kr, R3_kr;

  // Unit definitions:
  unit perSecond = 1 / second;

  // Display Names:
  kr_f is "Forward repression binding rate";
  kr_r is "Reverse repression binding rate";
  ka_f is "Forward activation binding rate";
  ka_r is "Reverse activation binding rate";
  kc_f is "Forward complex formation rate";
  kc_r is "Reverse complex formation rate";
  ko_f is "Forward RNAP binding rate";
  ko_r is "Reverse RNAP binding rate";
  kao_f is "Forward activated RNAP binding rate";
  kao_r is "Reverse activated RNAP binding rate";
  kmdiff_f is "Forward membrane diffusion rate";
  kmdiff_r is "Reverse membrane diffusion rate";
  kd is "Degradation rate";
  kecd is "Extracellular degradation rate";
  nc is "Stoichiometry of binding";
  nr is "Initial RNAP count";
  ko is "Open complex production rate";
  kb is "Basal production rate";
  ng is "Initial promoter count";
  np is "Stoichiometry of production";
  ka is "Activated production rate";
  kecdiff is "Extracellular diffusion rate";
end

CompModel is "CompModel"

model *CompTest()

  // Sub-modules, and any changes to those submodules:
  C1: CompModel();
  C1.kf is kf;
  C1.R1_kf0 is kf;
  C1.Cell is Cell;
  C1.S2 is S1;
  C1.S1 is S2;
  C1.R3_kf0 is topKf;

  // Compartments and Species:
  substanceOnly species S2 in Cell, S1 in Cell;

  // Variable initializations:
  kf = 2;
  kr_f = 0.5;
  kr_r = 1;
  ka_f = 0.0033;
  ka_r = 1;
  kc_f = 0.05;
  kc_r = 1;
  ko_f = 0.033;
  ko_r = 1;
  kao_f = 1;
  kao_r = 1;
  kmdiff_f = 1;
  kmdiff_r = 0.01;
  kd = 0.0075;
  kecd = 0.005;
  nc = 2;
  nr = 30;
  ko = 0.05;
  kb = 0.0001;
  ng = 2;
  np = 10;
  ka = 0.25;
  kecdiff = 1;
  topKf = 3;

  // Deleted elements from submodels:
  delete C1.perSecond, C1.event0, C1.event1;

  // Other declarations:
  const topKf, kr_f, kr_r, ka_f, ka_r, kc_f, kc_r, ko_f, ko_r, kao_f, kao_r;
  const kmdiff_f, kmdiff_r, kd, kecd, nc, nr, ko, kb, ng, np, ka, kecdiff;

  // Display Names:
  kr_f is "Forward repression binding rate";
  kr_r is "Reverse repression binding rate";
  ka_f is "Forward activation binding rate";
  ka_r is "Reverse activation binding rate";
  kc_f is "Forward complex formation rate";
  kc_r is "Reverse complex formation rate";
  ko_f is "Forward RNAP binding rate";
  ko_r is "Reverse RNAP binding rate";
  kao_f is "Forward activated RNAP binding rate";
  kao_r is "Reverse activated RNAP binding rate";
  kmdiff_f is "Forward membrane diffusion rate";
  kmdiff_r is "Reverse membrane diffusion rate";
  kd is "Degradation rate";
  kecd is "Extracellular degradation rate";
  nc is "Stoichiometry of binding";
  nr is "Initial RNAP count";
  ko is "Open complex production rate";
  kb is "Basal production rate";
  ng is "Initial promoter count";
  np is "Stoichiometry of production";
  ka is "Activated production rate";
  kecdiff is "Extracellular diffusion rate";
end
'''

# Original source: <antimony-root>/src/test/test-data/QTPop.txt
QTPop = '''// Created by libAntimony v2.12.0
function get2DArrayElement(a, b, c)
  a;
end


model QuorumTrigger()

  // Compartments and Species:
  compartment default;
  species Env in default, LuxR in default, Complex in default, LuxI in default;
  species GFP in default, P1 in default, P5 in default;

  // Reactions:
  Production_P1 in default:  => 10LuxR; (P1*(kb*(ko_f/ko_r)*nr + ka*(kao_f/kao_r)*nr*(ka_f/ka_r*Env)^nc))/(1 + ko_f/ko_r*nr + kao_f/kao_r*nr*(ka_f/ka_r*Env)^nc);
  Complex_Complex in default: 2LuxR + 2LuxI -> Complex; kc_f*LuxR^nc*LuxI^nc - kc_r*Complex;
  Production_P5 in default:  => 10GFP + 10LuxI + 10LuxR; (P5*(kb*(ko_f/ko_r)*nr + ka*(kao_f/kao_r)*nr*(ka_f/ka_r*Complex)^nc))/(1 + ko_f/ko_r*nr + kao_f/kao_r*nr*(ka_f/ka_r*Complex)^nc);
  Degradation_GFP in default: GFP => ; kd*GFP;
  Degradation_LuxI in default: LuxI => ; kd*LuxI;
  Degradation_Complex in default: Complex => ; kd*Complex;
  Degradation_LuxR in default: LuxR => ; kd*LuxR;
  MembraneDiffusion_LuxI in default: LuxI -> ; kmdiff_f*LuxI - kmdiff_r;

  // Events:
  event0: at time >= 10000, t0=false, persistent=false, fromTrigger=false: Env = 100;

  // Species initializations:
  Env = 0;
  LuxR = 0;
  Complex = 0;
  LuxI = 0;
  GFP = 0;
  P1 = 2/default;
  P5 = 2/default;

  // Compartment initializations:
  default = 1;

  // Variable initializations:
  kr_f = 0.5;
  kr_r = 1;
  ka_f = 0.0033;
  ka_r = 1;
  kc_f = 0.05;
  kc_r = 1;
  ko_f = 0.033;
  ko_r = 1;
  kao_f = 1;
  kao_r = 1;
  kmdiff_f = 1;
  kmdiff_r = 0.01;
  kd = 0.0075;
  kecd = 0.005;
  nc = 2;
  nr = 30;
  ko = 0.05;
  kb = 0.0001;
  ng = 2;
  np = 10;
  ka = 0.25;
  kecdiff = 1;

  // Other declarations:
  const default, kr_f, kr_r, ka_f, ka_r, kc_f, kc_r, ko_f, ko_r, kao_f, kao_r;
  const kmdiff_f, kmdiff_r, kd, kecd, nc, nr, ko, kb, ng, np, ka, kecdiff;

  // Display Names:
  kr_f is "Forward repression binding rate";
  kr_r is "Reverse repression binding rate";
  ka_f is "Forward activation binding rate";
  ka_r is "Reverse activation binding rate";
  kc_f is "Forward complex formation rate";
  kc_r is "Reverse complex formation rate";
  ko_f is "Forward RNAP binding rate";
  ko_r is "Reverse RNAP binding rate";
  kao_f is "Forward activated RNAP binding rate";
  kao_r is "Reverse activated RNAP binding rate";
  kmdiff_f is "Forward membrane diffusion rate";
  kmdiff_r is "Reverse membrane diffusion rate";
  kd is "Degradation rate";
  kecd is "Extracellular degradation rate";
  nc is "Stoichiometry of binding";
  nr is "Initial RNAP count";
  ko is "Open complex production rate";
  kb is "Basal production rate";
  ng is "Initial promoter count";
  np is "Stoichiometry of production";
  ka is "Activated production rate";
  kecdiff is "Extracellular diffusion rate";
end

model *QTPop()

  // Sub-modules, and any changes to those submodules:
  GRID__QuorumTrigger: QuorumTrigger();

  // Compartments and Species:
  compartment default;
  species LuxI in default;

  // Reactions:
  Degradation_LuxI in default: LuxI => ; Degradation_LuxI_kecd*get2DArrayElement(LuxI, Degradation_LuxI_i, Degradation_LuxI_j);
  Diffusion_LuxI_Above in default: LuxI -> LuxI; Diffusion_LuxI_Above_kecdiff*get2DArrayElement(LuxI, Diffusion_LuxI_Above_i, Diffusion_LuxI_Above_j) - Diffusion_LuxI_Above_kecdiff*get2DArrayElement(LuxI, Diffusion_LuxI_Above_i - 1, Diffusion_LuxI_Above_j + 0);
  Diffusion_LuxI_Below in default: LuxI -> LuxI; Diffusion_LuxI_Below_kecdiff*get2DArrayElement(LuxI, Diffusion_LuxI_Below_i, Diffusion_LuxI_Below_j) - Diffusion_LuxI_Below_kecdiff*get2DArrayElement(LuxI, Diffusion_LuxI_Below_i + 1, Diffusion_LuxI_Below_j + 0);
  Diffusion_LuxI_Left in default: LuxI -> LuxI; Diffusion_LuxI_Left_kecdiff*get2DArrayElement(LuxI, Diffusion_LuxI_Left_i, Diffusion_LuxI_Left_j) - Diffusion_LuxI_Left_kecdiff*get2DArrayElement(LuxI, Diffusion_LuxI_Left_i + 0, Diffusion_LuxI_Left_j - 1);
  Diffusion_LuxI_Right in default: LuxI -> LuxI; Diffusion_LuxI_Right_kecdiff*get2DArrayElement(LuxI, Diffusion_LuxI_Right_i, Diffusion_LuxI_Right_j) - Diffusion_LuxI_Right_kecdiff*get2DArrayElement(LuxI, Diffusion_LuxI_Right_i + 0, Diffusion_LuxI_Right_j + 1);
  MembraneDiffusion_LuxI in default: LuxI -> LuxI; get2DArrayElement(kmdiff_f, MembraneDiffusion_LuxI_i, MembraneDiffusion_LuxI_j)*get2DArrayElement(LuxI, MembraneDiffusion_LuxI_i, MembraneDiffusion_LuxI_j) - get2DArrayElement(kmdiff_r, MembraneDiffusion_LuxI_i, MembraneDiffusion_LuxI_j)*get2DArrayElement(LuxI, MembraneDiffusion_LuxI_i, MembraneDiffusion_LuxI_j);

  // Species initializations:
  LuxI = 0;

  // Compartment initializations:
  default = 1;

  // Variable initializations:
  kr_f = 0.5;
  kr_r = 1;
  ka_f = 0.0033;
  ka_r = 1;
  kc_f = 0.05;
  kc_r = 1;
  ko_f = 0.033;
  ko_r = 1;
  kao_f = 1;
  kao_r = 1;
  kmdiff_f = 1;
  kmdiff_r = 0.01;
  kd = 0.0075;
  kecd = 0.005;
  nc = 2;
  nr = 30;
  ko = 0.05;
  kb = 0.0001;
  ng = 2;
  np = 10;
  ka = 0.25;
  kecdiff = 1;
  QuorumTrigger__locations = ;
  QuorumTrigger_size = 16;
  Degradation_LuxI_i = ;
  Degradation_LuxI_j = ;
  Degradation_LuxI_kecd = 0.005;
  Degradation_LuxI_kecd has u_1_second_n1;
  Diffusion_LuxI_Above_i = ;
  Diffusion_LuxI_Above_j = ;
  Diffusion_LuxI_Above_kecdiff = 1;
  Diffusion_LuxI_Above_kecdiff has u_1_second_n1;
  Diffusion_LuxI_Below_i = ;
  Diffusion_LuxI_Below_j = ;
  Diffusion_LuxI_Below_kecdiff = 1;
  Diffusion_LuxI_Below_kecdiff has u_1_second_n1;
  Diffusion_LuxI_Left_i = ;
  Diffusion_LuxI_Left_j = ;
  Diffusion_LuxI_Left_kecdiff = 1;
  Diffusion_LuxI_Left_kecdiff has u_1_second_n1;
  Diffusion_LuxI_Right_i = ;
  Diffusion_LuxI_Right_j = ;
  Diffusion_LuxI_Right_kecdiff = 1;
  Diffusion_LuxI_Right_kecdiff has u_1_second_n1;
  MembraneDiffusion_LuxI_i = ;
  MembraneDiffusion_LuxI_j = ;

  // Other declarations:
  var QuorumTrigger__locations, QuorumTrigger_size;
  const default, kr_f, kr_r, ka_f, ka_r, kc_f, kc_r, ko_f, ko_r, kao_f, kao_r;
  const kmdiff_f, kmdiff_r, kd, kecd, nc, nr, ko, kb, ng, np, ka, kecdiff;

  // Unit definitions:
  unit u_1_second_n1 = 1 / second;

  // Display Names:
  kr_f is "Forward repression binding rate";
  kr_r is "Reverse repression binding rate";
  ka_f is "Forward activation binding rate";
  ka_r is "Reverse activation binding rate";
  kc_f is "Forward complex formation rate";
  kc_r is "Reverse complex formation rate";
  ko_f is "Forward RNAP binding rate";
  ko_r is "Reverse RNAP binding rate";
  kao_f is "Forward activated RNAP binding rate";
  kao_r is "Reverse activated RNAP binding rate";
  kmdiff_f is "Forward membrane diffusion rate";
  kmdiff_r is "Reverse membrane diffusion rate";
  kd is "Degradation rate";
  kecd is "Extracellular degradation rate";
  nc is "Stoichiometry of binding";
  nr is "Initial RNAP count";
  ko is "Open complex production rate";
  kb is "Basal production rate";
  ng is "Initial promoter count";
  np is "Stoichiometry of production";
  ka is "Activated production rate";
  kecdiff is "Extracellular diffusion rate";
end
'''