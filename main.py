import requests, pickle
import webbrowser
import re , stringify
from bs4 import BeautifulSoup
import re
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QInputDialog, QMessageBox)

# # class AnimeMagnetDownloader(QWidget):
# #     def __init__(self):
# #         super().__init__()

# #         # Create the "Add Anime" button
# #         self.add_button = QPushButton("Add Anime")
# #         self.add_button.clicked.connect(self.add_anime)

# #         # Create the "Download" button
# #         self.download_button = QPushButton("Download")
# #         self.download_button.clicked.connect(self.download)

# #         # Create the anime list widget
# #         self.anime_list = QListWidget()

# #         # Create the layout for the main window
# #         layout = QVBoxLayout()
# #         layout.addWidget(self.add_button)
# #         layout.addWidget(self.download_button)
# #         layout.addWidget(self.anime_list)
# #         self.setLayout(layout)

# #         self.setWindowTitle("Anime Magnet Downloader")

# #     def add_anime(self):
# #         # Display an input dialog for the user to enter the name of an anime
# #         anime_name, ok = QInputDialog.getText(self, "Add Anime", "Anime Name:")
# #         if ok:
# #             # Add the anime to the anime list
# #             self.anime_list.addItem(anime_name)

# #     def download(self):
# #         # Get the list of anime to download
# #         anime_list = [self.anime_list.item(i).text() for i in range(self.anime_list.count())]

# #         # Fetch the HTML from animetosho.org
# #         r = requests.get("https://animetosho.org/")
# #         soup = BeautifulSoup(r.text, "html.parser")

# #         # Find the latest episodes
# #         episodes = []
# #         for td in soup.find_all("td"):
# #             # Check if the td element contains an episode link
# #             episode_link = td.find("a", href=True)
# #             if episode_link:
# #                 title = td.text.strip()
# #                 magnet_link = episode_link
# #                 # Check if the episode is an anime episode
# #                 if any(anime in title for anime in anime_list):
# #                     # Check if the episode has [ASW] or [Judas] in the title
# #                     if "[ASW]" in title or "[Judas]" in title:
# #                         # Add the episode to the list
# #                         episodes.append((title, magnet_link["href"]))

# #         # Download the latest episodes
# #         for title, magnet_link in episodes:
# #             print(f"Downloading {title}")
# #             # Add the magnet link to the torrent client
# #             # Replace this with your torrent client's API call to add a magnet link
# #             # client.add_magnet(magnet_link)

# # if __name__ == "__main__":
# #     app = QApplication([])
# #     downloader = AnimeMagnetDownloader()
# #     downloader.show()
# #     app.exec_()

# # 2
# # import requests
# # from bs4 import BeautifulSoup
# # from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
# #                              QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QInputDialog, QMessageBox)

# # class AnimeMagnetDownloader(QWidget):
# #     def __init__(self):
# #         super().__init__()

# #         # Create the "Add Anime" button
# #         self.add_button = QPushButton("Add Anime")
# #         self.add_button.clicked.connect(self.add_anime)

# #         # Create the "Download" button
# #         self.download_button = QPushButton("Download")
# #         self.download_button.clicked.connect(self.download)

# #         # Create the anime list widget
# #         self.anime_list = QListWidget()

# #         # Create the layout for the main window
# #         layout = QVBoxLayout()
# #         layout.addWidget(self.add_button)
# #         layout.addWidget(self.download_button)
# #         layout.addWidget(self.anime_list)
# #         self.setLayout(layout)

# #         self.setWindowTitle("Anime Magnet Downloader")

# #     def add_anime(self):
# #         # Display an input dialog for the user to enter the name of an anime
# #         anime_name, ok = QInputDialog.getText(self, "Add Anime", "Anime Name:")
# #         if ok:
# #             # Add the anime to the anime list
# #             self.anime_list.addItem(anime_name)

# #     def download(self):
# #         # Get the list of anime to download
# #         anime_list = [self.anime_list.item(i).text() for i in range(self.anime_list.count())]

# #         # Fetch the HTML from animetosho.org
# #         r = requests.get("https://animetosho.org/")
# #         soup = BeautifulSoup(r.text, "html.parser")
# #         print(soup)
# #         # Find the latest episodes
# #         episodes = []
# #         for td in soup.find_all("td"):
# #             # Check if the td element contains an episode link
# #             episode_link = td.find("a", href=True)
# #             if episode_link:
# #                 title = td.text.strip()
# #                 magnet_link = episode_link
# #                 # Check if the episode is an anime episode
# #                 if any(anime in title for anime in anime_list):
# #                     # Check if the episode has [ASW] or [Judas] in the title
# #                     if "[ASW]" in title or "[Judas]" in title:
# #                         # Add the episode to the list
# #                         episodes.append((title, magnet_link["href"]))

# #         if len(episodes) == 0:
# #             QMessageBox.information(self, "Anime Magnet Downloader", "No episodes found.")
# #             return

# #         # Download the latest episodes
# #         for title, magnet_link in episodes:
# #             print(f"Downloading {title}")
# #             # Add the magnet link to the torrent client
# #             # Replace this with your torrent client's API call to add a magnet link
# #             # client.add_magnet(magnet_link)

# #         QMessageBox.information(self, "Anime Magnet Downloader", f"{len(episodes)} episode(s) added to the torrent client.")

# # if __name__ == "__main__":
# #     app = QApplication([])
# #     downloader = AnimeMagnetDownloader()
# #     downloader.show()
# #     app.exec_()



# 3 (most complete)
# import requests, pickle
# import webbrowser
# import re , stringify
# from bs4 import BeautifulSoup
# import re
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
#                              QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QInputDialog, QMessageBox)

# class AnimeMagnetDownloader(QWidget):
#     def __init__(self):
#         super().__init__()

#         try:
#             with open("anime_list.pkl", "rb") as f:
#                 self.anime_list = pickle.load(f)
#         except FileNotFoundError:
#             self.anime_list = []

#         # Create the "Add Anime" button
#         self.add_button = QPushButton("Add Anime")
#         self.add_button.clicked.connect(self.add_anime)

#         # Create the "Download" button
#         self.download_button = QPushButton("Download")
#         self.download_button.clicked.connect(self.download)

#         # Create the anime list widget
#         self.anime_list_widget = QListWidget()
#         for anime in self.anime_list:
#             self.anime_list_widget.addItem(anime)

#         # Create the layout for the main window
#         layout = QVBoxLayout()
#         layout.addWidget(self.add_button)
#         layout.addWidget(self.download_button)
#         layout.addWidget(self.anime_list_widget)
#         self.setLayout(layout)

#         self.setWindowTitle("Anime Magnet Downloader")

#     def add_anime(self):
#         # Display an input dialog for the user to enter the name of an anime
#         anime_name, ok = QInputDialog.getText(self, "Add Anime", "Anime Name:")
#         if ok:
#             # Add the anime to the anime list
#             # self.anime_list.addItem(anime_name)
            
#             # Add the anime to the anime list
#             self.anime_list.append(anime_name)
#             self.anime_list_widget.addItem(anime_name)

#             # Save the list of animes to a file
#             with open("anime_list.pkl", "wb") as f:
#                 pickle.dump(self.anime_list, f)

#     def download(self):
#         # Get the list of anime to download
#         anime_list = [self.anime_list.item(i).text() for i in range(self.anime_list.count())]

#         # Fetch the HTML from animetosho.org
#         r = requests.get("https://animetosho.org/")
#         soup = BeautifulSoup(r.text, "html.parser")

#         # Find the latest episodes
#         episodes = []
#         for div in soup.find_all("div", class_="home_list_entry"):
#             # Check if the div element contains an episode link
#             episode_link = div.find("a", text=re.compile("Magnet"))
#             if episode_link:
#                 title = div.text.strip()
#                 magnet_link = episode_link
#                 # Check if the title matches one of the anime in the list
#                 for anime in anime_list:
#                     if re.search(anime, title, re.IGNORECASE):
#                         # Check if the episode has [ASW] or [Judas] in the title
#                         if "[ASW]" in title or "[Anime Time]" in title:
#                             episodes.append((title, magnet_link))
#                             break

#         # Download the episodes
#         if episodes:
#             QMessageBox.information(self, "Download", f"Found {len(episodes)} episodes")
#             # TODO: download the episodes using the magnet links
#             for episode in episodes:
#                 # magnet_link_download = re.sub(r'^<a href="|">Magnet</a>$', '', episode[1])
#                 webbrowser.open_new_tab(episode[1].get('href'))
                
#                 print(episode[1].get('href'))
#         else:
#             QMessageBox.warning(self, "Download", "No episodes found")

# if __name__ == "__main__":
#     app = QApplication([])
#     window = AnimeMagnetDownloader()
#     window.show()
#     app.exec_()

# 4
# import requests
# from bs4 import BeautifulSoup
# import re
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
#                                     QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QInputDialog, QMessageBox)

# class AnimeMagnetDownloader(QWidget):
#     def init(self):
#         super().init()

#         # Create the "Add Anime" button
#         self.add_button = QPushButton("Add Anime")
#         self.add_button.clicked.connect(self.add_anime)

#         # Create the "Download" button
#         self.download_button = QPushButton("Download")
#         self.download_button.clicked.connect(self.download)

#         # Create the anime list widget
#         self.anime_list = QListWidget()

#         # Create the layout for the main window
#         layout = QVBoxLayout()
#         layout.addWidget(self.add_button)
#         layout.addWidget(self.download_button)
#         layout.addWidget(self.anime_list)
#         self.setLayout(layout)

#         self.setWindowTitle("Anime Magnet Downloader")

#     def add_anime(self):
#         # Display an input dialog for the user to enter the name of an anime
#         anime_name, ok = QInputDialog.getText(self,"Add Anime", "Anime Name:")
#         if ok:
#             # Add the anime to the anime list
#             self.anime_list.addItem(anime_name)
                
#     def download(self):
#         # Get the list of anime to download
#         anime_list = [self.anime_list.item(i).text() for i in range(self.anime_list.count())]

#         # Fetch the HTML from animetosho.org
#         r = requests.get("https://animetosho.org/")
#         soup = BeautifulSoup(r.text, "html.parser")

        # # Find the latest episodes
        # episodes = []
        # for div in soup.find_all("div", class_="home_list_entry"):
        #     # Check if the div element contains an episode link
        #     episode_link = div.find("a", text=re.compile("Magnet"))
        #     if episode_link:
        #         title = div.text.strip()
        #         magnet_link = episode_link
        #         # Check if the title matches one of the anime in the list
        #         for anime in anime_list:
        #             if re.search(anime, title, re.IGNORECASE):
        #                 episodes.append((title, magnet_link))
        #                 break

#         # Check if any episodes were found
#         if not episodes:
#             QMessageBox.warning(self, "Error", "No episodes were found.")
#             return

#         # Display a message box showing the number of episodes found
#         message = f"{len(episodes)} episode(s) found.\n\n"
#         message += "\n".join([f"{episode[0]} - {episode[1]}" for episode in episodes])
#         QMessageBox.information(self, "Results", message)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = AnimeMagnetDownloader()
#     window.show()
#     app.exec_()


# episodes = []
# for div in soup.find_all("div", class_="home_list_entry"):
# # Check if the div element contains an episode link
# episode_link = div.find("a", text=re.compile("Magnet"))
# if episode_link:
# title = div.text.strip()
# magnet_link = episode_link
# # Check if the episode is for an anime in the list
# for anime in anime_list:
# if anime in title:
# episodes.append((title, magnet_link))
# break

# Display a message if no episodes were found
# if not episodes:
# QMessageBox.warning(self, "Error", "No episodes were found")
# return

# Ask the user where to save the episodes
# save_folder = QFileDialog.getExistingDirectory(self, "Save Folder")
# if not save_folder:
# return

# Download the episodes
# for title, magnet_link in episodes:
# # Get the file name from the title
# file_name = re.sub(r"[^\w\s]", "", title) + ".torrent"
# file_path = os.path.join(save_folder, file_name)

# Copy code
# # Download the file
# urllib.request.urlretrieve(magnet_link["href"], file_path)


# 5


class AnimeMagnetDownloader(QWidget):
    def __init__(self):
        super().__init__()

        # Load the list of animes and their pages from a file
        try:
            with open("anime_list.pkl", "rb") as f:
                self.anime_list = pickle.load(f)
        except FileNotFoundError:
            self.anime_list = {}

        # Create the "Add Anime" button
        self.add_button = QPushButton("Add Anime")
        self.add_button.clicked.connect(self.add_anime)

        # Create the "Download" button
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download)

        # Create the anime list widget
        self.anime_list_widget = QListWidget()
        for anime in self.anime_list:
            self.anime_list_widget.addItem(anime)

        # Create the layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(self.add_button)
        layout.addWidget(self.download_button)
        layout.addWidget(self.anime_list_widget)
        self.setLayout(layout)

        self.setWindowTitle("Anime Magnet Downloader")


    # def add_anime(self):
    #     # Display an input dialog for the user to enter the name of an anime
    #     anime_name, ok = QInputDialog.getText(self, "Add Anime", "Anime Name:")
    #     if ok:
    #         # Display an input dialog for the user to enter the page number
    #         page, ok = QInputDialog.getInt(self, "Add Anime", "Page:")
    #         if ok:
    #             # Add the anime and page number to the anime list
    #             self.anime_list[anime_name] = page
    #             self.anime_list_widget.addItem(anime_name)
    #             # Save the list of animes to a file
    #             with open("anime_list.pkl", "wb") as f:
    #                 pickle.dump(self.anime_list, f)

    def add_anime(self):
        # Display an input dialog for the user to enter the name of an anime
        anime_name, ok = QInputDialog.getText(self, "Add Anime", "Anime Name:")
        if ok:
            # Add the anime to the anime list
            self.anime_list[anime_name] = ""
            self.anime_list_widget.addItem(anime_name)

            # Display an input dialog for the user to enter the URL of the anime's page
            anime_page, ok = QInputDialog.getText(self, "Add Anime", "Anime Page URL:")
            if ok:
                # Update the anime's page URL in the dictionary
                self.anime_list[anime_name] = anime_page

            # Save the list of animes and their pages to a file
            with open("anime_list.pkl", "wb") as f:
                pickle.dump(self.anime_list, f)



    # def download(self):
    #     # Get the list of anime to download
    #     anime_list = [self.anime_list_widget.item(i).text() for i in range(self.anime_list_widget.count())]
    #     # Fetch the HTML from animetosho.org
    #     r = requests.get("https://animetosho.org/")
    #     soup = BeautifulSoup(r.text, "html.parser")

    #     # Find the latest episodes
    #     episodes = []
    #     for div in soup.find_all("div", class_="home_list_entry"):
    #         # Check if the div element contains an episode link
    #         episode_link = div.find("a", href=True, text=re.compile("Magnet"))
    #         if episode_link:
    #             title = div.text.strip()
    #             magnet_link = episode_link['href']
    #             # Check if the title of the episode contains the name of an anime in the list
    #             for anime in anime_list:
    #                 if anime.lower() in title.lower():
    #                     episodes.append((title, magnet_link))
    #                     break

    #     # Open the magnet links in the default web browser
    #     for episode in episodes:
    #         webbrowser.open_new_tab(episode[1])
    #     if not episodes:
    #         QMessageBox.warning(self, "No Episodes Found", "No episodes were found for the selected anime.")
    # def download(self):
    #     # Get the list of anime and their pages to download
    #     anime_list = self.anime_list
    #     # Fetch the HTML from animetosho.org
    #     r = requests.get("https://animetosho.org/")
    #     soup = BeautifulSoup(r.text, "html.parser")

    #     # Find the latest episodes
    #     episodes = []
    #     for anime, page in anime_list.items():
    #         # Find the home_list_entry divs on the page
    #         divs = soup.find_all("div", class_="home_list_entry", page=page)
    #         for div in divs:
    #             # Check if the div contains an episode link for the current anime
    #             episode_link = div.find("a", string=re.compile(anime), href=True)
    #             if episode_link:
    #                 title = episode_link.text.strip()
    #                 magnet_link = episode_link["href"]
    #                 episodes.append((title, magnet_link))

    #     # Display the episodes in a message box
    #     message = "\n".join(f"{title}: {magnet_link}" for title, magnet_link in episodes)
    #     QMessageBox.information(self, "Episodes", message)

    def download(self):
        # Get the list of anime to download
        anime_list = [self.anime_list_widget.item(i).text() for i in range(self.anime_list_widget.count())]

        # Fetch the HTML from the pages for the anime
        episodes = []
        for anime in anime_list:
            # Get the page for the anime
            page = self.anime_list[anime]
            print(page)
            # Fetch the HTML from the page
            r = requests.get(page)
            soup = BeautifulSoup(r.text, "html.parser")

            # Find the latest episode
            divs = soup.find_all("div", class_="home_list_entry")
            for div in divs:
                # Check if the div contains an episode link for the current anime
                print(anime)
                episode_link = div.find("a", text=re.compile("Magnet"))
                title = div.text.strip()
                print(episode_link)
                # Check if the episode has [ASW] or [Anime Time] in the title
                if "[ASW]" in title: # or "[Anime Time]" in title:
                    if episode_link:
                        title = episode_link.text.strip()
                        magnet_link = episode_link["href"]
                        episodes.append((title, magnet_link))

        # Display the episodes in a message box
        message = "\n".join(f"{title}: {magnet_link}" for title, magnet_link in episodes)
        QMessageBox.information(self, "Episodes", message)
        for episode in episodes:
             webbrowser.open_new_tab(episode[1])



if __name__ == "__main__":
    app = QApplication([])
    window = AnimeMagnetDownloader()
    window.show()
    app.exec_()
