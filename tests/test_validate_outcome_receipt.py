import copy
import unittest

from scripts.validate_outcome_receipt import validate_receipt


VALID = {
    "schema_version": 1,
    "receipt_id": "example-2026-08-20-001",
    "recorded_at": "2026-08-20T12:00:00-07:00",
    "source_commit": "0123456789abcdef0123456789abcdef01234567",
    "skill": "measurement-analytics",
    "claim_type": "business-effectiveness",
    "decision": "promote",
    "public_safe": False,
    "change": {
        "hypothesis": "Removing the capacity constraint should increase completed jobs.",
        "intervention": "Fix the constrained funnel stage before buying more demand.",
        "keep_threshold": "Completed profitable jobs rise without worse refunds.",
        "revert_threshold": "Gross profit or customer-quality guardrail declines.",
    },
    "scope": {
        "cohort": "named private pilot",
        "period_start": "2026-07-01",
        "period_end": "2026-07-31",
        "timezone": "America/Los_Angeles",
    },
    "primary_outcome": {
        "metric": "completed_profitable_jobs",
        "tier": "business-outcome",
        "definition": "Completed jobs with positive contribution margin.",
        "source": "CRM and accounting receipt",
        "quality": "verified",
        "baseline": 10,
        "result": 12,
        "attribution_window": "30 days",
        "sample_size": 100,
    },
    "guardrails": [
        {"metric": "refund_rate", "baseline": 0.02, "result": 0.02, "source": "CRM"}
    ],
    "alternative_explanations": ["Seasonality was checked against the prior-year period."],
    "evidence": ["private://receipt/run-001"],
}


class OutcomeReceiptTests(unittest.TestCase):
    def test_verified_business_outcome_can_promote(self):
        self.assertEqual(validate_receipt(VALID), [])

    def test_diagnostic_cannot_promote_business_effectiveness(self):
        receipt = copy.deepcopy(VALID)
        receipt["primary_outcome"]["tier"] = "diagnostic"
        receipt["primary_outcome"]["metric"] = "ranking_position"

        errors = validate_receipt(receipt)

        self.assertTrue(any("diagnostics can propose or canary only" in e for e in errors))

    def test_unverified_result_cannot_promote(self):
        receipt = copy.deepcopy(VALID)
        receipt["primary_outcome"]["quality"] = "estimated"

        errors = validate_receipt(receipt)

        self.assertIn("a promoted change requires a verified primary outcome", errors)

    def test_canary_may_use_a_diagnostic_without_claiming_success(self):
        receipt = copy.deepcopy(VALID)
        receipt["decision"] = "canary"
        receipt["primary_outcome"]["tier"] = "diagnostic"
        receipt["primary_outcome"]["quality"] = "estimated"

        self.assertEqual(validate_receipt(receipt), [])

    def test_missing_guardrail_fails(self):
        receipt = copy.deepcopy(VALID)
        receipt["guardrails"] = []

        errors = validate_receipt(receipt)

        self.assertTrue(any("guardrails" in error for error in errors))

    def test_provenance_fields_must_be_strings(self):
        receipt = copy.deepcopy(VALID)
        receipt["receipt_id"] = 123
        receipt["recorded_at"] = 123
        receipt["source_commit"] = 123
        receipt["skill"] = True

        errors = validate_receipt(receipt)

        self.assertIn("receipt.receipt_id must be a string", errors)
        self.assertIn("receipt.recorded_at must be a string", errors)
        self.assertIn("receipt.source_commit must be a string", errors)
        self.assertIn("receipt.skill must be a string", errors)

    def test_placeholder_evidence_and_numeric_boolean_fail(self):
        receipt = copy.deepcopy(VALID)
        receipt["public_safe"] = 1
        receipt["guardrails"] = [{}]
        receipt["alternative_explanations"] = [""]
        receipt["evidence"] = [""]

        errors = validate_receipt(receipt)

        self.assertIn("receipt.public_safe must be true or false", errors)
        self.assertIn("receipt.guardrails[0].metric is required", errors)
        self.assertIn("receipt.guardrails[0].baseline is required", errors)
        self.assertIn("receipt.guardrails[0].result is required", errors)
        self.assertIn("receipt.guardrails[0].source is required", errors)
        self.assertIn(
            "receipt.alternative_explanations[0] must be a non-empty string", errors
        )
        self.assertIn("receipt.evidence[0] must be a non-empty string", errors)


if __name__ == "__main__":
    unittest.main()
