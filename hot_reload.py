
import os
import time
import subprocess


def monitorar_e_reiniciar(diretorio, script):
    # Função para obter os arquivos e seus timestamps, incluindo subdiretórios
    def obter_arquivos_com_timestamps(diretorio):
        arquivos_timestamps = {}
        for root, _, files in os.walk(diretorio):
            for arquivo in files:
                caminho_arquivo = os.path.join(root, arquivo)
                arquivos_timestamps[caminho_arquivo] = os.path.getmtime(
                    caminho_arquivo)
        return arquivos_timestamps

    # Obter os timestamps iniciais de todos os arquivos no diretório e subdiretórios
    arquivos_iniciais = obter_arquivos_com_timestamps(diretorio)

    # Inicia o script principal
    processo = subprocess.Popen(["python", script])

    try:
        while True:
            time.sleep(1)  # Aguarda 1 segundo antes de verificar novamente
            arquivos_atualizados = obter_arquivos_com_timestamps(diretorio)

            # Verificar arquivos modificados ou novos
            for caminho_arquivo, timestamp_atual in arquivos_atualizados.items():
                if caminho_arquivo not in arquivos_iniciais or arquivos_iniciais[caminho_arquivo] != timestamp_atual:
                    print(f"Alteração detectada no arquivo: {caminho_arquivo}. Reiniciando {script}...")
                    arquivos_iniciais[caminho_arquivo] = timestamp_atual
                    processo.terminate()  # Encerra o script atual
                    # Reinicia o script principal
                    processo = subprocess.Popen(["python", script])
                    break  # Sai do loop para evitar múltiplas reinicializações simultâneas

            # Verificar se algum arquivo foi removido
            arquivos_removidos = [
                arq for arq in arquivos_iniciais if not os.path.exists(arq)]
            for arquivo in arquivos_removidos:
                print(f"Arquivo removido: {arquivo}")
                del arquivos_iniciais[arquivo]

    except KeyboardInterrupt:
        print("Monitoramento encerrado.")
        processo.terminate()  # Encerra o script ao finalizar o monitoramento


if __name__ == "__main__":
    # Monitorar o diretório atual e reiniciar main.py
    monitorar_e_reiniciar(".", "main.py")
