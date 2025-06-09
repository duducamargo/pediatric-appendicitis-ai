def coletar_dados_paciente():
    """Coleta dados do paciente via input do usuário"""
    print("\n" + "="*50)
    print("DADOS DO PACIENTE".center(50))
    print("="*50 + "\n")
    
    paciente = {}
    
    # Dados demográficos
    paciente['Age'] = input("Idade (anos): ")
    paciente['Sex'] = input("Sexo (masculino/feminino): ")
    paciente['Height'] = input("Altura (cm): ")
    paciente['Weight'] = input("Peso (kg): ")
    
    # Sintomas principais
    print("\nSINTOMAS PRINCIPAIS")
    paciente['Lower_Right_Abd_Pain'] = input("Dor no quadrante inferior direito? (sim/não): ")
    paciente['Migratory_Pain'] = input("Dor migratória? (sim/não): ")
    paciente['Nausea'] = input("Náuseas? (sim/não): ")
    paciente['Loss_of_Appetite'] = input("Perda de apetite? (sim/não): ")
    paciente['Body_Temperature'] = input("Temperatura corporal (°C): ")
    
    # Exames físicos
    print("\nEXAMES FÍSICOS")
    paciente['Contralateral_Rebound_Tenderness'] = input("Dor à descompressão contralateral? (sim/não): ")
    paciente['Ipsilateral_Rebound_Tenderness'] = input("Dor à descompressão ipsilateral? (sim/não): ")
    paciente['Psoas_Sign'] = input("Sinal do psoas positivo? (sim/não): ")
    
    # Exames laboratoriais
    print("\nEXAMES LABORATORIAIS")
    paciente['WBC_Count'] = input("Contagem de leucócitos (WBC): ")
    paciente['Neutrophil_Percentage'] = input("Percentual de neutrófilos (%): ")
    paciente['CRP'] = input("Proteína C Reativa (mg/L): ")
    
    # Exames de imagem
    print("\nEXAMES DE IMAGEM")
    paciente['US_Performed'] = input("Ultrassom foi realizado? (sim/não): ")
    if paciente['US_Performed'].lower() in ['sim', 'yes']:
        paciente['Appendix_on_US'] = input("Apendice visível no US? (sim/não): ")
        paciente['Appendix_Diameter'] = input("Diâmetro do apêndice (mm): ")
        paciente['Free_Fluids'] = input("Líquido livre na cavidade? (sim/não): ")
    else:
        paciente['Appendix_on_US'] = 'não'
        paciente['Appendix_Diameter'] = 0
        paciente['Free_Fluids'] = 'não'
    
    # Outros dados
    print("\nOUTROS DADOS")
    paciente['Ketones_in_Urine'] = input("Cetonas na urina? (sim/não): ")
    paciente['RBC_in_Urine'] = input("Hemácias na urina? (sim/não): ")
    paciente['WBC_in_Urine'] = input("Leucócitos na urina? (sim/não): ")
    paciente['Stool'] = input("Consistência das fezes (normal/pastoso/duro): ")
    paciente['Peritonitis'] = input("Sinais de peritonite? (sim/não): ")
    
    return paciente