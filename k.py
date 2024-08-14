import sounddevice as sd
import numpy as np
import speech_recognition as sr
from scipy.io.wavfile import write

def gravar_audio(duracao, fs=44100):
    print("Gravando...")
    gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=2)
    sd.wait()
    print("Gravação concluída.")
    return gravacao, fs

def salvar_audio(nome_arquivo, gravacao, fs):
    write(nome_arquivo, fs, gravacao)
    print(f"Áudio salvo como {nome_arquivo}")

def transcrever_audio(nome_arquivo):
    reconhecedor = sr.Recognizer()
    
    with sr.AudioFile(nome_arquivo) as source:
        audio = reconhecedor.record(source)
        try:
            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            print("Transcrição:")
            print(texto)
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
        except sr.RequestError:
            print("Erro ao se conectar ao serviço de transcrição.")

def main():
    duracao = int(input("Digite a duração da gravação em segundos: "))
    gravacao, fs = gravar_audio(duracao)
    nome_arquivo = "gravacao.wav"
    salvar_audio(nome_arquivo, gravacao, fs)

    transcrever_audio(nome_arquivo)

if __name__ == "__main__":
    main()
