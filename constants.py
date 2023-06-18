


# From XXXX
NEGATION_WORDS = ["aint", "arent", "cannot", "cant", "couldnt", "darent", "didnt", "doesnt", "ain't", "aren't", "can't",
          "couldn't", "daren't", "didn't", "doesn't", "dont", "hadnt", "hasnt", "havent", "isnt", "mightnt", "mustnt",
          "neither", "don't", "hadn't", "hasn't", "haven't", "isn't", "mightn't", "mustn't", "neednt", "needn't",
          "never", "none", "nope", "nor", "not", "nothing", "nowhere", "oughtnt", "shant", "shouldnt", "wasnt",
          "werent", "oughtn't", "shan't", "shouldn't", "wasn't", "weren't", "without", "wont", "wouldnt", "won't",
          "wouldn't", "rarely", "seldom", "despite", "no", "nobody"]


GT_POSITIVE_MODIFIERS = ['above', 'accelerate', 'accelerated', 'accelerates', 'accelerating', 'accommodate', 'accommodated', 'accommodates', 'accommodating', 'added', 'augment', 'augmented', 'augmenting', 'augments', 'benign', 'best', 'better', 'biggest', 'boost', 'boosted', 'boosting', 'boosts', 'brighter', 'buoy', 'buoyant', 'buoyed', 'buoying', 'buoys', 'calm', 'calmed', 'calming', 'calms', 'climb', 'climbed', 'climbing', 'climbs', 'depreciate', 'depreciated', 'depreciates', 'depreciating', 'dynamic', 'elevate', 'elevated', 'elevates', 'elevating', 'encouraging', 'escalate', 'escalated', 'escalates', 'escalating', 'exceed', 'exceeded', 'exceeding', 'exceeds', 'expand', 'expanded', 'expanding', 'expands', 'expansionary', 'expansive', 'fast', 'faster', 'fastest', 'favorable', 'favourable', 'firmer', 'good', 'great', 'greater', 'greatest', 'grew', 'grow', 'growing', 'grown', 'grows', 'healthier', 'high', 'higher', 'highest', 'improve', 'improved', 'improves', 'improving', 'impulse', 'impulsed', 'impulses', 'impulsing', 'increase', 'increased', 'increases', 'increasing', 'inflationary', 'large', 'larger', 'largest', 'lift', 'lifted', 'lifting', 'lifts', 'loose', 'loosen', 'loosened', 'loosening', 
                         'loosens', 'looser', 'maximum', 'mitigate', 'mitigated', 'mitigates', 'mitigating', 'more', 'mount', 
                         'mounted', 'mounting', 'mounts', 'optimistic', 'outperform', 'outperformed', 'outperforming', 'outperforms', 
                         'peak', 'peaked', 'peaking', 'peaks', 'pick', 'picked', 'picking', 'picks', 'positive', 'raise', 'raised', 'raises', 
                          'raising', 'ramp', 'ramped', 'ramping', 'ramps', 'rapid', 'recover', 'recovered', 'recovering', 'recovers', 'reinforce', 'reinforced', 
                          'reinforces', 'reinforcing', 'restore', 'restored', 'restores', 'restoring', 'rise', 'risen', 'rises', 'rising', 'rose', 'satisfactory', 
                          'skyrocket', 'skyrocketed', 'skyrocketing', 'skyrockets', 'spike', 'spiked', 'spikes', 'spiking', 'spur', 'spurred', 'spurring', 'spurs', 
                          'stabilise', 'stabilised', 'stabilises', 'stabilising', 'stabilize', 'stabilized', 'stabilizes', 'stabilizing', 'stable', 'steady', 'stimulate', 
                          'stimulated', 'stimulates', 'stimulating', 'stimulative', 'stimulatory', 'strengthen', 'strengthened', 'strengthening', 'strengthens', 'strong', 
                          'stronger', 'strongest', 'successful', 'surge', 'surged', 'surges', 'surging', 'swifter', 'upper', 'upside', 'upswing', 'upswinging', 'upswings', 
                          'upswung', 'uptrend', 'upturn', 'upturned', 'upturning', 'upturns', 'upward', 'vigorous', 'widen', 'widened', 'widening', 'widens', 'wider']

GT_NEGATIVE_MODIFIERS = [
    'adverse', 'aggravate', 'aggravated', 'aggravates', 'aggravating', 'appreciate', 'appreciated', 'appreciates', 'appreciating', 'appreciatory', 'bad', 'bottom', 
    'bottomed', 'bottoming', 'bottoms', 'concern', 'concerned', 'concerning', 'concerns', 'conservative', 'constrain', 'constrained', 'constraining', 'constrains', 
    'contract', 'contracted', 'contracting', 'contractionary', 'contracts', 'cut', 'cuts', 'cutting', 'dampen', 'dampened', 'dampening', 'dampens', 'decelerate', 
    'decelerated', 'decelerates', 'decelerating', 'decline', 'declined', 'declines', 'declining', 'decrease', 'decreased', 'decreases', 'decreasing', 'deepen', 
    'deepened', 'deepening', 'deepens', 'deflationary', 'descend', 'descended', 'descending', 'descends', 'destabilizing', 'deteriorate', 'deteriorated', 'deteriorates', 
    'deteriorating', 'difficult', 'diminish', 'diminished', 'diminishes', 'diminishing', 'disappointing', 'disinflationary', 'dovish', 'down', 'downside', 'downsize', 
    'downsized', 'downsizes', 'downsizing', 'downward', 'downwards', 'drop', 'dropped', 'dropping', 'drops', 'erode', 'eroded', 'erodes', 'eroding', 'fade', 'faded', 
    'fades', 'fading', 'fail', 'failed', 'failing', 'fails', 'fall', 'fallen', 'falling', 'falls', 'fell', 'fewer', 'flatten', 'flattened', 'flattening', 'flattens', 
    'fluctuate', 'fluctuated', 'fluctuates', 'fluctuating', 'fragile', 'harm', 'harmed', 'harming', 'harms', 'inconsistent', 'jeopardise', 'jeopardised', 'jeopardises', 
    'jeopardising', 'jeopardize', 'jeopardized', 'jeopardizes', 'jeopardizing', 'lackluster', 'least', 'less', 'low', 'lower', 'lowered', 'lowering', 'lowers', 'lowest', 
    'mild', 'minimal', 'minimum', 'minor', 'moderate', 'moderated', 'moderates', 'moderating', 'modest', 'negative', 'pessimistic', 'poor', 'recessionary', 'reduce', 
    'reduced', 'reduces', 'reducing', 'restrictive', 'riskier', 'risky', 'sank', 'shorten', 'shortened', 'shortening', 'shortens', 'shrink', 'shrinking', 'shrinks', 
    'shrunk', 'shrunken', 'sink', 'sinking', 'slow', 'slowed', 'slower', 'slowest', 'slowing', 'slows', 'sluggish', 'small', 'smaller', 'smallest', 'soften', 'softened', 'softening', 
    'softens', 'speculate', 'speculated', 'speculates', 'speculating', 'stress', 'stressed', 'stresses', 'stressing', 'stringent', 'subdued', 'subprime', 'sunk', 
    'suppress', 'suppressed', 'suppresses', 'suppressing', 'threaten', 'threatened', 'threatening', 'threatens', 'tighten', 'tightened', 'tightening', 'tightens', 'tighter', 
    'tougher', 'turbulent', 'uncertain', 'unclear', 'undermine', 'unfavorable', 'unfavourable', 'unstable', 'volatile', 'vulnerable', 'wane', 'waned', 'wanes', 
    'waning', 'weak', 'weaken', 'weakened', 'weakening', 'weakens', 'weaker', 'weakest', 'worse', 'worsen', 'worsened', 'worsening', 'worsens', 'worst'
]

# From GT(2021)
HAWKISH_SA = ['bank', 'consumption' 'expenditure', 'core inflation', 'country', 'cpix inflation', 'demand', 'development',
               'domestic', 'economy', 'electricity', 'employment', 'environment', 'exchange rate', 'expenditure', 'food',
               'food price', 'forecast', 'global', 'growth', 'inflation', 'inflation expectation', 'inflation outlook',
                'inflation target', 'inflationary pressure', 'mining sector', 'outlook', 'petrol price', 'price', 'rand',
                'recovery', 'upside risk']

DOVISH_SA = []

HAWKISH_NORWAY = ['activity', 'assessment', 'bank', 'consumer price', 'development', 'economy', 'employment', 'euro area', 'expectation', 'growth', 'house price', 
                'inflation', 'inflation report', 'interest rate', 'norway', 'norwegian', 
                 'norwegian economy', 'outlook', 'price', 'project', 'projection', 'wage growth']
DOVISH_NORWAY = ["risk"]

HAWKISH_PERU  = ['credit', 'dollar', 'domestic', 'domestic currency', 'domestic demand', 'economic activity', 'financial system', 'food product', 'foreign currency', 'foreign exchange', 
                 'global economic', 'growth', 'inflation', 'inflation determinant', 
                  'inflation forecast', 'international financial', 'market', 'price', 'recovery', 'supply shock']

DOVISH_PERU   = []

HAWKISH_PHILLIPINES = ["assessment", "growth", "inflation", "inflation outlook", "price"]
DOVISH_PHILLIPINES  = ["pressure", "risk"]

HAWKISH_POLAND  = ['activity', 'demand', 'deposit', 'economic condition', 'economy', 'employment', 'exchange rate', 'growth', 'growth rate', 'household', 'inflation', 'inflation expectation', 'interest', 'loan', 'price', 'price growth', 'production', 'wage']
DOVISH_POLAND   = ["deposit rate"]

HAWKISH_ROMANIA = ['banking system', 'consumer price', 'credit', 'credit institution', 'current account', 'development', 'domestic', 'economic', 'economic growth', 'financial stability', 'foreign currency', 
                   'foreign exchange', 'global economic', 'growth', 'inflation expectation', 'inflation report', 'lending', 'liquidity', 'loan', 'price', 'stability']

DOVISH_ROMANIA  = ["deficit", "disinflation", "risk", "uncertainty"]

HAWKISH_SOUTH_KOREA = ['consumer', 'consumption', 'demand', 'expectation', 'export', 'financial', 'growth', 
                      'housing', 'inflation', 'lending', 'liquidity', 'market', 'oil', 'petroleum', 'price', 
                       'recovery', 'sentiment', 'stock', 'surplus']
DOVISH_SOUTH_KOREA  = ["risk", "slowdown", "uncertainty"]

HAWKISH_SWEDEN      = ['assessment', 'demand', 'development', 'economic activity', 'economic development', 'economy', 'energy price', 
                       'growth', 'inflation', 'inflation report', 'inflationary pressure', 'market', 'price', 'recovery', 
                       'resource utilisation', 'swedish economy']

DOVISH_SWEDEN      = [] 


HAWKISH_THAILAND  = ['recovery', 'economy', 'export', 'policy rate', 'growth', 'expect', 'investment', 'outcome']
DOVISH_THAILAND   = []

HAWKISH_AUS        = ['business', 'businesses','commodity price', 'condition', 'confidence', 'credit', 'demand', 'economic', 'economy',
                      'employment', 'exchange rate', 'expansion', 'expect', 'expected', 'expectation','financial market', 'global',
                      'growth', 'household', 'housing', 'housing market', 'inflation', 'international', 'investment', 'lending', 'market',
                      'pressure', 'price', 'prospect', 'recovery', 'spending', 'stance', 'trade', 'trend', 'wage', 'world']

DOVISH_AUS       = ['risk', 'spare capacity', 'uncertainty']

HAWKISH_BRAZIL   = ['economy', 'economic activity', 'expectation', 'inflation', 
                    'inflation projection', 'inflation prospect', 'inflation trajectory', 
                     'recovery supply', 'total cpi', 'trade']

DOVISH_BRAZIL   = ["disinflation", "monetary easing"]


HAWKISH_CANADA = ['activity', 'anticipate', 'bank', 'condition', 'core inflation', 'demand', 'deposit rate', 
                  'economy', 'global', 'growth', 'inflation', 'price']

DOVISH_CANADA  = []

HAWKISH_CHILE  = ["inflation", "growth", "price"]
DOVISH_CHILE   = []

HAWKISH_HUNGARY = ['activity', 'assessment', 'condition', 'consumer price', 'core inflation', 'cost', 'cost shock', 'councils assessment', 'demand', 'development', 'domestic', 'domestic demand', 'economic agent', 'economic growth', 'economy', 'euro area', 'financial market', 'growth', 'household consumption', 'hungarian economy', 'inflation', 
                   'inflation expectation', 'inflation target', 'inflationary pressure', 'labour market', 'market', 'output', 
                    'price', 'price stability', 'private sector', 'wage']

DOVISH_HUNGARY  = ['disinflationary impact', 'reduction', 'risk', 'slowdown', 'unused capacity']

HAWKISH_ICELAND = ['appreciation', 'banks forecast', 'capital account', 'current account', 'demand', 'domestic demand', 'economic activity', 'economic development', 'economic recovery', 'economy', 'exchange rate', 'foreign currency', 'foreign exchange', 'growth', 'inflation', 'inflation expectation', 'inflation outlook', 
                   'krona', 'labour market', 'market', 'monetary stance', 'output', 'output growth', 'private consumption', 'recovery']
DOVISH_ICELAND  = ['demand pressure', 'disinflation', 'risk', 'slack', 'spare capacity', 'uncertainty']

HAWKISH_INDONESIA = ['banking industry', 'banking system', 'capital adequacy', 'consumption', 'core inflation', 'credit expansion', 'credit growth', 'current account', 'demand', 'development', 'domestic economic', 'economic', 'economic growth', 'economic recovery', 'economy', 'exchange rate', 'financial market', 'financial system', 'foreign capital', 'global economic', 'global economy', 'global financial', 
                     'growth', 'inflation', 'inflation target', 'inflationary pressure', 
                     'inflow', 'investment', 'market', 'price', 'recovery', 'rupiah', 'surplus']

DOVISH_INDONESIA  = ["debt", "import", "risk", "volatile food"]

HAWKISH_ISRAEL   = ['activity', 'government', 'growth', 'inflation', 'interest', 'interest rate', 'market']
DOVISH_ISRAEL    = [] 

HAWKISH_NZL     = ['activity', 'annual cpi', 'bank', 'capacity', 'commodity', 'commodity price', 'confidence', 'construction sector', 'consumption', 'cost', 'demand', 'depreciation', 'dollar', 'economic activity', 'economy', 'employment', 'exchange rate', 'export', 'export commodity', 'export price', 'firm', 'fuel', 'growth', 'headline inflation', 'house price', 'housing', 'housing market', 'income', 'inflation', 'inflation expectation', 'inflation pressure', 'investment', 'market', 'ocr', 'oil', 'pace', 'price', 'rate ocr', 
                  'reconstruction', 'recovery', 'repair', 'resource', 'sentiment', 'spending', 'supply', 'tradables inflation', 'trade', 'upside', 'view']
DOVISH_NZL      = ["import"]


GT_DICTIONARY  = {"hawkish": {"zaf":HAWKISH_SA, "nor": HAWKISH_NORWAY, "per": HAWKISH_PERU, "phl": HAWKISH_PHILLIPINES, "pol": HAWKISH_POLAND,
                              "rou": HAWKISH_ROMANIA, "kor": HAWKISH_SOUTH_KOREA, "swe": HAWKISH_SWEDEN, "tha": HAWKISH_THAILAND, "aus": HAWKISH_AUS,
                              "bra": HAWKISH_BRAZIL, "can": HAWKISH_CANADA, "chl": HAWKISH_CHILE, "hun": HAWKISH_HUNGARY, "isl": HAWKISH_ICELAND,
                              "idn": HAWKISH_INDONESIA, "isr": HAWKISH_ISRAEL, "nzl": HAWKISH_NZL}, 
                 "dovish":   {"zaf":DOVISH_SA, "nor": DOVISH_NORWAY, "per": DOVISH_PERU, "phl": DOVISH_PHILLIPINES, "pol": DOVISH_POLAND,
                              "rou": DOVISH_ROMANIA, "kor": DOVISH_SOUTH_KOREA, "swe": DOVISH_SWEDEN, "tha": DOVISH_THAILAND, "aus": DOVISH_AUS,
                              "bra": DOVISH_BRAZIL, "can": DOVISH_CANADA, "chl": DOVISH_CHILE, "hun": DOVISH_HUNGARY, "isl": DOVISH_ICELAND,
                              "idn": DOVISH_INDONESIA, "isr": DOVISH_ISRAEL, "nzl": DOVISH_NZL}}