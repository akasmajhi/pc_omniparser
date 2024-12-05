import { By } from 'selenium-webdriver';
import { WaitUtils } from '../utils/wait-utils.js';

export class LoginPage {
    constructor(driver) {
        this.driver = driver;
        this.selectors = {
            username: By.id('username'),
            password: By.id('password'),
            dropdown: By.id('dropdown'),
            loginButton: By.id('login')
        };
    }

    async enterUsername(username) {
        const element = await WaitUtils.waitForElement(this.driver, this.selectors.username);
        await element.clear();
        await element.sendKeys(username);
    }

    async enterPassword(password) {
        const element = await WaitUtils.waitForElement(this.driver, this.selectors.password);
        await element.clear();
        await element.sendKeys(password);
    }

    async selectDropdownOption(optionText) {
        const dropdown = await WaitUtils.waitForElement(this.driver, this.selectors.dropdown);
        await dropdown.click();
        const option = await WaitUtils.waitForElement(
            this.driver,
            By.xpath(`//option[text()='${optionText}']`)
        );
        await option.click();
    }

    async clickLogin() {
        const button = await WaitUtils.waitForClickable(this.driver, this.selectors.loginButton);
        await button.click();
    }

    async isLoggedIn() {
        try {
            const loggedInIndicator = await WaitUtils.waitForElement(
                this.driver,
                By.id('logged-in-indicator')
            );
            return await loggedInIndicator.isDisplayed();
        } catch (error) {
            return false;
        }
    }
}