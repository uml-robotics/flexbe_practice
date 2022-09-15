#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_practice_states.read_userdata_state import readUserdataState
from flexbe_practice_states.read_write_userdata_state import readWriteUserdataState
from flexbe_practice_states.write_userdata_state import writeUserdataState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Apr 11 2022
@author: Brian Flynn
'''
class UserdataParameterTestSM(Behavior):
	'''
	Testing how states interact with parameters and userdata, and the conditions for which each can/must be used
	'''


	def __init__(self):
		super(UserdataParameterTestSM, self).__init__()
		self.name = 'UserdataParameterTest'

		# parameters of this behavior
		self.add_parameter('starting_value', 2)
		self.add_parameter('log_test', 'The number is now: {}')

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:109 y:484, x:335 y:241
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.my_number = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:63 y:72
			OperatableStateMachine.add('ReadUserdata',
										readUserdataState(text=self.log_test, severity=Logger.REPORT_HINT),
										transitions={'continue': 'WriteUserdata', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_userdata': 'my_number'})

			# x:62 y:261
			OperatableStateMachine.add('ReadUserdata2',
										readUserdataState(text=self.log_test, severity=Logger.REPORT_HINT),
										transitions={'continue': 'ReadWriteUserdata', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_userdata': 'my_number'})

			# x:59 y:356
			OperatableStateMachine.add('ReadWriteUserdata',
										readWriteUserdataState(text=self.log_test, severity=Logger.REPORT_HINT),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_userdata': 'my_number', 'output_userdata': 'my_number'})

			# x:63 y:163
			OperatableStateMachine.add('WriteUserdata',
										writeUserdataState(initial_data=self.starting_value, text=self.log_test, severity=Logger.REPORT_HINT),
										transitions={'continue': 'ReadUserdata2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'output_userdata': 'my_number'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
