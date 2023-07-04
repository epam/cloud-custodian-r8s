import os
from unittest.mock import patch

import pandas as pd

from commons.constants import ACTION_SCALE_UP
from tests_executor.base_executor_test import BaseExecutorTest
from tests_executor.constants import POINTS_IN_DAY, WEEK_DAYS
from tests_executor.utils import constant_to_series, \
    generate_timestamp_series, generate_constant_metric_series, dateparse


class TestComplexCustomerPreferences(BaseExecutorTest):
    def setUp(self) -> None:
        super().setUp()

        self.instance_id = 'complex_customer_preferences'

        length = POINTS_IN_DAY * 14
        instance_id_series = constant_to_series(
            value=self.instance_id,
            length=length
        )
        instance_type_series = constant_to_series(
            value='t2.medium',
            length=length
        )
        
        timestamp_series = generate_timestamp_series(length=length)
        cpu_load_series = generate_constant_metric_series(
            distribution='normal',
            loc=85,
            scale=1,
            size=length
        )
        memory_load_series = generate_constant_metric_series(
            distribution='normal',
            loc=83,
            scale=0.8,
            size=length
        )
        net_output_load_series = generate_constant_metric_series(
            distribution='normal',
            loc=78,
            scale=0.8,
            size=length
        )
        avg_disk_iops = constant_to_series(-1, length)
        max_disk_iops = constant_to_series(-1, length)
        df_data = {
            'instance_id': instance_id_series,
            'instance_type': instance_type_series,
            'timestamp': timestamp_series,
            'cpu_load': cpu_load_series,
            'memory_load': memory_load_series,
            'net_output_load': net_output_load_series,
            'avg_disk_iops': avg_disk_iops,
            'max_disk_iops': max_disk_iops,
        }
        df = pd.DataFrame(df_data)
        self.metrics_file_path = os.path.join(self.metrics_dir,
                                              f'{self.instance_id}.csv')
        df.to_csv(self.metrics_file_path, sep=',', index=False)
        self.df = pd.read_csv(self.metrics_file_path, parse_dates=True,
                              date_parser=dateparse, index_col='timestamp')
        self.create_plots()
        self.meta = {}

    @patch.dict(os.environ, {'KMP_DUPLICATE_LIB_OK': "TRUE"})
    def test_constant_custom_preferences(self):
        from models.parent_attributes import ParentMeta
        allowed_series = ['c5', 'c6a']
        allowed_shapes = ['c5a.xlarge']
        meta = {
            "algorithm": self.algorithm.name,
            "cloud": "AWS",
            "scope": "ALL_TENANTS",
            "shape_rules": [
                {
                    "rule_id": "any_c6a",
                    "action": "allow",
                    "condition": "match",
                    "field": "name",
                    "value": "c6a.+"
                },
                {
                    "rule_id": "any_c5",
                    "action": "allow",
                    "condition": "match",
                    "field": "name",
                    "value": "c5\..+"
                },
                {
                    "rule_id": "c5a.xlarge",
                    "action": "allow",
                    "condition": "equal",
                    "field": "name",
                    "value": "c5a.xlarge"
                },
                {
                    "rule_id": "non_graviton",
                    "action": "deny",
                    "condition": "contains",
                    "field": "physical_processor",
                    "value": "Graviton"
                },
                {
                    "rule_id": "c6a.2xlarge",
                    "action": "prioritize",
                    "condition": "equal",
                    "field": "name",
                    "value": "c6a.2xlarge"
                }
            ]


        }
        parent_meta = ParentMeta(**meta)
        result = self.recommendation_service.process_instance(
            metric_file_path=self.metrics_file_path,
            algorithm=self.algorithm,
            reports_dir=self.reports_path,
            instance_meta_mapping={self.instance_id: {'profile': 'test'}},
            parent_meta=parent_meta
        )

        self.assertEqual(result.get('instance_id'), self.instance_id)

        schedule = result.get('schedule')

        self.assertEqual(len(schedule), 1)
        schedule_item = schedule[0]

        start = schedule_item.get('start')
        stop = schedule_item.get('stop')

        self.assertEqual(start, '00:00')
        self.assertEqual(stop, '23:50')

        weekdays = schedule_item.get('weekdays')
        self.assertEqual(set(weekdays), set(WEEK_DAYS))

        recommended_shapes = result.get('recommended_shapes')
        instance_types = [i['name'] for i in recommended_shapes]

        self.assertTrue('c5a.xlarge' in instance_types)

        for instance_type in instance_types:
            series = instance_type.split('.')[0]

            self.assertTrue(series in allowed_series
                            or instance_type in allowed_shapes)

        self.assert_stats(result=result)
        self.assert_action(result=result, expected_actions=[ACTION_SCALE_UP])
