# bc_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def invest_on_IBM_stock(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'A', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.invest_on_IBM_stock: got unexpected plan from when clause 1"
            with engine.prove('facts', 'B', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_rules.invest_on_IBM_stock: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def invest_in_growth_stocks(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'D', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.invest_in_growth_stocks: got unexpected plan from when clause 1"
            with engine.prove('facts', 'C', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_rules.invest_in_growth_stocks: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def invest_in_growth_stocks_from_securities(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'B', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.invest_in_growth_stocks_from_securities: got unexpected plan from when clause 1"
            with engine.prove('facts', 'E', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_rules.invest_in_growth_stocks_from_securities: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def college_education_for_younger_than_30(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'B', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.college_education_for_younger_than_30: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def invest_in_IBM_from_growth_stocks(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'F', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_rules.invest_in_IBM_from_growth_stocks: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_rules')
  
  bc_rule.bc_rule('invest_on_IBM_stock', This_rule_base, 'invest_on_IBM_stock',
                  invest_on_IBM_stock, None,
                  (pattern.pattern_literal("Invest in IBM stocks."),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('invest_in_growth_stocks', This_rule_base, 'invest_in_growth_stocks',
                  invest_in_growth_stocks, None,
                  (pattern.pattern_literal("Invest in growth stocks."),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('invest_in_growth_stocks_from_securities', This_rule_base, 'invest_in_growth_stocks_from_securities',
                  invest_in_growth_stocks_from_securities, None,
                  (pattern.pattern_literal("Invest in growth stocks."),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('college_education_for_younger_than_30', This_rule_base, 'college_education_for_younger_than_30',
                  college_education_for_younger_than_30, None,
                  (pattern.pattern_literal("Education at college level."),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('invest_in_IBM_from_growth_stocks', This_rule_base, 'invest_in_IBM_from_growth_stocks',
                  invest_in_IBM_from_growth_stocks, None,
                  (pattern.pattern_literal("Invest in IBM stocks."),),
                  (),
                  (pattern.pattern_literal(True),))


Krb_filename = '..\\bc_rules.krb'
Krb_lineno_map = (
    ((14, 18), (3, 3)),
    ((20, 25), (5, 5)),
    ((26, 31), (6, 6)),
    ((44, 48), (10, 10)),
    ((50, 55), (12, 12)),
    ((56, 61), (13, 13)),
    ((74, 78), (17, 17)),
    ((80, 85), (19, 19)),
    ((86, 91), (20, 20)),
    ((104, 108), (24, 24)),
    ((110, 115), (26, 26)),
    ((128, 132), (30, 30)),
    ((134, 139), (32, 32)),
)
