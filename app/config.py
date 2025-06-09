from pathlib import Path

MODELS_DIR = Path(__file__).parent / 'models'

DIAGNOSIS_MODEL_PATH = MODELS_DIR / 'modeloDiagnosis.pkl'
SEVERITY_MODEL_PATH = MODELS_DIR / 'modeloSeverity.pkl'
MANAGEMENT_MODEL_PATH = MODELS_DIR / 'modeloManagement.pkl'
NORMALIZER_PATH = MODELS_DIR / 'modelo_normalizador_num.pkl'
