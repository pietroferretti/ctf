# 2017.03.03 20:14:03 CET
#Embedded file name: /home/vigna/workspace/ictf-framework/services/ponypoem/src/ponypoem.py
import os
import sys
import random
import pprint
import glob
import crypto
import time
words = ['rigors',
 'messengers',
 'devils',
 'beehives',
 'normalizes',
 'rumpus',
 'recruits',
 'absconds',
 'remodels',
 'urns',
 'springiness',
 'acquires',
 'presides',
 'bulkheads',
 'evenness',
 'sinusoids',
 'drunkards',
 'affairs',
 'beakers',
 'lazarus',
 'chubbiness',
 'moons',
 'divergences',
 'ornaments',
 'offenses',
 'aides',
 'sloppiness',
 'reuses',
 'bosoms',
 'corks',
 'tautologies',
 'dopes',
 'completes',
 'rescuers',
 'vicissitudes',
 'pillows',
 'digits',
 'boats',
 'succeeds',
 'thunders',
 'weds',
 'goddess',
 'raters',
 'toads',
 'certainties',
 'goldenness',
 'distinctness',
 'braves',
 'bankrupts',
 'clogs',
 'diggers',
 'lacks',
 'diggings',
 'ballplayers',
 'tardiness',
 'hobbies',
 'sweets',
 'infuses',
 'raisers',
 'withholdings',
 'fearlessness',
 'bottlenecks',
 'badness',
 'recipients',
 'simplifications',
 'eunuchs',
 'tabulators',
 'mourners',
 'prevents',
 'outlines',
 'fears',
 'accesses',
 'subverts',
 'harmlessness',
 'vignettes',
 'begrudges',
 'succubus',
 'anoints',
 'subscribes',
 'electives',
 'sanctimonious',
 'glues',
 'polaris',
 'warships',
 'exhausts',
 'clusterings',
 'monarchies',
 'infiniteness',
 'additives',
 'fliers',
 'treacheries',
 'blowers',
 'improves',
 'precepts',
 'dyes',
 'arrestors',
 'turbans',
 'cursors',
 'tinniness',
 'nervousness',
 'endures',
 'screamers',
 'fits',
 'upholsters',
 'shooters',
 'privates',
 'crutches',
 'eavesdroppers',
 'stores',
 'repetitious',
 'tumors',
 'anomalous',
 'daylights',
 'resoluteness',
 'deceivers',
 'captures',
 'cherishes',
 'curriculums',
 'inferiors',
 'felicities',
 'bijections',
 'lifetimes',
 'antipodes',
 'timings',
 'minerals',
 'northerners',
 'lordosis',
 'collects',
 'rubs',
 'cantors',
 'manometers',
 'athens',
 'cigars',
 'crucifies',
 'beatings',
 'analogues',
 'macromolecules',
 'shortcomings',
 'cleans',
 'stretches',
 'ludicrousness',
 'outrageous',
 'wagers',
 'taboos',
 'morbidness',
 'cliches',
 'sojourners',
 'sweepers',
 'cringes',
 'clasps',
 'blurs',
 'modalities',
 'axolotls',
 'waves',
 'selfishness',
 'wards',
 'intentions',
 'devotions',
 'biases',
 'audits',
 'centralizes',
 'simpleness',
 'oats',
 'consanguineous',
 'nurseries',
 'funds',
 'servings',
 'articulations',
 'infectious',
 'sympathizes',
 'adores',
 'antiquarians',
 'likenesses',
 'recurs',
 'acropolis',
 'installments',
 'highlands',
 'cans',
 'interferences',
 'wrappers',
 'massages',
 'amanuensis',
 'quiets',
 'seekers',
 'coziness',
 'abstractions',
 'naps',
 'wristwatches',
 'talks',
 'cots',
 'dissimilarities',
 'principals',
 'stewards',
 'lingers',
 'icarus',
 'substances',
 'statues',
 'prohibits',
 'senates',
 'pities',
 'herbivorous',
 'possums',
 'analyzes',
 'cons',
 'geniuses',
 'playfulness',
 'dreams',
 'drops',
 'offers',
 'leakages',
 'steepness',
 'chloroplasts',
 'capes',
 'avows',
 'inns',
 'liberates',
 'respectfulness',
 'motionlessness',
 'toothpicks',
 'beds',
 'astounds',
 'borrows',
 'launches',
 'preparations',
 'ampersands',
 'units',
 'surliness',
 'phelps',
 'strives',
 'interns',
 'praises',
 'jungles',
 'begins',
 'aggressions',
 'stupidities',
 'whiteness',
 'narrows',
 'valets',
 'disperses',
 'artisans',
 'guerrillas',
 'misgivings',
 'comparisons',
 'maps',
 'facades',
 'spongers',
 'embroideries',
 'armaments',
 'wholes',
 'legions',
 'psyches',
 'squirms',
 'boastings',
 'obliqueness',
 'briefcases',
 'prowlers',
 'disjunctions',
 'reduces',
 'convents',
 'scares',
 'treatises',
 'submodules',
 'electrophoresis',
 'cosmos',
 'pros',
 'fractures',
 'buildups',
 'earnings',
 'semiramis',
 'adjusts',
 'rattlesnakes',
 'prepositions',
 'pots',
 'brotherliness',
 'troubles',
 'subtasks',
 'aquinas',
 'nationalists',
 'slippers',
 'concentrates',
 'bumptious',
 'vials',
 'psalms',
 'hostesses',
 'flavors',
 'displacements',
 'rolls',
 'whorls',
 'greatness',
 'microwords',
 'indictments',
 'darkness',
 'reads',
 'lowlands',
 'beers',
 'twisters',
 'restorers',
 'disrupts',
 'enjoins',
 'mugs',
 'chalmers',
 'handicaps',
 'dregs',
 'defines',
 'arbutus',
 'slacks',
 'commodores',
 'reexamines',
 'economizers',
 'reiterates',
 'absolutes',
 'helplessness',
 'instabilities',
 'intertwines',
 'journalizes',
 'bungalows',
 'gratuitous',
 'usefulness',
 'parameterizations',
 'entertainers',
 'lasers',
 'trimness',
 'soles',
 'firearms',
 'harness',
 'prestigious',
 'homogeneous',
 'antelopes',
 'describes',
 'spacers',
 'cusps',
 'handiness',
 'alternations',
 'minicomputers',
 'parrots',
 'backstitches',
 'relentlessness',
 'brochures',
 'overprints',
 'blots',
 'centerpieces',
 'bothers',
 'knights',
 'disastrous',
 'smoothes',
 'hoppers',
 'coasters',
 'sorcerers',
 'conservationists',
 'devotes',
 'venturings',
 'terminologies',
 'attendances',
 'wins',
 'supercilious',
 'longs',
 'clutches',
 'captivates',
 'restores',
 'vaporous',
 'abounds',
 'peeks',
 'firings',
 'ferrous',
 'garrulous',
 'decorations',
 'smuggles',
 'bulls',
 'residues',
 'chasms',
 'juices',
 'recognitions',
 'halvers',
 'discoveries',
 'brokenness',
 'directrices',
 'meningitis',
 'screens',
 'backdrops',
 'melodies',
 'lexicons',
 'deserves',
 'matchers',
 'demands',
 'calculus',
 'fabricates',
 'liveness',
 'citadels',
 'relabels',
 'questionings',
 'yelps',
 'exasperates',
 'mandates',
 'messiness',
 'rabies',
 'microprograms',
 'reuters',
 'referents',
 'randomness',
 'driveways',
 'stews',
 'wavers',
 'testers',
 'sanctuaries',
 'permutes',
 'documentaries',
 'accidents',
 'departs',
 'decliners',
 'delegations',
 'explicitness',
 'deals',
 'detections',
 'socks',
 'veterinarians',
 'wolves',
 'checkbooks',
 'pocketbooks',
 'promenades',
 'effects',
 'compromisers',
 'renames',
 'glasses',
 'affiliates',
 'hocus',
 'highlights',
 'vaults',
 'boyishness',
 'instructors',
 'nationals',
 'decimals',
 'terms',
 'specialists',
 'educators',
 'oranges',
 'blockades',
 'includes',
 'alienates',
 'provers',
 'furrows',
 'quarters',
 'drafters',
 'increments',
 'meats',
 'settlements',
 'brutes',
 'damsels',
 'congregates',
 'wades',
 'breakwaters',
 'screams',
 'packs',
 'europeans',
 'attorneys',
 'voicers',
 'hitchhikes',
 'sicknesses',
 'crews',
 'interpolations',
 'stubbornness',
 'sprinters',
 'armpits',
 'permissions',
 'mosses',
 'fragrances',
 'sentiments',
 'fighters',
 'aeolus',
 'offsets',
 'rights',
 'correlations',
 'islets',
 'suiters',
 'majorities',
 'propositions',
 'bans',
 'pliers',
 'hazes',
 'orbiters',
 'keeps',
 'busts',
 'subsets',
 'slops',
 'gleans',
 'bailiffs',
 'depositions',
 'cherubs',
 'digitalis',
 'contemporaneous',
 'bunnies',
 'bunkmates',
 'gradations',
 'fibrosities',
 'attractions',
 'illnesses',
 'airers',
 'gleanings',
 'barbados',
 'jaws',
 'sleepless',
 'brothels',
 'indoors',
 'procurements',
 'relatives',
 'topics',
 'organs',
 'bedspreads',
 'approximations',
 'contents',
 'brambles',
 'multiples',
 'mates',
 'bimonthlies',
 'nonlinearities',
 'trainees',
 'toughness',
 'hendricks',
 'osseous',
 'progresses',
 'guarantees',
 'thieves',
 'orders',
 'monasteries',
 'hails',
 'repeaters',
 'ares',
 'copes',
 'finds',
 'baptizes',
 'censors',
 'exaggerations',
 'underwriters',
 'genuineness',
 'gelatinous',
 'races',
 'noses',
 'confederations',
 'wits',
 'botches',
 'permits',
 'cassius',
 'balks',
 'ideals',
 'appearers',
 'granaries',
 'inhabits',
 'jeres',
 'cries',
 'spacious',
 'cargoes',
 'pappas',
 'perpetrations',
 'mercenaries',
 'variables',
 'acceptances',
 'rockers',
 'edges',
 'sips',
 'foreheads',
 'predictions',
 'visas',
 'contretemps',
 'displays',
 'silences',
 'endlessness',
 'expertness',
 'smells',
 'erectors',
 'elections',
 'buffoons',
 'gangs',
 'bovines',
 'borderings',
 'jerks',
 'trumps',
 'requisitions',
 'ships',
 'ignominious',
 'maidens',
 'ostriches',
 'pruners',
 'abscess',
 'promotes',
 'dismiss',
 'targets',
 'waives',
 'sorters',
 'shouters',
 'formalizes',
 'interrupts',
 'fuses',
 'beginners',
 'facts',
 'babies',
 'ephemeris',
 'regions',
 'confirmations',
 'northwards',
 'excretions',
 'conveniences',
 'tabulations',
 'blips',
 'giggles',
 'reckons',
 'bakes',
 'enrages',
 'contesters',
 'nests',
 'synthesizes',
 'ethics',
 'embarrasses',
 'caucasus',
 'shatters',
 'scatters',
 'habitations',
 'buyers',
 'earmarkings',
 'alkaloids',
 'haplessness',
 'indirects',
 'sonorous',
 'truthfulness',
 'endangers',
 'recesses',
 'mayors',
 'buffetings',
 'boxcars',
 'empires',
 'schizomycetes',
 'advantages',
 'healthiness',
 'sprints',
 'launders',
 'omissions',
 'schemes',
 'marquess',
 'districts',
 'adaptations',
 'hobbyists',
 'sates',
 'jealousies',
 'truncates',
 'resents',
 'depresses',
 'multiprocessors',
 'intercepts',
 'gustavus',
 'antares',
 'assails',
 'quavers',
 'darlings',
 'sympathies',
 'homomorphisms',
 'prisons',
 'indefiniteness',
 'harpers',
 'uprisings',
 'pyrolysis',
 'cowboys',
 'spareness',
 'heels',
 'adopts',
 'parsers',
 'refutes',
 'suppresses',
 'gambles',
 'natures',
 'pares',
 'consciousness',
 'perkins',
 'articles',
 'allocates',
 'flashes',
 'scorings',
 'trickiness',
 'multiplexes',
 'contractors',
 'eccentrics',
 'aquarius',
 'earthquakes',
 'flavorings',
 'tablets',
 'bartenders',
 'circumlocutions',
 'healers',
 'driers',
 'accelerates',
 'marcus',
 'absoluteness',
 'contradictions',
 'contrives',
 'mumbles',
 'sprinkles',
 'contiguous',
 'scoops',
 'processors',
 'procrastinates',
 'confrontations',
 'parades',
 'foes',
 'validates',
 'obscurities',
 'debates',
 'hierarchies',
 'ascends',
 'ties',
 'strings',
 'reunions',
 'shillings',
 'aristocrats',
 'animates',
 'saturates',
 'softness',
 'reparations',
 'leviticus',
 'dims',
 'buffs',
 'enormous',
 'retentions',
 'auspicious',
 'awfulness',
 'blinds',
 'jets',
 'confounds',
 'affiliations',
 'loftiness',
 'fathers',
 'fictions',
 'psychologists',
 'mets',
 'oaths',
 'influences',
 'confesses',
 'allis',
 'places',
 'delusions',
 'tears',
 'comfortabilities',
 'perpetuates',
 'rusts',
 'ascensions',
 'picturesqueness',
 'facets',
 'subscriptions',
 'gayness',
 'hiss',
 'hams',
 'experiments',
 'perils',
 'oscillators',
 'contemplates',
 'gems',
 'chewers',
 'housewares',
 'iciness',
 'pods',
 'equations',
 'stencils',
 'righteousness',
 'managements',
 'camels',
 'caliphs',
 'concentrators',
 'buzzards',
 'coins',
 'migrates',
 'mindfulness',
 'campaigners',
 'laborers',
 'amusers',
 'stipends',
 'battalions',
 'dangles',
 'conspicuous',
 'headquarters',
 'findings',
 'permeates',
 'wills',
 'sizes',
 'receivers',
 'defends',
 'invades',
 'tightenings',
 'goats',
 'volunteers',
 'kilogauss',
 'backyards',
 'stearns',
 'occurs',
 'contemporariness',
 'hands',
 'shores',
 'individuals',
 'refreshments',
 'housewives',
 'improvements',
 'lips',
 'gases',
 'sensitiveness',
 'copiousness',
 'coupons',
 'cultures',
 'ogress',
 'generosities',
 'reprograms',
 'rebates',
 'expanses',
 'augustus',
 'parsings',
 'fierceness',
 'gallus',
 'catalogues',
 'coats',
 'sweetness',
 'pets',
 'camps',
 'zoos',
 'qualifies',
 'anesthetizes',
 'rugs',
 'supposes',
 'disables',
 'intellects',
 'posers',
 'realities',
 'broods',
 'thanks',
 'simplifies',
 'bunches',
 'correctness',
 'footprints',
 'billiards',
 'routings',
 'ermines',
 'relies',
 'guises',
 'prettiness',
 'intruders',
 'coefficients',
 'combings',
 'flinches',
 'cycles',
 'disgraces',
 'jauntiness',
 'chroniclers',
 'expenditures',
 'salters',
 'bituminous',
 'woos',
 'monograms',
 'tilts',
 'slanders',
 'discards',
 'gratuities',
 'suppleness',
 'confronts',
 'voids',
 'audacious',
 'courthouses',
 'canners',
 'appliers',
 'fasts',
 'extracts',
 'talkers',
 'bogus',
 'friendless',
 'arcades',
 'instants',
 'mantis',
 'effectiveness',
 'addis',
 'dollars',
 'naughtiness',
 'skulls',
 'sneaks',
 'matchings',
 'argus',
 'agonies',
 'imperialists',
 'vicious',
 'legislators',
 'kicks',
 'indebtedness',
 'obviates',
 'servants',
 'hermits',
 'underlines',
 'loquacious',
 'blindness',
 'flocks',
 'courtyards',
 'amends',
 'prows',
 'reconstructs',
 'counts',
 'glens',
 'connotes',
 'babbles',
 'postscripts',
 'tablespoons',
 'urges',
 'aerials',
 'consults',
 'booths',
 'switchings',
 'acclimates',
 'deemphasizes',
 'protrudes',
 'falters',
 'fewness',
 'paychecks',
 'lissajous',
 'dazzles',
 'takes',
 'sacks',
 'relocations',
 'sciences',
 'scribners',
 'cottages',
 'fatalities',
 'destinations',
 'dwarves',
 'branches',
 'ministries',
 'revenues',
 'rivets',
 'tends',
 'accreditations',
 'rosebuds',
 'nuts',
 'exposers',
 'alveolus',
 'interests',
 'coverings',
 'imaginings',
 'fedders',
 'actions',
 'friendliness',
 'depots',
 'precariousness',
 'pompous',
 'legalizes',
 'microscopes',
 'shortens',
 'themselves',
 'tanks',
 'lecturers',
 'brutalizes',
 'nonetheless',
 'significants',
 'electricalness',
 'trackers',
 'rascals',
 'animators',
 'appertains',
 'callus',
 'hepatitis',
 'sawmills',
 'larks',
 'pathogenesis',
 'communicates',
 'cartilaginous',
 'nicholas',
 'troubleshoots',
 'relationships',
 'combines',
 'feels',
 'weeds',
 'ulcers',
 'atlantis',
 'interdependencies',
 'exceptions',
 'incubates',
 'breathers',
 'hovers',
 'curries',
 'pyramids',
 'incubators',
 'courtiers',
 'liquifiers',
 'sobers',
 'boatyards',
 'successions',
 'lionesses',
 'repositions',
 'various',
 'sameness',
 'notorious',
 'sours',
 'distinctions',
 'clays',
 'punts',
 'agreeableness',
 'crumbles',
 'perspectives',
 'draughts',
 'consequents',
 'spellers',
 'drowns',
 'bikes']
debug = True
names = ['ponies',
 'rainbows',
 'unicorns',
 'rabbits',
 'piglets',
 'cubs',
 'hamsters',
 'lambs']
MAXWORDINDEX = len(words) - 1
MINVARS = 2
MAXVARS = 3
MINVARVAL = 0
MAXVARVAL = MAXWORDINDEX
MINVERSES = 3
MAXVERSES = 5
MAXLEVELS = 2
DATAPATH = './'
rules = {'c': '',
 'n': '',
 'm': 'with',
 'a': 'and'}
terminals = ('n', 'c')
operators = ('m', 'a')
relations = {'g': 'are sweeter than',
 's': 'are cuddlier than',
 'e': 'are shiny as'}
openpar = ('my ',
 'your ',
 'their ',
 'our ')
closepar = (':', ',', ';')

def versify(e):
    if e['t'] == 'n':
        verse = e['v']
    elif e['t'] == 'c':
        verse = words[e['v']]
    elif e['t'] in ('m', 'a'):
        s1 = versify(e['o1'])
        s2 = versify(e['o2'])
        verse = '%s%s %s %s%s' % (random.choice(openpar),
         s1,
         rules[e['t']],
         s2,
         random.choice(closepar))
    elif e['t'] in relations.keys():
        s1 = versify(e['o1'])
        s2 = versify(e['o2'])
        verse = '%s %s %s' % (s1, relations[e['t']], s2)
    else:
        print 'Oh my! All these ponies are confusing me!'
        verse = ''
    return verse


def expand(e, my_vars, level):
    if e == None:
        e = dict()
    if level == 0:
        r = random.choice(operators)  # m, a
    elif level > MAXLEVELS:
        r = random.choice(terminals)  # n, c
    else:
        r = random.choice(rules.keys())  # c->'', n->'', m->with, a->and
    e['t'] = r
    if r == 'c':
        e['v'] = random.randint(1, MAXVARVAL)
    elif r == 'n':
        e['v'] = random.choice(my_vars)
    elif r in ('m', 'a'):
        o1 = dict()
        o1['t'] = 'e'
        e['o1'] = expand(o1, my_vars, level + 1)
        o2 = dict()
        o2['t'] = 'e'
        e['o2'] = expand(o2, my_vars, level + 1)
    else:
        print 'A weird unicorn without a horn was just born...'
        return
    return e


def evaluate(e, vals):
    if e['t'] == 'c':
        return e['v']
    if e['t'] == 'n':
        return vals[e['v']]
    if e['t'] in ('m', 'a'):
        v1 = evaluate(e['o1'], vals)
        v2 = evaluate(e['o2'], vals)
        if e['t'] == 'm':
            return v1 - v2
        if e['t'] == 'a':
            return v1 + v2
    else:
        print 'I am terribly sorry, but I see zero teddy bears riding shiny ponies!'


def validate(expressions, vals):
    for e in expressions:
        v1 = evaluate(e['o1'], vals) % MAXVARVAL
        v2 = evaluate(e['o2'], vals) % MAXVARVAL
        if e['t'] == 'e':
            if v1 != v2:
                return False
        elif e['t'] == 'g':
            if v1 <= v2:
                return False
        elif e['t'] == 's':
            if v1 >= v2:
                return False
        else:
            print 'Oh my! I never thing anything like this before! Something is horribly wrong!'
            return False

    return True


def has_variables(e):
    if not e:
        return False
    if e['t'] == 'n':
        return True
    if e.has_key('o1'):
        b1 = has_variables(e['o1'])
    else:
        b1 = False
    if e.has_key('o2'):
        b2 = has_variables(e['o2'])
    else:
        b2 = False
    return b1 or b2


def request_input():
    try:
        answer = raw_input()
    except Exception as e:
        print 'Something went wrong, and all the rainbows disappeared!'
        closing()
        sys.exit(1)

    return answer


def create_poem(title, inspiration, password):
    num_vars = random.randint(MINVARS, MAXVARS)  # 2 or 3
    my_vars = random.sample(names, num_vars)   # prendi 2 o 3 nomi 
    vals = dict()
    characters = None
    for v in my_vars:
        vals[v] = random.randint(MINVARVAL, MAXVARVAL)   # per ogni nome associa un indice in words
        if not characters:
            characters = v
        else:
            characters = '%s,%s' % (characters, v)  # concatena i nomi in characters

    if debug:
        f = open('pp_%s_vals' % title, 'w+')
        f.write(pprint.pformat(vals))
        f.close()
    poem = 'Title: %s\nInspired by: %s\nCharacters: %s\n\n' % (title, inspiration, characters)
    verses = random.randint(MINVERSES, MAXVERSES)   # da 3 a 5
    expressions = list()
    for i in range(verses):
        while True:
            e1 = expand(None, my_vars, 0)  # expand
            if not has_variables(e1):
                continue
            e1_val = evaluate(e1, vals) % MAXVARVAL
            if e1_val > 1 and e1_val < MAXVARVAL:
                break

        e2 = dict()
        e2['t'] = 'c'
        e = dict()
        e['t'] = random.choice(relations.keys())
        if e['t'] == 'e':
            e2['v'] = e1_val
        elif e['t'] == 'g':
            e2['v'] = random.randint(0, e1_val - 1)
        elif e['t'] == 's':
            e2['v'] = random.randint(e1_val + 1, MAXVARVAL)
        e['o1'] = e1
        e['o2'] = e2
        expressions.append(e)
        verse = versify(e)
        print e
        print verse
        poem = '%s%s\n' % (poem, verse)

    print 'This is the beautiful, shiny, bedazzled poem that you asked for:'
    print poem
    sys.stdout.flush()
    num_words = len(vals.keys())
    print '%d words for my magic friends are now required, so that I can complete the spell!' % num_words
    sys.stdout.flush()
    user_vals = dict()
    for v in my_vars:
        print 'Tell me the word associated with %s:' % v
        sys.stdout.flush()
        user_word = request_input()
        user_word = sanitize(user_word)
        if user_word not in words:
            print 'Oh my! I never heard of such word in my unicorn world... This does not work for me!'
            sys.stdout.flush()
            return
        user_vals[v] = words.index(user_word)

    if not validate(expressions, user_vals):
        print "I am sorry but those are not the magic values! It's sad, but you can do so much with unicorn tears..."
        sys.stdout.flush()
        return (poem, password)
    print 'Your magic words are like a rainbow of glitter!'
    sys.stdout.flush()
    print 'Do you want to add a final magic word to your password?'
    sys.stdout.flush()
    answer = request_input()
    if answer[0].lower() == 'y':
        password = ''
        print 'What is the word, my friend?'
        sys.stdout.flush()
        answer = request_input()
        for name in vals.keys():
            password = password + name

        password = password + answer
        #password = sanitize(password)
    else:
        print 'Oh well, the spell is valid anyway!'
        sys.stdout.flush()
    return (poem, password)


def sanitize(s):
    s = s.strip()
    r = ''
    for l in s:
        if l.lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789 ,._()':
            continue
        r += l

    if len(r) > 1023:
        return r[0:1022]

    return r


def closing():
    print "\n                             \\\n                              \\\n                               \\\\\n                                \\\\\n                                 >\\/7\n                             _.-(6'  \\\n                            (=___._/` \\\n                                 )  \\ |\n                                /   / |\n                               /    > /\n                              j    < _\\\n                          _.-' :      ``.\n                          \\ r=._\\        `.\n                         <`\\\\_  \\         .`-.\n                          \\ r-7  `-. ._  ' .  `\\\n                           \\`,      `-.`7  7)   )\n                            \\/         \\|  \\'  / `-._\n                                       ||    .'\n                                        \\\\  (\n                                         >\\  >\n                                     ,.-' >.'\n                                    <.'_.''\n                                      <'\n\n    "
    sys.stdout.flush()
    return 0


def list_poems():
    filenames = glob.glob('pp*')
    poems = list()
    for filename in filenames:
        if filename.endswith('magic'):
            continue
        poems.append(filename[3:])

    if not poems:
        print 'Oh my! There are no sweet poems in my memory!'
        sys.stdout.flush()
    else:
        for poem in poems:
            print poem

    return 0


def main():
    random.seed(time.time())
    print 'Oh, lonely traveler who seeks ponies and raibows, do you want to hear a poem?'
    sys.stdout.flush()
    cmd = request_input()
    if not cmd or cmd[0].lower() != 'y':
        print 'Then, alas, seek elsewhere the motley sweetness you are looking for!'
        sys.stdout.flush()
        closing()
        return 1
    print 'Do you want me to recite to you the sweet titles of all the pony poems?'
    sys.stdout.flush()
    cmd = request_input()
    if cmd[0].lower() == 'y':
        print 'Fantastic! Rainbows! Unicorns! We have everything!!!'
        sys.stdout.flush()
        list_poems()
        sys.stdout.flush()
    print 'What is the title of your ultrasweet poem?'
    sys.stdout.flush()
    title = request_input()
    title = sanitize(title)
    while '_magic' in title:
        title = title.replace('_magic', '')
    print 'What is your magic word, which will open unicorn-filled kingdoms?'
    sys.stdout.flush()
    password = request_input()
    password = sanitize(password)
    if len(password) == 0 or len(title) == 0:
        print 'Your words are not sweet enough for my mini pony!'
        sys.stdout.flush()
        closing()
        return 1
    if not os.path.exists('pp_%s' % title):
        print 'The poem you seek has not yet been brought to existence!'
        print 'I will now create one for you!'
        print 'First give me a line, for inspiration...'
        sys.stdout.flush()
        inspiration = request_input()
        inspiration = sanitize(inspiration)
        res = create_poem(title, inspiration, password)
        if not res:
            print 'I am sorry, a flock of pink lambs interfered, and I cannot save your poem!'
            sys.stdout.flush()
            closing()
            return 1
        poem, password = res
        poem_fd = open('pp_%s_tmp' % title, 'w+')
        poem_fd.write(poem)
        poem_fd.close()
        pass_fd = open('pp_%s_magic' % title, 'w+')
        pass_fd.write(password)
        pass_fd.close()
        data = crypto.encrypt('pp_%s_tmp' % title, password)
        os.remove('pp_%s_tmp' % title)
        if not data:
            print 'I could not magically protect your data! This is bad!'
            sys.stdout.flush()
            closing()
            return 1
        poem_fd = open('pp_%s' % title, 'w+')
        poem_fd.write(data)
        print 'Your sweet, sweet poem is now forever with me, protected by magic words...'
        sys.stdout.flush()
        print data
        sys.stdout.flush()
        print 'You can come back anytime you want and a choir of rainbow pony unicorns will recite it for you!'
        sys.stdout.flush()
        closing()
        return 0
    print 'I see that your poem is already here, ready to be unlocked by your sweet magic words!'
    sys.stdout.flush()
    pass_fd = open('pp_%s_magic' % title, 'r')
    stored_password = pass_fd.read().strip()
    pass_fd.close()
    if stored_password != password:
        print 'Oh my! Your magic is just the wrong magic! No poem for you...'
        sys.stdout.flush()
        closing()
        return 1
    print 'The magic is the right magic and a rainbow just appeared in the sky!'
    sys.stdout.flush()
    poem = crypto.decrypt('pp_%s' % title, password)
    if not poem:
        print 'I could not break the spell that protected your data! This is bad!'
        sys.stdout.flush()
        closing()
        return 1
    print 'Here is your sweet poem, my weary rainbow traveler:'
    sys.stdout.flush()
    print poem
    sys.stdout.flush()
    print '...and this is the end of our magical tour!'
    sys.stdout.flush()
    closing()
    return 0


if __name__ == '__main__':
    main()
