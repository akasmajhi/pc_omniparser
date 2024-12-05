# Selenium Login Test Suite (Node.js)

This test suite demonstrates automated testing of a login page with username, password, and dropdown functionality using Selenium WebDriver for Node.js.

## Project Structure
```
├── src/
│   ├── pages/
│   │   └── LoginPage.js      # Page Object Model for login page
│   └── utils/
│       └── DriverFactory.js  # WebDriver setup and configuration
├── tests/
│   └── login.test.js        # Test cases
├── jest.config.js           # Jest configuration
└── package.json            # Project dependencies
```

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Update the website URL in `tests/login.test.js`

3. Update the element IDs in `src/pages/LoginPage.js` to match your website's actual element IDs

## Running Tests

Execute the tests using:
```bash
npm test
```