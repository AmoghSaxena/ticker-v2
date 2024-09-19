# On-Screen Ticker Display

This Python project uses Pygame to create a customizable on-screen ticker display, similar to those seen on news channels. The ticker can be configured to scroll text across the top or bottom of the screen with customizable colors and direction.

## Features

- **Customizable Ticker**: Configure the ticker's background color, font color, text, direction, and position.
- **Dynamic Sizing**: The ticker height and font size adjust dynamically based on the screen height.
- **Always on Top**: The ticker window stays on top of other windows.
- **YAML Configuration**: Easily modify settings using a `config.yml` file with comments for clarity.

---

## Dependencies are mentioned below. ##

### Linux OS related Dependency ###
1. Windows OS(recommended), but if you are using Linux based os then follow step 2 as Linux does not support Always on Top feature using python. It depends on which window manager you are using.
2. Desktop Environment Like `Ubuntu(Gnome/Mate/Lite/etc) - with hidden decorators and alwaysOnTop support`, `Fluxbox (window manager) - with hidden decorators and alwaysOnTop support`
> If you want to disable the decorator in Gnome then check my Stack Overflow solution over here : [StackOverflow Link](https://stackoverflow.com/a/71908794/8813647)
3. Supported Python Version 3.6 [![Supported Python Version 3.6+](https://img.shields.io/badge/Python-v3.6+-blue.svg?style=flat-square&logo=python)](#) BUT Recommended Python Version 3.8 [![Supported Python Version 3.6+](https://img.shields.io/badge/Python-v3.8+-blue.svg?style=flat-square&logo=python)](#)


## Installation

1. Head over to [Releases Section](https://github.com/AmoghSaxena/ticker-v2/releases)

2. Download the latest version of `tickerv2.exe`(for Windows) or `tickerv2bin`(for Linux) depending on your OS

3. Run the main file

4. You can edit config.yml to make changes in your ticker


## Running from source code

1. Clone the repository:
   ```bash
   git clone https://github.com/AmoghSaxena/ticker-v2.git
   cd ticker-v2
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit the `config.yml` file to customize the ticker:

```yaml
# Configuration for ticker
background_color: [255, 165, 0]  # Background color in RGB
font_color: [255, 255, 255]      # Font color in RGB
direction: left                  # Direction of ticker: left(<--) or right(-->)
ticker_text: "Breaking News: This is a configurable ticker!"  # Text to display
position: bottom                 # Position of ticker: top or bottom
logo_path: ""                    # Path to logo image (leave empty if no logo)
logo_position: left             # Position of logo: left or right
```

## Usage

Run the script to start the ticker:

```bash
python ticker.py
```

## Screenshots

![Ticker Example](https://pplx-res.cloudinary.com/image/upload/v1726150678/user_uploads/wasrnmswq/ticker.jpg)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For questions or suggestions, please contact rexter@amoghsaxena.com.




