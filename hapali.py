
class AnimeMagnetDownloader(QWidget):
    def init(self):
        super().init()

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

    def add_anime(self):
        # Display an input dialog for the user to enter the name of an anime
        anime_name, ok = QInputDialog.getText(self, "Add Anime", "Anime Name:")
        if ok:
            # Display an input dialog for the user to enter the page number
            page, ok = QInputDialog.getInt(self, "Add Anime", "Page:")
            if ok:
                # Add the anime and page number to the anime list
                self.anime_list[anime_name] = page
                self.anime_list_widget.addItem(anime_name)
                # Save the list of animes and their pages to a file
                with open("anime_list.pkl", "wb") as f:
                    pickle.dump(self.anime_list, f)
    def download(self):
        # Get the list of anime and their pages to download
        anime_list = self.anime_list
        # Fetch the HTML from animetosho.org
        r = requests.get("https://animetosho.org/")
        soup = BeautifulSoup(r.text, "html.parser")

        # Find the latest episodes
        episodes = []
        for anime, page in anime_list.items():
            # Find the home_list_entry divs on the page
            divs = soup.find_all("div", class_="home_list_entry", page=page)
            for div in divs:
                # Check if the div contains an episode link for the current anime
                episode_link = div.find("a", string=re.compile(anime), href=True)
                if episode_link:
                    title = episode_link.text.strip()
                    magnet_link = episode_link["href"]
                    episodes.append((title, magnet_link))

        # Display the episodes in a message box
        message = "\n".join(f"{title}: {magnet_link}" for title, magnet_link in episodes)
        QMessageBox.information(self, "Episodes", message)

if __name__ == "__main__":
    app = QApplication([])
    window = AnimeMagnetDownloader()
    window.show()
    app.exec_()




    # Find the latest episodes
episodes = []
for anime in anime_list:
    # Fetch the HTML from the page for the current anime
    r = requests.get(self.anime_list[anime])
    soup = BeautifulSoup(r.text, "html.parser")

    # Find the home_list_entry divs on the page
    divs = soup.find_all("div", class_="home_list_entry")
    for div in divs:
        # Check if the div contains an episode link for the current anime
        episode_link = div.find("a", string=re.compile(anime), href=True)
        if episode_link:
            title = episode_link.text.strip()
            magnet_link = episode_link["href"]
            episodes.append((title, magnet_link))

# Display the episodes in a message box
message = "\n".join(f"{title}: {magnet_link}" for title, magnet_link in episodes)
QMessageBox.information(self, "Episodes", message)



            episode_link = div.find("a", text=re.compile("Magnet"))
            if episode_link:
                title = div.text.strip()
                magnet_link = episode_link
                # Check if the title matches one of the anime in the list
                for anime in anime_list:
                    if re.search(anime, title, re.IGNORECASE):
                        # Check if the episode has [ASW] or [Judas] in the title
                        if "[ASW]" in title or "[Anime Time]" in title:
                            episodes.append((title, magnet_link))
                            break