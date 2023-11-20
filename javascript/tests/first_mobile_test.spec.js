import { test, expect } from '@playwright/test';

test.use({ 
  viewport: { width: 390, height: 844 },
});

test('Check events and workshops link', async ({ page }) => {
  await page.goto('https://lib.msu.edu/');

  // Click the library spaces link.
  // a negative test case
  //await expect(page).not.getByRole('link', { name: 'View all Events & Workshops' }).click();

  // Expects the URL to contain spaces.
  // a negative test case
  //await expect(page).toHaveURL('https://bookings.lib.msu.edu/calendar/events/?cid=3079&t=g&d=0000-00-00&cal=3079&inc=0');

  expect(await page.getByRole('link', { name: 'View all Events & Workshops' }).count()).toEqual(0);
});
