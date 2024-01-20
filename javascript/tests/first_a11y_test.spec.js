
const { test, expect } = require('@playwright/test');

const AxeBuilder = require('@axe-core/playwright').default;

const fs = require("fs");


const jsonString = fs.readFileSync("./tests/urls.json", "utf8");

const urls = JSON.parse(jsonString);

for (const key in urls) {
  test.describe(key, () => { // 2
    test('should not have any automatically detectable accessibility issues', async ({ page }) => {
      await page.goto(urls[key]);

      const accessibilityScanResults = await new AxeBuilder({ page }).analyze();

      expect(accessibilityScanResults.violations).toEqual([]);
    });
  });
  
}


