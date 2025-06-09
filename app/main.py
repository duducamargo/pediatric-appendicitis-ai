from core.model_loader import carregar_modelos
from core.data_preparation import preparar_dados
from core.inference import mostrar_resultados
from utils.input_handler import coletar_dados_paciente

def main():
    """Função principal"""
    print("\n" + "="*50)
    print("SISTEMA DE DIAGNÓSTICO DE APENDICITE".center(50))
    print("="*50)
    
    # Carregar modelos
    print("\nCarregando modelos...")
    diagnosis_model, severity_model, management_model, normalizador = carregar_modelos()
    
    while True:
        try:
            # Coletar dados do paciente
            paciente = coletar_dados_paciente()
            
            # Preparar dados para o modelo
            dados_paciente = preparar_dados(paciente, normalizador, diagnosis_model.feature_names_in_)
            
            # Fazer previsões
            diagnostico = diagnosis_model.predict(dados_paciente)[0]
            
            resultado = {
                'Diagnóstico': diagnostico,
                'Severidade': None,
                'Tratamento Recomendado': None
            }
            
            if diagnostico == 'appendicitis':
                resultado['Severidade'] = severity_model.predict(dados_paciente)[0]
                resultado['Tratamento Recomendado'] = management_model.predict(dados_paciente)[0]
            
            # Mostrar resultados
            mostrar_resultados(resultado)
            
            # Perguntar se deseja avaliar outro paciente
            continuar = input("Deseja avaliar outro paciente? (sim/não): ").lower()
            if continuar not in ['sim', 'yes', 's', 'y']:
                print("\nObrigado por utilizar o sistema!")
                break
                
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"\nErro durante a avaliação: {e}")
            continuar = input("Deseja tentar novamente? (sim/não): ").lower()
            if continuar not in ['sim', 'yes', 's', 'y']:
                break

if __name__ == "__main__":
    main()