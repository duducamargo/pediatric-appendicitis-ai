import pickle
import sys
from config import *

def carregar_modelos():
    try:
        with open(DIAGNOSIS_MODEL_PATH, 'rb') as f:
            diagnosis = pickle.load(f)
        with open(SEVERITY_MODEL_PATH, 'rb') as f:
            severity = pickle.load(f)
        with open(MANAGEMENT_MODEL_PATH, 'rb') as f:
            management = pickle.load(f)
        with open(NORMALIZER_PATH, 'rb') as f:
            normalizer = pickle.load(f)
        return diagnosis, severity, management, normalizer
    except Exception as e:
        print(f"Erro ao carregar modelos: {e}")
        sys.exit(1)
