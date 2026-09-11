import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/Brainstorm Server/);
});

test('can connect to server', async ({ page }) => {
  await page.goto('/');
  const message = page.locator('text=Connected');
  await expect(message).toBeVisible();
});
