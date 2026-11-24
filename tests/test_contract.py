"""输入资料的基线检查。"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from learning_experiment_remediation.input_contract import load_bundle


class BundleContractTest(unittest.TestCase):
    def test_synthetic_bundle_has_required_collections(self):
        bundle = load_bundle(Path(__file__).parents[1] / "data")
        self.assertEqual(bundle["source_info.json"]["source_kind"], "synthetic")
        self.assertIsInstance(bundle["events.json"], list)
        self.assertIsInstance(bundle["entities.json"], list)
        self.assertIsInstance(bundle["observations.json"], list)


if __name__ == "__main__":
    unittest.main()
