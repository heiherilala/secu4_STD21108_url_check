import concurrent.futures
import requests
import sys
import os
import threading

# Récupérer un fichier et le transformer en tableau de chaînes de caractères
def read_end_points_file(file_path):
    end_points = []
    with open(file_path, 'r') as file:
        for line in file:
            # Nettoyer les espaces blancs et les sauts de ligne
            end_point = line.strip()
            # Pour chaque ligne du fichier, l'ajouter au tableau de chaînes de caractères
            end_points.append(end_point)
    return end_points

# Vérifier que le code de réponse n'est pas 400..499 , si c'est le cas : l'obtenir et l'imprimer
def check_url(url, accepted_urls, lock):
    try:
        response = requests.get(url)
        thread_number = threading.current_thread().name
        print(f"Essai dans le thread {thread_number}: {url}")
        if response.status_code < 400 or response.status_code > 499:
            with lock:
                accepted_urls.append(url)
    except Exception as e:
        # Exception, si la demande ne fonctionne pas
        print(f"Erreur lors de la vérification de l'URL {url}: {e}")

def main(file_path, num_threads, url_path):
    # Charger les end_points depuis un fichier
    end_points = read_end_points_file(file_path)
    lock = threading.Lock()
    accepted_urls = []

    if num_threads > 0:
        max_threads = min(os.cpu_count(), num_threads)
    else:
        max_threads = os.cpu_count()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(check_url, url_path + "/" + end_point, accepted_urls, lock)
                   for end_point in end_points]

    # Attendre la fin de l'exécution de tous les threads
    for future in concurrent.futures.as_completed(futures):
        pass

    # Imprimer les URLs acceptées
    print("Chemin trouvé :")
    for url in accepted_urls:
        print(url)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Utilisation: python script.py chemin_vers_fichier nombre_de_threads path_url")
        sys.exit(1)
    
    file_path = sys.argv[1]
    num_threads = int(sys.argv[2])
    url_path = sys.argv[3]

    main(file_path, num_threads, url_path)
