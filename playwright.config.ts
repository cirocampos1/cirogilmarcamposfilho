import { defineConfig, devices } from '@playwright/test';
import dotenv from 'dotenv';

dotenv.config({ path: '.env.playwright', quiet: true });

const baseURL = process.env._PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:8000';
const browserChannel = process.env._PLAYWRIGHT_BROWSER_CHANNEL || 'chrome';

export default defineConfig({
  testDir: './tests/e2e',
  outputDir: './artifacts/playwright/test-results',
  timeout: 60_000,
  expect: {
    timeout: 10_000,
  },
  fullyParallel: false,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: [
    ['list'],
    ['html', { outputFolder: 'artifacts/playwright/html-report', open: 'never' }],
  ],
  use: {
    baseURL,
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    {
      name: 'chromium-desktop',
      use: {
        ...devices['Desktop Chrome'],
        channel: browserChannel,
        viewport: { width: 1440, height: 1100 },
      },
    },
    {
      name: 'chromium-mobile',
      use: { ...devices['Pixel 7'], channel: browserChannel },
    },
  ],
});
