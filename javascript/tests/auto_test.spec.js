import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://mainweb9.lib.msu.edu/');
  await page.getByPlaceholder('Books, articles, databases, and more ').click();
  await page.getByPlaceholder('Books, articles, databases, and more ').click();
  await page.getByPlaceholder('Books, articles, databases, and more ').click();
  await page.getByPlaceholder('Books, articles, databases, and more ').fill('Acc 321');
  await page.locator('#search-btn').click();
  await expect(page.getByText('Connors, Elizabeth')).toHaveCount(1);
});