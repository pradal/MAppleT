
# This file has been generated at Fri Aug 13 09:30:46 2010

from openalea.core import *


__name__ = 'vplants.stocatree.configuration'

__editable__ = True
__description__ = 'stocatree.'
__license__ = 'CECILL-C'
__url__ = 'http://openalea.gforge.inria.fr/doc/openalea/pylab/doc/_build/html/contents.html'
__alias__ = []
__version__ = '0.8.0'
__authors__ = 'Thomas Cokelaer'
__institutes__ = 'INRIA/CIRAD'
__icon__ = 'icon.png'


__all__ = ['stocatree_TreeConfig', 'stocatree_FruitConfig', 'stocatree_WoodConfig', 'stocatree_MarkovConfig', 'stocatree_InternodeConfig', 'stocatree_OutputConfig', 'stocatree_GeneralConfig', 'stocatree_ApexConfig', 'stocatree_LeafConfig', 'stocatree_Config2', 'configuration', 'stocatree_Config', 'configuration2', 'configuration3']



stocatree_TreeConfig = Factory(name='TreeConfig',
                authors='Thomas Cokelaer (wralea authors)',
                description='markov config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='TreeConfig',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




stocatree_FruitConfig = Factory(name='FruitConfig',
                authors='Thomas Cokelaer (wralea authors)',
                description='fruit config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='FruitConfig',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




stocatree_WoodConfig = Factory(name='WoodConfig',
                authors='Thomas Cokelaer (wralea authors)',
                description='markov config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='WoodConfig',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




stocatree_MarkovConfig = Factory(name='MarkovConfig',
                authors='Thomas Cokelaer (wralea authors)',
                description='markov config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='MarkovConfig',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




stocatree_InternodeConfig = Factory(name='InternodeConfig',
                authors='Thomas Cokelaer (wralea authors)',
                description='markov config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='InternodeConfig',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




stocatree_OutputConfig = Factory(name='OutputConfig',
                authors='Thomas Cokelaer (wralea authors)',
                description='markov config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='OutputConfig',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




stocatree_GeneralConfig = Factory(name='GeneralConfig',
                authors='Thomas Cokelaer (wralea authors)',
                description='general config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='GeneralConfig',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




stocatree_ApexConfig = Factory(name='ApexConfig',
                authors='Thomas Cokelaer (wralea authors)',
                description='apex config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='ApexConfig',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




stocatree_LeafConfig = Factory(name='LeafConfig',
                authors='Thomas Cokelaer (wralea authors)',
                description='leaf config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='LeafConfig',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




stocatree_Config2 = Factory(name='Config2',
                authors='Thomas Cokelaer (wralea authors)',
                description='leaf config file.',
                category='Unclassified',
                nodemodule='stocatree',
                nodeclass='Config2',
                inputs=[{'interface': None, 'name': 'IN1', 'value': None, 'desc': ''}, {'interface': None, 'name': 'IN2', 'value': None, 'desc': ''}],
                outputs=[{'interface': None, 'name': 'OUT1', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




configuration = CompositeNodeFactory(name='configuration',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[  {  'desc': '', 'interface': None, 'name': 'IN1', 'value': None},
   {  'desc': '', 'interface': None, 'name': 'IN2', 'value': None}],
                             outputs=[{  'desc': '', 'interface': None, 'name': 'OUT1'}],
                             elt_factory={  2: ('vplants.stocatree.configuration', 'WoodConfig'),
   3: ('vplants.stocatree.configuration', 'Config'),
   4: ('vplants.stocatree.configuration', 'ApexConfig')},
                             elt_connections={  142941696: (4, 0, 3, 0), 142941708: (2, 0, 3, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'WoodConfig',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xa29decc> : "WoodConfig"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -98.0,
         'posy': -143.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'Config',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xa2a91ac> : "Config"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -84.0,
         'posy': 28.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'ApexConfig',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xa29df0c> : "ApexConfig"',
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -143.53658536585368,
         'posy': -115.69918699186992,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [  (0, '1000'),
         (1, '0.10000000000000001'),
         (2, '50000000.0'),
         (3, '0.5'),
         (4, '1.1000000000000001')],
   3: [],
   4: [  (0, '2.0000000000000002e-05'),
         (1, '0.0060000000000000001'),
         (2, '0.00075000000000000002')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-98.0, -143.0], 'useUserColor': False, 'userColor': None},
   3: {  'position': [-84.0, 28.0], 'useUserColor': False, 'userColor': None},
   4: {  'position': [-143.53658536585368, -115.69918699186992],
         'useUserColor': False,
         'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




stocatree_Config = Factory(name='Config',
                authors='Thomas Cokelaer (wralea authors)',
                description='leaf config file.',
                category='visualization, data processing',
                nodemodule='stocatree',
                nodeclass='Config',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




configuration2 = CompositeNodeFactory(name='configuration2',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[  {  'desc': '', 'interface': None, 'name': 'IN1', 'value': None},
   {  'desc': '', 'interface': None, 'name': 'IN2', 'value': None}],
                             outputs=[{  'desc': '', 'interface': None, 'name': 'OUT1'}],
                             elt_factory={  2: ('vplants.stocatree.configuration', 'FruitConfig'),
   3: ('vplants.stocatree.configuration', 'ApexConfig'),
   4: ('vplants.stocatree.configuration', 'Config2')},
                             elt_connections={  154058240: (2, 0, 4, 1), 154058252: (3, 0, 4, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'FruitConfig',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xc5d1aec> : "FruitConfig"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -539.0,
         'posy': -191.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'ApexConfig',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xe2c33cc> : "ApexConfig"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -790.0,
         'posy': -183.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'Config2',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xbdf464c> : "Config2"',
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -761.0,
         'posy': -19.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [  (0, '10.0'),
         (1, '0.16700000000000001'),
         (2, '28'),
         (3, '147'),
         (4, '0.29999999999999999'),
         (5, '0.0018')],
   3: [  (0, '2.0000000000000002e-05'),
         (1, '0.0060000000000000001'),
         (2, '0.00075000000000000002')],
   4: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-539.0, -191.0], 'useUserColor': False, 'userColor': None},
   3: {  'position': [-790.0, -183.0], 'useUserColor': False, 'userColor': None},
   4: {  'position': [-761.0, -19.0], 'useUserColor': False, 'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




configuration3 = CompositeNodeFactory(name='configuration3',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[  {  'desc': '', 'interface': None, 'name': 'IN1', 'value': None},
   {  'desc': '', 'interface': None, 'name': 'IN2', 'value': None}],
                             outputs=[{  'desc': '', 'interface': None, 'name': 'OUT1'}],
                             elt_factory={  2: ('vplants.stocatree.configuration', 'ApexConfig'),
   3: ('vplants.stocatree.configuration', 'FruitConfig'),
   5: ('vplants.stocatree.configuration', 'Config2')},
                             elt_connections={  160181760: (3, 0, 5, 0), 160181772: (2, 0, 5, 1)},
                             elt_data={  2: {  'block': False,
         'caption': 'ApexConfig',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xb2d954c> : "ApexConfig"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -288.0,
         'posy': -197.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'FruitConfig',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xb2d92cc> : "FruitConfig"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -314.0,
         'posy': -303.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'Config2',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xb2d960c> : "Config2"',
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -355.0,
         'posy': -66.0,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [  (0, '2.0000000000000002e-05'),
         (1, '0.0060000000000000001'),
         (2, '0.00075000000000000002')],
   3: [  (0, '10.0'),
         (1, '0.16700000000000001'),
         (2, '28'),
         (3, '147'),
         (4, '0.29999999999999999'),
         (5, '0.0018')],
   5: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [-288.0, -197.0], 'userColor': None, 'useUserColor': False},
   3: {'position': [-314.0, -303.0], 'userColor': None, 'useUserColor': False},
   5: {'position': [-355.0, -66.0], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




