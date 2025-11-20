# test_evaluate_model.py
import pytest
from evaluation import evaluate_model   # function will be implemented later

def test_perfect_accuracy():
    y_true = [1, 0, 1, 0]
    y_pred = [1, 0, 1, 0]

    result = evaluate_model(y_true, y_pred)

    assert result["accuracy"] == 1.0


def test_f1_zero_when_all_predictions_wrong():
    y_true = [1, 1, 0, 0]
    y_pred = [0, 0, 1, 1]

    result = evaluate_model(y_true, y_pred)

    # all predictions are wrong → precision = 0, recall = 0 → f1 = 0
    assert result["f1_score"] == 0.0


def test_output_contains_required_keys():
    y_true = [1, 0]
    y_pred = [1, 0]

    result = evaluate_model(y_true, y_pred)

    assert "accuracy" in result
    assert "f1_score" in result
