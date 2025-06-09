import pandas as pd
import sys

def preparar_dados(paciente, normalizador, expected_features):
    """Prepara os dados do paciente para o modelo"""
    # Criar DataFrame com todas features esperadas
    dados_paciente = pd.DataFrame(columns=expected_features)
    
    # Mapeamento de valores
    binary_map = {'sim': 1, 'não': 0, 'yes': 1, 'no': 0}
    sex_map = {'masculino': 1, 'feminino': 0, 'male': 1, 'female': 0}
    
    # Preencher features binárias
    binary_features = [
        'Appendix_on_US', 'Migratory_Pain', 'Lower_Right_Abd_Pain',
        'Nausea', 'Loss_of_Appetite', 'US_Performed', 'Free_Fluids'
    ]
    
    for feature in binary_features:
        if feature in paciente:
            dados_paciente[feature] = binary_map.get(str(paciente[feature]).lower(), 0)
    
    # Preencher features categóricas one-hot
    categorical_features = {
        'Sex': sex_map,
        'Ketones_in_Urine': {'não': 0, 'sim': 1, 'no': 0, 'yes': 1},
        'RBC_in_Urine': {'não': 0, 'sim': 1, 'no': 0, 'yes': 1},
        'WBC_in_Urine': {'não': 0, 'sim': 1, 'no': 0, 'yes': 1},
        'Stool': {'normal': 1, 'pastoso': 0, 'duro': 0, 'normal': 1, 'soft': 0, 'hard': 0},
        'Peritonitis': {'não': 0, 'sim': 1, 'no': 0, 'yes': 1}
    }
    
    for base_feature, mapping in categorical_features.items():
        value = str(paciente.get(base_feature, 'não')).lower()
        for feature in expected_features:
            if feature.startswith(base_feature):
                category = feature.split('_')[-1]
                dados_paciente[feature] = [1 if value == mapping.get(category, 0) else 0]
    
    # Preencher features numéricas
    numerical_features = [
        'Age', 'BMI', 'Height', 'Weight', 'Length_of_Stay', 'Appendix_Diameter',
        'Body_Temperature', 'WBC_Count', 'Neutrophil_Percentage', 'RBC_Count',
        'Hemoglobin', 'RDW', 'Thrombocyte_Count', 'CRP'
    ]
    
    for feature in numerical_features:
        if feature in paciente:
            try:
                dados_paciente[feature] = [float(paciente[feature])]
            except (ValueError, TypeError):
                print(f"Valor inválido para {feature}. Usando valor padrão.")
                dados_paciente[feature] = 0
        else:
            # Valores padrão clinicamente razoáveis
            default_values = {
                'Length_of_Stay': 2,
                'Appendix_Diameter': 7.0,
                'RBC_Count': 4.5,
                'Hemoglobin': 12.0,
                'RDW': 13.0,
                'Thrombocyte_Count': 250,
                'CRP': 5
            }
            dados_paciente[feature] = [default_values.get(feature, 0)]
    
    # Normalizar features numéricas
    try:
        numerical_cols = [col for col in numerical_features if col in normalizador.feature_names_in_]
        dados_paciente[numerical_cols] = normalizador.transform(dados_paciente[numerical_cols])
    except Exception as e:
        print(f"Erro na normalização: {e}")
        sys.exit(1)
    
    # Garantir a ordem correta das colunas
    dados_paciente = dados_paciente[expected_features]
    
    return dados_paciente
    