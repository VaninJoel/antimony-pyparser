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
        print("")

    def test_assignment_rule_parses_correctly(self):
        self.compare_parsed_tokens(initialValue, "param_init", ["x", "3"])

    def test_initialValue_parses_correctly(self):
        """

        :return:
        """
        self.compare_parsed_tokens(initialValue, "param_init", ["x", "3"])

    def test_parameter_parses_correctly(self):
        self.compare_parsed_tokens(parameter, "param_init", ["a", "3"])

    def test_parameter_inf_parses_correctly(self):
        self.compare_parsed_tokens(parameter_inf, "param_init_inf", ["a"])

    def test_parameter_nan_parses_correctly(self):
        self.compare_parsed_tokens(parameter_nan, "param_init_nan", ["a"])

    def test_compartment_parses_correctly(self):
        self.compare_parsed_tokens(compartment, "compartmentinit", ["x", "y"])

    def test_rxn_right_parses_correctly(self):
        self.compare_parsed_tokens

    def test_initialAssignment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_assignmentRule_parses_correctly(self):
        self.compare_parsed_tokens

    def test_negparen_parses_correctly(self):
        self.compare_parsed_tokens

    def test_non_ascii_parses_correctly(self):
        self.compare_parsed_tokens

    def test_rateRule_parses_correctly(self):
        self.compare_parsed_tokens

    def test_mean_parses_correctly(self):
        self.compare_parsed_tokens

    def test_initialConcentration_parses_correctly(self):
        self.compare_parsed_tokens

    def test_mode_parses_correctly(self):
        self.compare_parsed_tokens

    def test_parameter_neginf_parses_correctly(self):
        self.compare_parsed_tokens

    def test_reaction_parses_correctly(self):
        self.compare_parsed_tokens

    def test_median_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_param_parses_correctly(self):
        self.compare_parsed_tokens

    def test_species_parses_correctly(self):
        self.compare_parsed_tokens

    def test_event_parses_correctly(self):
        self.compare_parsed_tokens

    def test_kurtosis_parses_correctly(self):
        self.compare_parsed_tokens

    def test_skewness_parses_correctly(self):
        self.compare_parsed_tokens

    def test_variance_parses_correctly(self):
        self.compare_parsed_tokens

    def test_reactionIn_parses_correctly(self):
        self.compare_parsed_tokens

    def test_names_parses_correctly(self):
        self.compare_parsed_tokens

    def test_range_parses_correctly(self):
        self.compare_parsed_tokens

    def test_sampleSize_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_flux_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_flux2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_initialAmount_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_flux_neg_parses_correctly(self):
        self.compare_parsed_tokens

    def test_standardError_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_param2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_units_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_species_parses_correctly(self):
        self.compare_parsed_tokens

    def test_interactionActivation_parses_correctly(self):
        self.compare_parsed_tokens

    def test_interactionGeneric_parses_correctly(self):
        self.compare_parsed_tokens

    def test_interactionInhibition_parses_correctly(self):
        self.compare_parsed_tokens

    def test_standardDeviation_parses_correctly(self):
        self.compare_parsed_tokens

    def test_substance_only_species_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_objective_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_objective2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_two_sided_flux_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventT0_parses_correctly(self):
        self.compare_parsed_tokens

    def test_distribution_parses_correctly(self):
        self.compare_parsed_tokens

    def test_encodes_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hasPart_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_compartment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_credibleInterval_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventPriority_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hasTaxon_parses_correctly(self):
        self.compare_parsed_tokens

    def test_identity_parses_correctly(self):
        self.compare_parsed_tokens

    def test_interquartileRange_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isPartOf_parses_correctly(self):
        self.compare_parsed_tokens

    def test_occursIn_parses_correctly(self):
        self.compare_parsed_tokens

    def test_rxn_right_mod_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_reaction_parses_correctly(self):
        self.compare_parsed_tokens

    def test_coefficientOfVariation_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hasVersion_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_localvar_parses_correctly(self):
        self.compare_parsed_tokens

    def test_confidenceInterval_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hasProperty_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isEncodedBy_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isHomologTo_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isVersionOf_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_flux_and_objective_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_flux_and_objective2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isPropertyOf_parses_correctly(self):
        self.compare_parsed_tokens

    def test_compound_units4_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isDescribedBy_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventPersistent_parses_correctly(self):
        self.compare_parsed_tokens

    def test_formula_objective_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_objective4_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_objective5_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventFromTrigger_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_event_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_module_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_objective3_parses_correctly(self):
        self.compare_parsed_tokens

    def test_function_name_parses_correctly(self):
        self.compare_parsed_tokens

    def test_compound_units1_parses_correctly(self):
        self.compare_parsed_tokens

    def test_module_name_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_submodel_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_function_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hierarchy_parses_correctly(self):
        self.compare_parsed_tokens

    def test_compound_units2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_port_parses_correctly(self):
        self.compare_parsed_tokens

    def test_defaultSubCompartment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_flux3_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_flux3_reverse_parses_correctly(self):
        self.compare_parsed_tokens

    def test_compound_units3_parses_correctly(self):
        self.compare_parsed_tokens

    def test_externalParameter2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_externalParameter3_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_module_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deletion_parses_correctly(self):
        self.compare_parsed_tokens

    def test_externalParameter1_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionOnly_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionOnly2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_units_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_function_name_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteAssignmentRuleOfAnother_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteRateRuleOfAnother_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionWithKineticLaw_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_function_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteAssignmentRuleIndirect_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteInitialAssignmentOfAnother_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteRateRuleIndirect_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteInitialAssignmentIndirect_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpeciesInDefaultCompartment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpeciesPortDefaultCompartment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceInitialAssignment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceParameter_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceAssignmentRule_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceRateRule_parses_correctly(self):
        self.compare_parsed_tokens

    def test_compound_units4_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteAssignmentRuleDirect_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteInitialAssignmentDirect_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteKineticLaw_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteRateRuleDirect_parses_correctly(self):
        self.compare_parsed_tokens

    def test_formula_objective2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpecies_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionWithCompartments1_parses_correctly(self):
        self.compare_parsed_tokens

    def test_compound_units1_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteProduct_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteReactant_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpeciesPort_parses_correctly(self):
        self.compare_parsed_tokens

    def test_submodelInteraction_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment3_parses_correctly(self):
        self.compare_parsed_tokens

    def test_defaultSubSubCompartment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionWithKineticLawRxnRef_parses_correctly(self):
        self.compare_parsed_tokens

    def test_three_level_constraints_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceCompartment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceSpeciesDefaultCompartment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_assignmentRule_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpeciesInDefaultCompartment2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment5_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment4_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteTrigger_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionWithCompartments2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_subport_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceSpecies_parses_correctly(self):
        self.compare_parsed_tokens

    def test_initialValue_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_parameter_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceInteraction_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteModifierKineticLaw_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteReaction_parses_correctly(self):
        self.compare_parsed_tokens

    def test_initialAssignment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_parameter_inf_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_parameter_neginf_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_parameter_nan_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_simple_flux_eq_neq_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_submodel_shadowed_parses_correctly(self):
        self.compare_parsed_tokens

    def test_subport2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_compound_units2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_compound_units3_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_initialConcentration_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_defaultOrNotCompartment_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteModifier_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteDelay_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deletePriority_parses_correctly(self):
        self.compare_parsed_tokens

    def test_negparen_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_global_units_parses_correctly(self):
        self.compare_parsed_tokens

    def test_rateRule_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_substance_only_species_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_numeric_constraints_parses_correctly(self):
        self.compare_parsed_tokens

    def test_event_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_param_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_param2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hasPart_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_names_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hasTaxon_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_numeric_constraints_neg_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hasVersion_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isEncodedBy_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isHomologTo_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_species_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventDelay_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventDelay_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hasProperty_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_identity_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isPartOf_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isVersionOf_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_occursIn_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_rxn_right_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_localvar_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_encodes_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventT0_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_mean_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_mode_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_fluxes_and_objectives_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isDescribedBy_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_model1_parses_correctly(self):
        self.compare_parsed_tokens

    def test_median_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_subsubport_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventPriority_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_isPropertyOf_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_module_name_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_skewness_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_variance_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_kurtosis_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_sampleSize_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_submodel_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventPersistent_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_range_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_eventFromTrigger_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_standardError_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_standardDeviation_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_coefficientOfVariation_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_confidenceInterval_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_credibleInterval_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_distribution_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_event_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_reaction_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_rxn_right_mod_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_interquartileRange_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_compartment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_interactionActivation_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_interactionGeneric_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_interactionInhibition_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_compartment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteDelay2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deletePriority2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_global_units_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_species_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_externalParameter2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_externalParameter1_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_externalParameter3_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_initialAmount_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_reaction_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_two_sided_flux_complete_parses_correctly(self):
        self.compare_parsed_tokens

    def test_hierarchy_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_port_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_defaultSubCompartment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_formula_objective_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceSpeciesDefaultCompartment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_formula_objective2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteAssignmentRuleDirect_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceAssignmentRule_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteAssignmentRuleIndirect_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_model2_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deletion_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceParameter_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteInitialAssignmentDirect_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteInitialAssignmentIndirect_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceInitialAssignment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpeciesInDefaultCompartment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_reactionIn_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpeciesPortDefaultCompartment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionOnly2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionOnly_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteInitialAssignmentOfAnother_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteRateRuleDirect_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceRateRule_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteRateRuleIndirect_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_numeric_distributions_rev_parses_correctly(self):
        self.compare_parsed_tokens

    def test_defaultSubSubCompartment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_submodelInteraction_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_subport_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_SBO_submodel_shadowed_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_subport2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionWithKineticLawRxnRef_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceCompartment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_fixname_test_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment3_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_numeric_distributions_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteRateRuleOfAnother_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment4_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteAssignmentRuleOfAnother_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceSpecies_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpeciesInDefaultCompartment2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment5_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteModifier_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_fluxes_and_objectives_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deletePriority_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionWithKineticLaw_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpecies_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteSpeciesPort_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteDelay_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteKineticLaw_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceInteraction_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionWithCompartments1_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteProduct_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteReactant_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_numeric_distributions_extended_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteModifierKineticLaw_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_subsubport_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_defaultOrNotCompartment_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replaceReactionWithCompartments2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test45_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteReaction_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteTrigger_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test24_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test39_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test54_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test27_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test46_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteEventAssignment2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deleteDelay2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test44_parses_correctly(self):
        self.compare_parsed_tokens

    def test_deletePriority2_rt_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test58_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test59_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test48_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test47_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test25_parses_correctly(self):
        self.compare_parsed_tokens

    def test_exchangetest_parses_correctly(self):
        self.compare_parsed_tokens

    def test_comp_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test22_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test23_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test28_parses_correctly(self):
        self.compare_parsed_tokens

    def test_test61_parses_correctly(self):
        self.compare_parsed_tokens

    def test_replace_rules_and_constraints_parses_correctly(self):
        self.compare_parsed_tokens

    def test_CompTest_parses_correctly(self):
        self.compare_parsed_tokens

    def test_QTPop_parses_correctly(self):
        self.compare_parsed_tokens

    # def test_assignment_rule_rt_parses_correctly(self):
    #     input_text = assignmentRule_rt
    #     ass
    #     print(input_text)
    #     tree = self.parser.parse("""x := 3; var x""")
        # for i in tree.find_data("assignment"):
        #     assignment_tokens = i.children
        #     word_token = assignment_tokens[0]
        #     number_token = assignment_tokens[1]
        #     self.assertEqual(word_token, "x")
        #     self.assertEqual(number_token, "4.8")




if __name__ == '__main__':
    unittest.main()
