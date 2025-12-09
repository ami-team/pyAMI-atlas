# -*- coding: utf-8 -*-
from __future__ import (division, print_function, unicode_literals)
#############################################################################
# Author  : Jerome ODIER, Jerome FULACHIER, Fabian LAMBERT, Solveig ALBRAND
#
# Email   : jerome.odier@lpsc.in2p3.fr
#           jerome.fulachier@lpsc.in2p3.fr
#           fabian.lambert@lpsc.in2p3.fr
#           solveig.albrand@lpsc.in2p3.fr
#
# Version : 5.X.X (2014)
#
#############################################################################

import pyAMI.config, pyAMI_atlas.config

#############################################################################

pyAMI.config.version = pyAMI_atlas.config.version

pyAMI.config.bug_report = pyAMI_atlas.config.bug_report

#############################################################################

pyAMI.config.endpoint_descrs['atlas'] = {'prot': 'https', 'host': 'atlas-ami.cern.ch', 'port': '443', 'path': '/AMI2/FrontEnd'}

#############################################################################

pyAMI.config.tables['projects'] = {
	'description': 'description',
	'is_base_type': 'isBaseType',
	'manager': 'createdBy',
	'read_status': 'status=valid',
	'tag': 'project',
	'write_status': 'status',

	'@catalog': 'AMI_TEST',
	'@entity': 'project',

	'@primary': 'tag',
}

pyAMI.config.tables['subprojects'] = {
	'description': 'description',
	'is_base_type': 'isBaseType',
	'manager': 'createdBy',
	'read_status': 'status=valid',
	'tag': 'subProject',
	'write_status': 'status',

	'@catalog': 'AMI_TEST',
	'@entity': 'sub_project',

	'@primary': 'tag',
}

pyAMI.config.tables['types'] = {
	'description': 'description',
	'name': 'dataType',
	'read_status': 'status=valid',
	'write_status': 'status',

	'@catalog': 'AMI_TEST',
	'@entity': 'data_type',

	'@primary': 'name',
}

pyAMI.config.tables['subtypes'] = {
	'description': 'description',
	'name': 'subDataType',
	'read_status': 'status=valid',
	'write_status': 'status',

	'@catalog': 'AMI_TEST',
	'@entity': 'sub_data_type',

	'@primary': 'name',
}

#pyAMI.config.tables['nomenclature'] = {
#	'description': 'nomenclatureName',
#	'read_status': 'readStatus=valid',
#	'tag': 'nomenclatureTag',
#	'template': 'nomenclatureTemplate',
#	'write_status': 'writeStatus',
#
#	'@catalog': 'Atlas_Production:Atlas_Production',
#	'@entity': 'nomenclature',
#
#	'@primary': 'tag, template',
#}

pyAMI.config.tables['prodsteps'] = {
	'name': 'productionStep',
	'read_status': 'status=VALID',
	'write_status': 'status',

	'@catalog': 'AMI_TEST',
	'@entity': 'production_step',

	'@primary': 'name',
}

pyAMI.config.tables['datasets'] = {
    'scope': 'scope',
	'ami_status': 'amiStatus=VALID',
	'atlas_release': 'atlasRelease',
	'beam': 'beamType',
#	'conditions_tag': 'conditionsTag',
#	'completion': 'completion',
	'cross_section': 'crossSection',
	'dataset_number': 'datasetNumber',
	'ecm_energy': 'ecmEnergy',
	'events': 'nEvents',
	'generator_name': 'generatorName',
	'generator_tune': 'generatorTune',
	'generator_filter_efficiency': 'genFiltEff',
#	'geometry': 'geometryVersion',
	'in_container': 'inContainer',
#	'job_config': 'jobConfig',
    'k_factor' : 'kFactor',
	'ldn': 'ldn',
	'modified': 'modified',
	'nfiles': 'nFiles',
#	'period': 'period',
#	'pdf': 'PDF',
#	'physics_comment': 'physicsComment',
	'physics_short': 'physicsShort',
	'production_step': 'productionStep',
	'prodsys_status': 'productionStatus',
	'project': 'scope',
	'requested_by': 'createdBy',
	'responsible': 'responsible',
	'run_number': 'runNumber',
	'stream': 'streamName',
	'total_size': 'size',
#	'transformation_package': 'TransformationPackage',
#	'trash_annotation': 'trashAnnotation',
#	'trash_date': 'trashDate',
#	'trash_trigger': 'trashTrigger',
#	'trigger_config': 'triggerConfig',
	'type': 'dataType',
	'ami_tags': 'version',

    # ATTENTION LOGIQUE A MODIFIER... WILDCARD SUR ENTITY ?
	'@catalog': 'AMI_TEST',
	'@entity': 'g_dataset',

	'@primary': 'ldn',
	'@foreign': 'files',
}

pyAMI.config.tables['files'] = {
    'scope': 'scope',
	'lfn': 'lfn',
	'guid': 'fileGUID',
	'size': 'fileSize',
	'events': 'nEvents',
#	'input_file': 'inputFile',
	'generator_filter_efficiency': 'genFiltEff',
	'cross_section': 'crossSection',
	'neg_weights' : 'sumOfNegWeights',
	'neg_weights-no-filter' : 'sumOfNegWeightsNoFilter',
	'pos_weights' : 'sumOfPosWeights',
	'pos_weights_no_filter' : 'sumOfPosWeightsNoFilter',
	'lhe_neg_weights' : 'lheSumOfNegWeights',
	'lhe_neg_weights_no_filter' : 'lheSumOfNegWeightsNoFilter',
	'sqr_weights' : 'sumOfSqrWeights',
	'sqr_weights_no_filter' : 'sumOfSqrWeightsNoFilter',

	'file_status': 'fileStatus=VALID',

	'@catalog': 'AMI_TEST',

	'@entity': 'file',
	'@primary': 'lfn',
}

#pyAMI.config.tables['keywords'] = {
#
#	'name': 'keyword',
#
#	'@catalog': 'mc[0-9].*|data[0-9].*',
#	'@entity': 'dataset_keywords',
#
#	'@primary': 'name',
#}

#pyAMI.config.tables['hashtags'] = {
#
#	'scope': 'scope',
#	'name': 'name',
#	'fullname': 'fullname',
#	'comment': 'comment',
#
#	'@catalog': 'mc[0-9].*|data[0-9].*',
#	'@entity': 'HASHTAGS',
#
#	'@primary': 'fullname',
#}

#############################################################################
