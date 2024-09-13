# On-Screen Ticker Display

This Python project uses Pygame to create a customizable on-screen ticker display, similar to those seen on news channels. The ticker can be configured to scroll text across the top or bottom of the screen with customizable colors and direction.

## Features

- **Customizable Ticker**: Configure the ticker's background color, font color, text, direction, and position.
- **Dynamic Sizing**: The ticker height and font size adjust dynamically based on the screen height.
- **Always on Top**: The ticker window stays on top of other windows.
- **YAML Configuration**: Easily modify settings using a `config.yml` file with comments for clarity.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AmoghSaxena/ticker-v2.git
   cd ticker-v2
   ```

2. Install the required packages:
   ```bash
   pip install pygame pyyaml pywin32
   ```

## Configuration

Edit the `config.yml` file to customize the ticker:

```yaml
# Configuration for ticker
background_color: [255, 165, 0]  # Background color in RGB
font_color: [255, 255, 255]      # Font color in RGB
direction: left                  # Direction of ticker: left or right
ticker_text: "Breaking News: This is a configurable ticker!"  # Text to display
position: bottom                 # Position of ticker: top or bottom
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




