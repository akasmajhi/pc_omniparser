import { Builder } from 'selenium-webdriver';
import chrome from 'selenium-webdriver/chrome.js';

export class DriverFactory {
    static async createDriver() {
        const options = new chrome.Options();
        options.addArguments('--headless');
        
        return await new Builder()
            .forBrowser('chrome')
            .setChromeOptions(options)
            .build();
    }

    static async quitDriver(driver) {
        if (driver) {
            await driver.quit();
        }
    }
}