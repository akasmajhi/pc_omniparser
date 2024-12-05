import { until } from 'selenium-webdriver';
import { TEST_CONFIG } from '../config/test-config.js';

export class WaitUtils {
    static async waitForElement(driver, locator) {
        return await driver.wait(
            until.elementLocated(locator),
            TEST_CONFIG.defaultTimeout
        );
    }

    static async waitForClickable(driver, locator) {
        return await driver.wait(
            until.elementIsEnabled(await driver.findElement(locator)),
            TEST_CONFIG.defaultTimeout
        );
    }
}