import unittest
import unittest.mock as mock
from antimony_parser import AntimonyParser
import inspect
from .test_strings import *


class AntimonyParserModuleStatementTests(unittest.TestCase):
    parser = AntimonyParser()

    def check_import_statement_parses_correctly(self, filename_string: str) -> None:
        antimony_string = f"import \"{filename_string}\""
        print(f"checking string '{antimony_string}' passes")
        tree = self.parser.parse(antimony_string)
        assert len(tree.children) == 1
        token = tree.children[0]
        self.assertEqual(str(token), f"\"{filename_string}\"")

    def compare_parsed_tokens(self, string, branch_name, token_values):
        """
        Parse :param string: and search for :param branch_name:. Then
        check that the list of tokens are equal to the children of branch_name
        :param string: The antmiony string to parse
        :param branch_name: The name of the branch in the lark.Tree. This is either the name of the rule or
        the value at the right side of the "->" operator.
        :param token_values: list of strings that are tokens you expect.
        :return:
        """
        print(f"Current test method being executed: \n\t\"{inspect.stack()[0][3]}\"")
        print(f"input string is: \n\t\"{string}\"")
        tree = self.parser.parse(string)
        print(f"parsed tree is: \n\t\"{tree}\"")
        # print(branch_name in tree)
        x = list(tree.find_data(branch_name))
        if len(x) == 0 :
            raise ValueError(f"Branch name {branch_name} not found")
        for i in tree.find_data(branch_name):
            self.assertEqual(i.children, token_values)
        print("\n\n")

    def test_absolute_import_string_parses_correctly(self):
        print(import_string)
        tree = self.parser.parse(import_string)
        print(tree)

    def test_module_name_parses_correctly(self):
        print(module_name)
        tree = self.parser.parse(module_name)
        print(tree)

    def test_module_name_with_astrisk_parses_correctly(self):
        print(module_name)
        tree = self.parser.parse(module_name_with_astrisk)
        print(tree)

    def test_assignment_rule_parses_correctly(self):
        tree_with_tokens = dict(
            variable=["x"]

        )
        tree = self.parser.parse(assignmentRule)
        print(tree)
        # self.compare_parsed_tokens(initialValue, "variable", ["x", "3"])

    def test_initialValue_parses_correctly(self):
        """

        :return:
        """
        tree = self.parser.parse(assignmentRule)
        print(tree)
        # self.compare_parsed_tokens(initialValue, "param_init", ["x", "3"])

    def test_parameter_parses_correctly(self):
        tree = self.parser.parse(parameter)
        print(tree)
        # self.compare_parsed_tokens(parameter, "param_init", ["a", "3"])

    def test_parameter_inf_parses_correctly(self):
        tree = self.parser.parse(parameter_inf)
        print(tree)
        # self.compare_parsed_tokens(parameter_inf, "param_init_inf", ["a"])

    def test_parameter_nan_parses_correctly(self):
        tree = self.parser.parse(parameter_nan)
        print(tree)
        # self.compare_parsed_tokens(parameter_nan, "param_init_nan", ["a"])

    def test_compartment_parses_correctly(self):

        tree = self.parser.parse(compartment)
        print(tree)
        # self.compare_parsed_tokens(compartment, "compartmentinit", ["x", "y"])

    def test_rxn_right_parses_correctly(self):
        print(rxn_right)
        tree = self.parser.parse(rxn_right)
        print(tree)

    def test_initialAssignment_parses_correctly(self):
        print(initialAssignment)
        tree = self.parser.parse(initialAssignment)
        print(tree)

    def test_assignmentRule_parses_correctly(self):
        print(assignmentRule)
        tree = self.parser.parse(assignmentRule)
        print(tree)

    def test_negparen_parses_correctly(self):
        print(negparen)
        tree = self.parser.parse(negparen)
        print(tree)

    def test_non_ascii_parses_correctly(self):
        print(non_ascii)
        tree = self.parser.parse(non_ascii)
        print(tree)
        self.assertTrue(True)

    def test_rateRule_parses_correctly(self):
        print(rateRule)
        tree = self.parser.parse(rateRule)
        print(tree)

    def test_mean_parses_correctly(self):
        print(mean)
        tree = self.parser.parse(mean)
        print(tree)

    def test_initialConcentration_parses_correctly(self):
        print(initialConcentration)
        tree = self.parser.parse(initialConcentration)
        print(tree)

    def test_mode_parses_correctly(self):
        print(mode)
        tree = self.parser.parse(mode)
        print(tree)

    def test_parameter_neginf_parses_correctly(self):
        print(parameter_neginf)
        tree = self.parser.parse(parameter_neginf)
        print(tree)

    def test_reaction_parses_correctly(self):
        print(reaction)
        tree = self.parser.parse(reaction)
        print(tree)

    def test_median_parses_correctly(self):
        print(median)
        tree = self.parser.parse(median)
        print(tree)

    def test_SBO_param_parses_correctly(self):
        print(SBO_param)
        tree = self.parser.parse(SBO_param)
        print(tree)

    def test_species_parses_correctly(self):
        print(species)
        tree = self.parser.parse(species)
        print(tree)

    def test_event_parses_correctly(self):
        print(event)
        tree = self.parser.parse(event)
        print(tree)

    def test_kurtosis_parses_correctly(self):
        print(kurtosis)
        tree = self.parser.parse(kurtosis)
        print(tree)

    def test_skewness_parses_correctly(self):
        print(skewness)
        tree = self.parser.parse(skewness)
        print(tree)

    def test_variance_parses_correctly(self):
        print(variance)
        tree = self.parser.parse(variance)
        print(tree)

    def test_reactionIn_parses_correctly(self):
        print(reactionIn)
        tree = self.parser.parse(reactionIn)
        print(tree)

    def test_names_parses_correctly(self):
        print(names)
        tree = self.parser.parse(names)
        print(tree)

    def test_range_parses_correctly(self):
        print(range)
        tree = self.parser.parse(range)
        print(tree)

    def test_sampleSize_parses_correctly(self):
        print(sampleSize)
        tree = self.parser.parse(sampleSize)
        print(tree)

    def test_simple_flux_parses_correctly(self):
        print(simple_flux)
        tree = self.parser.parse(simple_flux)
        print(tree)

    def test_simple_flux2_parses_correctly(self):
        print(simple_flux2)
        tree = self.parser.parse(simple_flux2)
        print(tree)

    def test_initialAmount_parses_correctly(self):
        print(initialAmount)
        tree = self.parser.parse(initialAmount)
        print(tree)

    def test_simple_flux_neg_parses_correctly(self):
        print(simple_flux_neg)
        tree = self.parser.parse(simple_flux_neg)
        print(tree)

    def test_standardError_parses_correctly(self):
        print(standardError)
        tree = self.parser.parse(standardError)
        print(tree)

    def test_SBO_param2_parses_correctly(self):
        print(SBO_param2)
        tree = self.parser.parse(SBO_param2)
        print(tree)

    def test_units_parses_correctly(self):
        print(units)
        tree = self.parser.parse(units)
        print(tree)

    def test_SBO_species_parses_correctly(self):
        print(SBO_species)
        tree = self.parser.parse(SBO_species)
        print(tree)

    def test_interactionActivation_parses_correctly(self):
        print(interactionActivation)
        tree = self.parser.parse(interactionActivation)
        print(tree)

    def test_interactionGeneric_parses_correctly(self):
        print(interactionGeneric)
        tree = self.parser.parse(interactionGeneric)
        print(tree)

    def test_interactionInhibition_parses_correctly(self):
        print(interactionInhibition)
        tree = self.parser.parse(interactionInhibition)
        print(tree)

    def test_standardDeviation_parses_correctly(self):
        print(standardDeviation)
        tree = self.parser.parse(standardDeviation)
        print(tree)

    def test_substance_only_species_parses_correctly(self):
        print(substance_only_species)
        tree = self.parser.parse(substance_only_species)
        print(tree)

    def test_simple_objective_parses_correctly(self):
        print(simple_objective)
        tree = self.parser.parse(simple_objective)
        print(tree)

    def test_simple_objective2_parses_correctly(self):
        print(simple_objective2)
        tree = self.parser.parse(simple_objective2)
        print(tree)

    def test_two_sided_flux_parses_correctly(self):
        print(two_sided_flux)
        tree = self.parser.parse(two_sided_flux)
        print(tree)

    def test_eventT0_parses_correctly(self):
        print(eventT0)
        tree = self.parser.parse(eventT0)
        print(tree)

    def test_distribution_parses_correctly(self):
        print(distribution)
        tree = self.parser.parse(distribution)
        print(tree)

    def test_encodes_parses_correctly(self):
        print(encodes)
        tree = self.parser.parse(encodes)
        print(tree)

    def test_hasPart_parses_correctly(self):
        print(hasPart)
        tree = self.parser.parse(hasPart)
        print(tree)

    def test_SBO_compartment_parses_correctly(self):
        print(SBO_compartment)
        tree = self.parser.parse(SBO_compartment)
        print(tree)

    def test_credibleInterval_parses_correctly(self):
        print(credibleInterval)
        tree = self.parser.parse(credibleInterval)
        print(tree)

    def test_eventPriority_parses_correctly(self):
        print(eventPriority)
        tree = self.parser.parse(eventPriority)
        print(tree)

    def test_hasTaxon_parses_correctly(self):
        print(hasTaxon)
        tree = self.parser.parse(hasTaxon)
        print(tree)

    def test_identity_parses_correctly(self):
        print(identity)
        tree = self.parser.parse(identity)
        print(tree)

    def test_interquartileRange_parses_correctly(self):
        print(interquartileRange)
        tree = self.parser.parse(interquartileRange)
        print(tree)

    def test_isPartOf_parses_correctly(self):
        print(isPartOf)
        tree = self.parser.parse(isPartOf)
        print(tree)

    def test_occursIn_parses_correctly(self):
        print(occursIn)
        tree = self.parser.parse(occursIn)
        print(tree)

    def test_rxn_right_mod_parses_correctly(self):
        print(rxn_right_mod)
        tree = self.parser.parse(rxn_right_mod)
        print(tree)

    def test_SBO_reaction_parses_correctly(self):
        print(SBO_reaction)
        tree = self.parser.parse(SBO_reaction)
        print(tree)

    def test_SBO_reaction_basic_parses_correctly(self):
        print("J0.sboTerm = 888")
        tree = self.parser.parse("J0.sboTerm = 888")
        print(tree)

    def test_coefficientOfVariation_parses_correctly(self):
        print(coefficientOfVariation)
        tree = self.parser.parse(coefficientOfVariation)
        print(tree)

    def test_hasVersion_parses_correctly(self):
        print(hasVersion)
        tree = self.parser.parse(hasVersion)
        print(tree)

    def test_SBO_localvar_parses_correctly(self):
        print(SBO_localvar)
        tree = self.parser.parse(SBO_localvar)
        print(tree)

    def test_confidenceInterval_parses_correctly(self):
        print(confidenceInterval)
        tree = self.parser.parse(confidenceInterval)
        print(tree)

    def test_hasProperty_parses_correctly(self):
        print(hasProperty)
        tree = self.parser.parse(hasProperty)
        print(tree)

    def test_isEncodedBy_parses_correctly(self):
        print(isEncodedBy)
        tree = self.parser.parse(isEncodedBy)
        print(tree)

    def test_isHomologTo_parses_correctly(self):
        print(isHomologTo)
        tree = self.parser.parse(isHomologTo)
        print(tree)

    def test_isVersionOf_parses_correctly(self):
        print(isVersionOf)
        tree = self.parser.parse(isVersionOf)
        print(tree)

    def test_simple_flux_and_objective_parses_correctly(self):
        print(simple_flux_and_objective)
        tree = self.parser.parse(simple_flux_and_objective)
        print(tree)

    def test_simple_flux_and_objective2_parses_correctly(self):
        print(simple_flux_and_objective2)
        tree = self.parser.parse(simple_flux_and_objective2)
        print(tree)

    def test_isPropertyOf_parses_correctly(self):
        print(isPropertyOf)
        tree = self.parser.parse(isPropertyOf)
        print(tree)

    def test_compound_units4_parses_correctly(self):
        print(compound_units4)
        tree = self.parser.parse(compound_units4)
        print(tree)

    def test_isDescribedBy_parses_correctly(self):
        print(isDescribedBy)
        tree = self.parser.parse(isDescribedBy)
        print(tree)

    def test_eventPersistent_parses_correctly(self):
        print(eventPersistent)
        tree = self.parser.parse(eventPersistent)
        print(tree)

    def test_formula_objective_parses_correctly(self):
        print(formula_objective)
        tree = self.parser.parse(formula_objective)
        print(tree)

    def test_simple_objective4_parses_correctly(self):
        print(simple_objective4)
        tree = self.parser.parse(simple_objective4)
        print(tree)

    def test_simple_objective5_parses_correctly(self):
        print(simple_objective5)
        tree = self.parser.parse(simple_objective5)
        print(tree)

    def test_eventFromTrigger_parses_correctly(self):
        print(eventFromTrigger)
        tree = self.parser.parse(eventFromTrigger)
        print(tree)

    def test_SBO_event_parses_correctly(self):
        print(SBO_event)
        tree = self.parser.parse(SBO_event)
        print(tree)

    def test_SBO_module_parses_correctly(self):
        print(SBO_module)
        tree = self.parser.parse(SBO_module)
        print(tree)

    def test_simple_objective3_parses_correctly(self):
        print(simple_objective3)
        tree = self.parser.parse(simple_objective3)
        print(tree)

    def test_function_name_parses_correctly(self):
        print(function_name)
        tree = self.parser.parse(function_name)
        print(tree)

    def test_compound_units1_parses_correctly(self):
        print(compound_units1)
        tree = self.parser.parse(compound_units1)
        print(tree)


    def test_SBO_submodel_parses_correctly(self):
        print(SBO_submodel)
        tree = self.parser.parse(SBO_submodel)
        print(tree)

    def test_SBO_function_parses_correctly(self):
        print(SBO_function)
        tree = self.parser.parse(SBO_function)
        print(tree)

    def test_hierarchy_parses_correctly(self):
        print(hierarchy)
        tree = self.parser.parse(hierarchy)
        print(tree)

    def test_compound_units2_parses_correctly(self):
        print(compound_units2)
        tree = self.parser.parse(compound_units2)
        print(tree)

    def test_port_parses_correctly(self):
        print(port)
        tree = self.parser.parse(port)
        print(tree)

    def test_defaultSubCompartment_parses_correctly(self):
        print(defaultSubCompartment)
        tree = self.parser.parse(defaultSubCompartment)
        print(tree)

    def test_simple_flux3_parses_correctly(self):
        print(simple_flux3)
        tree = self.parser.parse(simple_flux3)
        print(tree)

    def test_simple_flux3_reverse_parses_correctly(self):
        print(simple_flux3_reverse)
        tree = self.parser.parse(simple_flux3_reverse)
        print(tree)

    def test_compound_units3_parses_correctly(self):
        print(compound_units3)
        tree = self.parser.parse(compound_units3)
        print(tree)

    def test_externalParameter2_parses_correctly(self):
        print(externalParameter2)
        tree = self.parser.parse(externalParameter2)
        print(tree)

    def test_externalParameter3_parses_correctly(self):
        print(externalParameter3)
        tree = self.parser.parse(externalParameter3)
        print(tree)

    def test_SBO_module_rt_parses_correctly(self):
        print(SBO_module_rt)
        tree = self.parser.parse(SBO_module_rt)
        print(tree)

    def test_deletion_parses_correctly(self):
        print(deletion)
        tree = self.parser.parse(deletion)
        print(tree)

    def test_externalParameter1_parses_correctly(self):
        print(externalParameter1)
        tree = self.parser.parse(externalParameter1)
        print(tree)

    def test_replaceReactionOnly_parses_correctly(self):
        print(replaceReactionOnly)
        tree = self.parser.parse(replaceReactionOnly)
        print(tree)

    def test_replaceReactionOnly2_parses_correctly(self):
        print(replaceReactionOnly2)
        tree = self.parser.parse(replaceReactionOnly2)
        print(tree)

    def test_units_rt_parses_correctly(self):
        print(units_rt)
        tree = self.parser.parse(units_rt)
        print(tree)

    def test_function_name_rt_parses_correctly(self):
        print(function_name_rt)
        tree = self.parser.parse(function_name_rt)
        print(tree)

    def test_deleteAssignmentRuleOfAnother_parses_correctly(self):
        print(deleteAssignmentRuleOfAnother)
        tree = self.parser.parse(deleteAssignmentRuleOfAnother)
        print(tree)

    def test_deleteRateRuleOfAnother_parses_correctly(self):
        print(deleteRateRuleOfAnother)
        tree = self.parser.parse(deleteRateRuleOfAnother)
        print(tree)

    def test_replaceReactionWithKineticLaw_parses_correctly(self):
        print(replaceReactionWithKineticLaw)
        tree = self.parser.parse(replaceReactionWithKineticLaw)
        print(tree)

    def test_SBO_function_rt_parses_correctly(self):
        print(SBO_function_rt)
        tree = self.parser.parse(SBO_function_rt)
        print(tree)

    def test_deleteAssignmentRuleIndirect_parses_correctly(self):
        print(deleteAssignmentRuleIndirect)
        tree = self.parser.parse(deleteAssignmentRuleIndirect)
        print(tree)

    def test_deleteInitialAssignmentOfAnother_parses_correctly(self):
        print(deleteInitialAssignmentOfAnother)
        tree = self.parser.parse(deleteInitialAssignmentOfAnother)
        print(tree)

    def test_deleteRateRuleIndirect_parses_correctly(self):
        print(deleteRateRuleIndirect)
        tree = self.parser.parse(deleteRateRuleIndirect)
        print(tree)

    def test_deleteInitialAssignmentIndirect_parses_correctly(self):
        print(deleteInitialAssignmentIndirect)
        tree = self.parser.parse(deleteInitialAssignmentIndirect)
        print(tree)

    def test_deleteSpeciesInDefaultCompartment_parses_correctly(self):
        print(deleteSpeciesInDefaultCompartment)
        tree = self.parser.parse(deleteSpeciesInDefaultCompartment)
        print(tree)

    def test_deleteSpeciesPortDefaultCompartment_parses_correctly(self):
        print(deleteSpeciesPortDefaultCompartment)
        tree = self.parser.parse(deleteSpeciesPortDefaultCompartment)
        print(tree)

    def test_replaceInitialAssignment_parses_correctly(self):
        print(replaceInitialAssignment)
        tree = self.parser.parse(replaceInitialAssignment)
        print(tree)

    def test_replaceParameter_parses_correctly(self):
        print(replaceParameter)
        tree = self.parser.parse(replaceParameter)
        print(tree)

    def test_replaceAssignmentRule_parses_correctly(self):
        print(replaceAssignmentRule)
        tree = self.parser.parse(replaceAssignmentRule)
        print(tree)

    def test_replaceRateRule_parses_correctly(self):
        print(replaceRateRule)
        tree = self.parser.parse(replaceRateRule)
        print(tree)

    def test_compound_units4_rt_parses_correctly(self):
        print(compound_units4_rt)
        tree = self.parser.parse(compound_units4_rt)
        print(tree)

    def test_deleteAssignmentRuleDirect_parses_correctly(self):
        print(deleteAssignmentRuleDirect)
        tree = self.parser.parse(deleteAssignmentRuleDirect)
        print(tree)

    def test_deleteInitialAssignmentDirect_parses_correctly(self):
        print(deleteInitialAssignmentDirect)
        tree = self.parser.parse(deleteInitialAssignmentDirect)
        print(tree)

    def test_deleteKineticLaw_parses_correctly(self):
        print(deleteKineticLaw)
        tree = self.parser.parse(deleteKineticLaw)
        print(tree)

    def test_deleteRateRuleDirect_parses_correctly(self):
        print(deleteRateRuleDirect)
        tree = self.parser.parse(deleteRateRuleDirect)
        print(tree)

    def test_formula_objective2_parses_correctly(self):
        print(formula_objective2)
        tree = self.parser.parse(formula_objective2)
        print(tree)

    def test_deleteSpecies_parses_correctly(self):
        print(deleteSpecies)
        tree = self.parser.parse(deleteSpecies)
        print(tree)

    def test_replaceReactionWithCompartments1_parses_correctly(self):
        print(replaceReactionWithCompartments1)
        tree = self.parser.parse(replaceReactionWithCompartments1)
        print(tree)

    def test_compound_units1_rt_parses_correctly(self):
        print(compound_units1_rt)
        tree = self.parser.parse(compound_units1_rt)
        print(tree)

    def test_deleteProduct_parses_correctly(self):
        print(deleteProduct)
        tree = self.parser.parse(deleteProduct)
        print(tree)

    def test_deleteReactant_parses_correctly(self):
        print(deleteReactant)
        tree = self.parser.parse(deleteReactant)
        print(tree)

    def test_deleteSpeciesPort_parses_correctly(self):
        print(deleteSpeciesPort)
        tree = self.parser.parse(deleteSpeciesPort)
        print(tree)

    def test_submodelInteraction_parses_correctly(self):
        print(submodelInteraction)
        tree = self.parser.parse(submodelInteraction)
        print(tree)

    def test_deleteEventAssignment3_parses_correctly(self):
        print(deleteEventAssignment3)
        tree = self.parser.parse(deleteEventAssignment3)
        print(tree)

    def test_defaultSubSubCompartment_parses_correctly(self):
        print(defaultSubSubCompartment)
        tree = self.parser.parse(defaultSubSubCompartment)
        print(tree)

    def test_replaceReactionWithKineticLawRxnRef_parses_correctly(self):
        print(replaceReactionWithKineticLawRxnRef)
        tree = self.parser.parse(replaceReactionWithKineticLawRxnRef)
        print(tree)

    def test_three_level_constraints_parses_correctly(self):
        print(three_level_constraints)
        tree = self.parser.parse(three_level_constraints)
        print(tree)

    def test_replaceCompartment_parses_correctly(self):
        print(replaceCompartment)
        tree = self.parser.parse(replaceCompartment)
        print(tree)

    def test_replaceSpeciesDefaultCompartment_parses_correctly(self):
        print(replaceSpeciesDefaultCompartment)
        tree = self.parser.parse(replaceSpeciesDefaultCompartment)
        print(tree)

    def test_assignmentRule_rt_parses_correctly(self):
        print(assignmentRule_rt)
        tree = self.parser.parse(assignmentRule_rt)
        print(tree)

    def test_deleteSpeciesInDefaultCompartment2_parses_correctly(self):
        print(deleteSpeciesInDefaultCompartment2)
        tree = self.parser.parse(deleteSpeciesInDefaultCompartment2)
        print(tree)

    def test_deleteEventAssignment5_parses_correctly(self):
        print(deleteEventAssignment5)
        tree = self.parser.parse(deleteEventAssignment5)
        print(tree)

    def test_deleteEventAssignment_parses_correctly(self):
        print(deleteEventAssignment)
        tree = self.parser.parse(deleteEventAssignment)
        print(tree)

    def test_deleteEventAssignment4_parses_correctly(self):
        print(deleteEventAssignment4)
        tree = self.parser.parse(deleteEventAssignment4)
        print(tree)

    def test_deleteTrigger_parses_correctly(self):
        print(deleteTrigger)
        tree = self.parser.parse(deleteTrigger)
        print(tree)

    def test_replaceReactionWithCompartments2_parses_correctly(self):
        print(replaceReactionWithCompartments2)
        tree = self.parser.parse(replaceReactionWithCompartments2)
        print(tree)

    def test_subport_parses_correctly(self):
        print(subport)
        tree = self.parser.parse(subport)
        print(tree)

    def test_replaceSpecies_parses_correctly(self):
        print(replaceSpecies)
        tree = self.parser.parse(replaceSpecies)
        print(tree)

    def test_initialValue_rt_parses_correctly(self):
        print(initialValue_rt)
        tree = self.parser.parse(initialValue_rt)
        print(tree)

    def test_parameter_rt_parses_correctly(self):
        print(parameter_rt)
        tree = self.parser.parse(parameter_rt)
        print(tree)

    def test_replaceInteraction_parses_correctly(self):
        print(replaceInteraction)
        tree = self.parser.parse(replaceInteraction)
        print(tree)

    def test_deleteModifierKineticLaw_parses_correctly(self):
        print(deleteModifierKineticLaw)
        tree = self.parser.parse(deleteModifierKineticLaw)
        print(tree)

    def test_deleteReaction_parses_correctly(self):
        print(deleteReaction)
        tree = self.parser.parse(deleteReaction)
        print(tree)

    def test_initialAssignment_rt_parses_correctly(self):
        print(initialAssignment_rt)
        tree = self.parser.parse(initialAssignment_rt)
        print(tree)

    def test_parameter_inf_rt_parses_correctly(self):
        print(parameter_inf_rt)
        tree = self.parser.parse(parameter_inf_rt)
        print(tree)

    def test_parameter_neginf_rt_parses_correctly(self):
        print(parameter_neginf_rt)
        tree = self.parser.parse(parameter_neginf_rt)
        print(tree)

    def test_parameter_nan_rt_parses_correctly(self):
        print(parameter_nan_rt)
        tree = self.parser.parse(parameter_nan_rt)
        print(tree)

    def test_simple_flux_eq_neq_parses_correctly(self):
        print(simple_flux_eq_neq)
        tree = self.parser.parse(simple_flux_eq_neq)
        print(tree)

    def test_SBO_submodel_shadowed_parses_correctly(self):
        print(SBO_submodel_shadowed)
        tree = self.parser.parse(SBO_submodel_shadowed)
        print(tree)

    def test_subport2_parses_correctly(self):
        print(subport2)
        tree = self.parser.parse(subport2)
        print(tree)

    def test_compound_units2_rt_parses_correctly(self):
        print(compound_units2_rt)
        tree = self.parser.parse(compound_units2_rt)
        print(tree)

    def test_compound_units3_rt_parses_correctly(self):
        print(compound_units3_rt)
        tree = self.parser.parse(compound_units3_rt)
        print(tree)

    def test_initialConcentration_rt_parses_correctly(self):
        print(initialConcentration_rt)
        tree = self.parser.parse(initialConcentration_rt)
        print(tree)

    def test_defaultOrNotCompartment_parses_correctly(self):
        print(defaultOrNotCompartment)
        tree = self.parser.parse(defaultOrNotCompartment)
        print(tree)

    def test_deleteModifier_parses_correctly(self):
        print(deleteModifier)
        tree = self.parser.parse(deleteModifier)
        print(tree)

    def test_deleteDelay_parses_correctly(self):
        print(deleteDelay)
        tree = self.parser.parse(deleteDelay)
        print(tree)

    def test_deletePriority_parses_correctly(self):
        print(deletePriority)
        tree = self.parser.parse(deletePriority)
        print(tree)

    def test_negparen_rt_parses_correctly(self):
        print(negparen_rt)
        tree = self.parser.parse(negparen_rt)
        print(tree)

    def test_global_units_parses_correctly(self):
        print(global_units)
        tree = self.parser.parse(global_units)
        print(tree)

    def test_rateRule_rt_parses_correctly(self):
        print(rateRule_rt)
        tree = self.parser.parse(rateRule_rt)
        print(tree)

    def test_substance_only_species_rt_parses_correctly(self):
        print(substance_only_species_rt)
        tree = self.parser.parse(substance_only_species_rt)
        print(tree)

    def test_numeric_constraints_parses_correctly(self):
        print(numeric_constraints)
        tree = self.parser.parse(numeric_constraints)
        print(tree)

    def test_event_rt_parses_correctly(self):
        print(event_rt)
        tree = self.parser.parse(event_rt)
        print(tree)

    def test_SBO_param_rt_parses_correctly(self):
        print(SBO_param_rt)
        tree = self.parser.parse(SBO_param_rt)
        print(tree)

    def test_SBO_param2_rt_parses_correctly(self):
        print(SBO_param2_rt)
        tree = self.parser.parse(SBO_param2_rt)
        print(tree)

    def test_hasPart_rt_parses_correctly(self):
        print(hasPart_rt)
        tree = self.parser.parse(hasPart_rt)
        print(tree)

    def test_names_rt_parses_correctly(self):
        print(names_rt)
        tree = self.parser.parse(names_rt)
        print(tree)

    def test_hasTaxon_rt_parses_correctly(self):
        print(hasTaxon_rt)
        tree = self.parser.parse(hasTaxon_rt)
        print(tree)

    def test_numeric_constraints_neg_parses_correctly(self):
        print(numeric_constraints_neg)
        tree = self.parser.parse(numeric_constraints_neg)
        print(tree)

    def test_hasVersion_rt_parses_correctly(self):
        print(hasVersion_rt)
        tree = self.parser.parse(hasVersion_rt)
        print(tree)

    def test_isEncodedBy_rt_parses_correctly(self):
        print(isEncodedBy_rt)
        tree = self.parser.parse(isEncodedBy_rt)
        print(tree)

    def test_isHomologTo_rt_parses_correctly(self):
        print(isHomologTo_rt)
        tree = self.parser.parse(isHomologTo_rt)
        print(tree)

    def test_SBO_species_rt_parses_correctly(self):
        print(SBO_species_rt)
        tree = self.parser.parse(SBO_species_rt)
        print(tree)

    def test_eventDelay_parses_correctly(self):
        print(eventDelay)
        tree = self.parser.parse(eventDelay)
        print(tree)

    def test_eventDelay_rt_parses_correctly(self):
        print(eventDelay_rt)
        tree = self.parser.parse(eventDelay_rt)
        print(tree)

    def test_hasProperty_rt_parses_correctly(self):
        print(hasProperty_rt)
        tree = self.parser.parse(hasProperty_rt)
        print(tree)

    def test_identity_rt_parses_correctly(self):
        print(identity_rt)
        tree = self.parser.parse(identity_rt)
        print(tree)

    def test_isPartOf_rt_parses_correctly(self):
        print(isPartOf_rt)
        tree = self.parser.parse(isPartOf_rt)
        print(tree)

    def test_isVersionOf_rt_parses_correctly(self):
        print(isVersionOf_rt)
        tree = self.parser.parse(isVersionOf_rt)
        print(tree)

    def test_occursIn_rt_parses_correctly(self):
        print(occursIn_rt)
        tree = self.parser.parse(occursIn_rt)
        print(tree)

    def test_rxn_right_rt_parses_correctly(self):
        print(rxn_right_rt)
        tree = self.parser.parse(rxn_right_rt)
        print(tree)

    def test_SBO_localvar_rt_parses_correctly(self):
        print(SBO_localvar_rt)
        tree = self.parser.parse(SBO_localvar_rt)
        print(tree)

    def test_encodes_rt_parses_correctly(self):
        print(encodes_rt)
        tree = self.parser.parse(encodes_rt)
        print(tree)

    def test_eventT0_rt_parses_correctly(self):
        print(eventT0_rt)
        tree = self.parser.parse(eventT0_rt)
        print(tree)

    def test_mean_rt_parses_correctly(self):
        print(mean_rt)
        tree = self.parser.parse(mean_rt)
        print(tree)

    def test_mode_rt_parses_correctly(self):
        print(mode_rt)
        tree = self.parser.parse(mode_rt)
        print(tree)

    def test_fluxes_and_objectives_parses_correctly(self):
        print(fluxes_and_objectives)
        tree = self.parser.parse(fluxes_and_objectives)
        print(tree)

    def test_isDescribedBy_rt_parses_correctly(self):
        print(isDescribedBy_rt)
        tree = self.parser.parse(isDescribedBy_rt)
        print(tree)

    def test_model1_parses_correctly(self):
        print(model1)
        tree = self.parser.parse(model1)
        print(tree)

    def test_median_rt_parses_correctly(self):
        print(median_rt)
        tree = self.parser.parse(median_rt)
        print(tree)

    def test_subsubport_parses_correctly(self):
        print(subsubport)
        tree = self.parser.parse(subsubport)
        print(tree)

    def test_eventPriority_rt_parses_correctly(self):
        print(eventPriority_rt)
        tree = self.parser.parse(eventPriority_rt)
        print(tree)

    def test_isPropertyOf_rt_parses_correctly(self):
        print(isPropertyOf_rt)
        tree = self.parser.parse(isPropertyOf_rt)
        print(tree)

    def test_module_name_rt_parses_correctly(self):
        print(module_name_rt)
        tree = self.parser.parse(module_name_rt)
        print(tree)

    def test_skewness_rt_parses_correctly(self):
        print(skewness_rt)
        tree = self.parser.parse(skewness_rt)
        print(tree)

    def test_variance_rt_parses_correctly(self):
        print(variance_rt)
        tree = self.parser.parse(variance_rt)
        print(tree)

    def test_kurtosis_rt_parses_correctly(self):
        print(kurtosis_rt)
        tree = self.parser.parse(kurtosis_rt)
        print(tree)

    def test_sampleSize_rt_parses_correctly(self):
        print(sampleSize_rt)
        tree = self.parser.parse(sampleSize_rt)
        print(tree)

    def test_SBO_submodel_rt_parses_correctly(self):
        print(SBO_submodel_rt)
        tree = self.parser.parse(SBO_submodel_rt)
        print(tree)

    def test_eventPersistent_rt_parses_correctly(self):
        print(eventPersistent_rt)
        tree = self.parser.parse(eventPersistent_rt)
        print(tree)

    def test_range_rt_parses_correctly(self):
        print(range_rt)
        tree = self.parser.parse(range_rt)
        print(tree)

    def test_eventFromTrigger_rt_parses_correctly(self):
        print(eventFromTrigger_rt)
        tree = self.parser.parse(eventFromTrigger_rt)
        print(tree)

    def test_standardError_rt_parses_correctly(self):
        print(standardError_rt)
        tree = self.parser.parse(standardError_rt)
        print(tree)

    def test_standardDeviation_rt_parses_correctly(self):
        print(standardDeviation_rt)
        tree = self.parser.parse(standardDeviation_rt)
        print(tree)

    def test_coefficientOfVariation_rt_parses_correctly(self):
        print(coefficientOfVariation_rt)
        tree = self.parser.parse(coefficientOfVariation_rt)
        print(tree)

    def test_confidenceInterval_rt_parses_correctly(self):
        print(confidenceInterval_rt)
        tree = self.parser.parse(confidenceInterval_rt)
        print(tree)

    def test_credibleInterval_rt_parses_correctly(self):
        print(credibleInterval_rt)
        tree = self.parser.parse(credibleInterval_rt)
        print(tree)

    def test_distribution_rt_parses_correctly(self):
        print(distribution_rt)
        tree = self.parser.parse(distribution_rt)
        print(tree)

    def test_SBO_event_rt_parses_correctly(self):
        print(SBO_event_rt)
        tree = self.parser.parse(SBO_event_rt)
        print(tree)

    def test_SBO_reaction_rt_parses_correctly(self):
        print(SBO_reaction_rt)
        tree = self.parser.parse(SBO_reaction_rt)
        print(tree)

    def test_rxn_right_mod_rt_parses_correctly(self):
        print(rxn_right_mod_rt)
        tree = self.parser.parse(rxn_right_mod_rt)
        print(tree)

    def test_interquartileRange_rt_parses_correctly(self):
        print(interquartileRange_rt)
        tree = self.parser.parse(interquartileRange_rt)
        print(tree)

    def test_SBO_compartment_rt_parses_correctly(self):
        print(SBO_compartment_rt)
        tree = self.parser.parse(SBO_compartment_rt)
        print(tree)

    def test_interactionActivation_rt_parses_correctly(self):
        print(interactionActivation_rt)
        tree = self.parser.parse(interactionActivation_rt)
        print(tree)

    def test_interactionGeneric_rt_parses_correctly(self):
        print(interactionGeneric_rt)
        tree = self.parser.parse(interactionGeneric_rt)
        print(tree)

    def test_interactionInhibition_rt_parses_correctly(self):
        print(interactionInhibition_rt)
        tree = self.parser.parse(interactionInhibition_rt)
        print(tree)

    def test_compartment_rt_parses_correctly(self):
        print(compartment_rt)
        tree = self.parser.parse(compartment_rt)
        print(tree)

    def test_deleteEventAssignment2_parses_correctly(self):
        print(deleteEventAssignment2)
        tree = self.parser.parse(deleteEventAssignment2)
        print(tree)

    def test_deleteDelay2_parses_correctly(self):
        print(deleteDelay2)
        tree = self.parser.parse(deleteDelay2)
        print(tree)

    def test_deletePriority2_parses_correctly(self):
        print(deletePriority2)
        tree = self.parser.parse(deletePriority2)
        print(tree)

    def test_global_units_rt_parses_correctly(self):
        print(global_units_rt)
        tree = self.parser.parse(global_units_rt)
        print(tree)

    def test_species_rt_parses_correctly(self):
        print(species_rt)
        tree = self.parser.parse(species_rt)
        print(tree)

    def test_externalParameter2_rt_parses_correctly(self):
        print(externalParameter2_rt)
        tree = self.parser.parse(externalParameter2_rt)
        print(tree)

    def test_externalParameter1_rt_parses_correctly(self):
        print(externalParameter1_rt)
        tree = self.parser.parse(externalParameter1_rt)
        print(tree)

    def test_externalParameter3_rt_parses_correctly(self):
        print(externalParameter3_rt)
        tree = self.parser.parse(externalParameter3_rt)
        print(tree)

    def test_initialAmount_rt_parses_correctly(self):
        print(initialAmount_rt)
        tree = self.parser.parse(initialAmount_rt)
        print(tree)

    def test_reaction_rt_parses_correctly(self):
        print(reaction_rt)
        tree = self.parser.parse(reaction_rt)
        print(tree)

    def test_two_sided_flux_complete_parses_correctly(self):
        print(two_sided_flux_complete)
        tree = self.parser.parse(two_sided_flux_complete)
        print(tree)

    def test_hierarchy_rt_parses_correctly(self):
        print(hierarchy_rt)
        tree = self.parser.parse(hierarchy_rt)
        print(tree)

    def test_port_rt_parses_correctly(self):
        print(port_rt)
        tree = self.parser.parse(port_rt)
        print(tree)

    def test_defaultSubCompartment_rt_parses_correctly(self):
        print(defaultSubCompartment_rt)
        tree = self.parser.parse(defaultSubCompartment_rt)
        print(tree)

    def test_formula_objective_rt_parses_correctly(self):
        print(formula_objective_rt)
        tree = self.parser.parse(formula_objective_rt)
        print(tree)

    def test_replaceSpeciesDefaultCompartment_rt_parses_correctly(self):
        print(replaceSpeciesDefaultCompartment_rt)
        tree = self.parser.parse(replaceSpeciesDefaultCompartment_rt)
        print(tree)

    def test_formula_objective2_rt_parses_correctly(self):
        print(formula_objective2_rt)
        tree = self.parser.parse(formula_objective2_rt)
        print(tree)

    def test_deleteAssignmentRuleDirect_rt_parses_correctly(self):
        print(deleteAssignmentRuleDirect_rt)
        tree = self.parser.parse(deleteAssignmentRuleDirect_rt)
        print(tree)

    def test_replaceAssignmentRule_rt_parses_correctly(self):
        print(replaceAssignmentRule_rt)
        tree = self.parser.parse(replaceAssignmentRule_rt)
        print(tree)

    def test_deleteAssignmentRuleIndirect_rt_parses_correctly(self):
        print(deleteAssignmentRuleIndirect_rt)
        tree = self.parser.parse(deleteAssignmentRuleIndirect_rt)
        print(tree)

    def test_model2_parses_correctly(self):
        print(model2)
        tree = self.parser.parse(model2)
        print(tree)

    def test_deletion_rt_parses_correctly(self):
        print(deletion_rt)
        tree = self.parser.parse(deletion_rt)
        print(tree)

    def test_replaceParameter_rt_parses_correctly(self):
        print(replaceParameter_rt)
        tree = self.parser.parse(replaceParameter_rt)
        print(tree)

    def test_deleteInitialAssignmentDirect_rt_parses_correctly(self):
        print(deleteInitialAssignmentDirect_rt)
        tree = self.parser.parse(deleteInitialAssignmentDirect_rt)
        print(tree)

    def test_deleteInitialAssignmentIndirect_rt_parses_correctly(self):
        print(deleteInitialAssignmentIndirect_rt)
        tree = self.parser.parse(deleteInitialAssignmentIndirect_rt)
        print(tree)

    def test_replaceInitialAssignment_rt_parses_correctly(self):
        print(replaceInitialAssignment_rt)
        tree = self.parser.parse(replaceInitialAssignment_rt)
        print(tree)

    def test_deleteSpeciesInDefaultCompartment_rt_parses_correctly(self):
        print(deleteSpeciesInDefaultCompartment_rt)
        tree = self.parser.parse(deleteSpeciesInDefaultCompartment_rt)
        print(tree)

    def test_reactionIn_rt_parses_correctly(self):
        print(reactionIn_rt)
        tree = self.parser.parse(reactionIn_rt)
        print(tree)

    def test_deleteSpeciesPortDefaultCompartment_rt_parses_correctly(self):
        print(deleteSpeciesPortDefaultCompartment_rt)
        tree = self.parser.parse(deleteSpeciesPortDefaultCompartment_rt)
        print(tree)

    def test_replaceReactionOnly2_rt_parses_correctly(self):
        print(replaceReactionOnly2_rt)
        tree = self.parser.parse(replaceReactionOnly2_rt)
        print(tree)

    def test_replaceReactionOnly_rt_parses_correctly(self):
        print(replaceReactionOnly_rt)
        tree = self.parser.parse(replaceReactionOnly_rt)
        print(tree)

    def test_deleteInitialAssignmentOfAnother_rt_parses_correctly(self):
        print(deleteInitialAssignmentOfAnother_rt)
        tree = self.parser.parse(deleteInitialAssignmentOfAnother_rt)
        print(tree)

    def test_deleteRateRuleDirect_rt_parses_correctly(self):
        print(deleteRateRuleDirect_rt)
        tree = self.parser.parse(deleteRateRuleDirect_rt)
        print(tree)

    def test_replaceRateRule_rt_parses_correctly(self):
        print(replaceRateRule_rt)
        tree = self.parser.parse(replaceRateRule_rt)
        print(tree)

    def test_deleteRateRuleIndirect_rt_parses_correctly(self):
        print(deleteRateRuleIndirect_rt)
        tree = self.parser.parse(deleteRateRuleIndirect_rt)
        print(tree)

    def test_numeric_distributions_rev_parses_correctly(self):
        print(numeric_distributions_rev)
        tree = self.parser.parse(numeric_distributions_rev)
        print(tree)

    def test_defaultSubSubCompartment_rt_parses_correctly(self):
        print(defaultSubSubCompartment_rt)
        tree = self.parser.parse(defaultSubSubCompartment_rt)
        print(tree)

    def test_submodelInteraction_rt_parses_correctly(self):
        print(submodelInteraction_rt)
        tree = self.parser.parse(submodelInteraction_rt)
        print(tree)

    def test_subport_rt_parses_correctly(self):
        print(subport_rt)
        tree = self.parser.parse(subport_rt)
        print(tree)

    def test_SBO_submodel_shadowed_rt_parses_correctly(self):
        print(SBO_submodel_shadowed_rt)
        tree = self.parser.parse(SBO_submodel_shadowed_rt)
        print(tree)

    def test_subport2_rt_parses_correctly(self):
        print(subport2_rt)
        tree = self.parser.parse(subport2_rt)
        print(tree)

    def test_replaceReactionWithKineticLawRxnRef_rt_parses_correctly(self):
        print(replaceReactionWithKineticLawRxnRef_rt)
        tree = self.parser.parse(replaceReactionWithKineticLawRxnRef_rt)
        print(tree)

    def test_replaceCompartment_rt_parses_correctly(self):
        print(replaceCompartment_rt)
        tree = self.parser.parse(replaceCompartment_rt)
        print(tree)

    def test_fixname_test_parses_correctly(self):
        print(fixname_test)
        tree = self.parser.parse(fixname_test)
        print(tree)

    def test_deleteEventAssignment3_rt_parses_correctly(self):
        print(deleteEventAssignment3_rt)
        tree = self.parser.parse(deleteEventAssignment3_rt)
        print(tree)

    def test_numeric_distributions_parses_correctly(self):
        print(numeric_distributions)
        tree = self.parser.parse(numeric_distributions)
        print(tree)

    def test_deleteRateRuleOfAnother_rt_parses_correctly(self):
        print(deleteRateRuleOfAnother_rt)
        tree = self.parser.parse(deleteRateRuleOfAnother_rt)
        print(tree)

    def test_deleteEventAssignment4_rt_parses_correctly(self):
        print(deleteEventAssignment4_rt)
        tree = self.parser.parse(deleteEventAssignment4_rt)
        print(tree)

    def test_deleteEventAssignment_rt_parses_correctly(self):
        print(deleteEventAssignment_rt)
        tree = self.parser.parse(deleteEventAssignment_rt)
        print(tree)

    def test_deleteAssignmentRuleOfAnother_rt_parses_correctly(self):
        print(deleteAssignmentRuleOfAnother_rt)
        tree = self.parser.parse(deleteAssignmentRuleOfAnother_rt)
        print(tree)

    def test_replaceSpecies_rt_parses_correctly(self):
        print(replaceSpecies_rt)
        tree = self.parser.parse(replaceSpecies_rt)
        print(tree)

    def test_deleteSpeciesInDefaultCompartment2_rt_parses_correctly(self):
        print(deleteSpeciesInDefaultCompartment2_rt)
        tree = self.parser.parse(deleteSpeciesInDefaultCompartment2_rt)
        print(tree)

    def test_deleteEventAssignment5_rt_parses_correctly(self):
        print(deleteEventAssignment5_rt)
        tree = self.parser.parse(deleteEventAssignment5_rt)
        print(tree)

    def test_deleteModifier_rt_parses_correctly(self):
        print(deleteModifier_rt)
        tree = self.parser.parse(deleteModifier_rt)
        print(tree)

    def test_fluxes_and_objectives_rt_parses_correctly(self):
        print(fluxes_and_objectives_rt)
        tree = self.parser.parse(fluxes_and_objectives_rt)
        print(tree)

    def test_deletePriority_rt_parses_correctly(self):
        print(deletePriority_rt)
        tree = self.parser.parse(deletePriority_rt)
        print(tree)

    def test_replaceReactionWithKineticLaw_rt_parses_correctly(self):
        print(replaceReactionWithKineticLaw_rt)
        tree = self.parser.parse(replaceReactionWithKineticLaw_rt)
        print(tree)

    def test_deleteSpecies_rt_parses_correctly(self):
        print(deleteSpecies_rt)
        tree = self.parser.parse(deleteSpecies_rt)
        print(tree)

    def test_deleteSpeciesPort_rt_parses_correctly(self):
        print(deleteSpeciesPort_rt)
        tree = self.parser.parse(deleteSpeciesPort_rt)
        print(tree)

    def test_deleteDelay_rt_parses_correctly(self):
        print(deleteDelay_rt)
        tree = self.parser.parse(deleteDelay_rt)
        print(tree)

    def test_deleteKineticLaw_rt_parses_correctly(self):
        print(deleteKineticLaw_rt)
        tree = self.parser.parse(deleteKineticLaw_rt)
        print(tree)

    def test_replaceInteraction_rt_parses_correctly(self):
        print(replaceInteraction_rt)
        tree = self.parser.parse(replaceInteraction_rt)
        print(tree)

    def test_replaceReactionWithCompartments1_rt_parses_correctly(self):
        print(replaceReactionWithCompartments1_rt)
        tree = self.parser.parse(replaceReactionWithCompartments1_rt)
        print(tree)

    def test_deleteProduct_rt_parses_correctly(self):
        print(deleteProduct_rt)
        tree = self.parser.parse(deleteProduct_rt)
        print(tree)

    def test_deleteReactant_rt_parses_correctly(self):
        print(deleteReactant_rt)
        tree = self.parser.parse(deleteReactant_rt)
        print(tree)

    def test_numeric_distributions_extended_parses_correctly(self):
        print(numeric_distributions_extended)
        tree = self.parser.parse(numeric_distributions_extended)
        print(tree)

    def test_deleteModifierKineticLaw_rt_parses_correctly(self):
        print(deleteModifierKineticLaw_rt)
        tree = self.parser.parse(deleteModifierKineticLaw_rt)
        print(tree)

    def test_subsubport_rt_parses_correctly(self):
        print(subsubport_rt)
        tree = self.parser.parse(subsubport_rt)
        print(tree)

    def test_defaultOrNotCompartment_rt_parses_correctly(self):
        print(defaultOrNotCompartment_rt)
        tree = self.parser.parse(defaultOrNotCompartment_rt)
        print(tree)

    def test_replaceReactionWithCompartments2_rt_parses_correctly(self):
        print(replaceReactionWithCompartments2_rt)
        tree = self.parser.parse(replaceReactionWithCompartments2_rt)
        print(tree)

    def test_test45_parses_correctly(self):
        print(test45)
        tree = self.parser.parse(test45)
        print(tree)

    def test_deleteReaction_rt_parses_correctly(self):
        print(deleteReaction_rt)
        tree = self.parser.parse(deleteReaction_rt)
        print(tree)

    def test_deleteTrigger_rt_parses_correctly(self):
        print(deleteTrigger_rt)
        tree = self.parser.parse(deleteTrigger_rt)
        print(tree)

    def test_test24_parses_correctly(self):
        print(test24)
        tree = self.parser.parse(test24)
        print(tree)

    def test_test39_parses_correctly(self):
        print(test39)
        tree = self.parser.parse(test39)
        print(tree)

    def test_test54_parses_correctly(self):
        print(test54)
        tree = self.parser.parse(test54)
        print(tree)

    def test_test27_parses_correctly(self):
        print(test27)
        tree = self.parser.parse(test27)
        print(tree)

    def test_test46_parses_correctly(self):
        print(test46)
        tree = self.parser.parse(test46)
        print(tree)

    def test_deleteEventAssignment2_rt_parses_correctly(self):
        print(deleteEventAssignment2_rt)
        tree = self.parser.parse(deleteEventAssignment2_rt)
        print(tree)

    def test_deleteDelay2_rt_parses_correctly(self):
        print(deleteDelay2_rt)
        tree = self.parser.parse(deleteDelay2_rt)
        print(tree)

    def test_test44_parses_correctly(self):
        print(test44)
        tree = self.parser.parse(test44)
        print(tree)

    def test_deletePriority2_rt_parses_correctly(self):
        print(deletePriority2_rt)
        tree = self.parser.parse(deletePriority2_rt)
        print(tree)

    def test_test58_parses_correctly(self):
        print(test58)
        tree = self.parser.parse(test58)
        print(tree)

    def test_test59_parses_correctly(self):
        print(test59)
        tree = self.parser.parse(test59)
        print(tree)

    def test_test48_parses_correctly(self):
        print(test48)
        tree = self.parser.parse(test48)
        print(tree)

    def test_test47_parses_correctly(self):
        print(test47)
        tree = self.parser.parse(test47)
        print(tree)

    def test_test25_parses_correctly(self):
        print(test25)
        tree = self.parser.parse(test25)
        print(tree)

    def test_exchangetest_parses_correctly(self):
        print(exchangetest)
        tree = self.parser.parse(exchangetest)
        print(tree)

    def test_comp_parses_correctly(self):
        print(comp)
        tree = self.parser.parse(comp)
        print(tree)

    def test_test22_parses_correctly(self):
        print(test22)
        tree = self.parser.parse(test22)
        print(tree)

    def test_test23_parses_correctly(self):
        print(test23)
        tree = self.parser.parse(test23)
        print(tree)

    def test_test28_parses_correctly(self):
        print(test28)
        tree = self.parser.parse(test28)
        print(tree)

    def test_test61_parses_correctly(self):
        print(test61)
        tree = self.parser.parse(test61)
        print(tree)

    def test_replace_rules_and_constraints_parses_correctly(self):
        print(replace_rules_and_constraints)
        tree = self.parser.parse(replace_rules_and_constraints)
        print(tree)

    # def test_CompTest_parses_correctly(self):
    #     print(CompTest)
    #     tree = self.parser.parse(CompTest)
    #     print(tree)
    #
    # def test_QTPop_parses_correctly(self):
    #     print(QTPop)
    #     tree = self.parser.parse(QTPop)
    #     print(tree)




if __name__ == '__main__':
    unittest.main()
