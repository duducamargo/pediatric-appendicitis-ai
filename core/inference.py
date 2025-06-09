from utils.translations import TRANSLATIONS

def mostrar_resultados(resultado):
    """Exibe os resultados de forma formatada"""
    print("\n" + "="*50)
    print("RESULTADOS DO DIAGNÓSTICO".center(50))
    print("="*50)
    
    print(f"\nDiagnóstico: {TRANSLATIONS['Diagnosis'].get(resultado['Diagnóstico'], resultado['Diagnóstico'])}")
    
    if resultado['Diagnóstico'] == 'appendicitis':
        print(f"Severidade: {TRANSLATIONS['Severity'].get(resultado['Severidade'], resultado['Severidade'])}")
        print(f"Tratamento Recomendado: {TRANSLATIONS['Management'].get(resultado['Tratamento Recomendado'], resultado['Tratamento Recomendado'])}")
    
    print("\n" + "="*50 + "\n")