import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('https://mainweb9.lib.msu.edu/');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/Home/);
});

test('Check spaces link', async ({ page }) => {
  await page.goto('https://mainweb9.lib.msu.edu/');

  // Click the library spaces link.
  await page.getByRole('link', { name: 'Discover Library Spaces' }).first().click();

  // Expects the URL to contain spaces.
  await expect(page).toHaveURL('https://mainweb9.lib.msu.edu/spaces');
});

test('Check events link', async ({ page }) => {
  await page.goto('https://mainweb9.lib.msu.edu/');

  // Click the events link.
  await page.getByRole('link', { name: 'View all Events & Workshops' }).click();

  // Expects the URL to contain bookings.
  await expect(page).toHaveURL('https://bookings.lib.msu.edu/calendar/events/?cid=3079&t=g&d=0000-00-00&cal=3079&inc=0');
});

