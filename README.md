# Anime Magnet Downloader

Anime Magnet Downloader is a lightweight application that allows users to manage a list of anime series with their relevant metadata, such as tags, page URLs, starting episodes, and resolution. With this program, you can add, edit, and delete anime entries easily, and export the data for later use. It's designed to simplify the process of organizing and managing your favorite anime for downloading.

This program uses PyQt5 for the graphical user interface and stores data in a `pickle` file for persistent storage.

## Features

- Add new anime entries with metadata:
  - Name
  - Page URL
  - Tag
  - Starting episode number
  - Resolution
- Edit existing anime entries.
- Delete anime entries.
- Persistent storage of data using a `.pkl` file.
- Easy-to-use graphical user interface.

## How to Use

### Adding a New Anime

1. Click the **"Add Anime"** button.
2. Fill in the required details in the dialog form:
   - Anime name
   - Page URL
   - Tag
   - Starting episode number
   - Resolution (choose between 1080p, 720p, or 480p).
3. Click **OK** to save the entry.

### Editing an Anime

1. Select an anime from the list.
2. Click the **"Edit"** button.
3. Modify the details in the dialog form.
4. Click **Save** to apply changes.

### Deleting an Anime

1. Select an anime from the list.
2. Click the **"Delete Anime"** button to remove the entry.

### Downloading

When you press the *Download* button the app automatically searches for the new episodes of the list of anime you added to it and adds the magnet link of it to your torrent client. 

## Technical Details

### Prerequisites

- Python 3.7 or later.
- Required Python packages:
  - `PyQt5` (for the GUI).
  - `pickle` (for data persistence).

### Installing Dependencies

Install the required libraries using `pip`:

```bash
pip install PyQt5
```

## Running the Application

1. Clone this repository or download the code files.
2. Navigate to the directory containing the script.
3. Run the program using:
```bash
python <script_name>.py
```

## Data File

- anime_list.pkl: Stores the anime list data in serialized format. If no file is found, the application will initialize with an empty list.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for feature requests, bug fixes, or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
