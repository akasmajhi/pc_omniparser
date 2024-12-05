import { describe, test, expect, beforeAll, afterAll } from '@jest/globals';
import { DriverFactory } from '../src/utils/DriverFactory.js';
import { LoginPage } from '../src/pages/LoginPage.js';
import { TEST_CONFIG } from '../src/config/test-config.js';

describe('Login Page Tests', () => {
    let driver;
    let loginPage;

    beforeAll(async () => {
        driver = await DriverFactory.createDriver();
        loginPage = new LoginPage(driver);
        await driver.get(TEST_CONFIG.baseUrl);
    });

    afterAll(async () => {
        await DriverFactory.quitDriver(driver);
    });

    test('should login successfully with different dropdown options', async () => {
        for (const option of TEST_CONFIG.dropdownOptions) {
            await loginPage.enterUsername(TEST_CONFIG.credentials.username);
            await loginPage.enterPassword(TEST_CONFIG.credentials.password);
            await loginPage.selectDropdownOption(option);
            await loginPage.clickLogin();
            
            expect(await loginPage.isLoggedIn()).toBe(true);
            
            // Navigate back or logout for next iteration
            await driver.get(TEST_CONFIG.baseUrl);
        }
    });
});