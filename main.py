import requests, pickle
import webbrowser
import re, stringify
import regex
from bs4 import BeautifulSoup
import re
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QInputDialog, QMessageBox, QListWidgetItem, QDialog , QComboBox, QDialogButtonBox)

from PyQt5.QtCore import pyqtSignal, Qt

class EditAnimeWindow(QDialog):
    anime_edited = pyqtSignal(dict)

    def __init__(self, anime_data):
        super().__init__()

        # Set up the window layout
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Create the widgets for editing the anime data
        self.page_label = QLabel("Page URL:")
        self.page_edit = QLineEdit(anime_data["page"])
        layout.addWidget(self.page_label)
        layout.addWidget(self.page_edit)

        self.tag_label = QLabel("Tag:")
        self.tag_edit = QLineEdit(anime_data["tag"])
        layout.addWidget(self.tag_label)
        layout.addWidget(self.tag_edit)

        self.resolution_label = QLabel("Resolution:")
        self.resolution_combo = QComboBox()
        self.resolution_combo.addItems(["1080p", "720p", "480p"])
        self.resolution_combo.setCurrentText(anime_data["resolution"])
        layout.addWidget(self.resolution_label)
        layout.addWidget(self.resolution_combo)

        self.episodes_label = QLabel("Episodes Downloaded:")
        self.episodes_edit = QLineEdit(str(anime_data.get("episodes_downloaded", "")))
        layout.addWidget(self.episodes_label)
        layout.addWidget(self.episodes_edit)

        # Add buttons to save or cancel the changes
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_changes)
        layout.addWidget(self.save_button)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.reject)
        layout.addWidget(self.cancel_button)

        # Set up the window properties
        self.setWindowTitle("Edit Anime")
        self.setModal(True)

        # Store a reference to the anime data
        self.anime_data = anime_data

    def save_changes(self):
        # Update the anime data with the changes
        self.anime_data["page"] = self.page_edit.text()
        self.anime_data["tag"] = self.tag_edit.text()
        self.anime_data["resolution"] = self.resolution_combo.currentText()
        self.anime_data["episodes_downloaded"] = int(self.episodes_edit.text())

        # Emit a signal to indicate that the anime data has been edited
        self.anime_edited.emit(self.anime_data)
        self.accept()


class AnimeMagnetDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.anime_list_file = "anime_list.pkl"

        # Load the list of animes and their pages from a file
        try:
            with open(self.anime_list_file, "rb") as f:
                self.anime_list = pickle.load(f)
        except FileNotFoundError:
            self.anime_list = {}

        print(self.anime_list)

        # Create the anime list widget
        self.anime_list_widget = QListWidget()

        # Add the anime names and tags to the widget
        for anime_name, data in self.anime_list.items():
            page = data['page']
            tag = data['tag']
            starting_episode = data['episodes_downloaded']
            item_text = f"[{tag}] {anime_name}" # add tag to the item text
            self.anime_list_widget.addItem(item_text)


        # Create the "Add Anime" button
        self.add_button = QPushButton("Add Anime")
        self.add_button.clicked.connect(self.add_anime)

        # Create the "Download" button
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download)

        # Create the "Delete" button
        self.delete_button = QPushButton("Delete Anime")
        self.delete_button.clicked.connect(self.delete_anime)

       

        # Create the layout for the main window
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.download_button)
        button_layout.addWidget(self.delete_button)
        layout = QVBoxLayout()
        layout.addLayout(button_layout)
        layout.addWidget(self.anime_list_widget)
        self.setLayout(layout)

        # Create the "Edit" button
        self.edit_button = QPushButton("Edit")
        self.edit_button.setEnabled(True)
        self.edit_button.clicked.connect(self.edit_anime)
        button_layout.addWidget(self.edit_button)

        # Connect to the accepted signal of the EditAnimeWindow
        # self.edit_dialog = EditAnimeWindow({})
        # self.edit_dialog.accepted.connect(self.reload_anime_list)

        self.setWindowTitle("Anime Magnet Downloader")

    def reload_anime_list(self):
        # Reload the list of animes from the pickle file
        try:
            with open(self.anime_list_file, "rb") as f:
                self.anime_list = pickle.load(f)
        except FileNotFoundError:
            self.anime_list = {}

        # Clear the anime list widget
        self.anime_list_widget.clear()

        # Add the anime names and tags to the widget
        for anime_name, data in self.anime_list.items():
            page = data['page']
            tag = data['tag']
            starting_episode = data['episodes_downloaded']
            item_text = f"[{tag}] {anime_name}" # add tag to the item text
            self.anime_list_widget.addItem(item_text)

    def anime_selected(self):
        # Enable the "Edit" button
        self.edit_button.setEnabled(True)

    def edit_anime(self):
        # Get the selected anime
        try:
            anime_name = self.anime_list_widget.currentItem().text()
        except:
            QMessageBox.warning(self, "No anime selected", "Please select an anime to edit.")
            return

        # Extract the tag from the anime name
        tag_match = re.match(r"\[(.*?)\]", anime_name)
        if tag_match:
            tag = tag_match.group(1)
            # Remove the tag from the anime name
            anime_name = anime_name.replace(f"[{tag}]", "").strip()
        else:
            tag = None

        # # Get the selected anime
        # selected_item = self.anime_list_widget.currentItem()
        # print('selected_item = ' , selected_item)
        # if not selected_item:
        #     return
        # anime_name = selected_item.data(Qt.UserRole)
        # print('anime_name = ' , anime_name )

        # number_match = re.search(r"\((\d+)\)$", anime_name)
        # if number_match:
        #     # Remove the tag from the anime name
        #     anime_name = anime_name.replace(number_match.group(0), "").strip()

        # Get the anime data
        anime_data = self.anime_list[anime_name]
        print('anime_data = ',anime_data)
        
        # Create a new window for editing the anime
        dialog = EditAnimeWindow(anime_data)
        if dialog.exec_() == QDialog.Accepted:
            # Update the anime data with the changes
            self.anime_list[anime_name] = anime_data
            # Save the modified anime data to the pickle file
            self.save_data() 
            # Reload the anime list in the QListWidget
            self.reload_anime_list()


    def save_data(self):
        with open(self.anime_list_file, "wb") as f:
            pickle.dump(self.anime_list, f)

    
    def add_anime(self):
        # Ask the user for the anime name, page, tag, and starting episode number
        anime_name, ok = QInputDialog.getText(self, "Add Anime", "Anime Name:")
        if ok and anime_name:
            anime_page, ok = QInputDialog.getText(self, "Add Anime", "Anime Page:")
            if ok and anime_page:
                anime_tag, ok = QInputDialog.getText(self, "Add Anime", "Anime Tag (optional):")
                if ok:
                    starting_episode, ok = QInputDialog.getInt(self, "Add Anime", "Starting Episode Number:", 1, 1)
                    if ok:
                        resolution_dialog = QDialog(self)
                        resolution_dialog.setWindowTitle("Select Resolution")
                        resolution_dialog_layout = QVBoxLayout(resolution_dialog)
                        resolution_combo = QComboBox(resolution_dialog)
                        resolution_combo.addItem("1080p")
                        resolution_combo.addItem("720p")
                        resolution_combo.addItem("480p")
                        resolution_dialog_layout.addWidget(resolution_combo)
                        resolution_button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, resolution_dialog)
                        resolution_button_box.accepted.connect(resolution_dialog.accept)
                        resolution_button_box.rejected.connect(resolution_dialog.reject)
                        resolution_dialog_layout.addWidget(resolution_button_box)

                        if resolution_dialog.exec_() == QDialog.Accepted:
                            selected_resolution = resolution_combo.currentText()

                            # Add the anime to the list
                            self.anime_list[anime_name] = {
                                "page": anime_page,
                                "tag": anime_tag,
                                "episodes_downloaded": starting_episode - 1,  # subtract 1 to account for 0-indexing
                                "resolution": selected_resolution
                            }

                            # Update the anime list widget
                            self.anime_list_widget.addItem(f"[{anime_tag}] {anime_name}")

                            # Save the updated anime list to the pickle file
                            with open(self.anime_list_file, "wb") as f:
                                pickle.dump(self.anime_list, f)

    # def add_anime(self):
    #     # Ask the user for the anime name, page, tag, and starting episode number
    #     anime_name, ok = QInputDialog.getText(self, "Add Anime", "Anime Name:")
    #     if ok and anime_name:
    #         anime_page, ok = QInputDialog.getText(self, "Add Anime", "Anime Page:")
    #         if ok and anime_page:
    #             anime_tag, ok = QInputDialog.getText(self, "Add Anime", "Anime Tag (optional):")
    #             if ok:
    #                 starting_episode, ok = QInputDialog.getInt(self, "Add Anime", "Starting Episode Number:", 1, 1)
    #                 if ok:
    #                     anime_resolution, ok = QInputDialog.getText(self, "Add Anime", "Resolution:")
    #                     if ok:
    #                         # Add the anime to the list
    #                         self.anime_list[anime_name] = {
    #                             "page": anime_page,
    #                             "tag": anime_tag,
    #                             "episodes_downloaded": starting_episode - 1,  # subtract 1 to account for 0-indexing
    #                             "resolution": anime_resolution
    #                         }

    #                         # Update the anime list widget
    #                         self.anime_list_widget.addItem(f"[{anime_tag}] {anime_name}")

    #                         # Save the updated anime list to the pickle file
    #                         with open(self.anime_list_file, "wb") as f:
    #                             pickle.dump(self.anime_list, f)


    def delete_anime(self):
        # Get the name of the anime to delete
        anime_name = self.anime_list_widget.currentItem().text()
        
        # Extract the tag from the anime name
        tag_match = re.match(r"\[(.*?)\]", anime_name)
        if tag_match:
            tag = tag_match.group(1)
            # Remove the tag from the anime name
            anime_name = anime_name.replace(f"[{tag}]", "").strip()
        else:
            tag = None

        # Confirm the deletion with the user
        message = f"Are you sure you want to delete {anime_name}?"
        reply = QMessageBox.question(self, "Delete Anime", message, QMessageBox.Yes, QMessageBox.No)

        # Delete the anime if the user confirms the deletion
        if reply == QMessageBox.Yes:
            # Remove the anime from the anime list
            if anime_name in self.anime_list:
                del self.anime_list[anime_name]
            else:
                # If the anime name with tag not found, try searching for the modified anime name without the tag
                for key in self.anime_list:
                    if anime_name == key.replace(f"[{tag}]", "").strip():
                        del self.anime_list[key]
                        break
                    
            # Remove the anime from the anime list widget
            self.anime_list_widget.takeItem(self.anime_list_widget.currentRow())

            # Save the updated anime list
            with open(self.anime_list_file, "wb") as f:
                pickle.dump(self.anime_list, f)


    def download(self):
        # Get the list of anime to download
        anime_list = [re.sub(r"\[[^\]]*\]", "", self.anime_list_widget.item(i).text()).strip() for i in range(self.anime_list_widget.count())]

        # Fetch the HTML from the pages for the anime
        for anime in anime_list:
            # Get the page for the anime
            episodes = []
            anime_data = self.anime_list[anime]
            page = anime_data["page"]
            tag = anime_data["tag"]
            episodes_downloaded = anime_data["episodes_downloaded"]
            resolution = anime_data["resolution"]
            last_episode = episodes_downloaded
            page_number = 1  # Add this line
            last_episode_found = False

            print('Checking Anime: ' , anime , resolution)
            

            # Keep fetching the next page as long as none of the episodes found are equal to episodes_downloaded
            while True:
                # Fetch the HTML from the page
                r = requests.get(f"{page}?page={page_number}")  # Modify the URL for the page by adding ?page=<page_number>
                soup = BeautifulSoup(r.text, "html.parser")

                # Find the latest episode
                divs = soup.find_all("div", class_="home_list_entry")
                for div in divs:
                    # Check if the div contains an episode link for the current anime
                    episode_link = div.find("a", text=re.compile("Magnet"))
                    title = div.text.strip()
                    # print('Checking for tag of: ' , title)
                    
                    # Check if the episode has fansub tag in the title
                    if tag not in title:
                        continue
                    
                    # print('Checking for Res of: ' , title)
                    # Check if the episode has a resolution tag in the title
                    if resolution not in title:
                        continue
                    # print('Beggining of regex of: ', title)
                    mod_title = title.replace("●NyaaWebsiteTorrent/Magnet", "")
                    # mod_title = title.replace("NZB | ClickNUpload | DownloadGG | GoFile | KrakenFiles | MdiaLoad | MultiUp", "")
                    # mod_title = mod_title[13:]
                    mod_title = re.sub(r"\[ENG\]\[POR-BR\]\[SPA-LA\]\[SPA\]\[ARA\]\[FRE\]\[GER\]\[ITA\]\[RUS\]", "", mod_title)
                    # print('=====now edited: ', mod_title)
                    # Extract the episode number from the title using regular expressions
                    try:
                        # match = re.search(r"\[.*?\]\s*(?:.*?\s*-\s*)?" + anime.replace(".", r"\.") + r"(?:\s*\[.*?\])*\s*-?\s*(?:\[[^\]]*\]\s*){0,2}(?:\([^\)]*\)\s*){0,2}(?:\S+\s*){0,10}(\d{2,})(?=[\s-])(?![^\[]*\])(?![^\(]*\))", title)
                        match = regex.search(r"\[.*?\]\s*(?:.*?\s*-\s*)?" + anime.replace(".", r"\.") + r"(?:\s*\[.*?\])*\s*-?\s*(?:\[[^\]]*\]\s*){0,2}(?:\([^\)]*\)\s*){0,2}(?:\S+\s*){0,10}(\d{2,})(?=[\s-])(?![^\[]*\])(?![^\(]*\))", mod_title)
                    except NameError:
                        print("error datta : " , NameError)
                    # print('found the ep number: ',match)
                    if not match:
                        continue
                    print(title)
                    episode_number = int(match.group(1))
                    
                    # Check if the last episode downloaded is in this page
                    # print('aya ', episode_number , '=' , episodes_downloaded , '?')
                    if episode_number == episodes_downloaded:
                        print('found the last episode!')
                        last_episode_found = True
                        continue
                    
                    # Check if the episode is higher than the
                    if episode_number <= episodes_downloaded:
                        continue
                    
                    

                    if last_episode < episode_number:
                        last_episode = episode_number
                    
                    title = f"{anime} - Episode {episode_number}"
                    magnet_link = episode_link["href"]
                    episodes.append((title, magnet_link))

                
                # If last episode were found or the last page was reached, break out of the while loop
                if last_episode_found or not soup.find("div", class_="home_list_entry"):
                    break

                # Otherwise, increment the page number and fetch the next page
                page_number += 1

            # Display the episodes in a message box
            message = "\n".join(f"{title}: {magnet_link}" for title, magnet_link in episodes)
            # QMessageBox.information(self, "Episodes", message)
            print("\n", message, "\n")

            
            #Download the episodes
            for title, magnet_link in episodes:
                webbrowser.open_new_tab(magnet_link)

            # Update the list of downloaded episodes for the anime
            if episodes:
                self.anime_list[anime]["episodes_downloaded"] = last_episode
                with open(self.anime_list_file, "wb") as f:
                    pickle.dump(self.anime_list, f)


if __name__ == "__main__":
    app = QApplication([])
    window = AnimeMagnetDownloader()
    window.show()
    app.exec_()