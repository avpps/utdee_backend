from unittest import TestCase
from unittest.mock import mock_open, patch

from git_hooks.utils import env_file_parser, env_files_keys_equal


class TestUtils(TestCase):
    env_file_sample = """

ENV_V_1=env_v_1_value
ENV_V_2=env_v_2_value


ENV_V_3=env_v_3_value

    """

    @patch(
        'builtins.open',
        new=mock_open(read_data=env_file_sample),
        create=True
    )
    def test_env_file_parser(self):
        result = env_file_parser("")
        self.assertEqual(result, {'ENV_V_1': 'env_v_1_value', 'ENV_V_2': 'env_v_2_value', 'ENV_V_3': 'env_v_3_value'})

    def test_env_files_keys_equal(self):
        result = env_files_keys_equal(
            env_file_1={'ENV_V_1': 'env_v_1_value', 'ENV_V_2': 'env_v_2_value', 'ENV_V_3': 'env_v_3_value'},
            env_file_2={'ENV_V_1': 'env_v_1_value', 'ENV_V_2': 'env_v_2_value', 'ENV_V_3': 'env_v_3_value'}
        )
        self.assertTrue(result)

    def test_env_files_keys_equal_negative(self):
        result = env_files_keys_equal(
            env_file_1={'ENV_V_1': 'env_v_1_value', 'ENV_V_2': 'env_v_2_value', 'ENV_V_3': 'env_v_3_value', "NEW": "t"},
            env_file_2={'ENV_V_1': 'env_v_1_value', 'ENV_V_2': 'env_v_2_value', 'ENV_V_3': 'env_v_3_value'}
        )
        self.assertFalse(result)
