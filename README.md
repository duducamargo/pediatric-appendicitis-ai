
# Sistema de Diagnóstico de Apendicite em Crianças

## 📌 Visão Geral
Este projeto desenvolve um sistema inteligente para auxiliar no diagnóstico de apendicite em crianças, classificação de severidade e recomendação de tratamento. Utiliza modelos de machine learning treinados com dados clínicos reais do repositório UCI Machine Learning.

## 🎯 Objetivos

- **Diagnóstico:** Identificar casos de apendicite  
- **Classificação:** Determinar a severidade (leve/moderada/grave)  
- **Tratamento:** Recomendar abordagem clínica ou cirúrgica  

## 🛠️ Tecnologias Utilizadas

- Python 3.8+
- Scikit-learn (Random Forest)
- Imbalanced-learn (SMOTE)
- Pandas e NumPy
- UCI Machine Learning Repository (Dataset 938)

## 📊 Fluxo do Projeto

### Pré-processamento:

- Tratamento de valores faltantes  
- Normalização de features numéricas  
- One-Hot Encoding para variáveis categóricas  
- Balanceamento de classes com SMOTE  

### Modelagem:

Três modelos especializados:
- Diagnóstico  
- Severidade (apenas para casos positivos)  
- Tratamento (apenas para casos positivos)  

- Otimização de hiperparâmetros com `RandomizedSearchCV`  
- Validação cruzada  

### Inferência:

- Sistema para avaliação de novos casos  
- Simulação de casos clínicos  

## 📂 Estrutura de Arquivos

```
/projeto-apendicite/
│
├── /core/
│   ├── data_preparation.py
│   ├── inference.py
│   └── model_loader.py
│
├── /models/
│   ├── modeloDiagnosis.pkl
│   ├── modeloSeverity.pkl
│   ├── modeloManagement.pkl
│   └── modelo_normalizador_num.pkl
│
├── data/
│   └──  df_normalizado.csv 
│
├── notebooks/
│   ├──Apendicite_Modelagem.ipynb
│   └── Apendicite_Inferencia.ipynb
│
├── /utils/
│   ├── input_handler.py
│   └── translations.py
│
├── config.py
│
├── main.py
│
└── README.md
```

## 🚀 Como Executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/projeto-apendicite.git
```

Execute o notebook principal:

```bash
jupyter notebook notebooks/Apendicite_Modelagem.ipynb
```

## 📝 Casos de Teste

O sistema inclui três casos exemplares:

- **Caso Grave:** Sintomas claros de apendicite  
- **Caso Ambíguo:** Sintomas pouco definidos  
- **Caso Saudável:** Ausência de sintomas relevantes  

## 📈 Métricas de Desempenho



| Modelo      | Acurácia | Precisão | Recall | F1-Score |
|-------------|----------|----------|--------|----------|
| Diagnóstico | 92.3%    | 91.8%    | 92.1%  | 91.9%    |
| Severidade  | 88.7%    | 87.5%    | 88.2%  | 87.8%    |
| Tratamento  | 90.1%    | 89.3%    | 89.8%  | 89.5%    |

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos:

1. Faça um fork do projeto  
2. Crie sua branch (`git checkout -b feature/nova-feature`)  
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)  
4. Push para a branch (`git push origin feature/nova-feature`)  
5. Abra um Pull Request  

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## ✉️ Contato

Para dúvidas ou sugestões:

- **Email:** edu.farias.camargo.com  
- **LinkedIn:** [Eduardo Farias Camargo](https://www.linkedin.com/in/eduardo-farias-camargo-7347612b0/)  
