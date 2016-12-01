from flowshop.engine.model import Model


def test_load_model_from_conf():
    model = Model()
    assert len(model._layers) == 3
