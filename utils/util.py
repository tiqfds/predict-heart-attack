import os
from zipfile import ZipFile


def build_project_structure():
    utils_path = "utils/"
    data_ext = "data/external/"
    data_int = "data/interim/"
    data_proc = "data/processed/"
    data_raw = "data/raw/"
    model_path = "models/"
    references_path = "references/"
    reports_path = "reports/figures/"
    test_path = "tests/"
    src_data = "src/data"
    src_features = "src/features"
    src_models = "src/models"
    src_visuals = "src/visualization"

    for _ in [utils_path, data_ext, data_int, data_proc, data_raw, model_path, references_path, reports_path, test_path, src_data, src_features, src_models, src_visuals]:
            if not os.path.exists(_):
                os.makedirs(_)



if __name__ == '__main__':
    build_project_structure()