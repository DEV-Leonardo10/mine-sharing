from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

#Definindo classe Handler para monitorar eventos de arquivos
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return None
        else:
            print(f'Arquivo modificado: {event.src_path}')
            
    def on_created(self, event):
        if event.is_directory:
            return None
        else:
            print(f'Arquivo criado: {event.src_path}')
            
    def on_deleted(self, event):
        if event.is_directory:
            return None
        else:
            print(f'Arquivo deletado: {event.src_path}')
            
# Caminho do diretório que você deseja monitorar
appdata_path = os.getenv('APPDATA')  # Obtém o caminho do AppData
save_minecraft = os.path.join(appdata_path, r'.minecraft\saves\FDS DIXA')

if not os.path.exists(save_minecraft):
    print(f"O diretório {save_minecraft} não existe.")
else:
    print(f"Iniciando monitoramento do diretório: {save_minecraft}")
    observer = Observer()
    observer.schedule(MyHandler(), save_minecraft, recursive=False)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Monitoramento interrompido.")
    observer.join()
    print("Monitoramento concluído.")

            
        