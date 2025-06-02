import pandas as pd
import numpy as np
from typing import Tuple
import os


class MLTrainingLogAnalyzer:
    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path
        self.training_data = None
    
    def load_training_logs(self) -> None:
        if not os.path.exists(self.csv_file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {self.csv_file_path}")
        
        self.training_data = pd.read_csv(self.csv_file_path)
        print(f"✅ Dados carregados: {len(self.training_data)} registros")
    
    def is_data_valid(self) -> bool:
        if self.training_data is None:
            print("❌ Dados não carregados")
            return False
        
        required_columns = ['modelo', 'tempo_execucao']
        missing_columns = [col for col in required_columns if col not in self.training_data.columns]
        
        if missing_columns:
            print(f"❌ Colunas obrigatórias ausentes: {missing_columns}")
            return False
        
        if self.training_data['tempo_execucao'].isnull().any():
            print("❌ Valores nulos encontrados na coluna tempo_execucao")
            return False
        
        return True
    
    def get_execution_time_statistics(self) -> Tuple[float, float]:
        if not self.is_data_valid():
            raise ValueError("Dados inválidos para cálculo")
        
        execution_times = self.training_data['tempo_execucao']
        mean_execution_time = np.mean(execution_times)
        standard_deviation = np.std(execution_times, ddof=1)
        
        return mean_execution_time, standard_deviation
    
    def get_fastest_model(self) -> str:
        min_time_index = self.training_data['tempo_execucao'].idxmin()
        return self.training_data.loc[min_time_index, 'modelo']
    
    def get_slowest_model(self) -> str:
        max_time_index = self.training_data['tempo_execucao'].idxmax()
        return self.training_data.loc[max_time_index, 'modelo']
    
    def get_min_execution_time(self) -> int:
        return self.training_data['tempo_execucao'].min()
    
    def get_max_execution_time(self) -> int:
        return self.training_data['tempo_execucao'].max()
    
    def get_execution_time_range(self) -> int:
        return self.get_max_execution_time() - self.get_min_execution_time()
    
    def print_analysis_results(self) -> None:
        mean_time, std_deviation = self.get_execution_time_statistics()
        
        print("\n" + "="*50)
        print("📊 ANÁLISE DE LOGS DE TREINAMENTO ML")
        print("="*50)
        
        print(f"\n📋 Dados carregados:")
        print(self.training_data.to_string(index=False))
        
        print(f"\n📈 Estatísticas dos Tempos de Execução:")
        print(f"   • Média: {mean_time:.2f} segundos")
        print(f"   • Desvio Padrão: {std_deviation:.2f} segundos")
        print(f"   • Número de modelos: {len(self.training_data)}")
        
        print(f"\n🔍 Análise Adicional:")
        print(f"   • Tempo mínimo: {self.get_min_execution_time()} segundos")
        print(f"   • Tempo máximo: {self.get_max_execution_time()} segundos")
        print(f"   • Amplitude: {self.get_execution_time_range()} segundos")
        
        print(f"\n🏆 Modelos Destacados:")
        print(f"   • Mais rápido: {self.get_fastest_model()} ({self.get_min_execution_time()}s)")
        print(f"   • Mais lento: {self.get_slowest_model()} ({self.get_max_execution_time()}s)")


def analyze_ml_training_logs():
    log_file_path = "Pratica7/logs_treinamento.csv"
    
    try:
        analyzer = MLTrainingLogAnalyzer(log_file_path)
        analyzer.load_training_logs()
        analyzer.print_analysis_results()
        
    except Exception as error:
        print(f"❌ Erro na execução: {error}")


if __name__ == "__main__":
    analyze_ml_training_logs()
