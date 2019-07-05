from hyperopt import hp

space0 = {
'learn_rate': hp.uniform('learn_rate', 10e-6, 10e-4),
'size1': hp.quniform('size1', 1, 200, 1),
'size2': hp.quniform('size2', 1, 200, 1),
'size3': hp.quniform('size3', 1, 200, 1),
'size4': hp.quniform('size4', 1, 200, 1),
'size5': hp.quniform('size5', 1, 200, 1),
'size6': hp.quniform('size6', 1, 200, 1),
'size7': hp.quniform('size7', 1, 200, 1),
'act1': hp.choice('act1', ['relu', 'elu', 'tanh']),
'act2': hp.choice('act2', ['relu', 'elu', 'tanh']),
'act3': hp.choice('act3', ['relu', 'elu', 'tanh']),
'act4': hp.choice('act4', ['relu', 'elu', 'tanh']),
'reg_weight': hp.uniform('reg_weight', 0, 1),
'rec_weight': hp.uniform('rec_weight', 0, 1)
}

space1 = {
'learn_rate': hp.uniform('learn_rate', 10e-6, 10e-4),
'size1': hp.quniform('size1', 1, 200, 1),
'size2': hp.quniform('size2', 1, 200, 1),
'size3': hp.quniform('size3', 1, 200, 1),
'size4': hp.quniform('size4', 1, 200, 1),
'size5': hp.quniform('size5', 1, 200, 1),
'act1': hp.choice('act1', ['relu', 'elu', 'tanh']),
'act2': hp.choice('act2', ['relu', 'elu', 'tanh']),
'act3': hp.choice('act3', ['relu', 'elu', 'tanh']),
'act4': hp.choice('act4', ['relu', 'elu', 'tanh']),
'act5': hp.choice('act4', ['relu', 'elu', 'tanh']),
'reg_weight': hp.uniform('reg_weight', 0, 1),
'rec_weight': hp.uniform('rec_weight', 0, 1)
}

parameter_spaces = {'space0': space0, 'space1': space1}
