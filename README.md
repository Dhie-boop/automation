# SauceDemo Automation Project

This project is a web automation script that tests the complete e-commerce flow on [SauceDemo](https://www.saucedemo.com/), including login, adding items to cart, checkout, and order completion using Playwright.

## Features

- **Page Object Model (POM)**: Clean, maintainable code structure
- **Screenshot Capture**: Automatic screenshots at each step for debugging
- **Error Handling**: Comprehensive error handling with timeout management
- **Logging**: Detailed logging for monitoring execution
- **JSON Output**: Order summary saved to JSON file

## Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- Windows, macOS, or Linux

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd automation
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv automate

# Activate virtual environment
# On Windows:
automate\Scripts\activate

# On macOS/Linux:
source automate/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

After installing the packages, you need to install the browser binaries:

```bash
playwright install
```

### 5. Create Configuration File

Create a `config.json` file in the project root with your test credentials:

```json
{
  "base_url": "https://www.saucedemo.com/",
  "username": "standard_user",
  "password": "secret_sauce"
}
```

## Project Structure

```
automation/
│
├── automate/                 # Virtual environment
├── screenshots/              # Generated screenshots folder
│   ├── 0_home.png           # Screenshot: Homepage
│   ├── 1_logged_in.png      # Screenshot: After login
│   ├── 2_items_added.png    # Screenshot: Items in cart
│   ├── 3_cart_view.png      # Screenshot: Cart page
│   ├── 4_checkout_info.png  # Screenshot: Checkout form
│   ├── 5_checkout_summary.png # Screenshot: Order summary
│   ├── 6_order_complete.png # Screenshot: Order confirmation
│   ├── error_timeout.png    # Screenshot: Timeout errors (if any)
│   └── error_unexpected.png # Screenshot: Unexpected errors (if any)
├── test.py                   # Main automation script
├── config.json              # Configuration file
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── cart.png                 # Sample screenshot
│
└── Generated files (after running):
    └── order_summary.json   # Order details and total price
```

## Usage

### Basic Usage

1. Ensure your virtual environment is activated:
   ```bash
   # Windows
   automate\Scripts\activate
   
   # macOS/Linux
   source automate/bin/activate
   ```

2. Run the automation script:
   ```bash
   python test.py
   ```

### Configuration Options

You can modify the `config.json` file to use different credentials or URLs:

```json
{
  "base_url": "https://www.saucedemo.com/",
  "username": "standard_user",
  "password": "secret_sauce"
}
```

**Available test users for SauceDemo:**
- `standard_user` - Regular user
- `problem_user` - User with issues
- `performance_glitch_user` - Slow user
- `error_user` - User with errors
- `visual_user` - Visual testing user

## What the Script Does

1. **Login**: Logs into SauceDemo with provided credentials
2. **Add Items**: Adds two specific items to the cart:
   - Sauce Labs Backpack
   - Sauce Labs Bike Light
3. **Navigate to Cart**: Goes to the shopping cart
4. **Checkout Process**: 
   - Proceeds to checkout
   - Fills in customer information
   - Reviews order summary
5. **Complete Order**: Finishes the order and captures confirmation
6. **Save Results**: Saves order total and status to `order_summary.json`

## Output Files

After successful execution, you'll find:

- **Screenshots**: Step-by-step visual documentation (0_home.png through 6_order_complete.png)
- **order_summary.json**: Contains order total and completion status
- **Console logs**: Detailed execution information

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'playwright'**
   ```bash
   pip install playwright
   playwright install
   ```

2. **Browser not found**
   ```bash
   playwright install chromium
   ```

3. **Permission denied on activation script**
   ```bash
   # Windows PowerShell - run this once
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Config file not found**
   - Ensure `config.json` exists in the project root
   - Check the JSON syntax is valid

### Error Screenshots

If errors occur, the script will capture error screenshots:
- `error_timeout.png` - For timeout issues
- `error_unexpected.png` - For unexpected errors

## Development

### Adding New Test Steps

The code uses Page Object Model pattern. To add new functionality:

1. **Add new page class** (if needed):
   ```python
   class NewPage:
       def __init__(self, page):
           self.page = page
       
       def new_action(self):
           # Your code here
           pass
   ```

2. **Update the main flow** in the `run()` function

### Customizing Screenshots

To change screenshot behavior, modify the `page.screenshot()` calls in the `run()` function.

### Modifying Items to Purchase

Update the `add_items_to_cart()` method in the `InventoryPage` class to change which items are added to the cart.

## Dependencies

- **playwright**: Web automation framework
- **Python 3.8+**: Programming language

## License

This project is for educational and testing purposes.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review Playwright documentation: https://playwright.dev/python/
3. Check SauceDemo site: https://www.saucedemo.com/

---

**Note**: This automation script is designed for the SauceDemo testing website. Do not use on production websites without proper authorization.
