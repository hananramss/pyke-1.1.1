import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)


def bc_ruleTest():
    engine.reset()  # Allows us to run tests multiple times.
    print("\nPerforming backward chaining proof...\n")

    try:
        # Activate the rule base containing the backward chaining rules
        engine.activate('bc_rules')

        # Prove the goal and print the results
        with engine.prove_goal('bc_rules.invest_on_IBM_stock($advice)') as gen:
            found = False
            for vars, plan in gen:
                print("Advice: %s" % (vars['advice']))  # Retrieving the value of $advice variable
                found = True
            if not found:
                print("Goal not proven.")
    except Exception as e:
        # Print traceback in case of error
        krb_traceback.print_exc()
        sys.exit(1)

    print("\nBackward chaining proof completed.\n")


def bc_questionTest():
    engine.reset()  # Allows us to run tests multiple times.
    print("\nPerforming backward chaining proof...\n")

    try:
        # Activate the rule base containing the backward chaining rules
        engine.activate('bc_rules_questions')

        # Prove the goal and print the results
        with engine.prove_goal('bc_rules_questions.college_education_for_younger_than_30($advice)') as gen:
            found = False
            for vars, plan in gen:
                print("Advice: %s" % (vars['advice']))  # Retrieving the value of $advice variable
                found = True
            if not found:
                print("Goal not proven.")
    except Exception as e:
        # Print traceback in case of error
        krb_traceback.print_exc()
        sys.exit(1)

    print("\nBackward chaining proof completed.\n")
